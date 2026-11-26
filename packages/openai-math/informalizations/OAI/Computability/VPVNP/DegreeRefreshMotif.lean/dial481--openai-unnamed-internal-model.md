---
{
  "module": "OAI/Computability/VPVNP/DegreeRefreshMotif.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DegreeRefreshMotif.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DegreeRefreshMotif.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The internal demand tensor of a degree refresh

In Section 7.3 of *VP and VNP differ over every field*, the nonlocal segment
ties in one block form two copies of the directed complete graph on the
ports, with its loops removed. The omitted ties are diagonal checks performed
locally. The remaining ties are evaluated on the binary wire basis used in
Theorem 6.1. An ordinary sum identity for this motif thus substitutes directly
into the external-wire contraction.


### `tieSource`

 Each demand edge starts at the port bearing the old half-wire. 

### `tieTarget`

 Its other endpoint is the slot port bearing the external segment. 

### `internalWidth`

 The old arc supplying this segment is recovered by inverting the port
permutation when the tie belongs to an incoming slot. 

### `internalDemand`

 The equality tensor of the two off-diagonal copies, in the basis
`Fin (2 ^ width)` of the fixed-motif theorem. 

### `PortSegments`

 Segment lists for the two external half-wires incident to a port, in
source-port order for the outgoing list and destination-port order for the incoming one. 

### `portSegments`

 Read the two incident external wires in the prescribed segment order. 

### `wordIndex`

 Encode a port's Boolean payload as the binary index of its motif wire. 

### `incomingHalf`

 Read an incoming half-wire directly from its destination port. 

### `portInput`

 The argument of a motif map at a single port. Its first coordinates read
the old incident wires, and its second coordinates read external segments. 

### `portDiagonal`

 Both diagonal ties are tested inside their common port. 

### `blockTies_factor`

 Entrywise decomposition into all local checks and the nonlocal binary
demand tensor, with each old half-wire and external segment read at its port. 

### `blockTies_expansion`

 Replacing the nonlocal ties with an ordinary sum of supply maps.
Each diagonal check is absorbed into the matrix at its own port. 
