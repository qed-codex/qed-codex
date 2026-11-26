---
{
  "module": "OAI/Computability/VPVNP/FixedModelDiagonal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/FixedModelDiagonal.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/FixedModelDiagonal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The per-length diagonal for a fixed joint model

The physical first-half counter vector stores production counts in parser order and
compressor counts after them. The midpoint advice reorders this vector into the label
coordinates of the joint equations. The same order is used in the evaluator's initial
configuration, its modular path count, and the weighted primed contraction.


### `diagonalGroundFintype`

 Enumerate the finite ground field in the local certificate. 

### `diagonalGroundAlgebra`

 Use the slice embedding to give the ambient field its ground-field algebra structure. 

### `diagonalProductionDecEq`

 Decide equality of production labels in the physical counter order. 

### `denseCount`

 Number of counters in the first-half live cut, in physical parser order. 

### `formalExponents`

 The midpoint scatter turns a physical counter vector into an evaluator input. 

### `prefix_lt`

 Every prefix of the `2^h` pairs fits in `Z` bits, including the last prefix. 

### `LocalCertificate`

 The length-specific compiler data used in Proposition 9.1 and §14.3. `program` and `E`
are explicit parameters so an eventual construction can fix both tables before choosing `n`.
The processor realization is supplied separately to `false_of_processor`. 

### `LocalCertificate.advice`

 The common advice bits distributed to all groups of the chain. 

### `LocalCertificate.Path`

 Finite paths for the given exterior, pair index and nominated production multiplicities. 

### `LocalCertificate.ν`

 Multiplicity of each compressor label on the selected pair path. 

### `LocalCertificate.initial`

 Initial scalar evaluator configuration for an exponent vector in formal label order. 

### `LocalCertificate.init`

 Bounded encoding of the midpoint configuration for counters in physical order. 

### `LocalCertificate.false_of_processor`

 The physical single-site equality and the certificate's single-group equality yield the
integer two-mode count. Reducing that count in the finite algebra gives the contradiction. 
