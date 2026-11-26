---
{
  "module": "OAI/Computability/VPVNP/PairRefreshHalfDecoder.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshHalfDecoder.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshHalfDecoder.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading the two independent arguments of a refresh node

The parent packet is read at its absolute DFS arena address. The unique old
half is parsed from the remaining choice tape in outgoing-then-incoming slot
order. Both operations use the state network's actual variable slot widths.


### `reader`

 Decode a half-wire assignment in outgoing slot order followed by incoming slot order, using
the state's payload widths. 

### `width`

 Total number of bits in the site's outgoing and incoming half-wire fields. 

### `packetBits`

 Read the parent's packed argument from private scratch as bits, interpreting a stored word
equal to one as true. 

### `parent`

 Read the parent packet from its DFS arena and decode its local half-wire assignment. The
packet supplies exactly the required number of bits. 
