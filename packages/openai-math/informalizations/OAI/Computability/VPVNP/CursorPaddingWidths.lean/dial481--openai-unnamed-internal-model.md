---
{
  "module": "OAI/Computability/VPVNP/CursorPaddingWidths.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorPaddingWidths.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorPaddingWidths.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Bit widths and initial energy of the padded cursor network

A genuine cursor wire concatenates the message systems in their slot order.
Its zero-width copies contribute a unique empty word. Under the compressor's
equal mass per arc the initial energy therefore satisfies the bound in §12.


### `paddedWidth`

 Width of an actual edge, with the parallel copies carrying zero bits. 

### `paddedPayloadEquiv`

 Concatenate the system fields in the supplied order. On a padded edge
the singleton symbol is equivalent to the empty bit word. 

### `ramSystemOrder`

 The successor-mask classes precede the sorting layers, in layer ordinal order. 

### `paddedEdge_card`

 The regular graph has exactly one edge for every outgoing slot at every
processor-cursor position. 

### `padded_sqrtEnergy_le`

 Upper bound on the initial square-root energy with the actual padding
and the uniform mass on the resulting edges. 

### `cursorRAM_sqrtEnergy_le`

 Specialization to the RAM routing layout of §12, using its position count
and the total bit width of all successor and sorting message systems. 
