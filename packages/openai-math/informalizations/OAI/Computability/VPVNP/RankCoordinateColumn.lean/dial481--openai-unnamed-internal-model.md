---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateColumn.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateColumn.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateColumn.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Selecting Cramer columns by scanning the original matrix

Restricting row vectors to the first `s` coordinates is a linear map. Its
image takes the full row span and the span of the greedy basis to the same
space. Thus column-prefix ranks, including their first increases, can be
queried in the original matrix independently of the selected row indices.


### `greedyRowBasis_columnPrefix_rank`

 Every column-prefix rank of the greedy row basis equals the corresponding
rank queried directly on the transpose of the original matrix. 

### `coordinateColumns_greedyRowBasis`

 Appendix D's columns of the selected-row matrix have the very same
original indices as the independently selected greedy rows of the transpose. 

### `greedyCoordinateQuery_eq_baseColumns`

 The Cramer query can use two independent base-matrix scans for its row
and column index sets. 

### `originalRowCoordinate_at_greedy`

 The sum defining the coordinate at a selected original row has one
contributing ordinal. 

### `natAdd_suffixBasisIndex`

 The selected suffix row, expressed in the combined row indexing. 

### `quotientCoordinate_at_suffix`

 For a queried basis monomial, Cramer's row ordinal is the rank of the
equation prefix plus its ordinal among the surviving monomials. 
