const form = document.querySelector("#console");
const input = document.querySelector("#sql");
const share = document.querySelector("#share");
const run = document.querySelector("#run");
const cancel = document.querySelector("#cancel");
const status = document.querySelector("#result-status");
const output = document.querySelector("#output");
let worker, timeout;

// Fragments stay in the browser. Opening a link fills the editor; Run is explicit.
function readLink() {
  const query = new URLSearchParams(location.hash.slice(1)).get("q");
  input.value = query ?? input.defaultValue;
  updateLink();
}
function updateLink() {
  const url = new URL(location.pathname, location.origin);
  url.hash = new URLSearchParams({q: input.value});
  share.href = url.href;
}
function idle() {
  clearTimeout(timeout);
  run.disabled = false;
  cancel.disabled = true;
  form.removeAttribute("aria-busy");
}
function stop(message) {
  worker?.terminate();
  worker = undefined;
  idle();
  status.textContent = message;
}
function showResult({columns, rows, limited}) {
  const table = document.createElement("table");
  const header = table.createTHead().insertRow();
  for (const column of columns) {
    const cell = document.createElement("th");
    cell.scope = "col";
    cell.textContent = column;
    header.append(cell);
  }
  const body = table.createTBody();
  for (const values of rows) {
    const row = body.insertRow();
    for (const value of values) row.insertCell().textContent = value === null ? "NULL" : String(value);
  }
  output.replaceChildren(table);
  status.textContent = limited ? `Showing ${rows.length} rows (result limit reached).` :
    `${rows.length} ${rows.length === 1 ? "row" : "rows"}.`;
}
form.addEventListener("submit", event => {
  event.preventDefault();
  if (run.disabled) return;
  output.replaceChildren();
  if (!input.value.trim()) { status.textContent = "Enter a query."; return; }
  run.disabled = true;
  cancel.disabled = false;
  form.setAttribute("aria-busy", "true");
  status.textContent = "Running query…";
  try {
    worker ??= new Worker("/console-worker.mjs", {type: "module"});
    let scanning = false;
    worker.onmessage = ({data}) => {
      if (data.wholeTableScan) {
        scanning = true;
        return;
      }
      idle();
      if (data.error) status.textContent = data.error;
      else showResult(data);
    };
    worker.onerror = () => stop("The SQL worker could not complete the query.");
    timeout = setTimeout(() => {
      const cause = scanning ? " A whole-table scan was reading pages over the network." : "";
      stop("Query stopped after 30 seconds." + cause + " Row counts are in summary. Filter on an indexed column for other lookups.");
    }, 30000);
    worker.postMessage(input.value);
  } catch {
    stop("The SQL worker could not start.");
  }
});
cancel.addEventListener("click", () => stop("Query cancelled."));
input.addEventListener("input", updateLink);
window.addEventListener("hashchange", readLink);
document.querySelector("#examples").addEventListener("click", event => {
  const example = event.target.closest("button[data-sql]");
  if (example) { input.value = example.dataset.sql; updateLink(); input.focus(); }
});
readLink();
