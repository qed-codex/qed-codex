---
{
  "module": "OAI/Computability/VPVNP/PolynomialPowerGap.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PolynomialPowerGap.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PolynomialPowerGap.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Polynomial losses in a finite sum of tensor powers

The cut bounds in §4.2 of *VP and VNP differ over every field* have bases strictly
smaller than the target spectral value. A polynomially growing multiplicity of
terms across each cut preserves the eventual strict inequality.


### `eventually_polynomial_weighted_pow_lt_target`

 A fixed polynomial factor times a finite sum of powers with smaller bases is
eventually strictly smaller than the target power. 
