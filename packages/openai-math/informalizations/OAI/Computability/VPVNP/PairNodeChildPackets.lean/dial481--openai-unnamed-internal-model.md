---
{
  "module": "OAI/Computability/VPVNP/PairNodeChildPackets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNodeChildPackets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNodeChildPackets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Ordered arguments at the child addresses in a descriptor row

Each child keeps its old site number, its actual outgoing and incoming
half-wire coordinates, and its absolute DFS node. Machine writes to these
addresses give the same scratch update as the logical list of packets.


### `Child`

 An old site and all independent field values guessed there. 

### `Child.site`

 Site in the older network whose descriptor row and incidence widths determine this
  child’s argument buffer and field lengths. 

### `Child.data`

 Independent bit values for every outgoing and incoming slot at the child site, indexed
  within the actual half-wire width of that slot. 

### `Child.ofHalf`

 Forms a child record from a network half-wire assignment by reading its coordinates in the
outgoing and incoming incidence orders of the site. 

### `childNode`

 Absolute DFS descriptor address of the old site, obtained from its ordinal in site order
and the row layout with base older and capacity cap. 

### `Child.payload`

 Serializes the child’s fields in port order, first for outgoing ports and then for incoming
ports. Each field contributes exactly its own bits. 

### `Child.packet`

 Pairs the child’s absolute descriptor address with its serialized half-wire bits so the
pending-argument arena can store the payload at the corresponding node. 

### `choose_slots`

 Any complete prefix is a possible independent assignment to the half-wire
fields. Width-zero fields contribute an empty segment. 

### `choose_payload`

 Split off precisely one full child's half-wire packet from an arbitrary tape. 

### `children`

 Actual ordered old-site arguments of a parent term. 

### `storePackets`

 Applying native stores for a list of complete child packets. 

### `scratch_storePackets`

 Projection of the native private memory after all writes is exactly the
logical scratch update for the list of packets. 
