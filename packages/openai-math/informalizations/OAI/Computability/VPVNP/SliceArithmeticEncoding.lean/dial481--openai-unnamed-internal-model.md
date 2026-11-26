---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticEncoding.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticEncoding.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticEncoding.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Power-basis encodings at the evaluator interface

Field values at the scalar-query boundary have canonical coefficient vectors.
The packed input to the arithmetic routines consists of those same residues
padded to the working register width. The first packed word computes the
prime-field coordinate used by the accepting-branch routine.


### `valueEquiv`

 The quotient representation and canonical low-degree-first coefficient
vectors form a bijection. 

### `scalarEncoding`

 Encode a scalar computed by the matrix-entry oracle into the chosen
polynomial basis of its actual ground field. 

### `mul_scalarEncoding`

 Arithmetic on the query result and accumulator produces the canonical
coefficient encoding of the product in the actual ground field. 

### `limb_padded`

 Widening a canonical limb for modular arithmetic appends high zero bits. 

### `packed_advice`

 The compact binary advice for a coefficient vector is exactly its packed
stream at the minimum coefficient width. 

### `packed_low_limb`

 The first complete word of a nonempty packed product is the low limb.
The terminal callback may carry arbitrary additional bits after the product. 

### `packed_primeCoordinate`

 On the selected advice, reading the first word of the accumulator gives
the representative in `[0,p)` of its evaluator output. 
