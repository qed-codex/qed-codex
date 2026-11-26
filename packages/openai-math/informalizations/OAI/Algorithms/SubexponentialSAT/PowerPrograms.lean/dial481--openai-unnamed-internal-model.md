---
{
  "module": "OAI/Algorithms/SubexponentialSAT/PowerPrograms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/PowerPrograms.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/PowerPrograms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Variable exponentiation with finite Boolean control

The exponent is a binary stack word.  The multiplication callback below uses
only fixed finite programs and leaves the countdown ports untouched.


### `stackState`

 Base, exponent, accumulator, five work ports, and counter scratch. 

### `nextAccumulator`

 The left operand is always a copy of the fixed base. 

### `iterateAccumulator`

 A specification of the successive accumulator words, not an instruction
that the compiled program evaluates on an unbounded natural register. 

### `Invariant`

 The invariant ignores the countdown's two ports and all finite registers. 

### `command`

 The only loop bound is the binary word on the exponent stack. 

### `program`

 A fixed 85-label program, independent of base and exponent. 

### `workBound`

 A polynomial in numerical exponent and the actual input word lengths. 

### `run_value`

 Complete natural-power correctness, including a bound for the actual raw
output representation and a halted instruction trace. Leading zeros are allowed. 

### `primitive_value`

 The same fixed program runs on primitive tapes with a fixed compilation
factor multiplying the explicit polynomial arithmetic-work bound. 
