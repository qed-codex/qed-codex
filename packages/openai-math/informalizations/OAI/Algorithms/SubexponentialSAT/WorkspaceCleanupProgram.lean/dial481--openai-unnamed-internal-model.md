---
{
  "module": "OAI/Algorithms/SubexponentialSAT/WorkspaceCleanupProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/WorkspaceCleanupProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/WorkspaceCleanupProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Actual fixed workspace cleanup

The selected ports are part of the finite program. Their initial contents
and lengths are arbitrary. Every clear is an existing measured instruction
loop, and all unselected stacks and non-scratch registers are preserved.


### `cost_after_runsIn`

 Actual trace growth bounds cleanup without a separate size assumption
for each work array. A concrete instruction allocates at most one new bit. 

### `prefixPorts`

 An explicit static initial segment of stack ports. 

### `procedure`

 Main procedures automatically place all scratch registers below the
three protected caller-control bits. The stack map is the identity. 
