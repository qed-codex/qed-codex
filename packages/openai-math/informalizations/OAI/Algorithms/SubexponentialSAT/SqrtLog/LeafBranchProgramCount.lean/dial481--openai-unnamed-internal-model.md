---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafBranchProgramCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafBranchProgramCount.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafBranchProgramCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Disjointness of the high-coordinate partition turns the native rank sum
into a full count over the original assignment space. 

### `enumerate_full_count`

 This theorem counts every original assignment exactly once. The inputs are
an actual measured residual program and its per-branch correctness proof. 
