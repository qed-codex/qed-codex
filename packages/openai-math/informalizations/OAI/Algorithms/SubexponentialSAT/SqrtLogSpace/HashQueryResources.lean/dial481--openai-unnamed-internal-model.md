---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashQueryResources.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashQueryResources.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashQueryResources.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete scope resources of the actual serialized raw-formula query.
The dependent clause-index cast preserves every repeated or zero raw slot;
these results use no identity with the former materialized selector. 

### `rawQuery_resources`

 The frontend's literal scopeRows has the resource bounds of the actual
raw rows and actual raw clause widths. The optional mark contributes at most
one clause; each produced variable scope is duplicate-free. 

### `history_resources`

 Every attained selected history, including the final unmarked query,
uses the concrete query record and the exact indexed raw formula. 

### `trial_resources`

 Every trial rank, including every losing candidate, uses the same bounds.
The candidate and all initial/selected row occurrences are retained. 

### `history_uniform_resources`

 Exact guard-resource envelope for the actual final or intermediate
selected-history query. Positivity is used only for the produced-code row
bound; no guard, layout, or evaluator is supplied. 

### `trial_uniform_resources`

 The same envelope includes every losing trial and optional marked clause.
It is precisely the three numeric inputs to the structural scan-guard proof. 

### `input_eq_forward_measured`

 The physical ambient and clause-count words identify the exact measured
input. The width word is a separate parameter and is not the clause count. 

### `scope_guard_cutoff`

 One cutoff is fixed before the actual query, its rows, optional mark,
and serialized numeric words. It requires only the proved raw scope bounds. 

### `history_guard_cutoff`

 Every attained history query, with any optional mark including none,
passes the same actual frontend guard after a width-fixed cutoff. 

### `trial_guard_cutoff`

 The cutoff also covers every losing candidate rank and every marked
clause on its literal candidate-plus-history query. 
