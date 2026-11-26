---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorProbeContinue.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorProbeContinue.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorProbeContinue.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Resuming the physical call after an admitted probe

The native read continuation sees the exact guessed value. The write
continuation sees its original register bank. Both consume precisely the
probe just staged and recorded by the graph.


### `event`

 Native read or write event corresponding to the staged probe. Its address comes from the
original register bank even if a read overwrites the address register. 

### `continue_run`

 Inductively transfer the entire successful or failed continuation. 
