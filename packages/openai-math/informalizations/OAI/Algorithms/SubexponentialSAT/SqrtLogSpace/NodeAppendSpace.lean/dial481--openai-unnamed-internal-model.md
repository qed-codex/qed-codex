---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NodeAppendSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NodeAppendSpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NodeAppendSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

### `command`

 Actual cache staging, original native readout, and order-preserving append. 

### `command_eval`

 This fixed command includes the actual cache copies, native readout and all
three transfers. No staging or concatenation service is assumed. 

### `run_space`

 The exact accumulated stream and all source prefixes belong to the same
concrete run. The bound includes all 896 incoming words and append scratch. 

### `handoff`

 Final paid handoff from the complete interpolation stream to the actual CRT
jet input. Two transfers retain the byte order. 

### `output_codes_dense`

 The appended bytes are the actual increasing-order coefficient codes. The
readout is additive and is used only after the completed node-array sum. 
