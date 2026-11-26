---
{
  "module": "OAI/Computability/VPVNP/PackingPreimages.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PackingPreimages.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PackingPreimages.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Old positions at each packed site

In either layout of §7.2 each new site receives exactly `K = 2^c d` old
positions. Half are thick and stay at their site. For thin positions the tag
offset and the chosen side of the bundle permute the ports. Each of the new
site's ports therefore receives the thin half of one old color-word fiber.


### `positionBitFiber`

 Recover the old site and slot from a routed port. The only free field
at that port is the bit word with its prescribed old color bit. 

### `card_placement`

 Every new position has exactly `K` immediate old positions in its history,
for either common layout. 
