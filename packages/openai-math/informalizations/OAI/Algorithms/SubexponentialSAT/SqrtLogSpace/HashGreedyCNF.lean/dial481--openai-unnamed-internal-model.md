---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashGreedyCNF.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashGreedyCNF.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashGreedyCNF.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The concrete streamed selector uses the original ternary row semantics.
Its exact scores and normalized reference coverage discharge the greedy
contraction hypotheses. These statements concern the deterministic history
refined by the native run; native query and resource closure remain separate. 

### `reference`

 Reference indices retain the original tuple multiplicities. 

### `history_mass_zero`

 The exact payload/score accessor removes evaluator and family-coverage
premises from the contraction theorem. The initial code distance is supplied
by the independently constructed sparse code. 

### `history_count_eq`

 Exact accepted-assignment count over the ambient Fin n, without deleting
unused coordinates or taking a low binary bit. 

### `history_support_le`

 Every selected history, including all intermediate rounds, retains at most
one depth-sized row per completed round. 

### `trial_support_le`

 Losing candidates satisfy the same trial support bound. 

### `decoded_history_support_le`

 The support estimate is directly usable on the decoded mathematical rows. 

### `trial_scope_le`

 Every marked query sees a trial whose variable-scope cost is charged,
including trials discarded by the minimum comparison. 
