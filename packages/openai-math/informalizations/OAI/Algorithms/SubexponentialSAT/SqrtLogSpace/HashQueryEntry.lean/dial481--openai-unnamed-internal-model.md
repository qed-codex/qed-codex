---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashQueryEntry.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashQueryEntry.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashQueryEntry.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The actual normalizer, trial source stage and marked-record parser supply
the literal query sources. These proofs impose no length cap on the suspended
reference tail or mass accumulator, and execute no extra marker stage. 

### `MarkedEntry`

 All source-side obligations at the actual marked callback entry. The
frontend itself owns the single paid marker operation. 

### `trial_entry`

 The actual counter word is normalized once, and its physical prefix plus
the attained history is exactly the raw-row table supplied to the frontend. 

### `prepared_trial_entry`

 Preparation supplies the actual low-bank blanks and canonical master
words. The six mutable selector ports are exactly those allowed by the
staged-rounds callback; no global retained-word size premise is needed. 

### `trial_guard_cutoff`

 One cutoff is fixed before all leaf inputs, attained histories, losing
candidates and marked clauses. It applies to the literal query assembled by
`trial_entry`, with no layout or evaluator premise. 

### `acceptedQuery`

 The final query receives precisely the attained history, with no trial
candidate and no marked clause. Its false index is written by `noMarkInput`. 

### `accepted_entry`

 The real paid accepted stage supplies the history-only source table and
clears its routing scratch. No second unmarked-input stage is introduced. 

### `prepared_accepted_entry`

 The actual completed greedy `RowBoundary` restores preparation's master
words and all lower blank workspace before the history-only count stage. 

### `accepted_guard_cutoff`

 The history-only final count passes its actual guard after one cutoff
fixed before all inputs and attained histories. 
