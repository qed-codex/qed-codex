---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparseAccumulatorProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparseAccumulatorProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparseAccumulatorProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A fixed finite binary accumulator with actual source traces and local prefixSteps bounds. 

### `command`

 One fixed bit program adds and immediately canonicalizes the accumulator.
The output occupies stack zero; both temporary stacks are empty at return. 

### `prefix_dataBits_le`

 The runtime bound is linear in both input word lengths, so this local
trace-growth estimate is polynomial independently of the number of leaves. 

### `canonical_execution`

 The same actual accumulator execution returns the canonical sum and has
linear all-prefix source-stack space whenever the sum is an `n`-variable count. 
