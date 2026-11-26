---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorInitFields.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorInitFields.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorInitFields.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Staging the site's prescribed initialization record

The input preparer supplies the site address and packed header word in fields
one and two. The fixed staging routine sets the initialization tag, copies the
site address to the start-cost field, and copies the zero word to the ordinal.
It restores all inputs and its two scratch stacks before record emission.


### `InitField`

 The initialization record fields supplied by the staging routine, namely its tag, start
cost and ordinal. 

### `initFields`

 Stage the initialization tag, copy the site address into the start-cost field and fill the
ordinal field with zero. 

### `initialized`

 Record-buffer contents after setting the initialization tag, the start cost equal to the
address, and the probe ordinal to zero. 
