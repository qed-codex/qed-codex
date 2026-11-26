---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Rectangle/Rows.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Rows.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Rows.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Paired secant inequalities for polynomial multiplication

One application of tripling controls both rows at a common comparison
index. Concavity transports the bound back to *different* indices in
the two rows. The reciprocal inequality then controls a weighted sum
of logarithmic increments.


### `Row`

 The indices are degrees, one less than the polynomial lengths. 

### `paired_secants`

 Lower bound on a pair of increments per unit increase of the index. 


# The polar formula for the rectangular benchmark

The three arm lengths `x,y,z` give wire lengths `x+y,x+z,y+z`.
The dual inequality follows by weighted Cauchy–Schwarz. At an active
shape all three arms of a maximizing tripod can be strictly positive.


### `Polar`

 The polar upper bound, with attainment at positive arms above the
largest pair sum. At or below that sum a single nonzero arm suffices. 

### `certificate`

 Three weights adding to one certify an upper bound on the objective. 

 # Three wires for a rectangular matrix product 

### `tensor`

 The output is at site 0, the two inputs at sites 1 and 2. 

### `tensor_le_iff`

 Restriction from a diagonal is exactly a coefficient decomposition.
Each site in the three-wire model has one unused index fixed to zero. 


# Positive spectral contact implies rectangular rigidity

The normalized price triples are arm lengths at diagonal rate one.
The two geometric inputs are the harmonic lower bound on the rate
and propagation from a positive triple attaining that lower bound.


### `Support`

 A support representation by nonnegative normalized arms. 

 # Three-site spectral points and normalized prices 


# Powers of a point in the Zariski closure

Polynomial evaluation carries a closure point into the linear span of
the evaluations on the original set. The degree-`n` products only use
monomials with each exponent at most `n`, giving a polynomial bound on
the number of points needed in one simultaneous interpolation.



# Scalar extension for the density bound

The weights and a rank witness lie in one countable subfield. Both embeddings
from that subfield preserve all coefficient equations and the set of nonzero
weights. The unweighted arithmetic exponent is invariant under extension.

