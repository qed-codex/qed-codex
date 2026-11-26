---
{
  "module": "OAI/Computability/VPVNP/RankQueryUniformResources.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryUniformResources.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryUniformResources.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniform coordinate costs before the field and slice are chosen

Rows, columns, rank, extension degree and limb width can depend on the prime
and affine slice. At each input length these five natural numbers lie in a
finite box fixed by the reader plan. Maximizing the clock and stack height
separately preserves their respective bounds. This also handles the ordinary
determinant's clock without a monotonicity assumption about its recursion.


### `maximum`

 Separate maxima of the clock and peak for all possible parameters at
one length. Only the estimates use the maxima. The machine runs the query
at the supplied parameters. 

### `Shapes`

 The natural parameters still undetermined after fixing the input
length. The first three coordinates are the two dimensions and minor order. 

### `mountedBudget`

 Time and stack-height budget for a mounted Cramer coordinate query, including minor
selection, preparation, and the caller's peak stack height. 

### `mounted_feasible_of_shape`

 The cap includes every ready denominator and numerator bank, as in
`SelectedMinor.den_ready_length` and `SelectedMinor.num_ready_length`. 

### `uniformBudget`

 Separate worst-case time and space budgets over the bounded matrix dimensions, minor order,
extension degree, and limb width. 

### `planDepth`

 The full rectangular and graded address kernel both fit one
prime-independent word width. 

### `planWidth`

 Word width sufficient for both the Gram rank cursor and the plan's matrix-entry reader. 

### `plan_query_shapes`

 The matrix-order and both degree-scan inequalities required by the
two orientations and by the ordinary determinant, at the common plan width. 
