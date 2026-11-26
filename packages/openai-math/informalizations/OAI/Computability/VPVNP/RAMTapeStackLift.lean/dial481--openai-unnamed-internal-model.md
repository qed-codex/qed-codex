---
{
  "module": "OAI/Computability/VPVNP/RAMTapeStackLift.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeStackLift.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeStackLift.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Installing a stack routine in a larger machine

Stack labels may be renamed into any disjoint set of ports. Control labels
may name states of the caller. Deterministic executions can be installed even
when a terminal state of the subroutine is used as a continuation by the caller.
Only the installed stacks can change during such an execution.


### `StackOp.rename`

 Relabel the stack and control references of an instruction, preserving its operation and
its halt verdict. 

### `StackOp.returns`

 A source `halt` can be a return boundary for the linked machine. 

### `installStacks`

 Replace the stacks at installed ports and retain the ambient values at all
other labels. The injection hypothesis is used in the restriction theorems. 

### `StackStep.lift`

 Lift one deterministic source instruction with exactly the same cost. 

### `StackRuns.lift`

 Linking preserves each step and each ambient stack outside the routine.
No control equality is required at the final state if it returns. 

### `stackPaths_lift`

 If all rows, including halts and choices, are renamed, the bounded path
counts agree on every installed stack. Control names need only agree on the
states used by the source. 
