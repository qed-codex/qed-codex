---
{
  "module": "OAI/Computability/VPVNP/EventualBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EventualBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EventualBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Transfer of eventual circuit-size bounds under polynomial projections

Section 15.1 of *VP and VNP differ over every field* uses two properties of a
complete family: its order-`j` polynomial projects from its order-`j+1`
polynomial for `j ≥ 2`, and the hard family projects from orders at most
`A * n ^ b`. Both projections preserve upper bounds on the number of binary
gates. The result below transfers the eventual lower bounds to every order.


### `EventuallySuperpolynomial`

 The all-sufficiently-large-length lower bound for each positive exponent. 

### `eventualBound_of_polynomialProjection`

 Section 15.1. For every order `m` above a fixed threshold, the floor root
of `m / A` supplies a length `n` whose projected order is at most `m` and whose
lower bound already exceeds `m ^ C`. The projection indices may have gaps. 

### `EventuallySuperpolynomial.not_polynomially_bounded`

 An eventual lower bound for each exponent excludes every polynomial size
bound, including bounds with a multiplicative constant and a length cutoff. 
