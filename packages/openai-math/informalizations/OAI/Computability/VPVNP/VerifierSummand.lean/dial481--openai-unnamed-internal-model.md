---
{
  "module": "OAI/Computability/VPVNP/VerifierSummand.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierSummand.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierSummand.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The Boolean witness sum for the paired counting polynomial

The summand of §1.1 of *VP and VNP differ over every field* has visible variables
`(j,b)` and three sets of Boolean summation variables. They encode the input word,
the path choices, and the gate values of the deterministic verifier. Specialization
of the Boolean variables leaves a formal polynomial in the visible variables.


### `Inputs`

 The verifier reads the word and the path choices. 

### `Witness`

 The summation also ranges over the claimed transcript of the verifier. 

### `Variables`

 Polynomial variables in the verifier summand, consisting of the paired input variables and
the Boolean witness coordinates. 

### `selector`

 Multilinear selector for one pair of indeterminates. 

### `specialize`

 Evaluate only the witness variables on the Boolean cube. 

### `summand`

 The verifier weight times the selectors, before any witness is fixed. 

### `specialize_summand`

 On fixing the witness, each selector becomes the single variable named by the input bit. 

### `sum_summand`

 Eliminate the auxiliary transcript bits to obtain the coefficient-counting polynomial. 

### `sum_summand_eq_map_P`

 The §1.1 summand computes the actual integer family after base change whenever its
Boolean circuit implements the canonical path verifier. This separates the exact counting
identity from the problem of constructing a polynomial-size circuit for that verifier. 
