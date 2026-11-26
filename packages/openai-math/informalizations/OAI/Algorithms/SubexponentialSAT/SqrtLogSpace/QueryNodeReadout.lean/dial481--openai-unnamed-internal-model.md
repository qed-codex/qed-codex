---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryNodeReadout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryNodeReadout.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryNodeReadout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The actual node dictionary is read into increasing Taylor coefficients,
appended to the interpolation stream, and reclaimed before the next node.
The dictionary witness, encoded result and resource trace are shared. 

### `list_of_readout`

 Equal truncated coefficients identify the complete fixed-length list,
including retained zero coefficients. 

### `master_common`

 Every readout cache comes from the actual retained query words. 

### `master_ready`

 Every readout cache comes from the actual retained query words. 

### `codes_value`

 The produced native coefficient words represent exactly the node's
additive shared-marker readout, in increasing Taylor order. 

### `run_common`

 Read, serialize, append and finish one completed interpolation node.
All zero Taylor slots remain in the actual stream; the next node index and
cursor guard are updated by paid native instructions. 

### `run`

 The original pair-specific entry remains an immediate specialization. 
