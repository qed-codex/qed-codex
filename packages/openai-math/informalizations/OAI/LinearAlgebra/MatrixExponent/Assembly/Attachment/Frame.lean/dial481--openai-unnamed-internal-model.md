---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Assembly/Attachment/Frame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Assembly/Attachment/Frame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Assembly/Attachment/Frame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Keeping frozen tables while the core moves

A second local record contains the full border and the tether endpoints.
Host addresses and the block number are shared with the core record. The
first station slot is reserved for the core, even if it is empty.


### `Encloses`

 The core and the border records must describe the same individual
core bits, in order. A frozen table is kept on its own assigned slot. 

 # Common stage boundary while the border is retained 
