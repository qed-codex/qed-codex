---
{
  "module": "OAI/Computability/VPVNP/RankQueryConcreteResources.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryConcreteResources.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryConcreteResources.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniform bounds on the concrete determinant and rank programs

The parameters below vary with the paper's input length. A matrix dimension
and an entry-query clock can be singly exponential in this length. Widths,
field-extension degree, and entry-query peak space are polynomial. The
proofs apply to the clock and storage formulas of the actual finite routines.


### `PB`

 Polynomial boundedness of a resource quantity as a function of the input length. 

### `LB`

 Polynomial boundedness of the ceiling binary logarithm of a resource quantity as a function
of the input length. 

### `log_const`

 A constant resource quantity has a polynomially bounded ceiling binary logarithm. 

### `plain_feasible`

 The full ordinary determinant clock and peak, uniformly for an
arbitrary family of singly exponential square minors. 

### `rank_feasible`

 The concrete rectangular rank scanner, including root initialization,
scalar zero tests, and every cursor update. The shared bit bound `d` may
vary polynomially with the external length. 

### `eventual_power`

 An eventual power of the input length bounds both the bit exponent of
the clock and the number of bits on any stack. 
