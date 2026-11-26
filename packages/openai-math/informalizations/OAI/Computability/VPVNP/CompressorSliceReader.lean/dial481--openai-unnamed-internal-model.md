---
{
  "module": "OAI/Computability/VPVNP/CompressorSliceReader.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSliceReader.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSliceReader.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The two advised physical readers for the actual compressor algebra

At every admissible prime and slice, the same two fixed programs return the
multiplication and Frobenius coordinates. All the initial field, coefficient,
rank and monomial advice is selected before the exponent widths and coordinate
ordinals. A single length-indexed budget bounds both programs.


### `read`

 The bit selects the fixed Frobenius or label-multiplication control. The
program and its ports do not depend on the input length or the field. 

### `sliceReaderFintype`

 Finite enumeration of the slice's ground field used in the coordinate reader construction. 

### `sliceReaderDecidable`

 Classical equality decision on ground-field elements used by the slice reader. 

### `exists_sliceReaderAdvice`

 The deterministic coordinate readers, their common advice and their
uniform bounds for one model. The field-coordinate map is the one used in
the terminal test of the nondeterministic evaluator. 
