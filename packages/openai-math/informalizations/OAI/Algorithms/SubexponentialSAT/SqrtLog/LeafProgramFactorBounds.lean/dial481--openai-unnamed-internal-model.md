---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramFactorBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramFactorBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramFactorBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The exact complete branch budgets admit a common polynomial bound.
Large sparse and incidence buffers are represented by explicit capacity and
live-word caps; none is silently bounded by the original formula bit length. 

### `branchBound`

 The source component is the checked, explicit native source polynomial.
The remaining branch cost is a fixed ninth-degree polynomial in actual sizes. 
