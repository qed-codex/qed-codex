---
{
  "module": "OAI/Computability/VPVNP/ExpandedMonomialDegree.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ExpandedMonomialDegree.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ExpandedMonomialDegree.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Degrees of paths in an expanded network contraction

The exponent of a complete path is the sum of its local map exponents. At a
placement node the previous factors are visited once in their placement fiber.
This associates each expanded path to a branch of the term history and bounds
its total degree using the map records of that same branch.


### `Term.pushWitness_degree_le`

 Pushing a vertex factor adds the degrees of the kernel and of its children. 

### `DegreeBound`

 Each expanded choice selects a single term chain. Its records suffice to
bound the exponents for any valid input occurrence bound and map degree cap. 

### `DegreeBound.castInput`

 Identify a pass output with the network of the next state, transporting
the history, witnesses, and selected term chains together. 

### `DegreeBound.expandedCount`

 Local RAM paths have exponent zero before any kernels are pushed. 

### `history_degreeBound`

 Lift per-site degree coverage to each complete monomial of a state execution. 
