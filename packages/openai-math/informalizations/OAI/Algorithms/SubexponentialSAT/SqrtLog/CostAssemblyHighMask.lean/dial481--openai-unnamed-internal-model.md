---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/CostAssemblyHighMask.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CostAssemblyHighMask.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CostAssemblyHighMask.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Guard success for the actual forward mask computed from all supplied raw
scopes.  The high cutoff counts raw entries, including harmless overcounts. 

### `eventually_forwardHighMask_guards`

 The large-input cutoff is uniform in every raw scope family and mark.
Only their explicit polylogarithmic upper resource bounds are supplied by
the caller; half-retention and all nondegeneracy guards are derived here. 
