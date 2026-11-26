const examples = {
  typeahead: "row", module: "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/RowSrc.lean",
  search: "RowSrc", declaration: "UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter",
  trail: "UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter"
};
const kind = document.querySelector("#kind"), value = document.querySelector("#value");
value.value = examples[kind.value];
let debounce, active = 0;
const form = document.querySelector("form");
const state = document.querySelector("#state"), output = document.querySelector("#result");
function reset() {
  clearTimeout(debounce);
  ++active;
  state.textContent = "Ready";
  output.textContent = "";
}
kind.onchange = () => { reset(); value.value = examples[kind.value]; };
value.oninput = () => {
  reset();
  if (kind.value === "typeahead" && value.value.trim()) {
    debounce = setTimeout(() => form.requestSubmit(), 150);
  }
};
document.querySelector("#everywhere").onclick = () => {
  kind.value = "search";
  form.requestSubmit();
};
let thread;
document.querySelector("form").onsubmit = event => {
  event.preventDefault();
  clearTimeout(debounce);
  const id = ++active;
  state.textContent = "Opening database…";
  thread ??= new Worker("./query-thread.mjs", { type:"module" });
  thread.onmessage = ({data}) => {
    if (data.id !== active) return;
    state.textContent = data.error ? "Failed" : "Complete";
    output.textContent = data.error || JSON.stringify(data.result,null,2);
  };
  thread.onerror = e => { state.textContent = "Failed"; output.textContent = e.message; };
  thread.postMessage({id,kind:kind.value,value:value.value});
};
