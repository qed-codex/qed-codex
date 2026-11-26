---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateFieldEquiv.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateFieldEquiv.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateFieldEquiv.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Transport of greedy coordinate queries across the advised field isomorphism

Every prefix rank is preserved when entries are mapped into an isomorphic
field. The two greedy scans therefore select the same physical indices. The
quotient of the two determinants then transports entrywise, for arbitrary
target rows.


### `rankQuery_map_eq`

 The physical rank scan commutes with interpretation into an isomorphic field. 

### `greedyRowIndex_map`

 A prefix-rank increase occurs at the same original row after mapping
the field. Casts identify only the two bounds on the dense ordinal. 

### `greedyRowBasis_map_apply`

 The two assembled row bases agree entrywise under the field map. 

### `coordinateColumns_map`

 On a full-row-rank matrix the transpose prefix scan selects the same columns. 

### `greedyColumns_map`

 Columns selected from the already selected rows commute with the
isomorphism, including when the original matrix is rectangular or singular. 

### `rowCoordinateQuery_map`

 Replacing the target row and dividing the two determinants commute
with the field map, even for targets outside the selected rows' span. 

### `greedyCoordinateQuery_map`

 The physical greedy coordinate over the advised representation maps to
the corresponding coordinate over the represented field. 
