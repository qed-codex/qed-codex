---
{
  "module": "OAI/Computability/VPVNP/CursorFieldOffsets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorFieldOffsets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorFieldOffsets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Contiguous field offsets on a cursor arc

The arc reserves one eight-word field for each successor mask class, followed
by one sorting block for each layer in phase order. The two choices of arc at
each cursor use the same layout. Its inverse recovers the system and in-field
index of every bit.


### `ramPayloadWidth`

 Length of the bit vector on either outgoing arc. 

### `ramFieldOffset`

 Number all bits in the arc payload, allowing empty fields and zero width. 

### `ramPayloadEquiv`

 Flatten the separate field functions to a single vector of arc bits. 

### `ramFieldAddress`

 Straight-line word arithmetic for a bit address. The sorting case computes
the triangular prefix from the phase and step counters. 

### `ramFieldAddress_work`

 The address calculation uses at most thirteen arithmetic instructions
regardless of the number of successor classes or sorting layers. 

### `ramFieldAddress_peak_le`

 Every temporary register fits below or at the total payload width. This
includes the product in the triangular prefix before division by two. 

### `ramFieldAddress_evalWord`

 With a register large enough to hold the payload length, modular word
evaluation gives the exact bit address. 
