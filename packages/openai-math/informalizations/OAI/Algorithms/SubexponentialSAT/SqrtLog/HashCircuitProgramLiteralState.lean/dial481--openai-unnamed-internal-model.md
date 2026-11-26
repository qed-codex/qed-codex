---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramLiteralState.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramLiteralState.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramLiteralState.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Direct-call interface from the actual caller state. This avoids preparing
an extra machine-state embedding between the record parser and literal lookup. 

### `fetched_clause_tail`

 The unread literal-list tail is preserved by the complete lookup call. 

### `fetched_row_tail`

 The unread weighted-row tail is also preserved while a literal is fetched. 

### `parseAndFetch_eval`

 One complete physical literal read: framed original literal code to raw
incidence dictionary, including both parser and lookup costs. 
