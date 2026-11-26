---
{
  "module": "OAI/Computability/VPVNP/RAMTapeRoutinePorts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeRoutinePorts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeRoutinePorts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Preserving the caller's other stacks when running a finite routine 

### `FiniteRoutine.onPorts`

 Run an existing routine at the caller's physical port names. The control
states, including the normal return, are copied verbatim. 
