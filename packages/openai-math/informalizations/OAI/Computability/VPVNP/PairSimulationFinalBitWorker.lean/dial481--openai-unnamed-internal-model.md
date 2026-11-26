---
{
  "module": "OAI/Computability/VPVNP/PairSimulationFinalBitWorker.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationFinalBitWorker.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationFinalBitWorker.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Final shared-bit worker on the eleven-operand pair interface

Each call reads the total width from the terminal header. A live ordinal
takes one choice and writes it in reverse address order. The closing ordinal
accepts with an empty choice stream, and an ordinal above the total rejects.


### `header`

 Base word of the terminal header shared with the stage controller. 

### `instruction`

 Instructions for computing the header address, testing the ordinal and writing one chosen bit. 

### `table`

 Width-independent terminal shared-bit table with all eleven live public operands. 

### `total`

 Number of wire bits published in terminal header cell 12. 

### `base`

 First wire address published in terminal header cell 13. 

### `address`

 Physical destination of the bit chosen at this ordinal. 

### `activeReport`

 Report of a data call, including both header reads and its sole external write. 

### `closeReport`

 Report of the accepting call at the final ordinal. 
