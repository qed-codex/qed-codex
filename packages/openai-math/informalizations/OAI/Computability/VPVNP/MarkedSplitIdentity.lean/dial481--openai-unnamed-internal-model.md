---
{
  "module": "OAI/Computability/VPVNP/MarkedSplitIdentity.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MarkedSplitIdentity.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MarkedSplitIdentity.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Splitting a marked tensor times an identity wire

In Appendix A.2 the new marked index is placed at the intermediate party. The
column of the exterior operator stays at the first endpoint and its row at
the second. These three roles retain their own local factors even when their
parties coincide.


### `tripleBasis`

 The new marked index, the exterior column, and the exterior row. 

### `triplePlace`

 Place the new index at `x`, the column at `a`, and the row at `b`. 

### `threeMarked`

 Place the table indexed by the new index, row, and column, in that order. 

### `splitMarkedTerm`

 Contract the old marked index against one of the two exterior-operator orders. 

### `marked_wire_mutual`

 Grouping the three indices of the marked tensor and the wire gives the
coefficient of the marked tensor times the row-column Kronecker delta. 

### `marked_split_restricts`

 The two contracted arrays dominate the product of the marked tensor and
its identity wire under direct sum. 

### `value_marked_wire_le_split`

 Applying the spectral point gives the subadditivity step of the relocation inequality. 
