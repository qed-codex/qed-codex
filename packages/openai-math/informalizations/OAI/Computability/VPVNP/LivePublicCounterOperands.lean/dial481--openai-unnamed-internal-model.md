---
{
  "module": "OAI/Computability/VPVNP/LivePublicCounterOperands.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LivePublicCounterOperands.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LivePublicCounterOperands.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The auxiliary public table in the live linker's operand format 

### `actualPrefix`

 The length and packed word of the supplied universal-machine program's literal prefix. 

### `operands`

 Positions 7 and 12 come from the input prefix. Every other operand uses geometry arithmetic. 

### `fixed_runs`

 Physical execution of the auxiliary table loader, with a fixed program independent of its own prefix. 
