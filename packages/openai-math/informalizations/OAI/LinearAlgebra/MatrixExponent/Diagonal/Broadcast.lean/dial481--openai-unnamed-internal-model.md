---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Diagonal/Broadcast.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Diagonal/Broadcast.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Diagonal/Broadcast.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Choosing processor, batch, and broadcast lengths 

### `Scales`

 Simultaneous bounds for the cube layout, packet budget, and processor tape. 

### `scales`

 Choose the sizes before the batch and degree are known. A fixed
positive exponent suffices for the batch hypothesis. 

 # Balanced exterior labels shared across all copies 

### `exterior`

 Balance literals separately so that rerouting them has a small cost
even on a tape dominated by communication bits. 


# Communication budget for literal pins

Each worker sends at most one copy of its own literal string. For
incoming literals a single label coordinate bounds the number of
relevant positions, shared across all processors.



# Encoding the public report

The first bit distinguishes an ordinary report from the extra branch.
A binary cut index and fixed-width binary counts follow, in lexicographic
class order. All unused bits are zero.


### `encodeReport`

 Reports and the extra branch have disjoint broadcast strings. 

### `encodeReport`

 Specialize the public encoding to the batch dimensions of this scheme. 

 # Choosing a communication scheme with prescribed exterior labels 

### `prepare`

 The colors can be chosen by `exterior` before the diagram is known.
The two density bounds concern a single copy of the diagram. 

 # Diagonalization over a fixed coefficient field 

### `Programs`

 Each processor has a literal programming the unit branch and
the explicit local evaluation of the replacement graph. 

### `diagonal`

 No graph implementing a batch of these processors can have all
its replacement computations programmed back into the processors. 


# Descent and tagged-permutation hardness

At each step the wide version of descent gives a lower bound on the
current per-copy cost. This absorbs the exterior cost of the trivalent
version. A fixed number of iterations then contradicts the lower bound.



# A common batch size independent of the replacement

Repeat any proposed small network until it reaches the prescribed
power. Feed surplus copies an input of weight one. This allows all
processor array dimensions to be fixed before choosing a diagram.


### `batch_floor`

 A power of two within a factor of two of the square root
of the number of homes. 


# The local processor implementation requirement

The implementation must be chosen before any replacement diagram is
given. Only the literal settings, wire numbering and report code can
depend on the diagram. This requirement is a hypothesis.


### `Implements`

 Every admissible diagram of the indicated size must have a local
program at each site, without any promise about the tensor it computes. 

### `Programmable`

 A quasi-linear universal processor for the concrete local evaluations. 

 # The remaining estimates for exact many-list hardness 
