const header = document.querySelector("[data-header]");
const menuButton = document.querySelector("[data-menu-button]");
const navigation = document.querySelector("[data-nav]");
const revealItems = document.querySelectorAll("[data-reveal]");

document.documentElement.classList.add("reveal-ready");

const updateHeader = () => {
  header?.classList.toggle("is-scrolled", window.scrollY > 24);
};

const closeMenu = () => {
  if (!menuButton || !navigation) return;
  menuButton.setAttribute("aria-expanded", "false");
  navigation.classList.remove("is-open");
};

menuButton?.addEventListener("click", () => {
  const willOpen = menuButton.getAttribute("aria-expanded") !== "true";
  menuButton.setAttribute("aria-expanded", String(willOpen));
  navigation?.classList.toggle("is-open", willOpen);
});

navigation?.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", closeMenu);
});

document.addEventListener("keydown", (event) => {
  if (event.key !== "Escape") return;
  closeMenu();
  menuButton?.focus();
});

document.addEventListener("click", (event) => {
  if (!navigation?.classList.contains("is-open")) return;
  if (navigation.contains(event.target) || menuButton?.contains(event.target)) return;
  closeMenu();
});

window.addEventListener("scroll", updateHeader, { passive: true });
window.addEventListener("resize", () => {
  if (window.innerWidth > 800) closeMenu();
});

updateHeader();

if ("IntersectionObserver" in window) {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    },
    { threshold: 0.12, rootMargin: "0px 0px -7%" },
  );

  revealItems.forEach((item) => observer.observe(item));
} else {
  revealItems.forEach((item) => item.classList.add("is-visible"));
}
