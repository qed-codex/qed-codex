---
{
  "module": "OAI/Computability/VPVNP/CoordinateQueries.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CoordinateQueries.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CoordinateQueries.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Greedy row and column coordinate queries

Appendix D.2 of *VP and VNP differ over every field* selects rows using ranks
of prefixes of the original matrix. For an independent list of rows it
selects independent columns by the same test on the transpose. A coordinate
of a target in their span then uses two ordinary determinant queries.


### `squareDetQuery`

 Ordinary determinant recovered at the top pencil degree, with its sign. 

### `prefixRows`

 The first `s` rows, retaining every column. 

### `mem_greedyIndices_iff_prefixRank_lt`

 The next row is retained exactly at the indices where the prefix rank increases. 

### `firstPrefixAbove`

 Retrieve the zero-based `k`-th selected index by scanning prefixes
until the number of selected items first exceeds `k`. 

### `rowCoordinateQuery`

 Query one coordinate in a row basis from an oracle for square determinants.
Both input matrices are given entrywise, from the selected columns. 

### `rowCoordinateQuery_eq`

 Replacing row `i` by the restricted target multiplies the determinant by
the `i`-th coefficient in every representation of that target. 

### `rowCoordinateQuery_reconstruct`

 When the target lies in the span, querying the coordinates reconstructs
the target on all columns of the original rectangular matrix. 

### `greedyRowIndex`

 The indexed row of the greedy basis. Every rank query during the scan
uses an initial block of the supplied matrix. 

### `coordinateColumns`

 The independent columns of an assembled full-row-rank matrix, queried
by their ordinal among the selected columns. 

### `coordinateQuery`

 Coordinate of the target row in an independent row list, using only
entrywise prefix rank queries and two scalar determinant queries. 

### `greedyRowBasis`

 The rectangular matrix of the selected rows, still presented by an entry
function so querying its entries only requests their indices in the original matrix. 

### `greedyCoordinateQuery`

 Coordinate of a target in the greedy row basis of an arbitrary matrix. 
