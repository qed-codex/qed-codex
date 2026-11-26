---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortGatherWord.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortGatherWord.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortGatherWord.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Moving one word of a sort block onto a reverse buffer

The input and buffer hold arbitrary bits. A separate unary word-width stack
is restored after the move so the same finite control can read all five
fields of a record and all records before the selected slot.


### `Port`

 Gather ports for the record block, unary offset and width, reversible width counter,
skipped and selected buffers and output. 

### `Port`

 The word mover's source block, reversible width tally and reverse destination buffer. 

### `Phase`

 Control for moving a fixed-width word bit by bit, saving width markers, then restoring the
width tally. 

### `code`

 Use one width marker per bit moved from the block to the destination and restore all
markers at the end of the word. 

### `Buffer`

 Distinguish a word from a skipped record from one belonging to the selected record. 

### `Buffer.dest`

 Use the saved-prefix port for skipped words and the selected-record reverse buffer for
selected words. 

### `word`

 Move one width-delimited word from the current block to the named reverse buffer. 
