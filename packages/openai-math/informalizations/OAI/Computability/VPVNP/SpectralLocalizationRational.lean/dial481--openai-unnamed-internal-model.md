---
{
  "module": "OAI/Computability/VPVNP/SpectralLocalizationRational.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralLocalizationRational.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralLocalizationRational.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Rational scalars in the localization of a spectral semiring

In characteristic zero the images of the positive natural numbers become
units when we invert the nonzero elements of the semiring. This supplies the
rational scalar action used in the algebraic separation argument. Clearing
denominators then writes each nonnegative rational as a ratio of naturals.


### `ratAlgebraOfUnits`

 A commutative ring in which positive natural numbers are units is a
rational algebra by the universal property of the localization of `ℤ`. 

### `den_mul_algebraMap_eq_num_toNat`

 Clearing the positive denominator of a nonnegative rational in any
rational algebra gives its natural numerator. 
