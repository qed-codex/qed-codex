---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Rectangle/Speedup/Dense.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Speedup/Dense.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Speedup/Dense.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Codes with prescribed slot words

A new word conflicts with an earlier word only if both the slot and
symbol match outside some set of `n` coordinates. Counting these sets
and the possibilities within them leaves room for a greedy assignment.


 # Sparse decoder rows and narrow factorizations with sparse right factors 

### `Narrow.of_low`

 A basis selected from the rows retains their support bound. 

 # Multiscale approximation of a decoder 

### `layers`

 Consecutive approximants give an exact expansion. Each difference
has controlled support and rank, including the two end terms. 

### `row_layers`

 Linear envelopes for the row costs suffice on the square grid. 


# Packing short rows on both sides of the decomposition

For a product of layers of total index below the threshold, pay for
every row. Otherwise select just enough high layers to reach the
threshold. Use a sparse row basis on those coordinates and the
identity on the rest.


 # Finite decompositions and polynomial paths for grouped speedup 

### `path_closure`

 A polynomial path stays in the Zariski closure if it is in the
set except possibly at the finitely many roots of a nonzero polynomial. 

 # Adjoining a disjoint wire to the original three legs 


# Spanning pivot columns suffice

Interpolate the first `d` columns at each site to a padded basis.
Away from the roots of three minors, these columns span the whole leg.



# Pole cancellation in one group

The pivot columns `P,Q` span the remaining columns `X,Y`. A pairing
of size `d` cancels all the poles from the perturbation. Its only
uncancelled correction is divisible by the path parameter.


 # A group of rank-one terms returns a larger disjoint pairing 
