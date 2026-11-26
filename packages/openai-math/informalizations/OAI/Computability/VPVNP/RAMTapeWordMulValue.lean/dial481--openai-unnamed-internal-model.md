---
{
  "module": "OAI/Computability/VPVNP/RAMTapeWordMulValue.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWordMulValue.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWordMulValue.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Multiplication on fixed-width bit tapes

In each round the multiplier supplies its next low bit. A single synchronous
scan of the other two words shifts the multiplicand and adds its selected
bits to the accumulator. Discarding the last shifted bit and the last carry
implements the word RAM's multiplication modulo its word size.


### `mulScan`

 Emit the previous multiplicand bit and the current accumulator sum bit.
The finite control retains the shifted-out bit and the adder carry. 

### `mulRound`

 Start one shift-and-add scan with zero incoming shift bit and carry. 

### `mulFold`

 Consume the multiplier from low to high, retaining the two output words
between rounds. 

### `mulScan_overflow`

 Each finite scan discards whole multiples of the word modulus. 

### `value_mulFold`

 The full shift-and-add computation, including an arbitrary initial
accumulator, is the low word of the mathematical product plus that accumulator. 

### `mulFold_wordBits`

 Starting with a zero tape produces the canonical bit string of the
word product, including when the word multiplication wraps around. 
