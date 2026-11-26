---
{
  "module": "OAI/Computability/VPVNP/PairSelectedPacketFormat.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSelectedPacketFormat.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSelectedPacketFormat.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Typed packets at all rows of a selected traversal

A genuine packet consists of an actual row header and a half-wire value
encoded in that row's state. This remains a finite union of genuine row
formats when the tape after the current vertex is arbitrary.


### `AtRow`

 The packet pairs a site's row-header address in the supplied order with the encoded bits of
a half-wire assignment at that same site. 

### `PacketFormat`

 Each packet witnesses a concrete site and half assignment in the
initial state or the true output state of one selected pass. 

### `PacketFormat.cases`

 The format provides the exact typed input of a heterogeneous physical
row parser. In the second case the dependent pair identifies both the pass
occurrence and its site, using the shared directory's native address. 

### `PacketFormat.node_lt`

 All formatted packets fit in the published row region. This is an
address bound before converting the natural header to a machine word. 

### `SelectedPacketFormat`

 Packet format for the chosen execution branch at the template's record limit. Its row and
payload come from either the initial cursor layer or an output layer of a selected pass. 

### `selected_format`

 Both the old half packets guessed at a physical level and the real
terminal root packet at the final layer have the selected format. 
