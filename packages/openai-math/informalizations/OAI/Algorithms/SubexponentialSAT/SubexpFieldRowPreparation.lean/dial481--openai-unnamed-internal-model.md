---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpFieldRowPreparation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpFieldRowPreparation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpFieldRowPreparation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preserving preparation of a local field-label row

Copy the enumerator's rank and the factor's unary arity into the checked
unranking routine, produce the fixed-width digit stream, and clear the padded
final quotient. The modulus, rank master, and arity master are preserved.


### `tapes`

 The unranking workspace occupies ports 0--12. Ports 13 and 14 are masters. 

### `command_eval`

 The local row label stream is built without changing either enumeration
master. The padded final quotient is actually cleared, even when its value is zero. 
