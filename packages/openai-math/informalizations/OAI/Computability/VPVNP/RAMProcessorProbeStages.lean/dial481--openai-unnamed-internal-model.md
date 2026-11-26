---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorProbeStages.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorProbeStages.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorProbeStages.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# External-probe stages of the burst processor

Only a complete guessed word enters the register-update and record staging
routine. The successful path consumes exactly that word and preserves the
rest of the private stream. A write consumes no private bits.


### `read`

 On a read, resume at the caller's successful label or short-input label. 

### `read_work_le`

 In a normal architectural bank the destination is one word, and the
record fields are empty or left over from a single preceding record. 
