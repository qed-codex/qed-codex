---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafWeightProgramModel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafWeightProgramModel.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafWeightProgramModel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The native three-mask branch computes the exact squarefree head weight. 

### `localBoolWeight_eq`

 This also covers empty ambient sets and empty support intersections. 

### `result_decode`

 Supplying the actual encoded zero and one is sufficient: the executed
branch, rather than a semantic weight callback, chooses the correct word. 

### `program_localBoolWeight`

 One complete physical execution, including preservation of all five
masters, returns the exact local Boolean weight at its measured bit cost. 
