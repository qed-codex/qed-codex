---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashCandidateRank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashCandidateRank.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashCandidateRank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

### `wordRank`

 Proof-level rank of the actual retained word, including leading zeroes. 

### `payload_wordRank`

 The parser reverses the current odometer word, exactly as the reference
candidate accessor does. No native decoding of the exponential rank occurs. 

### `tuple_eq_singleton_flatten`

 A singleton shape contains exactly the one physical payload word. 

### `prepare_eval`

 The actual preparation command emits the reference candidate at the
current word's rank and preserves every other physical leaf stack. 

### `trace_space`

 Rank identification, measured execution and all-prefix source storage
refer to the same compiled preparation run. 
