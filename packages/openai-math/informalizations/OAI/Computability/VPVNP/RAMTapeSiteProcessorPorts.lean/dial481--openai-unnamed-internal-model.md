---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSiteProcessorPorts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteProcessorPorts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteProcessorPorts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical port names shared by the live processor passes

The call loop reads the same fuel and cost stacks prepared by the parser and the same two
cut words just checked by the guard. Separate stacks hold the predecessor records, the
unconsumed incident vector, and the read-only slot count needed by the sorting pass.


### `Port`

 Full site bank combining operand initialization and native execution with guard and sorting
workspaces. 

### `pub`

 Embed a parsed public processor port into the full site bank. 

### `native`

 Embed a native private-interpreter port into the full site bank. 

### `cut`

 Connect public guard ports to the parsed fields and private guard ports to their dedicated
auxiliary stacks. 

### `external`

 The operand, credit, comparison and record ports that share existing stacks. 

### `callPorts`

 Route call-controller ports to their shared public or guard stacks when connected, and
otherwise to their native stacks. 
