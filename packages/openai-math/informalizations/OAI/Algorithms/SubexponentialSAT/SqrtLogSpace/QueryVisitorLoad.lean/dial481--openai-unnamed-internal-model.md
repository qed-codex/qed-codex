---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryVisitorLoad.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryVisitorLoad.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryVisitorLoad.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Paid reverse-head reload for the two-pass query visitor. The same native
run returns every integer row, preserves the suspended query data, and restores
a fixed retained word cap before the next head. 

### `result`

 The physical result of that one concrete head loader. 

### `result_masters`

 The source words and caches retain their exact values across the loader. 

### `result_wordBound`

 The retained bound is restored exactly; the transient loader envelope is
never fed into the next boundary bound. 

### `load_run`

 The complete loader run is obtained from actual native inputs and paid
cache values. No successful matrix execution is an input to this theorem. 

### `runEnvelope`

 Both the time and every-prefix loader storage are bounded by one fixed
input polynomial. This envelope is transient and is never the next F. 
