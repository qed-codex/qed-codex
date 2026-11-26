---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramRows.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramRows.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramRows.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Physical opening of an inline weighted clause record. The record payload is
`frame coefficient ++ encodeList encodeNat clause`. It is supplied reversed by
the outer record parser. Both the weight frame and the literal list are traversed
by fixed bit programs; source clause IDs are resolved by the upstream producer. 

### `openWeighted_runs`

 The entire supplied literal list is preserved literally. In particular,
this is not an evaluation or enumeration of the clause's joint scope. 
