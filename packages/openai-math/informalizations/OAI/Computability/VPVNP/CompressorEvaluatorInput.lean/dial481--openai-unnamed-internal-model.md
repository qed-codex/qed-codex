---
{
  "module": "OAI/Computability/VPVNP/CompressorEvaluatorInput.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorEvaluatorInput.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorEvaluatorInput.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Advised coordinate readers for the compressor label system

This record describes the exact binary interface between the deterministic
coordinate queries and the fixed nondeterministic evaluator. All fields are
selected at the input length, before the exponent vector and its width.


### `readerInputFintype`

 Finite enumeration of the ground field used by the matrix-entry readers. 

### `readerInputDecidableEq`

 Decidable equality of slice ground-field elements for the evaluator input construction. 

### `readerInputAmbientAlgebra`

 Ambient algebra structure induced by the ground-field embedding used in the reader
presentation. 

### `SliceReaderAdvice`

 The physical advice and two verified entry readers for this particular
finite slice. The counters and field inputs are common to all later calls. 

### `SliceReaderAdvice.degreePred`

 One less than the extension degree in the polynomial presentation supplied to the reader. 

### `SliceReaderAdvice.coefficients`

 Prime-field coefficients specifying the monic modulus for the advised field presentation. 

### `SliceReaderAdvice.fieldMap`

 Algebra isomorphism identifying residue classes modulo the advised modulus with elements
  of the slice ground field. 

### `SliceReaderAdvice.indexWidth`

 Bit width used to address rows and columns of the advised query matrices. 

### `SliceReaderAdvice.limbWidth`

 Width of the arithmetic limbs used by the entry readers, large enough for their
  prime-field operations. 

### `SliceReaderAdvice.extra`

 Auxiliary input stacks made available to the Frobenius and label matrix readers. 

### `SliceReaderAdvice.extraSpace`

 Common upper bound on the length of each auxiliary reader stack. 

### `SliceReaderAdvice.peak`

 Peak space bound shared by the Frobenius and label entry-reading routines. 

### `SliceReaderAdvice.queryExponent`

 Exponent specifying the power-of-two time budget for one advised matrix-entry query. 

### `SliceReaderAdvice.binary`

 All persistent advice fields of the actual evaluator at this length. 

### `SliceReaderAdvice.envelope`

 Joint width, workspace and query-time exponent envelope for this length. 

### `SliceReaderAdvice.resources_and_value`

 At every exponent width, the fixed table returns the canonical model's
functional and its literal computation stays inside a polynomial tape window. 

### `SliceReaderAdvice.evaluate`

 The algebra value and full history window for callers which execute the
table at their own clock. 
