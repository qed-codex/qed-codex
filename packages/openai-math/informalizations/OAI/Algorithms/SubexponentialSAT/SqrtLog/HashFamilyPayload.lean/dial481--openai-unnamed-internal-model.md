---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HashFamilyPayload.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashFamilyPayload.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashFamilyPayload.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The actual tuple-generator bit alphabet and its reverse-aware semantic
decoder. The alphabet matches `SubexpAlphabetProgram.command_eval`. 

### `decodeRow`

 A total row decoder; the zero-dimensional case has only the zero row. 

### `powerRows_contains`

 Internal reversals of the generator's list order do not affect coverage. 

### `generated_coverage`

 Exact list coverage consumed by `HashSelect.listRun`: the generator emits
a payload for every indexed candidate, regardless of its internal order. 
