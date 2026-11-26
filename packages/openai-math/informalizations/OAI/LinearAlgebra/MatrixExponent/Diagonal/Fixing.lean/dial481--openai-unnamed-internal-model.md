---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Diagonal/Fixing.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Diagonal/Fixing.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Diagonal/Fixing.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reconnecting processor inputs

Copies at the same input position have the same label. Consequently
all occurrences of a broadcast or physical bit are colocated at a
single worker. Only literal bits may require additional communication.


 # Summing over copies of the literal bits 

### `mask`

 Each worker imposes only its own literal, without knowing the
program or wiring information provided to any other processor. 
