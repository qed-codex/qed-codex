---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpCRTExecution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpCRTExecution.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpCRTExecution.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executable represented jet reconstruction

Every polynomial is a dense coefficient list. The executable definitions take
only a `RingProgram`; the decoder appears in refinement theorems. Counters sum
the actual coefficient-callback counters. Machine/list overhead is separate.


### `completeProgram`

 Complete reconstruction, including all inverse-table preprocessing. 

### `head_decode_of_denote_eq`

 The first output coefficient, with a zero default for an empty list,
has the expected constant-coefficient semantics. 

### `selectedDecoder`

 This decoder is used only in specifications. The CRT program receives
the binary callback record and never evaluates the semantic quotient map. 
