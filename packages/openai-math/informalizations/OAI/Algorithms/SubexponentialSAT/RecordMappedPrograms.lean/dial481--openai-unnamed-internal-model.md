---
{
  "module": "OAI/Algorithms/SubexponentialSAT/RecordMappedPrograms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/RecordMappedPrograms.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/RecordMappedPrograms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Actual record iteration over encoded logical values

The instruction sequence is `RecordPrograms.iterate`. The contract below is
required only for payloads emitted by the supplied encoder. It does not ask a
callback for correct behavior on malformed encodings, and it does not install
the encoder, test, or cost function as a machine instruction.


### `iterate_run`

 Genuine execution of one fixed iterator over any list of encodable values.
The encoder appears only in the input/output specification and bound. 

### `program_budget_le_input`

 A linear bound in the actual encoded input length, provided the callback
bound is linear in its current encoded payload length. 
