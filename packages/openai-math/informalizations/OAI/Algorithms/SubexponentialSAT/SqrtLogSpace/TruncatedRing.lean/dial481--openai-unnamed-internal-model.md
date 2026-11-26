---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/TruncatedRing.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/TruncatedRing.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/TruncatedRing.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Dense lifting and Taylor coefficients

`Truncated R n` stores exactly `n` coefficients. Its multiplication is the
existing total-order convolution, and its ring laws follow from the surjective
coefficient projection from `R[X]`. Nesting the construction stores the shared
lifting marker outside the Taylor variable. The final marker readout is additive.


### `Truncated`

 A dense canonical representative modulo the indicated power of the variable. 

### `coeff_mul`

 Explicit bounded convolution, with out-of-range reads equal to zero. 

### `ofPolynomial`

 The coefficient projection. This is a semantic map, not the native evaluator. 

### `polynomial`

 The canonical polynomial represented by the stored array. 

### `coeffHom`

 Each stored coordinate is additive, but generally not multiplicative. 

### `ofPolynomialHom`

 The quotient-ring projection is multiplicative; the marker readout is not. 

### `readout`

 Add the coefficients of the chosen representative, after multiplication. 

### `Dense`

 `t * J` scalar slots: shared lifting marker outside, Taylor variable inside. 

### `ofPolynomial`

 First project Taylor coefficients, then truncate the shared marker. 

### `readout`

 Final additive shared-marker readout; a Taylor array remains. 
