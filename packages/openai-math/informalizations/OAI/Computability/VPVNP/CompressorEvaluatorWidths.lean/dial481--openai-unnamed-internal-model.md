---
{
  "module": "OAI/Computability/VPVNP/CompressorEvaluatorWidths.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorEvaluatorWidths.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorEvaluatorWidths.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniform field widths and the canonical compressor presentation

The physical slice-field representation, including the Frobenius divisor and
Fermat-inversion workspace, uses a width bounded before choosing the advised
prime or the exponent array. The indexed matrices come from the same joint
grammar and compressor equations used by the algebraic descent.


### `fieldWidthFintype`

 Finite enumeration of the slice ground field used when bounding its physical
representation. 

### `fieldWidthDecidableEq`

 Decidable equality of elements of the slice ground field used in the width calculation. 

### `fieldWidthAmbientAlgebra`

 Algebra structure induced on the ambient field by the slice embedding for the given column
bound. 

### `fieldWordBound`

 Width for field limbs and their Fermat-inversion counters. 

### `cardinalBits`

 Choose the actual bit array for the field-cardinality divisor with one
extra bit so a cardinality which is a power of two is encoded literally. 

### `field_parameters_le`

 Every allowed characteristic uses the same length bounds for the input
divisor, extension degree and required field working width. 

### `compressorCanonical`

 The canonical monomial listing for the actual two-block compressor model.
Its integer reader addresses word equations first, followed by the two fixed
templates' equations. 
