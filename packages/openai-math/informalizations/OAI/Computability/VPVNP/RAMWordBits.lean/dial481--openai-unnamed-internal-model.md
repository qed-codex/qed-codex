---
{
  "module": "OAI/Computability/VPVNP/RAMWordBits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMWordBits.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMWordBits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading one RAM word from a bit stream

The private choices for a reported RAM call contain fixed-width read answers.
They use the same least-significant-bit-first encoding as the shared messages.


### `wordBits`

 The `w` consecutive bits of a word, in increasing order of significance. 

### `takeWord`

 Consume one bit per iteration. Each return computes the word by a single
left shift and the addition of its low bit, without inspecting the suffix. 

### `meteredTakeWord`

 Meter the width test, list dispatch, low-bit conversion, shift and addition.
On a short stream, including when the first missing bit is the last requested
bit, the parser returns within the same bound as on a complete word. 

### `meteredTakeWord_spec`

 The metered stream parser realizes the decoder used by local calls. 
