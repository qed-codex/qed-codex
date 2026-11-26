---
{
  "module": "OAI/Computability/VPVNP/SlotBundleCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotBundleCount.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotBundleCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact number of demands per packed bundle

For a fixed bundle, Appendix C counts outgoing thin-endpoint demands in the
original outgoing numbering and incoming demands from thick endpoints in the
original incoming numbering. The tag offset and lane slot are fixed in both
enumerations, leaving only the old arc slot and its color bits.


### `arcAtBundle`

 Actual arc at an endpoint with prescribed bundle assignment. The old
incident slot is independent of the assignment's outgoing-slot coordinate. 

### `assignedArcEquiv`

 A fixed assignment has one fiber for each incident slot, with the bit word
as its only free parameter. 

### `card_motifs_bundle`

 Every packed bundle receives exactly Q old wires as CD demands. 

### `arcBit`

 Original base-color bit at a numbered endpoint. 

### `card_bundle_types`

 For any two endpoint types, a fixed base arc and source site carry K/4
wires of those types, including the bundle's thick–thick wires. 

### `card_thick_bundle`

 Size of the thick–thick bundle whose payload is concatenated in §7.2. 

### `rolePortEquiv`

 Count motifs at an endpoint by splitting that endpoint into its ports.
The permutation is the identity for A and the site arc matching for B. 

### `card_roleA`

 Exactly dQ incidences of A occur at each packed site. 

### `card_roleB`

 Exactly dQ incidences of B occur at each packed site, including parallel arcs. 
