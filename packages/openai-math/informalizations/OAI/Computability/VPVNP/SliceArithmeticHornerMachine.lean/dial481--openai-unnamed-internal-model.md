---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticHornerMachine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticHornerMachine.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticHornerMachine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniform bit-stack multiplication in the advised polynomial basis

One finite instruction table reads a stack of Horner digits, runs a complete
coefficient scan for each digit and installs the resulting accumulator. Its
control is independent of the prime, extension degree and register width.


### `digitRoutine`

 A digit body stages its input, runs the coefficient scan and restores the accumulator. 

### `machine`

 Consume one round marker per Horner digit and execute a complete coefficient scan for each
digit. 

### `digitCap`

 Cost of the preparation, inner scan and output reversal. 

### `initialRegisters`

 The register bank at entry holds the prime modulus and zero coefficients. 

### `machine_runs`

 A single fixed finite control multiplies arbitrary coefficient vectors
of positive degree. It consumes all digits and stores the quotient-ring
product as low-degree-first, little-endian words in the accumulator port. 
