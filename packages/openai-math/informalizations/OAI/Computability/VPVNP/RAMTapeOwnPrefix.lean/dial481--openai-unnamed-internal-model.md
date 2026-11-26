---
{
  "module": "OAI/Computability/VPVNP/RAMTapeOwnPrefix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeOwnPrefix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeOwnPrefix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Packing the processor's own parsed prefix

The prefix remains on the processor's input-reader stack. A fixed stack
routine extends these bits to the physical word width and counts their
actual length into a second word. It takes the prefix solely as data.


### `program`

 Extend the copied prefix and count its bits. The same stack table is
used for every processor and every program on the input tape. 

### `steps`

 Step count for padding and packing the parsed prefix and computing its length as a word. 

### `runs`

 `.header` is the saved prefix and `.width` the saved unary word width.
The two output fields receive its packed bits and its packed length. 
