---
{
  "module": "OAI/Computability/VPVNP/AdviceCircuitCompiler.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/AdviceCircuitCompiler.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/AdviceCircuitCompiler.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Translating coefficient verifiers to bit-stack interpreter advice

The initial valuation stack holds zero, one, the query word, and the candidate
witness, in that order. A gate pushes its result, so a reference to an earlier
gate is addressed from the newest gate backwards. Two final NOT instructions
copy the designated output to the top, including for circuits with no gates.


### `inputs`

 Initial valuation in stack order, with false and true followed by the query bits and the
candidate witness bits. 

### `address`

 Address in the valuation stack after `n` instructions. 

### `instructions`

 Compile the gates of a Boolean transcript program into unary-address instructions in gate
order. 

### `compile`

 Compile all gates and copy the designated output to the top. 

### `compile_size`

 Unary addresses make the bit length quadratic in the combined input and gate bound. 
