---
{
  "module": "OAI/Computability/VPVNP/EvaluatorAdviceSerialization.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorAdviceSerialization.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorAdviceSerialization.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Binary advice for the finite-algebra evaluator

The tape begins with a fixed-width prime header. Once the prime is known, the
extension degree is determined by the system's variable and degree bounds.
The following fields contain the low coefficients of the monic modulus, one
pin bit per variable, and one field element per variable. The pin values use
the same power basis as the evaluator's final coordinate query.


### `degree`

 The extension degree chosen for characteristic p and the column-count bound on the slice
system in t variables of degree at most d. 

### `vectorBits`

 Bit width of one power-basis coefficient vector. Each of its e residues occupies the
ceiling of the base-two logarithm of p in bits. 

### `length`

 The length of the advice prefix consisting of the prime header, modulus coefficients, pin
mask and t value vectors. 

### `Fields`

 The modulus coefficients, pin mask and specialized field elements in the advice for a slice
over characteristic p. 

### `Fields.coefficients`

 The e lower coefficients of the monic modulus defining the advised power-basis field
  representation. 

### `Fields.pins`

 One bit per system variable identifying the coordinates fixed by the slice. 

### `Fields.values`

 The advised power-basis value for each variable, including each coordinate marked by the
  pin mask. 

### `valueBits`

 Serialize all `t` values consecutively, including those at unpinned coordinates. 

### `encode`

 Write the fixed-width prime, the lower modulus coefficients, the pin mask and all
coordinate values consecutively on the binary advice tape. 

### `readBits`

 Read consecutive bits at an absolute address, with zero outside the tape. 

### `readPrime`

 Decode the prime header as a natural number from the first w bits of the advice tape,
padding missing bits with zero. 

### `readFields`

 After the prime header is decoded, all remaining offsets are fixed. 

### `parse`

 Parse a prime from the tape and use the degree selected in Section 8.2.
The tape may have trailing padding. A composite header or short tape fails. 

### `noncomputable local instance (p : Nat.Primes) (t d : ℕ) : Fintype (Ground p t d)`

 A finite enumeration of the slice ground field for representing the advised pin values. 

### `exists_model_advice`

 All advised pin values have coefficient vectors in the same quotient
presentation that realizes the evaluator's prime-field coordinate. 
