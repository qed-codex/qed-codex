---
{
  "module": "OAI/Computability/VPVNP/LiveConfigGather.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveConfigGather.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveConfigGather.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Gathering a live configuration word from contiguous bit cells

One burst call reads the `w` bits of one cut word, least significant first.
Each source cell must be zero or one. The running sum and binary place are
machine words; doubling the place at the final bit may wrap. The completed
word is written once, then the next call processes the next word.


### `Block`

 A native configuration-gather code block with 32 registers and four public operands. 

### `Pub`

 The four public operand indices of the configuration-gather worker. 

### `Reg`

 The 32 register indices available to the configuration-gather worker. 

### `load`

 The public parameters are source bit base, destination word base, word
width and word count. A call's persistent word is its destination index. 

### `readBit`

 Read one source cell, verify that it holds a bit, add its place value to the word, and
advance the bit index and place. 

### `scan`

 Repeat the bit-reading block until the current word's specified width has been processed. 

### `save`

 Write the gathered word at the destination and prepare the next word's cursor. 

### `body`

 The complete word-gathering flow, from loading operands through the bit scan to the
destination write. 

### `table`

 The native burst-call template for gathering one word, using the next cursor and word-count
registers to control its return. 

### `loaded`

 The register bank at scan entry, with source and destination addresses for the current
word, a zero accumulator, and unit place. 

### `advanced`

 The register bank after consuming one source bit, including the updated sum, doubled place,
and incremented bit index. 

### `folded`

 The register bank after incorporating the supplied bits in little-endian order. 

### `scanEvents`

 The loop-test, source-read, and arithmetic events for scanning the given sequence of
configuration bits. 

### `events`

 The full event sequence for a successful word-gather call, ending with the reconstructed
word's destination write. 

### `BitImage`

 A complete word's little-endian bit image at its source address. 

### `gather_call`

 The genuine scheduled call executes the bit loop and writes the entire
decoded word. Surplus branch bits are rejected at its terminal instruction. 

### `report`

 The complete native report, including the final cursor comparison. 

### `gather_call_at_fuel`

 Uniform fuel bound at every cursor, with the exact report for a normal
call and rejection of every nonempty choice stream. 
