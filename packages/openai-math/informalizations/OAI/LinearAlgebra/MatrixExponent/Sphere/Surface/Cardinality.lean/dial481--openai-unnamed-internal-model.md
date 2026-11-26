---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Sphere/Surface/Cardinality.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Surface/Cardinality.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Surface/Cardinality.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Polynomial cardinality estimates for local data 

 # A designated active insertion and its stationary marks 

 # Selecting the destination of an insertion collision 

 # Availability and size of a seam crossing 

 # One productive step at any active insertion 

### `branches`

 The number of branches in one step is bounded independently of the
actual field cardinality. 


# Elimination of all active insertions

Each productive step lowers an integer potential. The bound counts
only outer choices. All seam states and ordinary residue indices
remain inside the terms.


### `complete`

 Eliminate every mover, uniformly over ordinary inputs. The local
room requirement follows from the initial bounds in `Reach.room`. 


# Scales of one local concentration

The accuracy parameter `q` sets the private-wire rate. There are `d*b`
public species and `d` private ones. Their ratio `b` equals the
Frobenius power `P` times `q^4`. Only the number of blocks `d`
grows with the input scale `T`.


### `slots`

 Enough distinct points for all original and auxiliary marks. 

 # Polynomial bounds for the local expansion at one occupied cell 


# Choosing a field and block sizes

The planting field, positions, Frobenius power and block size can all
be fixed before the width tends to infinity. Rounding the number of
blocks to a multiple of the chunk count loses at most half the width.

