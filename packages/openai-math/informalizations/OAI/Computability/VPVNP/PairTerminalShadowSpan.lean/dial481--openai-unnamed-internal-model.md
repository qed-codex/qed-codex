---
{
  "module": "OAI/Computability/VPVNP/PairTerminalShadowSpan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalShadowSpan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalShadowSpan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The auxiliary header length recovered by the terminal pair program

The histogram target is the third word of the seventh auxiliary descriptor.
Subtracting the shadow base from that target recovers the reserved bit-header
length, including both padded exterior cuts. The pair operand supplying the
histogram length completes the span used to bound a leaf's external read.


### `terminalOperands`

 The eleven public words supplied to the terminal pair program. 

### `histogramTargetAddress`

 The word preceding the counter base is the histogram's descriptor target. 

### `PreparedBranch.shadowSpan`

 Actual word computed by the eleven-operand terminal bootstrap on the
memory returned by the native auxiliary initializer and copy sweep. 

### `histogramTarget_lt_workspace`

 The histogram descriptor is strictly below the compression workspace. 

### `PreparedBranch.shadowSpan_of_frame`

 Changes confined to the compression workspace preserve the recovered span. 
