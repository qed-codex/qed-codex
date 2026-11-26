---
{
  "module": "OAI/Computability/VPVNP/SpectralMatching.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralMatching.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralMatching.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Matching the prescribed generator values in an exact extension

Section 2.3 uses a compactness argument to test a finite list of generators.
If every spectral point misses a target, one polynomial supply dominates the
balanced monomial at every spectral point. Its contraction bound contradicts
the exponential growth of contractions of that monomial.


### `contraction_budget_of_power_comparison`

 A comparison between all powers bounds their contracted growth. The supply
is evaluated as a polynomial in the chosen generators, so its monomial bounds
apply even to covectors acting jointly on all factors. 

### `exists_matching_spectral_point`

 Finite-generator matching in the proof of Theorem 2.4. A contraction
functional bounds all monomials by their target products. If the bound is
asymptotically attained on each balanced reference monomial, some spectral
point realizes every generator target simultaneously. 
