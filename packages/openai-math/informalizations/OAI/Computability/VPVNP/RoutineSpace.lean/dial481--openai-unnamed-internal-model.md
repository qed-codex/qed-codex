---
{
  "module": "OAI/Computability/VPVNP/RoutineSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RoutineSpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RoutineSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Preserving stack space across nested calls

Installation, returning calls and sequential composition reuse the same bit-stack
space bound. They can therefore compose exponentially long subroutines without
adding their running times to the caller's space use.


### `SpaceRun.lift`

 Lift control and ports without changing the number of steps or the cap, provided
all caller stacks outside the installed bank already lie below the cap. 

### `BoundedRun`

 Execution of a standalone routine from entry to return in exactly `n` steps with every
stack height bounded by `cap`. 
