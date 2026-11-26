---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafParametersProgramSerializationUnary.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafParametersProgramSerializationUnary.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafParametersProgramSerializationUnary.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Paid, preserving serialization of parameter words as unary loop counters.
This is the checked bit conversion already used for clause-factor masters. 

### `unaryCopy_eval`

 Ports 11--13 are temporary. The binary parameter remains at `src`, and
`dst` receives one true bit per unit of the parameter. 

### `unaryCopyBound_eq`

 The value-dependent cost is exposed; unary serialization is never free. 
