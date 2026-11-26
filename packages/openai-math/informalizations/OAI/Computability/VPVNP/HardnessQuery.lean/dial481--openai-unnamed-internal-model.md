---
{
  "module": "OAI/Computability/VPVNP/HardnessQuery.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HardnessQuery.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HardnessQuery.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Weighted Boolean predicates as projections of the universal family

A finite query program reads the bits of a proposed assignment. Each selected
bit contributes its assigned weight, which may be a scalar or a formal variable.
Pinning the literal program prefix and projecting the payload gives the sum of
those products over the accepted assignments, in every characteristic.


### `weightedPredicate`

 The formal generating polynomial of a Boolean predicate with variable or scalar weights. 

### `weightedQuery_projection`

 For a single weighted query program the source length is bounded explicitly
in its state count, query budget, and payload length. 

### `weightedQuery_PProjects`

 A polynomial-size family of query predicates gives one p-projection, including
all the finite initial lengths. Weights may be chosen independently at each length. 
