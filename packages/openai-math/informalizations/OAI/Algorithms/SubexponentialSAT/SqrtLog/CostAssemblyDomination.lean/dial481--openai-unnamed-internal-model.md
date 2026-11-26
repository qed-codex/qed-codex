---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/CostAssemblyDomination.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CostAssemblyDomination.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CostAssemblyDomination.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Lower bounds on the assembled counter used to substitute concrete native
costs.  Positivity of actual inventories is explicit, since upper resource
bounds alone do not exclude empty, degenerate records. 

### `quadratic_headAssignments_le`

 The quadratic head-assignment factor in native bucket grouping is paid
by a square of the assembled counter, not by an ordinary polynomial in n. 
