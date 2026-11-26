---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ExecCNFSemanticHelpers.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecCNFSemanticHelpers.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecCNFSemanticHelpers.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Exact list identities used when composing executable CNF filters. 

### `length_encodeList_filter_le`

 Filtering discards complete frames; this bound needs no property of the
payload encoder. 

### `absorb_eq_filter_dedup`

 An implementation may first remove duplicate clauses, then use that same
list as the scan master, without changing the exact ordered output of absorb. 

### `length_encodeList_dedupClauses_le`

 Clause deduplication retains a subsequence of the original payloads. 

### `length_encodeList_absorb_le`

 Absorption cannot increase the serialized formula length, even when the
payload encoder uses unequal-length clause encodings. 
