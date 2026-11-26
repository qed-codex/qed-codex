---
{
  "module": "OAI/Computability/VPVNP/PairSimulationHistoryBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationHistoryBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationHistoryBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Size of the binary stream at a final vertex

Only locally summed fields contribute bits at an internal history node.
The other bits belong to the placement-fiber children. This gives the
same recursion as the occurrence count in Theorem 7.1, with the maximum
per-record or initial-validator bit length as its multiplier.


### `SiteParsers`

 Local vertex factors with their finite monomial choices and binary
readers. The factor may depend on independently chosen half-wires. 

### `SiteParsers.factors`

 Value of each site's factor as a function of its incident half-wire assignment. 

### `SiteParsers.witnesses`

 Finite monomial expansion of each site factor at the given half-wire assignment. 

### `SiteParsers.read`

 Binary reader for a monomial witness choice at a site with the specified incident
  half-wire assignment. 

### `TermParsers`

 Data for reading one compression term's contribution at an output site, including the child
order, input payload readers, and local kernel witnesses. 

### `TermParsers.order`

 Orders of the children at each output site and of the two families of incident arcs at
  each child. 

### `TermParsers.payload`

 Binary reader for the payload type of each input arc, used to encode the children's
  half-wire assignments. 

### `TermParsers.witness`

 Monomial expansion of the local kernel for each output site, placed input assignment, and
  output half-wire assignment. 

### `TermParsers.read`

 Binary reader for a choice in the local kernel's monomial expansion at the supplied
  arguments. 

### `TermParsers.push`

 Push the input site factors and their parsers through the term. The output parser reads the
old halves, a local kernel choice, and the children in descriptor order. 

### `TermParsers.ownBits`

 The bits consumed at the node, before it expands any children. 

### `TermParsers.Covered`

 The descriptor's fields cover the old halves and locally summed indices.
A field used by several maps can appear once on the left-hand side. 

### `outgoingOrder`

 The outgoing descriptor list has the native outgoing-slot order. 

### `incomingOrder`

 The incoming descriptor list follows the inverse slot permutation.
Thus parallel arcs appear at their own incoming and outgoing positions. 

### `statePass_covered`

 The common slot-record constructor charges each old half and all
absorbed-word bits to genuine fields of the new site. 

### `ChainParsers`

 Parsers for the actual terms on one selected branch. 

### `finalParsers`

 Propagate the initial site parsers through each term to obtain parsers for the final
network. 

### `Covered`

 At every term and output site, the bits for the old halves and the local kernel choice fit
within the sum of that site's recorded field widths. 

### `finalParsers_bound`

 A vertex's binary choices are bounded by its recursive history size
times the largest allowance for one field or initial validator. 

### `finalParsers_blockBound`

 Combine the local parser's size recurrence with the compressor's block
count, field widths and initial-vertex bit bound. 

### `stateOrder`

 Supply the fixed native slot numbering and use only the recorded list
of old child positions at each output site. 

### `shrinkStateParsers`

 Parse the shrinking pass in the dyadic state coordinates actually used
by the scheduled procedure. 

### `shrinkStateParsers_covered`

 The concrete kernel's word choices are included in the original
shrinking-site descriptor used in the proof of Theorem 7.1. 

### `refreshStateParsers`

 The degree-refresh map in the same coordinates as the actual block execution. 

### `refreshStateParsers_covered`

 Its kernel is a deterministic entry check. Only the placed old halves
contribute private wire guesses, all covered by the slot records. 

### `cursorSiteParsers`

 The input factors and their concrete binary readers in compressor-state coordinates. 
