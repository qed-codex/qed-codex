---
{
  "module": "OAI/Computability/VPVNP/CompressorEvaluatorAdvice.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorEvaluatorAdvice.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorEvaluatorAdvice.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Polynomial-length slice advice for the joint compressor labels

The prime header allows the fixed positive characteristic, as well as the
good prime chosen at the current length in characteristic zero. With that
header width one fixed padding exponent accommodates the actual serialized
finite-field presentation and all affine-slice pin data.


### `adviceGroundFintype`

 Finite enumeration of the slice ground field used to encode the evaluator's advice. 

### `compressorHeaderWidth`

 The extra high bit ensures the prime fits even at equality in the
characteristic-zero estimate. 

### `exists_compressorAdvicePadding`

 A single length exponent works for the slice advice of every eventual
small circuit and every admitted prime of the fixed characteristic. 

### `exists_compressorEvaluatorTape`

 The actual finite-slice advice decoded by the evaluator. The prescribed
padding may be followed by additional public fields. The field presentation
preserves the coordinate used for the final prime-field tally. 
