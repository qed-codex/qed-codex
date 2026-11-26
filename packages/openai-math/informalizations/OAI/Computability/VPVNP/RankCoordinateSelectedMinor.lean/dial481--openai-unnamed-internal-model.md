---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateSelectedMinor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateSelectedMinor.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateSelectedMinor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Physical coefficient readers for the two Cramer minors

One bank supplies each greedy selector and a third supplies the underlying
scalar reader. A target-row read uses the same selected column as an
ordinary entry. The numerator stores its replacement ordinal separately
from these three banks.


### `Select.Side`

 Stack addresses for the greedy selector's controller words and its prefix-rank workspace. 

### `Host`

 Disjoint stack addresses for the row selector, column selector, and underlying scalar
reader. 

### `Work`

 Stack addresses for the selected submatrix's two saved indices and its three reader banks. 

### `local instance : DecidableEq (PrefixPort K)`

 Compare the prefix scan addresses used when locating a pivot for a Cramer minor. 

### `local instance : DecidableEq (PrefixWorkspace.Aux (PrefixPort K))`

 Decide equality of template, work, and scratch addresses within a pivot selector. 

### `local instance : DecidableEq (Select.Side K)`

 Decide equality of controller and workspace stack addresses in a greedy selector bank. 

### `local instance : DecidableEq (Host K R)`

 Compare stack addresses by bank and then by their row-selector, column-selector, or
scalar-reader label. 

### `local instance : DecidableEq (Work K R)`

 Decide equality of the two saved-index addresses and the auxiliary bank addresses for a
minor read. 

### `selectorBank`

 Idle state of an ordinal selector, with its rank template configured for a matrix with
`cols` columns. 

### `Ready`

 The row and column selectors are in their designated idle states and the scalar reader
satisfies its readiness predicate. 

### `initial`

 Combine idle selectors for the matrix and its transpose with the supplied scalar-reader
stacks. 

### `restrictEntry`

 Pivot selection is always performed on the original relation matrix.
The final scalar can be read from that matrix or from a powered target row. 

### `space`

 Uniform stack-length bound for selector calls, scalar reads, and the stored input banks. 

### `time`

 Step bound for selecting an original row and column, reading their scalar entry, and
handling the two address words. 

### `cols`

 Column indices that form the nonsingular coordinate minor of the interpreted matrix's
greedy row basis. 

### `selected`

 Square submatrix of `D` at the greedy row and column indices chosen from the interpreted
pivot matrix `M`. 

### `restrictEntry_correctSpace`

 Complete denominator or selected-target entry reader from the physical
base scalar queries. Both true pivot selectors use the same live matrix. 

### `numerator`

 Read a Cramer numerator entry, using the target at the selected column on the replacement
row and the ordinary minor entry elsewhere. 

### `numerator_correctSpace`

 The native numerator has the chosen dense row replaced by the target,
evaluated at exactly the selected original columns. 

### `selected_map`

 The interpreted denominator matrix is Appendix D.2's canonical square minor. 
