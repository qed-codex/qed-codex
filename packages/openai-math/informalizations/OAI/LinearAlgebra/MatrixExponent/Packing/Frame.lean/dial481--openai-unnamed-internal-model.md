---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Packing/Frame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Packing/Frame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Packing/Frame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Double counting the two ends of directed wires 

 # Internal and exterior arity of an aggregate site 


# Blocks on a common host

Retain a separate exterior port of the core for every tether bit.
The frozen tensors and all their other exterior legs need no transformation.
Recording the incidence and charges suffices to reattach them, term by
term, at the end of a sequence of contractions.


### `HostNet`

 All internal edges lie in the core. Frozen tables are indexed by `T`,
independently of the grouping and contraction history. 

### `Fringe.reserve`

 Reserved space for histories of eliminated wires. 

### `mass`

 Each eliminated internal port remains part of the local description. 

 # Conservation of load in a grouped core 

### `outside_le`

 Exterior and parked charges follow the site assignment. Only the
internal edges need a fresh estimate after contraction. 

### `reassign`

 Absorb the discounted history of old incident edges into their
existing port charge. New edges are charged at full width. 

### `Preserves`

 Every old occurrence has one destination. Frozen labels and tether
ports that coincide at an occurrence stay together. A common surjective
linear map on binary block indices controls all occurrences. Every host
has a uniform number of slots per old position, and parked tensors never
leave the slots allocated to their position. 


# Reattaching frozen tables

Each exposed slot on the core becomes a separate wire to its original frozen
table. Only the ports of the frozen tables remain exterior. Contraction is
linear in the core tensor, so exact sums survive reattachment.



# Separating off the frozen vertices

All exterior positions lie on frozen vertices. No internal wire
joins two frozen vertices. Partition the wires into core edges and
the two directions of tethers, giving each tether a separate name.


 # Partitioning parallel core wires into equal bundles 

### `Packets`

 Uniform packets of bits, each with one ordered pair of endpoints. 

 # Recovering loads from station arities 

 # Each tether uses a distinct port of its frozen table 


# Placing the split diagram on its block host

Uniform internal multiplicities suffice to construct the core bundles.
The two exterior legs of the core consist precisely of its tethers.
Every other leg stays attached to the original frozen table.


### `hostOf`

 The caller may specify the ordering within each packet. 
