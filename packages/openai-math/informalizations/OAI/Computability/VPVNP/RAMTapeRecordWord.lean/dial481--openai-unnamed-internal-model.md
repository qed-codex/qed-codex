---
{
  "module": "OAI/Computability/VPVNP/RAMTapeRecordWord.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeRecordWord.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeRecordWord.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Record buffer word registers

The pre-sort probe records are accumulated in reverse bit order. Copying a
staged word into the buffer restores the source using one scratch stack.


### `Port`

 The five staged word fields, temporary copy stack, reverse buffer, free-slot counter,
zeros, and output of the record emitter. 

### `appendWord`

 Copy one staged word into the reverse record buffer, restoring the source word afterward. 
