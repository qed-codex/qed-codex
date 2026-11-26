---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateSliceMinors.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateSliceMinors.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateSliceMinors.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Encoded entries and selected minors of a slice coordinate query 

### `encode`

 Packs the extension-field coordinates of a field element into the scalar representation
used by the entry reader. 

### `fieldMatrix`

 The Macaulay relation matrix with the monomial rows appended below the equation rows. 

### `row`

 Original row indices selected by the greedy independent-row scan of the appended matrix. 

### `col`

 Original column indices forming the invertible coordinate minor of the greedy row basis. 

### `baseMatrix`

 The appended matrix with every field entry packed as a scalar for the native reader. 

### `denominator`

 The square Cramer denominator formed by restricting the encoded matrix to the chosen
independent rows and columns. 

### `target`

 The encoded target row for applying the given operation at one quotient-basis coordinate. 

### `numerator`

 The denominator minor with the row for the next coordinate replaced by the current target
on the selected columns. 

### `reads`

 The two scalar matrices consumed by the determinant roots are built from
the selected row and column addresses of the full indexed equation matrix. 
