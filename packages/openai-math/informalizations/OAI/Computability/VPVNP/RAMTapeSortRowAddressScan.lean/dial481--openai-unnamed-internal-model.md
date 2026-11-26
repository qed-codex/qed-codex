---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortRowAddressScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortRowAddressScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortRowAddressScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Indexed bit reads and stride-bit flips in the row address machine 

### `read`

 Read a little-endian bit with zero extension. 

### `flip`

 Toggle a bit within a fixed width. An out-of-range index preserves the word. 

### `Port`

 The bit stream, unary position counter, reverse buffer and one-bit result of an indexed
address scan. 

### `State`

 Control for consuming the unary index, recording or flipping the addressed bit, draining
the remaining stream and reporting the result. 

### `code`

 The same scan is used in two modes. A read returns the observed bit.
A partner scan emits the modified word in high-to-low order and returns
whether the stride bit belongs to the row. 

### `bank`

 Install the source bits, remaining count, reversed bits and result flag on their
indexed-scan ports. 

### `routine`

 Read the requested bit with zero extension, or in peer mode toggle it when present and
produce the reversed partner bits and local-stride flag. 
