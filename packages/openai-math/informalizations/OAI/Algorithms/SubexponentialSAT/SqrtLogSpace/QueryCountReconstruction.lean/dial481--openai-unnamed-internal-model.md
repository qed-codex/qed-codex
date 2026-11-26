---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryCountReconstruction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryCountReconstruction.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryCountReconstruction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The coefficients emitted by the actual ordered node loop determine the
same fixed-length Hermite inputs consumed by the native reconstruction tail.
No canonical choice of coefficient bytes across node states is required. 

### `jets_of_outputs`

 Package the very coefficient words emitted at each node. The witness
selection is proof-only; the actual machine already retained their flat bytes. 

### `outputs_take_length`

 Each physical node output retains exactly all J coefficient words,
including zero coefficients. Every prefix of the stream therefore has the
same exact linear storage charge. 

### `run_space_of_outputs`

 The native recovery consumes exactly the ordered coefficient words emitted
by the node loop. Its Hermite certificate is derived from those same words. 

### `run_space_of_outputs_with_full_frame`

 The native recovery consumes exactly the ordered coefficient words emitted
by the node loop. Its Hermite certificate is derived from those same words. 

### `query_run_space`

 The authentic native source and produced precision determine the recovered
natural count. No target-value, degree, no-wrap, or HasJets service is supplied. 
