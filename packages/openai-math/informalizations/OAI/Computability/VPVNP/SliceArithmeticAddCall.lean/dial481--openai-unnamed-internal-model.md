---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticAddCall.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticAddCall.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticAddCall.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Vector addition with a clean calling convention

The two operand streams belong to the caller. A copy of the degree markers
controls the scan, and copies of the modulus and zero word initialize its
registers. The scan consumes the query and writes its result directly onto
the accumulator. The registers are reclaimed before the call returns.


### `Port`

 Ports for a reusable scalar addition call, pairing its coefficient-scan workspace with the
caller's field and operand stacks. 

### `clean`

 The caller's external stacks, with every private port empty. 

### `operation`

 The coefficient scan has one fixed table for each prime-field operation. 

### `callCap`

 Initialization, the vector scan, and register cleanup, in bit-stack steps. 

### `operation_runs`

 Consume the query and replace the accumulator by the coefficientwise result. 

### `machine`

 Add two packed coefficient vectors with the shared field-arithmetic port convention. 

### `machine_runs`

 Add the query to the accumulator, consuming the query and reclaiming every
private stack. The modulus, zero word, degree markers and coefficient advice
are available to subsequent calls. 
