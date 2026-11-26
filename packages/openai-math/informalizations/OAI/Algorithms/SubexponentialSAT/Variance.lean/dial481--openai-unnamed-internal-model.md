---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Variance.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Variance.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Variance.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A finite dependency-graph variance bound

All expectations below are finite rational sums. The main theorem expands the
square of a centered count into a double sum of covariances. Nonneighbors have
zero covariance; at most `d + 1` entries in each row remain, each at most one.


### `mean`

 Finite weighted expectation. Normalization is an explicit theorem hypothesis. 

### `mean_centered_mul`

 Expanding a centered product gives the covariance formula. 

### `uniformWeight`

 Equal weights on a finite outcome space. 

### `mean_uniformWeight`

 Bridge to the ordinary sum-divided-by-cardinality finite average. 

### `sparse_sum_le`

 A sparse matrix with at most `d` off-diagonal nonzero entries per row,
all entries at most one, has total sum at most `(1+d) * card V`. 

### `centered_sum_square`

 The square of a centered sum is the sum of all centered products. 

### `mean_centered_sum_square`

 Algebraic expansion of the variance of the total count. 

### `variance_sum_le`

 Dependency-graph variance bound for identically distributed variables in
`[0,1]`. The independence hypothesis is exactly factorization of pair moments
for distinct nonneighbors; no independence of adjacent variables is assumed. 

### `typeIndicator`

 The indicator that chunk `v` has type `u` in outcome `ω`. 

### `typeCount`

 Number of chunks having a prescribed type. 

### `mean_typeCount`

 The center `D/N` is the actual mean of a uniformly distributed type count. 

### `typeCount_variance_le`

 The single-type estimate in Section 5.4. 

### `sum_typeCount_variances_le`

 Expected sum of squared type-count deviations, the bound preceding (5.8). 
