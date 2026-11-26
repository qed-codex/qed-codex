---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticStreamRow.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticStreamRow.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticStreamRow.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# One streamed Horner row on bit stacks

The fixed control reads the next modulus and multiplier coefficients, runs the
four residue operations, emits the resulting limb, and saves the old
accumulator coefficient for the next row. The output is built in reverse bit
order so a single stack reversal restores all limbs to their input order.


### `loadLimb`

 Consume the next limb from stream `s` and load it into arithmetic register `i`. 

### `emit`

 Store the result from register six on the output stack in reversed bit order for the final
reversal. 

### `body`

 Read a modulus limb and a multiplier limb, compute and emit the row result, then load the
next shifted predecessor. 

### `nextRegisters`

 Register contents after a Horner row, including its result, second product, and the old
accumulator limb needed by the next row. 

### `nextStreams`

 Stream contents after one Horner row, with consumed inputs replaced by their tails and the
emitted result on the output. 
