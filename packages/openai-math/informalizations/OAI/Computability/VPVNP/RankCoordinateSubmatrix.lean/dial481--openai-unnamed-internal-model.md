---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateSubmatrix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateSubmatrix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateSubmatrix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Entry reads for the selected Cramer submatrix

Two ordinal selectors return original row and column addresses into distinct
scratch words. The scalar reader uses both words directly. Their bits are
discarded before returning to the determinant engine, so later queries can
reuse the same two words.


### `clear_bounded`

 Popping a stack to empty never increases the peak height of any stack. 

### `Work`

 Private ports holding the selected original row and column ordinals together with the
scalar reader's workspace. 

### `Port`

 Public row, column and scalar-result ports extended by the selected-submatrix workspace. 

### `workBank`

 Installs the two selected address words alongside the underlying scalar reader's stacks. 

### `Ready`

 Both original addresses are recomputed for each scalar query. 

### `minorRead`

 The caller supplies dense row and column indices, and receives the
selected entry on its own scalar result stack. 

### `correctSpace`

 The square and rectangular versions use the same finite code. Only the
two short erase scans are added to the selectors' and entry reader's costs. 
