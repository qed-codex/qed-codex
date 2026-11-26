---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorCallStartup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorCallStartup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorCallStartup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # State and native semantics of a freshly charged physical call 

### `Snapshot.prepared`

 State just after charging call startup and initializing the fresh private instruction
configuration, when cumulative cost is below the cap. 

### `Snapshot.localResult`

 Run the template from the current snapshot using its fuel and choices and the least of its
call, global and site probe allowances. 
