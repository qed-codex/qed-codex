---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparseCharging.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparseCharging.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/SparseCharging.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Appendix A, insertion recurrence and the resulting path budgets. 

### `removed_card_le`

 Charge each removed marked clause to an inserted strict subset. Fibers may
overlap; their width-sensitive bounds are precisely those from marked priority. 

### `insertion_le`

 The recurrence in source equation `spar-insertions`, indexed from width one. 

### `depth_le`

 Every edge inserts at least one clause; summing the sharp per-width bounds
therefore bounds a path's number of edges. 

### `right_steps_mul_le`

 Count B-edges by their petal width. The integral multiplicative form
retains the exact bound without truncating division. 

### `trace_steps_le_insertions`

 Count actual edges by their insertion events, grouped by positive width. 

### `trace_units_le`

 Nonempty strict-subset replacements never remove an inserted unit clause. 

### `trace_insertion_recurrence`

 Equation `spar-insertions` for the actual insertion and removal events of
a finite path; the marked-degree hypothesis is supplied by priority. 

### `trace_insertions_le`

 The sharp source bound, now applied to an actual finite replacement trace. 

### `trace_depth_le`

 The source depth bound counts every edge of the same concrete path. 

### `trace_right_steps_mul_le`

 A B-edge of petal width `w` consumes at least `M^w` actual insertion events. 

### `selectedTrace`

 The concrete replacement trace induced by a selected formula path. 

### `trace_marked_degree`

 Priority bounds marked subset degrees at every prefix of a selected path. 

### `selected_path_depth_le`

 Every actual selected path has the draft's linear depth bound. 

### `selected_path_right_steps_mul_le`

 The B-choice bound for the same actual selected path. 
