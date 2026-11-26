---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Spectral/Path.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Spectral/Path.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Spectral/Path.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Direct sums as ordinary sums of restrictions

Expanding the source direct sum gives independent local matrices for
each summand. The formula holds in all characteristics.


 # Bit-label coordinates for arbitrary products of wires 

### `mask`

 Keep the bits incident to the given site. 

### `signals_prod`

 Each bit is visible at its two endpoints. Other sites see a fixed
dummy value in the same coordinate. 

 # From a direct-sum restriction to local bit tables 

### `packet_of_restriction`

 Expanding the direct sum and acting on the shared-label
coordinates gives one independent sum of local products per summand. 

 # Serial composition of exact wire packets 

### `Rule.series`

 Joining the last endpoint of each first demand to the first endpoint
of its successor requires no additional wires, even when sites coincide. 

### `Rule.path`

 Several paths may share sites. Their wire variables remain distinct. 

 # Reindexing a packet and keeping extra wires unchanged 

### `together`

 Disjoint union of two indexed families of directed edges. 

### `Rule.keep`

 Keeping a wire costs one additional supply bit and no selector. 

 # Parallel composition and placement of wire packets 

### `Rule.place`

 Identify sites along an arbitrary map, multiplying the tables in each fiber. 

### `parallelDemand`

 Demand legs keep their component labels. 

### `parallelSupply`

 Each component activates its own supply according to its own selector. 

### `Rule.parallel`

 The selector set is a Cartesian product. Assignments to different
components remain independent even when their endpoints coincide. 

 # Selecting and deploying exact wire packets 

### `Rule.select`

 Pin both ends of each unused demand to zero. 

### `Rule.parallel_one`

 Parallel one-term packets need no selector. 

### `Rule.reverse`

 Exchange the two endpoints of every demand. 

### `Rule.join_outputs`

 Join the two output legs of a pair of demands by one new supply
wire. The input legs become the endpoints of a single demand. 

### `Rule.supply_equiv`

 Reindex the supply of a one-term packet. 

### `Rule.bundle`

 Replace each single-bit wire by a bundle of independent bits. 

 # A wire packet from a partition of its demands 

### `Rule.partition`

 Independent supply bits serve the selected demands and their complement. 

 # Orientation of individual wire demands 

### `orient`

 A demand is an equality test, so its two legs can be exchanged. 
