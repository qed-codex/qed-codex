---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashGreedy.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashGreedy.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashGreedy.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The streamed strict argmin and its greedy invariant. Candidate indices describe
an iterator's successive callbacks; no list of candidates is constructed here.
The finite-program implementation must refine these recurrences. 

### `update`

 One cached-score update. Equal scores retain the earlier candidate. 

### `scan`

 Result after the seed and the next `t` candidates have been evaluated. 

### `scan_eq_best`

 The native iterator's proof-only visit log agrees with the indexed scan.
The seed's repeated visit at index zero leaves its cached score unchanged. 

### `scoreCost`

 The scan pays every score, including all losing candidates, once. 

### `selectionCost`

 Cost across all rounds, including scores of rows that are rejected. 

### `contraction_of_minimum`

 Averaging is over the reference ternary family, regardless of duplicates
or order in the stream used to find the minimizing row. 

### `scan_contraction`

 Reference coverage suffices even if the streamed decoder repeats rows. 

### `history`

 Selected rows are the only persistent history; trials are not retained. 

### `trial_cost`

 This includes every candidate query, not only the selected row. 

### `mass_lt_loopCap_capacity`

 The retained unary round-count word is a sufficient common score width,
including weighted violation mass with up to `m` contributions per assignment. 
