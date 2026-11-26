---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticAdd.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticAdd.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticAdd.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Vector addition on serialized coefficient streams

A marker-controlled loop consumes the two vectors in increasing degree
order. Each iteration loads two limbs, adds modulo the supplied modulus,
and emits the sum. One final reversal puts the coefficient vector into the
first input port, with the original order of limbs and bits.


### `vectorOp`

 Apply the chosen residue operation once per degree marker, then reverse the emitted limbs
onto the coefficient stack. 

### `streams`

 The two input ports retain their suffixes. The caller supplies a scratch
port, an output port and a marker port for the duration of the call. 

### `Preserves`

 Registers outside the two operand slots and the result slot are preserved. 

### `vectorOp_runs`

 Run one chosen prime-field operation on every pair of corresponding limbs. 

### `vectorAdd`

 Addition of two packed coefficient vectors. 

### `vectorAdd_runs`

 The coefficient vector returned by the fixed control is the exact vector
sum in the advised quotient. Both input suffixes survive the operation. 
