---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/VisitedTape.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/VisitedTape.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/VisitedTape.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Passive absolute-coordinate instrumentation for the primitive machine.
The interval on every tape includes its initial input cells and every visited
head coordinate. The instrumentation never changes a primitive transition. 

### `locatedTrace_space_le_of_length`

 Useful for polynomial-time preprocessing fragments only: substituting the
full exponential counting time here would not give polynomial space. 
