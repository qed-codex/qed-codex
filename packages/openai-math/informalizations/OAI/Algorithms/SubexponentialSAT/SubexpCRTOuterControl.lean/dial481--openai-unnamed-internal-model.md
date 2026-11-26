---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpCRTOuterControl.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpCRTOuterControl.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpCRTOuterControl.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete tape operations and traversal assertions for the outer CRT.
All operations in this module are fixed finite programs. Arithmetic is supplied
by the separately defined concrete CRT service commands. 

### `scalarPorts`

 Native multiplication bank 128--204 is shared with local convolution. 

### `hornerPort`

 Horner's ten higher ports avoid the constants at 206, 207, and 211. 

### `SweepWords`

 These fields describe physical traversal stacks. Other stacks, including
the scalar bank and retained inputs, are framed by the execution theorems. 

### `loadCurrent_run`

 Exact physical loading of one node, its index, and its matching padded jet. 
