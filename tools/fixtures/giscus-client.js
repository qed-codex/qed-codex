// Stand-in for the external client. Read the options supplied by discussion.mjs.
const script = document.currentScript;
const {repo, term, strict} = script.dataset;
const frame = document.createElement("iframe");
frame.className = "giscus-frame";
frame.src = "https://giscus.app/en/widget?" + new URLSearchParams({repo, term, strict});
script.parentElement.append(frame);
