---
{
  "module": "OAI/Computability/VPVNP/PairShrinkRoleChildTyped.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleChildTyped.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleChildTyped.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Recovering the old half-wire assignment from the native child tape

The outgoing slot order and the inverse incoming slot order reconstruct both
independent halves of each child. The native reader therefore returns the
actual typed arguments of a supplied witness, and every complete decode in
placement order yields such an assignment.


### `Child.half`

 The inverse to recording independent outgoing and incoming slot fields. 

### `exists_placed`

 Every list decoded in the placement order comes from old half-wire values
at precisely the sites in the placement fiber. 

### `Child.uniquePrefix`

 A site's exact tape prefix determines its entire independent slot assignment
and the rest of the tape uniquely. 

### `reader_encoded`

 Feeding the encoded list of arbitrary typed children returns the very same
list, writes its packets, and leaves the supplied kernel suffix intact. 

### `placedReader`

 The old half-wire part of the abstract site parser. 

### `reader_placed`

 Reading a placed half-wire witness consumes precisely its encoding and
returns the corresponding old children in the descriptor's order. 

### `reader_unique_placed`

 The exact tape, old sites, slot values, and scratch returned by a complete
native read determine one placed half-wire assignment. 

### `reader_childPackets`

 The actual native writes on the semantic witness establish exactly the
typed packets carried by the local vertex job. 
