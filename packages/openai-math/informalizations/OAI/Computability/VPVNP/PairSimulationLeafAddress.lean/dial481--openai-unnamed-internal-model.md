---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafAddress.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafAddress.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafAddress.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The native leaf address and auxiliary header reader

The descriptor address on the depth-first stack identifies a row in the initial
cursor layout. The reader divides out the row stride, recovers the cursor and
the two blocks of address bits, and reads the complete auxiliary header word.
Beyond the prepared shadow region it supplies zero without probing memory.


### `Reg`

 Registers for dividing a DFS node address into its row index, cursor and site, then loading
the site's auxiliary header word. 

### `Field`

 The row base and stride, two coordinate radices, and shadow base and span consumed by the
leaf address decoder. 

### `decode`

 Decode the two coordinates with the arithmetic of the host's word width. 

### `decode_leaf_row`

 The native word decoder recovers both coordinates of the auxiliary processor
from the physical address of its initial traversal row. 

### `instruction`

 Both exits receive the cursor, site, and header. The node register is read-only. 

### `Linked`

 The machine contains all 20 decoder instructions at the assigned labels, with the specified
register placement, operands, and launch and transit continuations. 

### `Preserved`

 Every register except the eight scratch slots is preserved, including the DFS node. 

### `head_native`

 The address arithmetic, including the bounds-test operands, occupies the first sixteen slots. 

### `events`

 The sole possible probe is issued at the translated physical address. 

### `header`

 Read the site's word at the shadow base plus its index. Return zero when the index reaches
or exceeds the prepared span. 

### `native`

 Every continuation receives the original bit suffix and external memory, the decoded
coordinates and the complete word, after the nineteen indicated instructions. 

### `headerMemory_widen`

 The auxiliary header at physical width `W` returns the widened virtual word,
including the complete nominated histogram and the zero padding. 

### `prepare_initial`

 Running the live descriptor and copy calls establishes the shadow-memory
hypothesis used by the leaf reader, including when the virtual width is smaller. 

### `header_initial`

 The translated read agrees with the virtual auxiliary RAM at every address,
including addresses beyond the histogram. 

### `leaf_native`

 On the descriptor emitted for this cursor processor, the fixed native table
enters the matching validator or transit routine with the entire auxiliary word.
The shadow hypothesis is the memory postcondition of header preparation. 
