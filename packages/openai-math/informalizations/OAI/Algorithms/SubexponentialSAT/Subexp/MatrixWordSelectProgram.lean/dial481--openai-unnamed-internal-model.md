---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/MatrixWordSelectProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/MatrixWordSelectProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/MatrixWordSelectProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Select one fixed-width framed scalar from the coefficient stream using
the actual persistent array reader, then decode its frame. The index and
frame width are supplied as unary runtime data. 

### `command_eval`

 The selected scalar is returned on stack 0; the coefficient array and
frame-width template are preserved, and the index is consumed. 
