---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramNodeConcreteRows.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramNodeConcreteRows.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramNodeConcreteRows.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The source rows used by the native factor callback retain their concrete
origin, degree, and original-coordinate support after incidence pullback. 

### `fixedSourceRow_origin`

 Repeated incidences are allowed. The actual first matching lookup selects
one Kronecker row, whose owner is still the original literal. 
