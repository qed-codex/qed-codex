---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SparseCodeRows.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SparseCodeRows.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SparseCodeRows.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Actual sparse-row serialization and its same-run source resource bound. 

### `rowsInputSpan`

 Every retained source input of the actual sparse-row serializer. In the
scheduled construction its vertex count is polynomial by graph_edge_upper. 

### `rows_runs_space`

 The serializer emits the actual incidence-slot words for the supplied
candidates. Its same trace has a local time bound and all-stack prefix bound. 

### `selected_vertex_count_le`

 The runtime vertex word supplied to the serializer is polynomial in m;
its length is not the number of searched graph candidates. 

### `emitted_rows_kernel_bound`

 Physical serialized rows inherit the selected graph/local-code guarantee.
Coverage, rather than agreement with an earlier search order, is sufficient. 

### `rowsInputSpan_le`

 The serializer's whole retained input span is polynomial once the actual
vertex count bound and runtime word-length bounds have been established. 

### `codeRows_explicitCost_le`

 Actual complete code-row production, after the graph-order inequality
has bounded its only exponential domain by the clause count. 

### `rows_runs_polynomial`

 One actual serializer trace has both polynomial running time and a
polynomial bound on every stack at every prefix, including its compiled halt. 
