---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpNodeCost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpNodeCost.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpNodeCost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # A polynomial instruction bound for the fixed four-coordinate node program 

### `cost_four`

 This is the actual composed-program budget, including all four tuple
expansions, nonzero filtering, initialization, and final control transfers. 

### `cost_le`

 A uniform polynomial bound; the exponent four comes from the fixed
dimension, not from an unbounded source-level loop parameter. 
