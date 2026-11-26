---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotAddresses.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotAddresses.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotAddresses.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Scanning the address space for surviving slot records

The absolute arc record uses a mixed-radix word. Every address can be decoded
locally into an old arc, a role edge, a subdivision, and an absolute lane,
or into a dummy site and dummy number. Only thick–thick old arcs and subdivision
numbers outside their type's range leave holes in this space.


### `ActualId`

 Identifier of a surviving arc, either a role edge and subdivision of a motif or a dummy
slot at a packed site. 

### `RecordCount`

 Size of the address space for surviving slot records, including unused genuine candidate
addresses and all dummy slots. 

### `decodeArc`

 Random-access decode of one numeric arc address. 

### `decodeArc_eq_some`

 Scanning numeric addresses visits every genuine or dummy arc exactly once. 

### `address_genuine_val`

 The high-order component of a genuine arc address is the relative key,
and the low-order component is the absolute lane of its original CD arc. 

### `address_div_lane`

 Taking the quotient of the absolute genuine record address recovers its
relative integer key directly. 
