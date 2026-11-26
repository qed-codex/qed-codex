// Display a pre-rendered sample before the directory opens SQLite.
{
  const main = document.querySelector("main");
  const params = new URLSearchParams(location.search);
  const type = main.dataset.type;
  const key = params.get(type === "module" ? "p" : "n");
  const samples = /* @samples@ */ [];
  const sample = samples.find(s => s.type === type && s.key === key && s.package === params.get("pkg"));
  if (sample) {
    document.title = sample.name + " · QED Codex";
    document.querySelector('[property="og:title"]').content = document.title;
    document.querySelector('[name="description"]').content = sample.description;
    document.querySelector('[property="og:description"]').content = sample.description;
    const canonical = document.querySelector('link[rel="canonical"]');
    if (canonical) canonical.href = new URL(sample.samplePath, canonical.href).href;
    main.innerHTML = sample.html;
    main.dataset.ready = "true";
  } else {
    main.textContent = "Opening " + main.dataset.type + "…";
  }
}
