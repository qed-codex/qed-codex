---
{
  "module": "OAI/Computability/VPVNP/DeterminantQueryBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DeterminantQueryBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DeterminantQueryBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Recomputation bounds for the determinant query

The call counts model the two nested recursions of Appendix D.2, including
every repeated request for a coefficient. A rank scan on a rectangular matrix
with dimensions bounded by `2^p` makes `2^O(p²)` scalar-query visits.


### `powerQueryVisits`

 Number of calls (including the root) made when every branch of a power
entry query on an `n × n` matrix is recomputed. Each degree split at each
intermediate index calls both children. 

### `powerQueryVisits_le`

 Full recomputation of a matrix-power coefficient makes at most
`(1 + 2n(z+1))^⌈log₂ h⌉` calls. 

### `powerQueryVisits_le_exp`

 For indices of at most exponential magnitude, the full tree of repeated
power coefficient queries has singly exponential size. 

### `balancedBivariateVisits`

 Count calls in the same balanced recursion as the bivariate coefficient query.
An empty leaf costs one visit. A nonempty leaf incurs its supplied cost, which
can include the recursion used to evaluate the factor. 

### `balancedBivariateVisits_le`

 Count all recursive calls, including empty and padded leaves. No restriction
on the starting index or the number of factors is needed for the bound. 

### `balancedBivariateVisits_unit_le`

 With a unit cost per terminal coefficient query this counts the product
recursion alone. 

### `balancedBivariateVisits_le_exp`

 Exponential bounds on the degree ranges and on a leaf query compose with
the balanced recursion to give a singly exponential recomputation bound. 

### `headFactorVisits`

 Number of scalar coefficient queries in one Schur factor, including the
factor query itself. A matrix-power base case counts as one visit. At each
higher bidegree, every degree split reads the last entry once and each inner
split reads the first entry and evaluates one trailing matrix power. 

### `headFactorVisits_le_exp`

 Bounding the two matrix indices and both streamed degree splits, together
with all calls of the power-entry recursion, gives a singly exponential bound. 

### `determinantQueryVisits`

 Calls made by one determinant coefficient query. Its leaves use the
corresponding trailing matrix size, and all identity leaves cost one visit. 

### `determinantQueryVisits_le_exp`

 The complete coefficient query, including both the product recursion and
the Schur-factor power recursions, makes at most exponentially many visits
when the dimension and both degrees have at most `p + 1` bits. 

### `rankQueryVisits`

 Total scalar-query visits over the complete rectangular scan used by
`rankQuery`, with full recomputation at every bidegree. 

### `rankQueryVisits_le_exp`

 The complete rank scan is singly exponential when both dimensions have
at most `p + 1` bits. Its inner degree needs at most `2*p+2` bits. 
