---
{
  "module": "OAI/Computability/VPVNP/PermanentLabels.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PermanentLabels.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PermanentLabels.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Literal projections of the generic permanent

A weighted directed graph whose edges carry constants or variables gives a
projection of the permanent. A simultaneous reindexing of both matrix axes
lets us use any finite vertex type.


### `permanent_submatrix_equiv_self`

 Relabeling the vertices bijectively preserves all cycle-cover weights. 

### `exists_permanent_label_projection`

 A finite matrix with literal labels is obtained by a projection of the
generic square matrix of the same order. 

### `map_graphLabels`

 Scalar specialization of the graph acts entrywise on its scalar labels. 

### `weightedLabelsProjection`

 Reindex the gadget graph and use each entry as a literal variable or constant
of the generic permanent. This uses exactly three internal vertices per occurrence,
one ring of length `m + 2` per variable, and one vertex per clause. 
