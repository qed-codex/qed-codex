---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Spectral/Transport.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Spectral/Transport.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Spectral/Transport.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exterior creation and contraction

Use the signed subset basis. Index a degree by its cardinality plus
one, so degree zero has a predecessor with empty basis. Maximizing
the weighted dimension bounds both neighboring dimensions at once.


### `exterior`

 The two orders of creation and contraction sum to the identity
for equal labels and to zero for unequal labels, in every characteristic. 

 # Joining shared labels by local equality tests 


# Restriction using shared indices

Each assignment of shared indices exposes a label at each site. Local
maps may read the label, select an input coordinate and apply a scalar.


 # Equality of marked indices as a wire 

### `link`

 Inactive indices may be ignored instead of fixed to zero. 


# Splitting an array with two marked indices

The first index passes through a kernel, with two catalyst indices
held at the endpoints. The second index is unchanged. Each inequality
below is a local linear restriction, also when some sites coincide.


 # The wire pseudometric of a spectral point 

 # Price inequalities for a pair of marked indices 

### `Splitting`

 `V` consists of scaled prices as functions of the two placements.
The split uses an exterior-algebra index at the endpoints `a, b`. 


# Convexity of distances between points on metric intervals

In the matrix of four endpoint exponents, keep the diagonal fixed.
On each branch of a split, updating just one off-diagonal entry halves
the difference between the two diagonal sums. All costs of splitting
are additive in base-two logarithmic units.


### `busemann`

 Points at the same fraction on two intervals satisfy Busemann convexity.
Neither existence of intermediate points nor separation of sites is required. 


# Busemann comparison for spectral distances

The exterior creation and contraction identity splits the first
marked index. Dividing both children by the price of the catalyst
gives the three inequalities needed for the halving argument.

