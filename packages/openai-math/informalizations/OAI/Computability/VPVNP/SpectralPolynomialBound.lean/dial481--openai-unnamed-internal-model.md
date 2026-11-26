---
{
  "module": "OAI/Computability/VPVNP/SpectralPolynomialBound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralPolynomialBound.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralPolynomialBound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Contraction bounds for polynomials in tensor generators

In Theorem 2.4 of *VP and VNP differ over every field*, a contraction of
each monomial in the generators satisfies its own target bound. Expanding
the direct sums and tensor powers on the right of the comparison gives a
polynomial with natural coefficients. Subadditivity and the bound for
copies extend the monomial estimates to this whole polynomial.


### `polynomial_target_bound`

 A subadditive function with a bound on copies respects the target
bound for every natural-coefficient polynomial in the generators, provided
it respects the bound on each coefficient-one monomial. 
