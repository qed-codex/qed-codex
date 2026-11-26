---
{
  "module": "OAI/Computability/VPVNP/PairShrinkHiddenStep.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkHiddenStep.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkHiddenStep.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading and guessing one stored absorbed-field row

The width reader follows the dense ID to the selected term's repetition and
role payload cells. The private destination is computed from that same ID.
The finite guess loop consumes precisely the indicated number of bits.


### `Stage`

 Labels of the complete field scan, partitioned into its outer controls, 18 width-reader
instructions, and seven private guess instructions. 

### `instruction`

 Emit one row of the field scan, linking the width reader to the slot address calculation
and the private guess loop to the remaining-count decrement. 

### `Linked`

 Every scan stage has its specified instruction in the machine at the supplied program
counter, using the given registers and exit address. 

### `Args.width`

 Width word for the given dense hidden ID, obtained from the opposite-layout role's payload
plus the term repetition count times the selector width. 

### `Args.header`

 Width-reader trace for the field whose dense ID is stored at the supplied pointer. The ID
determines the term row and hidden role to probe. 

### `Row`

 Each pair consists of a dense hidden ID and the actual independent
bits to consume. Address and width conditions are checked against memory. 

### `ValidAt`

 The external directory entry matches the field's dense ID, the term gives exactly its bit
length, and its private slot's exclusive bit end fits in a machine word. 

### `ValidRows`

 Each field in the list satisfies the ID, width, and slot-end checks at its successive
position in the owner's external row. 

### `storeRows`

 Update private memory in row order by storing each field's bit list at the slot selected by
its dense ID. 

### `fieldEvents`

 Trace for one field through the width lookup, the three slot-address instructions, and the
private guesses of its bit list. 
