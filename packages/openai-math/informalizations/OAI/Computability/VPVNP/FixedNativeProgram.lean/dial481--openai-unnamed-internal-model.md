---
{
  "module": "OAI/Computability/VPVNP/FixedNativeProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/FixedNativeProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/FixedNativeProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Choosing the exceptional length after the literal program

The same pair table, evaluator, public operand formulas, and layout powers
serve every candidate length. The actual compiled coefficient machine then
has one common eventual threshold. At a candidate small-circuit length the
integer equations supply the prime and a finite algebra. Only at that point
are the advice, weighted paths and evaluator configurations selected.


### `Program`

 The finite tables and exponents chosen before the exceptional length. 

### `Program.constants`

 Powers and label counts used by the live program at every input length. 

### `Program.evaluator`

 Scalar evaluator installed in the second half of the diagonal chain. 

### `Program.pair`

 Finite instruction table for a pair in the first half of the chain. 

### `Program.addressFactor`

 Multiplier of the binary address width at input length n. 

### `Program.numerator`

 Numerator of the rational exponent used to compute the live bucket size. 

### `Program.denominator`

 Denominator of the rational exponent used to compute the live bucket size. 

### `Program.initialLiteral`

 Initial persistent word supplied to the live RAM program. 

### `native`

 The linked RAM instruction table with the chosen evaluator and pair code. 

### `operands`

 Public operand expressions passed to the linked RAM table. 

### `literal`

 The fixed universal-machine program obtained by compiling the live RAM table and its operand expressions. 

### `geometry`

 Address width, bucket size and word width of the live program at the given input length. 

### `liveMachine`

 Instantiate the linked RAM table with public words computed from the compiled program prefix. 

### `OperandFits`

 Every public operand expression fits the available word width at this length. 

### `Certificate`

 Local realization for one chosen joint model. Its fields consist of
individual pair weights, individual tail counts and native one-group path
counts. The actual shared processor coefficient is proved separately. 

### `Realizes`

 At sufficiently large lengths the fixed tables meet the local model
obligations for the primes furnished by the arithmetic specialization. 
