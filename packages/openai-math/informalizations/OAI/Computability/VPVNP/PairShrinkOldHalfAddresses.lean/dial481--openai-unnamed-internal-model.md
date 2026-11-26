---
{
  "module": "OAI/Computability/VPVNP/PairShrinkOldHalfAddresses.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkOldHalfAddresses.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkOldHalfAddresses.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Stored old half-wires at the four shrink demand endpoints

At A and B each demand coordinate uses the old wire and bit selected by
the common bundle ordering. At C and D it uses the original unsplit wire.
The incoming pointer is at the actual target and its incoming slot. All
four reads allow arbitrary independent child half-wire assignments.


### `Packet.read_field`

 A child packet already present in scratch supplies each of its slot fields. 

### `position`

 Packed position at the chosen end of the old directed arc. 

### `slot`

 The slot of this directed arc at the original child. At the incoming
end the forward incidence column gives the destination slot. 

### `address`

 Private address of an old directed arc's chosen half, obtained from the corresponding old
site, its DFS node, and its oriented slot. 

### `halfWord`

 Independent word of the packed half-assignment. 

### `slot_bits`

 Reindexing from the old numbered state to packed coordinates reads the
actual outgoing or incoming slot of that arc. 

### `read`

 Native memory at the numbered pointer contains the word used by the packed
kernel at this endpoint. 

### `PlacedPackets`

 Scratch contains the child packets for precisely the old sites placed
at the given new site, with the packing isomorphism reversed on their values. 

### `abSite`

 Select the A site at the source end of the AB demand and the B site at its target end. 

### `abData`

 Source or target bits to be copied by the AB slice loop, in original
thick-wire coordinates. 

### `abData_A`

 Repartitioning the stored outgoing AB bits yields the A row. 

### `abData_B`

 Repartitioning the stored incoming AB bits yields the B row. 

### `cDirection`

 The unsplit C endpoint is incoming precisely when the old source is thick. 

### `noncomputable local instance : DecidableEq X.Base`

 Classical equality of old base vertices for resolving the sites and slots of placed demand
halves. 

### `placedInput`

 The placed old halves that the reindexed shrinking kernel reads from the
selected child assignment, in the packing coordinates of the demand rows. 

### `placedPackets_after_children`

 The native child batch supplies all and only the old sites at this
resident's placement. A child packet is found by its genuine fiber index. 

### `Header`

 Runtime addresses of the preceding descriptor layer and its old state
columns, together with the private argument arena parameters. 

### `Header.arenaBase`

 First private address of the argument arena in which the old node's packet is stored. 

### `Header.arenaStride`

 Word stride between private argument frames for consecutive node addresses. 

### `Header.layerBase`

 External DFS row base of the old layer supplying the child packets. 

### `Header.layerStride`

 Distance in external words between adjacent site rows in the old DFS layer. 

### `Header.actualOut`

 Head of the forward incidence column mapping an old outgoing slot to its actual target
  slot. 

### `Header.actualIn`

 Head of the inverse incidence column used to identify the outgoing arc of an incoming
  slot. 

### `Header.width`

 Head of the numbered old-arc widths used to locate a slot inside a packed half-wire
  argument. 

### `Header.port`

 Resolve the endpoint's own numerical port, using the forward incidence
column when the operand is at the destination. 

### `Header.input`

 Divide an oriented port by the degree to recover its site ordinal, then assemble the node
address, arena, and width-prefix inputs for the field reader. 

### `Header.field`

 Compute the pointer using only the row's old arc ID, stage pointers and
the fixed-degree prefix of actual widths. 

### `Header.Stored`

 The evaluated header supplies the designated arena start and stride, old layer start and
pitch, and the actual outgoing, incoming, and width column heads. 

### `field_eq`

 Evaluation of the physical expression yields the old half-wire pointer
at the real descriptor address of this endpoint's child. 

### `childNode_eq`

 The physical layer ordinal here is the one used by the native child
scan when it assigned the argument packet. 
