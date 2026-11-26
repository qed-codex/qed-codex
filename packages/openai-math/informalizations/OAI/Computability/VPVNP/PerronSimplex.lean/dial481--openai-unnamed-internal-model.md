---
{
  "module": "OAI/Computability/VPVNP/PerronSimplex.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PerronSimplex.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PerronSimplex.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Counting monomials of bounded total degree for Perron's theorem

Bound the exponent of the first input variable by `B` and the sum of the
remaining `m` exponents by `B`. Substituting polynomials of degree at most
`D` gives output monomials of total degree at most `2 * B * D`.
Dividing each output exponent by `2 * (D + 1)` places the quotients in the
simplex of degree `B`. The remainders account for at most `B` possibilities
when `B = (2 * (D + 1)) ^ m`.


### `Simplex`

 Exponents of the monomials of total degree at most `d` in `m` variables. 

### `perronRadius`

 Degree bound on each of the two input blocks. 

### `perronSimplexBound`

 Total degree bound on the resulting polynomial relation. 

### `divideSimplex`

 Divide each exponent by `q`, keeping both quotient and remainder. 

### `perron_simplex_card_lt`

 There are strictly more input monomials in the two blocks than there are
output monomials of the possible substituted degrees. 
