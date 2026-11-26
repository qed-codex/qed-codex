---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsAlgorithm.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsAlgorithm.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsAlgorithm.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Explicit finite list loops for head moments

The callbacks are the concrete bounded squarefree operations, not a source
evaluation oracle. The code computes every recursive result once. The cost
theorems charge every callback invocation; representation-specific costs are
substituted after the normalized-list size bound is proved.


### `head`

 One actual head bucket, with one scalar weight and one stored local jet
per assignment. No global assignment tuple is enumerated. 

### `heads`

 Multiply the independently computed head moments. 

### `run`

 Evaluate every retained support, extract it, and sum its contribution. 
