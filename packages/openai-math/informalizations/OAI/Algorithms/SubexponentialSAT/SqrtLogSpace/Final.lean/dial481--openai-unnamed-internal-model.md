---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Final.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Final.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Final.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Exact counting and SAT on one fixed primitive run, with the unchanged
ETH square-root-log time scale and polynomial all-prefix visited space. 

### `exact_count_and_sat`

 One fixed primitive machine exactly counts every bounded-width formula,
decides satisfiability, meets the square-root-logarithmic time bound, and uses
only polynomially many visited tape cells at every execution prefix. 
