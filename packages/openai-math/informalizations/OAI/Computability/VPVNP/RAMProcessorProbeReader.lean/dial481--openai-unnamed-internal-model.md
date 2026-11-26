---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorProbeReader.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorProbeReader.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorProbeReader.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# External read guesses on the architectural processor bank

The source address word supplies the width. The guessed value is placed in
the independent record-value field, so its bits cannot overwrite an aliased
address register before the address is recorded. A short stream exits in
rejection at the first missing bit.


### `reader`

 Read as many private choice bits as there are bits in the address register and stage the
resulting word. The Boolean exit reports whether the entire word was available. 

### `reader_run`

 Complete-word input preserves the address and leaves the exact unused
choice suffix. Width zero consumes no choice bits. 

### `reader_short`

 Short-word input reaches the rejecting exit without dispatching any
following instruction. The contents of that rejected branch need no rewind. 
