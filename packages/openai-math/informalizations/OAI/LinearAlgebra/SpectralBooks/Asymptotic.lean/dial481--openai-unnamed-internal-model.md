---
{
  "module": "OAI/LinearAlgebra/SpectralBooks/Asymptotic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/Asymptotic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/Asymptotic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # From finite height bounds to arithmetic exponents

Evaluate the finite bound at base sizes `2 ^ k`. Rounding each dimension
up only increases its logarithmic load. The logarithm of a constant in
a polynomial cost bound contributes a fixed additive term, which disappears
when the inequality holds at every dyadic scale.


### `scaledLoads`

 Logarithmic site loads at the three rounded wire dimensions of base size `N`. 

### `dyadic_load_le`

 The dyadic loads dominate the real weights multiplied by the scale exponent. 

### `le_of_dyadic_log_bound`

 A uniform polynomial bound at dyadic scales forces the growth exponent
to dominate the slope, independently of the multiplicative constant. 

### `heightTest_of_polynomial_bound`

 A polynomial upper bound on the finite height-test parameter implies
the corresponding test on exponent loads, with all positive slack removed. 

### `heightTest_sInf`

 Height tests pass to the infimum of any nonempty set of admissible exponents. 
