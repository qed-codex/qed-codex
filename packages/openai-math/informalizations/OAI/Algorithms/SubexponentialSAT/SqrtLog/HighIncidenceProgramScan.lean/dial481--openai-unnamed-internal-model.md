---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HighIncidenceProgramScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HighIncidenceProgramScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HighIncidenceProgramScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Full original-coordinate scan using a runtime unary loop counter. 

### `highPrefix`

 Reverse order is the physical stack order; reversing gives coordinates
`0, ..., n-1`. Unused coordinates have degree zero and are retained in the mask. 

### `scanProgram_primitive`

 One fixed primitive bit machine, polynomial in actual encoded scopes,
original ambient dimension, and the supplied integer cutoff. 
