---
{
  "module": "OAI/Computability/VPVNP/LabelEvaluatorReaderWidth.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LabelEvaluatorReaderWidth.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LabelEvaluatorReaderWidth.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Prime-independent word widths for the actual finite-slice equations 

### `readerWidthsFintype`

 Finite enumeration of the ground field used in bounding the reader's register widths. 

### `readerPlan`

 Address widths chosen before the prime, pins, or target monomial. 

### `readerWordWidth_polynomial`

 Uniform polynomial in the input length for the register width of the
augmented matrix and its target rows. 

### `readerLimbWidth`

 Uniform working widths for the coefficient limbs and the number of
extension coefficients staged in each matrix reader. 

### `readerExtensionBound`

 Bound for the extension degree in terms of the monomial column count and a bound on the
prime's bit length. 
