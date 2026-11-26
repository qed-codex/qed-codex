---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotNetwork.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotNetwork.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotNetwork.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The selected shrinking layout in the RAM slot directory

Both ends of an actual arc have adjacent field identifiers. The low bit is
zero for the outgoing end and one for the incoming end. The real owner array
uses the same convention on absolute sites. The native row and inverse scans
therefore leave two direct tables from which the next substep can query its
incoming site and slot using its outgoing site and slot.


### `siteIndex`

 Direct mixed-radix index of one absolute site. 

### `slotDirectory`

 Decode one candidate field by splitting off its side bit and using the
actual arc-address decoder. The owners are the two role endpoints of the
chosen layout, including the cyclic target of each padding arc. 

### `slotDirectory_degree`

 The two side arrays have exactly the common degree at each real owner. 

### `rectangular_slot`

 Every rectangular RAM index contains the regularized graph's prescribed
slot at the specified absolute endpoint, with the orientation bit retained. 

### `oppositeLookup`

 Starting with the rectangular outgoing slot, fetch its absolute field,
advance to the adjacent incoming field, and read the incoming rectangular slot. 

### `lookup_from_tables`

 The two native reads on any occupied outgoing slot return the incoming
slot of the same arc. The numbers used here are the paper's slot numbers by
`rectangular_slot`. Lane zero can use the destination site to read off the
remaining-lane displacement; the other lanes use the same matching. 
