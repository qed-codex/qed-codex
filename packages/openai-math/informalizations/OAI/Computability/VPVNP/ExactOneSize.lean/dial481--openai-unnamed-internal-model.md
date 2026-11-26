---
{
  "module": "OAI/Computability/VPVNP/ExactOneSize.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ExactOneSize.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ExactOneSize.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Size of the exact-one verifier

A clause with `m` occurrences has `m` selector bits and `m²` filler bits.
The selector clause has `m` literals, and each of its `m²` pair clauses has at
most three literals. Summing over the original clauses gives quadratic bounds
in the total number of literal occurrences, even in the presence of empty clauses.


### `sum_lengths`

 Sum of the clause lengths in their indexed presentation. 

### `width_le`

 The selectors and fillers use at most `L + L²` new variables. 

### `length_augment_le`

 One selector clause is retained per original clause, including empty ones. 

### `literalCount_augment_le`

 A bound depending only on literal occurrences, even with arbitrarily many empty clauses. 

### `polynomial_bounds`

 Polynomially bounded families of CNF verifiers retain polynomial width and literal count. 
