---
{
  "module": "OAI/Computability/VPVNP/SpectralStrictComparison.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralStrictComparison.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralStrictComparison.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniform comparison of powers from spectral separation

A strict inequality at every point of the compact spectrum gives an integer
margin. Detecting this stronger inequality in the rational order cone, clearing
denominators, and removing additive slack gives a restriction with a single
number of copies for all powers.


### `strict_spectral_comparison`

 Lemma 2.1 in the ordered-semiring setting of Appendix A.1. A monotone
natural-valued rank is a witness that the negative unit is outside the
localized order cone. Strict comparison at every spectral point gives the
same finite copy bound for all powers. 
