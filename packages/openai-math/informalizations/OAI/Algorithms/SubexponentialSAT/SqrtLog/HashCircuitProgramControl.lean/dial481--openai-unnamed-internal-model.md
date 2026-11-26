---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramControl.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramControl.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramControl.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed record-control code for sparse-hash evaluation. This module fixes
all parsing and traversal code. Arithmetic components below are finite native
commands, to be instantiated by the separate dictionary modules; no semantic
function is called by the machine. 

### `recordReturn`

 Both record loops use this physical three-instruction return convention. 

### `Arithmetic`

 Concrete fixed commands are supplied here, rather than semantic ring
operations. Their ABI is: complement61, product(67,61)→67 consuming61,
and scalar-weighted accumulation(65,67,68)→68 consuming65/67. 

### `literalStep`

 The polarity branch is taken before arithmetic may reuse the registers. 

### `weightedClauseStep`

 Each clause starts from a physical preserving copy of the cached one. 

### `rowLoop`

 One fixed dynamic outer loop, independent of the number of clauses,
literals, hash entries, variable count and numeric precisions. 
