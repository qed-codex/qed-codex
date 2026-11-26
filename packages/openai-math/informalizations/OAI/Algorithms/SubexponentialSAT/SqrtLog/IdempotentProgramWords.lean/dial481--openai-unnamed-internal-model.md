---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentProgramWords.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentProgramWords.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentProgramWords.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Instantiation on fixed-width Boolean words modulo 3^t.  The scalar
callbacks have existing primitive bit-program refinements.  The remaining
native obligation is the runtime-sized array traversal and Newton controller,
not an unprovided algebraic oracle. 

### `wordCoefficientRun`

 Both the half coefficient and every output coefficient are computed from
word callbacks. No semantic-to-word conversion is used. 

### `preparedWordCoefficientRun`

 The ternary modulus is prepared from the fixed literal `[true,true]`. 

### `preparedWordCoefficientRun_indicator`

 Full construction from t: the modulus, small constants, inverse of two,
multiplication table, and Newton lift are all generated explicitly. 

### `preparedWordOutput_length`

 Flat output has exactly three degree-below-three coefficients per digit,
with each scalar occupying 2t bits. 

### `tableWords`

 Table serialization is k-major, then i, with j fastest, matching the
native expansion/contraction service. 
