---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DifferencePairs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DifferencePairs.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DifferencePairs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Pruned finite-difference traversal. `none`, `some false`, and `some true`
encode membership in neither set, in `E \ U`, and in `U`, respectively.
`words` specifies visit order; the streaming fold does not construct it. 

### `fold`

 Runtime recursion retains one prefix and invokes its callback immediately.
The three branches share the accumulator; no list of completed pairs is built. 

### `sum_words_eq_sum_pairs`

 The reference visit order contains each admissible pair exactly once. 

### `fold_decode_sum`

 A decoded accumulator may have a validity condition; it is retained at
all callback boundaries, while the decoded result is the exact pair sum. 
