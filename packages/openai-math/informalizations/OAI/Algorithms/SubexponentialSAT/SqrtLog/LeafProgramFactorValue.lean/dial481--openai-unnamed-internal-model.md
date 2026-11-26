---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramFactorValue.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramFactorValue.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramFactorValue.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Execution of the computed factor value and its multiplication into the
current head product. Input incidence dictionaries are the physically
produced tables supplied by the preceding service. 

### `hash_value_eval`

 The native indicator is applied to the actual expanded row, then its
result is multiplied into151. The old hash and incidence table are cleared. 

### `marked_value_eval`

 The marked clause is evaluated directly and multiplied once. It does
not pass through the hash idempotent. 
