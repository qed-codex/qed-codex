---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashMassStagedSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashMassStagedSpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashMassStagedSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Physical staging, all marked counts, and actual source cleanup share one
prefix bound. Cleanup only removes bits, so it does not amplify the query's
transient cap into the next boundary allowance. 

### `spaceBudget`

 The caller cap L is distinct from the staged boundary cap 3*L+2. 

### `spaceBudget_le`

 The explicit staging/reference expression is bounded by one fixed cube;
the expensive query contributes only its independently proved prefix cap. 
