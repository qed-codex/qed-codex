---
{
  "module": "OAI/Computability/VPVNP/SpectralLocalization.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralLocalization.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralLocalization.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Clearing spectral comparison in the tensor semiring

The denominators in Appendix A.1 are images of nonzero tensors, even if their
images in the group completion are zero divisors. Equality after localization
first supplies a multiplicative factor and then a common additive term. Both
are elements of the original semiring.


### `denominators`

 The multiplicative system in the ring of formal differences. For a tensor
semiring without zero divisors it is exactly the image of the nonzero tensors. 

### `A`

 Ring of formal differences localized at the images of the non-zero-divisors of the
semiring. 

### `toA`

 The canonical map to the ring in which every nonzero tensor is invertible. 

### `fractionInverse`

 The inverse of the image of a nonzero tensor, chosen as the fraction with
numerator one. 

### `exists_fraction`

 A localized element has one denominator and a difference of two original
semiring elements as numerator. 

### `toA_eq_iff`

 Clearing an equality of images in the localized completion produces both
a common nonzero factor and a common summand in the original semiring. 

### `clear_comparison`

 Membership of a difference in the order cone clears to a single
restriction with a multiplicative catalyst and a common additive term. 

### `neg_one_notMem_orderCone`

 A monotone flattening rank excludes minus the unit from the order cone. 

### `orderCone_mul_of_fraction`

 All tensor fractions, including the two multipliers in the extreme-state
argument, preserve the order cone. 
