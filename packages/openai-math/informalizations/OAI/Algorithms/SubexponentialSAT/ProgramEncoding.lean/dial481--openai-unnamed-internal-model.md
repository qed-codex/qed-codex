---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ProgramEncoding.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ProgramEncoding.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ProgramEncoding.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Shared record representation for executable programs

A scalar is stored as a Boolean payload (little-endian bits for natural
numbers; the scalar module specifies any fixed padding). A record list uses
the existing `Encoding.encodeList id`: false terminates the list; true starts
an escaped frame. Matrices and other fixed-depth schemas nest this same
representation. These are executable decoders and exact size identities,
not assertions that a machine has run them.


### `readRecordsAux`

 Explicitly bounded recursive decoder. Every record consumes a leading
tag, so input length plus one is sufficient fuel. 

### `readRecordsAux_sound`

 Successful decoding determines exactly the consumed prefix. 
