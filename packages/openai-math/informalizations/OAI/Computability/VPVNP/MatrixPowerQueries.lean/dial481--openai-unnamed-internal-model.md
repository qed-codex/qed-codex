---
{
  "module": "OAI/Computability/VPVNP/MatrixPowerQueries.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MatrixPowerQueries.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MatrixPowerQueries.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Streaming coefficient queries for matrix powers

A query for one coefficient of a polynomial matrix power in Appendix D.2
splits its exponent into two halves. The implementation scans intermediate
indices and degree splits with scalar accumulators.


### `powerQuery_halves`

 Splitting a nontrivial exponent into its lower and upper halves decreases
the ceiling binary logarithm by at least one on both branches. 

### `powerEntryCoeff`

 From an oracle for coefficients of individual entries, compute the
coefficient of degree `z` in entry `(i,j)` of the `h`-th power. 

### `powerEntryCoeff_correct`

 The entry query returns exactly the specified coefficient of the matrix
power, using only the supplied entry oracle. 

### `foldl_add_eq_sum`

 A sequential scan over all indices uses a scalar accumulator. 

### `streamSum`

 Sum over a consecutive block of indices with a tail-recursive scan. 

### `streamAntiSum`

 Stream the ordered degree splits of `n` by keeping the first degree as
the loop index and computing the second by subtraction. 

### `streamedPowerEntryCoeff`

 Streaming implementation for matrices indexed by consecutive integers.
The tail-recursive folds carry the two running sums for intermediate indices
and for degree splits. Neither loop stores a list of all its indices. 

### `streamedPowerEntryCoeff_eq`

 The streaming loops evaluate the matrix-power coefficient recurrence. 
