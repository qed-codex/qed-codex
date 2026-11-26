---
{
  "module": "OAI/Computability/VPVNP/RAMTapeMapWord.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeMapWord.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeMapWord.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Emitting the bits of a record word without consuming its register

The buffer for the pre-sort probe records is accumulated in reverse bit
order. A fixed pop/push control copies each word's bits onto this buffer and
restores the source using one scratch stack.


### `saveBit`

 Copy a single popped bit to the accumulating record buffer and save it
temporarily for restoration. 

### `mapWord`

 Copy the source word to the reverse buffer bit by bit through the given Boolean map, then
restore the source from scratch. 

### `mapWord_run`

 Five primitive instructions per source bit and the two empty-stack tests. 

### `zero_template`

 Prepare a zero word from the preserved width template, using one empty
scratch stack. Every input bit contributes one output zero. 
