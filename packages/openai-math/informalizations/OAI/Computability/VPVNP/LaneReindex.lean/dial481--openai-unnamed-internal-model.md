---
{
  "module": "OAI/Computability/VPVNP/LaneReindex.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LaneReindex.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LaneReindex.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Relabeling the binary lanes of a wire network

The compression steps split the current lane into fresh port or packing
coordinates and the remaining lane. An additive equivalence on lanes
transports every base displacement, and its inverse recovers each original
width. This gives a network isomorphism and preserves the wire energy.


### `relane`

 Relabel all lane displacements using the same additive equivalence. 

### `relaneWidths`

 A wire keeps the width at its original outgoing slot and lane. 

### `relaneIso`

 Inverse lane relabeling identifies both ends and the payload of each
actual wire. Separate slots remain separate edges. 

### `relane_card_sites`

 The lane coordinate change preserves the number of positions. 

### `relane_sum_widths`

 Every sum over wire widths is preserved, in particular the sum of
squared widths divided by the common arc mass. 
