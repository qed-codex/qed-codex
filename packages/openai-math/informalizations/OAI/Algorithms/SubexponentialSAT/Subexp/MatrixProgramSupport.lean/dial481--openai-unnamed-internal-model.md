---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/MatrixProgramSupport.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/MatrixProgramSupport.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/MatrixProgramSupport.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed stack and frame-reading routines used by the encoded matrix checker. 

### `readWord_eval`

 Decode one frame and restore its little-endian order. 

### `emitFrame_eval`

 Consume a raw word and prepend its complete frame, with every encoding
step performed by fixed instructions. 
