---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafScalarStartup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafScalarStartup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafScalarStartup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Initializing all scalar stacks of the actual auxiliary RAM

Starting at the first allocation row, the only data-dependent inputs are
the real source registers, the arena base and capacity. The resulting
private memory function is determined on every address. The incident
stack is empty for the ensuing half-wire copy.


### `ScalarPort`

 A private stack port of the concrete leaf site processor with 52 registers and 34 public
operands. 

### `ScalarReg`

 The concrete register bank for filling the scalar ports from site data and the validator's
34 public operands. 

### `ScalarLabel`

 Instruction labels for allocating, staging and filling the concrete validator's scalar
stacks. 

### `portOrder`

 Enumerate all concrete scalar ports by consecutive indices for the startup traversal. 

### `scalarRows`

 The list of all scalar ports visited once, in the order used to allocate and fill the
private stacks. 

### `scalarInput`

 The scalar stacks encoded from the auxiliary site's input, its half-wire buffers and the
counter's public operands, with the incident stack awaiting its separate copy. 

### `scalarTicks`

 Exact instruction count for allocating and filling the concrete list of scalar ports at
this auxiliary site. 

### `scalar_start`

 The whole allocation-and-scalar pass in the enclosing machine, including
its exact scratch update and preservation of all other native registers. 
