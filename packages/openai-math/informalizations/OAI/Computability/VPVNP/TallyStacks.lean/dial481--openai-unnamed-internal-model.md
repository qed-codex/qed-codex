---
{
  "module": "OAI/Computability/VPVNP/TallyStacks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TallyStacks.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TallyStacks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Unary registers in a fixed bit-stack program

The validator's input offsets are natural numbers. A stack of true marks stores
such a number without placing it in the control. The routines below transfer
or add registers with an exact stack-instruction cost.


### `State`

 A natural-number value for each tally register. 

### `encode`

 Represents each unary register by a stack containing one true bit per unit of its value. 

### `drainRuns`

 Loop from a unary count `n` to zero. A body runs once per mark, with its
actual cost and state allowed to vary between iterations. 

### `move`

 Transfers marks from a source stack to a distinct destination until the source is empty,
adding its tally to the destination. 

### `copyAdd`

 Preserve the source while adding its contents to the destination. 
