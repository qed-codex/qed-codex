---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticPower.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticPower.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticPower.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Powers and inverses in the evaluator's finite slice field

Each instruction in the binary powering routine is one multiplication of
coefficient vectors. The inverse routine handles zero separately, including
the case of a field of order two where the Fermat exponent is zero.


### `PowerStep`

 An instruction takes the running product and either squares it or
multiplies it by the original base. 

### `powerSteps`

 Read the binary exponent from its most significant bit. 

### `powerSteps_length`

 The exact number of vector multiplications is the bit length plus the
number of one bits. 

### `PowerStep.run`

 Execute one binary powering instruction by squaring the accumulator or multiplying it by
the saved base modulo the defining polynomial. 

### `pow`

 Execute the binary powering program with initial value one. 

### `inverse`

 Zero gets the zero vector. A nonzero input uses the Fermat exponent. 

### `inverseSteps`

 The instructions executed for the input-dependent inverse routine. 

### `adjoinRoot_card`

 A monic presentation of degree `e` over the prime field has `q ^ e` elements. 
