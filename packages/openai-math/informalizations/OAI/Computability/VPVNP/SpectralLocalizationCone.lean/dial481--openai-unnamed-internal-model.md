---
{
  "module": "OAI/Computability/VPVNP/SpectralLocalizationCone.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralLocalizationCone.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralLocalizationCone.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The rational cone used for strict spectral comparison

Appendix A.1 writes a positive element as a sum of differences over nonzero
tensor denominators. Addition can be done over a common tensor denominator,
so a single ordered difference suffices. The witnesses are kept in the
original semiring so they can later be used to recover a restriction.


### `OrderBounds`

 The order properties of restriction that enter the localization argument. 

### `FractionPositive`

 An ordered difference with a common nonzero denominator. 

### `fractionPositive_add`

 Addition collects the two denominators and retains the numerator comparison. 

### `fractionPositive_mul`

 Multiplication by a tensor fraction preserves the cone. 

### `orderCone`

 The order cone in the rational algebra. Positive rational multiples use
the positive denominator of the scalar and its nonnegative integer numerator. 
