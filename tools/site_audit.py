#!/usr/bin/env python3
"""Dependency-free structural audit for the Perpetuity AI static site."""

from __future__ import annotations

import csv
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = sorted(ROOT.glob("*.html"))
PUBLIC_PAGES = {"index.html", "pilot.html", "trust.html", "evidence.html", "privacy.html", "terms.html"}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.links: list[str] = []
        self.assets: list[str] = []
        self.images_without_alt: list[str] = []
        self.h1_count = 0
        self.title = ""
        self._in_title = False
        self.description = ""
        self.canonical = ""
        self.lang = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        if tag == "html":
            self.lang = values.get("lang", "")
        if "id" in values:
            self.ids.append(values["id"])
        if tag == "a" and "href" in values:
            self.links.append(values["href"])
        if tag in {"script", "img", "source"} and "src" in values:
            self.assets.append(values["src"])
        if tag == "link" and values.get("href"):
            rel = set(values.get("rel", "").split())
            if "canonical" in rel:
                self.canonical = values["href"]
            elif rel.intersection({"stylesheet", "icon", "manifest"}):
                self.assets.append(values["href"])
        if tag == "img" and "alt" not in values:
            self.images_without_alt.append(values.get("src", "(unknown)"))
        if tag == "h1":
            self.h1_count += 1
        if tag == "title":
            self._in_title = True
        if tag == "meta" and values.get("name", "").lower() == "description":
            self.description = values.get("content", "").strip()

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title += data


def local_target(page: Path, raw_url: str) -> tuple[Path, str] | None:
    parsed = urlsplit(raw_url)
    if parsed.scheme or parsed.netloc or raw_url.startswith(("mailto:", "tel:", "data:")):
        return None
    path = unquote(parsed.path)
    if not path:
        target = page
    elif path in {".", "./"}:
        target = ROOT / "index.html"
    else:
        target = (page.parent / path).resolve()
        if target.is_dir() or path.endswith("/"):
            target = target / "index.html"
    return target, parsed.fragment


def main() -> int:
    errors: list[str] = []
    parsed_pages: dict[Path, PageParser] = {}

    for page in HTML_FILES:
        source = page.read_text(encoding="utf-8")
        parser = PageParser()
        parser.feed(source)
        parsed_pages[page.resolve()] = parser

        if not parser.lang:
            errors.append(f"{page.name}: missing html lang")
        if not parser.title.strip():
            errors.append(f"{page.name}: missing title")
        if parser.h1_count != 1:
            errors.append(f"{page.name}: expected one h1, found {parser.h1_count}")
        if len(parser.ids) != len(set(parser.ids)):
            errors.append(f"{page.name}: duplicate id")
        if page.name in PUBLIC_PAGES:
            if not parser.description:
                errors.append(f"{page.name}: missing meta description")
            if not parser.canonical:
                errors.append(f"{page.name}: missing canonical link")
        if parser.images_without_alt:
            errors.append(f"{page.name}: images missing alt: {', '.join(parser.images_without_alt)}")
        if "github.com/" in source.lower():
            errors.append(f"{page.name}: rendered page promotes a repository")

    for page, parser in parsed_pages.items():
        for raw_url in parser.links + parser.assets:
            result = local_target(page, raw_url)
            if result is None:
                continue
            target, fragment = result
            if not target.exists():
                errors.append(f"{page.name}: missing local target {raw_url}")
                continue
            if fragment and target.suffix.lower() == ".html":
                target_parser = parsed_pages.get(target.resolve())
                if target_parser is None:
                    target_parser = PageParser()
                    target_parser.feed(target.read_text(encoding="utf-8"))
                    parsed_pages[target.resolve()] = target_parser
                if fragment not in target_parser.ids:
                    errors.append(f"{page.name}: missing fragment #{fragment} in {target.name}")

    claim_path = ROOT / "research" / "claim-register.csv"
    if not claim_path.exists():
        errors.append("claim register is missing")
    else:
        with claim_path.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        if not rows:
            errors.append("claim register is empty")
        required = {"claim_id", "statement", "type", "status", "scope_as_of", "source_or_test", "next_action", "external_use"}
        if rows and not required.issubset(rows[0]):
            errors.append("claim register is missing required columns")
        ids = [row.get("claim_id", "") for row in rows]
        if len(ids) != len(set(ids)):
            errors.append("claim register has duplicate claim ids")

    schema_path = ROOT / "schemas" / "authorization-packet.schema.json"
    if not schema_path.exists():
        errors.append("authorization-packet schema is missing")
    else:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
            errors.append("authorization-packet schema does not declare JSON Schema 2020-12")
        if not {"packetId", "status", "requestedUse", "approvals", "events"}.issubset(schema.get("properties", {})):
            errors.append("authorization-packet schema is missing core properties")

    for template_name in ("pilot-measurement.csv", "pilot-risk-register.csv"):
        template_path = ROOT / "templates" / template_name
        if not template_path.exists():
            errors.append(f"missing template {template_name}")
            continue
        with template_path.open(newline="", encoding="utf-8") as handle:
            template_rows = list(csv.DictReader(handle))
        if not template_rows:
            errors.append(f"template {template_name} is empty")

    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    for page_name in sorted(PUBLIC_PAGES):
        expected = "https://dtrezise.github.io/PerpetuityAI/" if page_name == "index.html" else f"https://dtrezise.github.io/PerpetuityAI/{page_name}"
        if expected not in sitemap:
            errors.append(f"sitemap missing {page_name}")

    css = (ROOT / "styles.css").read_text(encoding="utf-8")
    if len(re.findall(r"@media\s*\(prefers-reduced-motion", css)) != 1:
        errors.append("expected one reduced-motion media query")

    if errors:
        print("Site audit failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Site audit passed: {len(HTML_FILES)} HTML pages, {len(rows)} registered claims, schema and pilot templates valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
