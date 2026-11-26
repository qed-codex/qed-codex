---
{
  "module": "OAI/Computability/VPVNP/RAMVirtualCeilLog.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMVirtualCeilLog.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMVirtualCeilLog.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Ceiling logarithm in the private word RAM

Each iteration replaces the operand by its rounded-up half. Registers zero and
one hold the constants one and two. Registers two and three hold the operand
and the iteration count. The terminal comparison is included in the cost.


### `clogStep`

 The three arithmetic instructions between successive loop tests. 

### `clogLoop`

 Repeated rounded-up halving of register two, counting in register three. 

### `clogRun`

 Starting at zero the counter returns the ceiling logarithm. The only events
are ticks, and the loop retains every register except its operand and counter. 
