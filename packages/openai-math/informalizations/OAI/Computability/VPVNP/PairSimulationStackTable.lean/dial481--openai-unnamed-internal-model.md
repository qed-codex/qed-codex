---
{
  "module": "OAI/Computability/VPVNP/PairSimulationStackTable.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationStackTable.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationStackTable.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite private RAM table for a named bit-stack program

Each continuing stack instruction uses exactly four native transitions.
Stack top and base pointers are retained in separate registers. No opcode
accesses external memory. The true halt jumps to the caller's continuation.


### `Register`

 Logical registers of the bit-stack machine, with a base and exclusive top pointer per stack
and shared zero, one, and temporary registers. 

### `instruction`

 Unused instruction slots reject. Empty and nonempty pops have separate
three-transition continuations after the initial pointer comparison. 

### `Linked`

 The host instruction table implements all seven slots for every stack-code state with the
specified register allocation and accepting continuation. 

### `PC`

 Standalone stack program addresses, consisting of seven instruction slots for each control
state and one accepting exit. 

### `rowPC`

 Numbered machine program counter for instruction slot `i` in the compiled row of stack-code
state `q`. 

### `donePC`

 Numbered accepting continuation of the standalone stack program. 

### `register`

 Embed the named stack registers in the standalone machine's consecutively numbered register
file. 

### `table`

 A finite complete table, before instantiating its word width. 
