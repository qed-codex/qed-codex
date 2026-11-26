// Included in a launch package when the owner supplies the discussion IDs.
const main = document.querySelector("main");

function mount(config) {
  const form = main.querySelector("form.contribute[data-path]");
  if (!form) return false;
  const slot = [...main.querySelectorAll("article.record > section")].find(
    section => section.querySelector("h2")?.textContent === "Discussion"
  )?.querySelector("p");
  if (!slot) return false;
  const container = document.createElement("div");
  container.className = "giscus";
  const script = document.createElement("script");
  script.src = "https://giscus.app/client.js";
  script.async = true;
  script.crossOrigin = "anonymous";
  Object.assign(script.dataset, {
    repo:"qed-codex/qed-codex", repoId:config.repoId, category:config.category, categoryId:config.categoryId,
    mapping:"specific", term:"module:" + form.dataset.package + ":" + form.dataset.path, strict:"1", reactionsEnabled:"0",
    theme:"preferred_color_scheme", lang:"en",
  });
  slot.replaceWith(container);
  container.append(script);
  return true;
}
async function start() {
  if (!main.querySelector("form.contribute") && main.dataset.type !== "module") return;
  const response = await fetch("/discussion.json");
  if (!response.ok) return;
  const config = await response.json();
  if (!config || !["repoId", "category", "categoryId"].every(key => typeof config[key] === "string" && config[key].trim())) return;
  if (!mount(config) && main.dataset.type === "module") {
    const observer = new MutationObserver(() => { if (mount(config)) observer.disconnect(); });
    observer.observe(main, {childList:true,subtree:true});
  }
}
start().catch(() => {});
