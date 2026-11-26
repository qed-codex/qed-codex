---
{
  "module": "OAI/Computability/VPVNP/RAMTapeISAPrepare.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeISAPrepare.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeISAPrepare.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Compiling the deterministic work of every RAM instruction

Each fixed instruction selects one finite stack routine. Register operands are
copied before overwriting a destination. Conditional branches leave one test
bit. Operations handled by the outer call controller return immediately.


### `prepare`

 Compile the deterministic portion of an instruction, staging operands and leaving a
comparison bit for a conditional jump. 

### `preparedBank`

 Bank after the instruction’s local effects, with its jump-test bit placed on work stack
zero when applicable. 

### `prepareBound`

 The dispatch bound is independent of register values, addresses, and
private branch choices. Each private load may inspect every prior write. 
