---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Rectangle/Sparse/Law.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Sparse/Law.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Sparse/Law.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Decompositions of weighted rectangular products 

### `weighted_volume`

 One term for every row, column and inner index. 

### `WeightedRankLE.tensor`

 Tensor two decompositions, allowing an arbitrary enumeration of paired
side indices. Summing over the paired terms factors the coefficient identity. 

 Permutation symmetry and the elementary area and volume bounds. 

### `RankLE.area`

 Fixing the inner index gives an identity submatrix of the output flattening. 

### `rank_volume`

 One product per row, column and inner index. 

 Tensor products, powers and cyclic symmetrization of rectangular decompositions. 

### `RankLE.tensor`

 Split each matrix index into two digits and multiply the corresponding
coefficients. Summing over pairs of terms factors the coefficient identity. 

### `RankLE.symmetrize`

 Tensoring the three cyclic arrangements makes all sides equal to the volume. 


# Powers of weighted products

Side indices of a power are digit strings. Coefficients multiply over
digits, so support sizes multiply and rank bounds are submultiplicative.



# Isolating triples by coloring the three alphabets

For two different labels only a fraction `1/m` of the `m`-colorings
identify them. The union bound and averaging retain at least five
sixths of the candidate triples at each of the three steps. Completion
lists always refer to the original support.


 # A finite rank comparison for bounded completion sets 

### `DegreeBound`

 The constant pays for three independent colorings and the
loss of at most half of the selected triples. Tensor powers remove it. 

 # Completion counts for powers of a partial product 

### `count_digits`

 Completed labels are independent digit strings. 

 # Completion counts on a fixed type of support words 

### `fiber`

 A type of independent supported triples gives as many distinct
triples in the power, all with the same three completion counts. 


# Nonnegative dual total correlation

Apply entropy subadditivity to the first index and the pair of
remaining indices, then to the two remaining indices within
each fixed first-index slice.


### `pair_bound`

 For the uniform distribution on a relation, the sum of the
two conditional entropies is bounded by the joint entropy. 

 # Multiplicative weights from completion counts 

 # Powers of a weighting supported on a set of output cells 
