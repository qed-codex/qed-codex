---
{
  "module": "OAI/Computability/VPVNP/EvaluatorAdviceBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorAdviceBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorAdviceBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Size of the advice and indices of the finite slice evaluator

The parameters are those of the actual coordinate slice in `LabelEvaluator`.
Its ground field has order greater than twice the Macaulay column bound, and
the geometric point count is bounded by the `t`th power of twice that bound.
Both logarithms are polynomial in the input length.

The advice stores the prime in an agreed width, one field element's worth
of coefficients for the defining polynomial, one selection bit per
coordinate, and one field element per coordinate. All these bounds hold
uniformly over the selected prime once its width is fixed.


### `listingBound_clog`

 Uniform width of indices in the monomial list scanned by the evaluator. 

### `elementWidth`

 This is the extension degree and width used by every coefficient block. 

### `primeHeaderWidth_polynomiallyBounded`

 In characteristic zero the prime-width exponent from the integer minor
is polynomially bounded even when the coefficient bit lengths are themselves
singly exponential. An extra bit represents the prime in the equality case. 

### `adviceLengthBound`

 Numerical upper bound independent of the prime, for the four fields
(prime header, monic polynomial, pin mask, and pin values). 

### `exists_advice_padding`

 A single padding exponent works for all admissible primes at every
sufficiently large length. In particular it is independent of the evaluator
exponents, pin choices, and later processor prefix. 

### `exists_padded_model_advice`

 Padding the actual chosen advice preserves its decoded prime, pin data,
and field presentation. The length is fixed before selecting a prime or model. 
