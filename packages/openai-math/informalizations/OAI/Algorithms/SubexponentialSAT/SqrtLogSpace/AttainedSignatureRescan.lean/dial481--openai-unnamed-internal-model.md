---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/AttainedSignatureRescan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/AttainedSignatureRescan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/AttainedSignatureRescan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Actual bounded-word predecessor rescan and its uniform source-prefix storage. 

### `workState_stackBits`

 All live arrays and all four retained words are included. 

### `visits_stack_bound`

 The exponential count of visits does not occur in this all-prefix bound. 

### `for_stack_bound`

 Every prefix of the actual counted rescan, including test and halt. 

### `command`

 The candidate word supplies the binary predecessor count. Its width is h;
the final zero countdown word resets the predecessor without a family table. 

### `prepareKey`

 Compute the candidate's whole key once and retain it through the rescan. 

### `ReverseLex`

 Lexicographic comparison with coordinate priority h−1,...,0: compare
higher coordinates first, and use the low bit only when their tails agree. 

### `polynomialBudget`

 A uniform polynomial local budget, before the exponential scan counts. 

### `candidate_run`

 One fixed actual candidate machine returns the canonical full key and
freshness bit, with time and every-prefix storage bounds on that same run. 

### `complete_candidate_run_budget`

 Include each concrete compiled invocation's halt in the full generator
charge; no emitted-key count multiplies the raw candidate scan. 

### `budgets_le_monomial`

 Both concrete resource expressions have one fixed degree, independent of
head width, matrix dimensions, coefficient values and the candidate cursor. 
