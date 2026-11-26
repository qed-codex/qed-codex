---
{
  "module": "OAI/Computability/VPVNP/RAMTapeISADispatch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeISADispatch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeISADispatch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# One finite stack control for a fixed RAM instruction table

The control for a template contains entry and exit states for every program
counter and the finite states of its operand routines. Its states and code
are fixed before choosing a word width, public data, or a private execution.
The typed boundary states allow the caller to implement external accesses,
binary choices, the per-instruction clock and return propagation.


### `State`

 Dispatcher states for program-counter entry, execution of its preparation routine,
instruction exit, and typed callback. 

### `entry`

 Enter the fixed table at the given program counter. 

### `callback`

 Embed a typed instruction exit in the dispatcher state space. 

### `resume`

 Identify precisely the outer-controller callback boundaries. 

### `code`

 The complete deterministic dispatch table, with callbacks initially
represented by halts. Linking replaces their behavior in the caller. 

### `dispatch_step`

 The outgoing bank and the typed callback are explicitly determined by the
instruction, independently of how the caller uses either one. 

### `dispatch_run`

 Every reached instruction follows its fixed template table to a typed exit
and implements exactly one native small step. The pathwise cost includes the
initial transfer and the final callback selection. 
