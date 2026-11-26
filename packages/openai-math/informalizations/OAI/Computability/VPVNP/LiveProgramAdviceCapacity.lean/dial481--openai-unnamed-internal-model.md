---
{
  "module": "OAI/Computability/VPVNP/LiveProgramAdviceCapacity.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramAdviceCapacity.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramAdviceCapacity.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Choosing the live advice exponents before the address multiplier

The raw evaluator prefix and the number of labels have bounds independent
of the processor geometry. For each fixed address multiplier the quartic
word width eventually fits in the input length. Thus one pair of exponents
suffices for the raw prefix capacity and the entire distributed advice
array for every later choice of multiplier.


### `capacity_exponents`

 The exponents are uniform in the address multiplier. The first capacity
bounds the actual raw input, and the second bounds the length word, the
padded raw region and the serialized ordinal table together. 

### `adviceTape`

 The canonical distributed tape includes exactly the remaining number
of zero padding cells after the ordinal table. 

### `adviceTape_eventually`

 The same exponents also give a canonical advice tape of exactly the
prescribed size for every possible raw string and ordinal table within
the uniform bounds. 

### `native_capacity_exponents`

 The raw capacity can be chosen once for the native evaluator's actual
bit-stack advice, uniformly over its endpoint, stack contents and divisor
whenever the divisor length and the payload bank satisfy the stated envelopes. 

### `native_raw_fits`

 Applying a single native capacity bound to the concrete advice payload.
The field, basis coordinates and endpoint may vary without changing the bound. 
