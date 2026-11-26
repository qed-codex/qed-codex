---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramEntries.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramEntries.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramEntries.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Executable scalar specifications in the physical side/joint list order.
These definitions do not assert a primitive runtime bound: their exact
identification lets the separately traced scan/arithmetic producer feed the
semantic layout without an arbitrary finite-type ordering oracle. 

### `orderedHeadMatrix`

 This is only the mathematical name for the actual byte enumeration order;
no invocation of `Fintype.equivFin` enters the matrix producer. 
