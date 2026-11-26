---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/PairScoreBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PairScoreBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PairScoreBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Closed bounds for the actual tuple generator and pair scorer

All costs below are the explicit bounds attached to proved executions of the
fixed programs.  The tuple recurrence is bounded from its actual list sizes;
no scalar-operation or callback-cost oracle is assumed.


### `stepCost_add_two_le`

 One actual expansion, including its loop overhead, has a uniform bound
in the number and maximum width of its input records. 

### `powerCost_le`

 The actual repeated Cartesian expansion is linear in its final tuple
count, with a fixed polynomial factor in depth and physical word width. 
