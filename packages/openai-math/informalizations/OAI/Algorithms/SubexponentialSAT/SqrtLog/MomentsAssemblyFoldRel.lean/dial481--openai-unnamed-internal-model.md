---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsAssemblyFoldRel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsAssemblyFoldRel.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsAssemblyFoldRel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The execution-associated relational fold used by moment assembly. Keeping
this relation in its own module lets machine proofs depend on the relation
without importing the materializing moment-assembly programs. 
