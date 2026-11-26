---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordPrivateDescriptor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordPrivateDescriptor.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordPrivateDescriptor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Publishing computed operand words to a private call descriptor

The same two-instruction store and increment used for the native scalar cache installs
an arbitrary fixed bank of words here. A two-instruction prelude copies the preserved
descriptor pointer and sets the increment to one. Every source register survives.


### `store`

 The instruction that stores the selected register value at the private descriptor cursor
and jumps to its increment. 

### `Linked`

 The linked instruction addresses that copy the descriptor pointer, set a unit increment,
and store and advance through all values. 

### `publish`

 The computed words are published contiguously while preserving the call pointer
and all private data outside its exact interval. 
