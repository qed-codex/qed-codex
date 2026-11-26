---
{
  "module": "OAI/Computability/VPVNP/PairSimulationTerminalRootGatherLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalRootGatherLayout.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalRootGatherLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Addresses and words gathered by a terminal vertex

The final slot count includes all sites. Its quotient by the number of sites
is the actual number of slots per site. Outgoing slots address the width and
prefix tables directly. Each incoming slot first selects its matched outgoing
slot from the inverse incidence table.


### `Layout`

 Addresses and sizes used to gather one final site's incident wire words from external
memory into the private argument block for its DFS root. 

### `Layout.vertex`

 Ordinal of the selected final site, used to locate its contiguous interval of incidence
  slots. 

### `Layout.sites`

 Number of final sites sharing the slot table. Dividing the total slot count by this value
  gives the scan length for one site. 

### `Layout.slots`

 Total number of slots across all final sites in one direction of the incidence table. 

### `Layout.widthHead`

 External base of the table giving the number of wire words for each outgoing slot. 

### `Layout.incomingHead`

 External base of the inverse incidence table mapping each incoming slot to the outgoing
  slot of its wire. 

### `Layout.prefixHead`

 External base of the exclusive width-prefix table. Its entry for an outgoing slot is that
  wire's offset from the wire bank base. 

### `Layout.wires`

 External base address of the packed wire words addressed by the slot prefix table. 

### `Layout.n`

 Private argument bank base supplied in public word six. The gather adds the root's stride
  offset to obtain its packet destination. 

### `Layout.root`

 Descriptor address of the selected site's DFS root, used as the index of its private
  argument block. 

### `Layout.stride`

 Number of private words between argument blocks for successive descriptor addresses,
  loaded from the geometry header at startup. 

### `degree`

 Slots scanned in each direction at one final site, computed by dividing the total slot
count by the site count. 

### `index`

 Global slot index at offset `j` in the selected site's interval. At the site degree it
gives the exclusive loop bound. 

### `edge`

 Outgoing slot that owns the wire at a local endpoint. Outgoing slots use their global index
directly, while incoming slots read their partner from the inverse incidence table. 

### `width`

 Length in words of the selected endpoint field, read from the width table using its
outgoing slot index. 

### `start`

 First external address of the endpoint field, obtained by adding its outgoing slot's
exclusive prefix to the wire bank base. 

### `field`

 Contiguous wire words of one selected slot in increasing external address order, including
the empty list for a zero-width slot. 

### `fields`

 Endpoint fields for all slots of the chosen site and direction in local slot order,
retaining their individual field boundaries. 

### `packet`

 Root argument packet in copy order, with all outgoing fields concatenated before all
incoming fields. 

### `dest`

 First private address of the root packet, equal to the argument bank base plus the root
descriptor address times the stride. 

### `Fits`

 Exactly the words whose addresses or endpoints must fit in a native
register. The source and destination cursors also hold the exclusive end. 

### `placed`

 Closed form of the private block written by the endpoint gather. 
