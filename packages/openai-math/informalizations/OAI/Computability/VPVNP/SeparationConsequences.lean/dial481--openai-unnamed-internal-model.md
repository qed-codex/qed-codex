---
{
  "module": "OAI/Computability/VPVNP/SeparationConsequences.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SeparationConsequences.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SeparationConsequences.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Quantifiers and consequences of the circuit lower bound

Theorem 1.1 uses one threshold for all fields of a fixed characteristic. In
§15.1 the projection and padding argument takes place over an algebraically
closed representative of the characteristic, so the threshold for each matrix
family can also be chosen before the field.


### `UniformPBound`

 The circuit bound in Theorem 1.1 for the paper's explicit integer family. 

### `uniform_P_bound_of_countable_contradiction`

 It suffices to rule out arbitrarily large exceptional lengths in one
countable algebraic closure per characteristic. 

### `uniform_P_bound_of_diagonal_contradiction`

 Form of the reduction for a diagonal contradiction that works in every
countable algebraically closed field. 

### `eventual_P_bound_of_uniform_P`

 Specialize the common threshold to the characteristic of a single field. 

### `vp_ne_vnp_of_uniform_P`

 The explicit complete family witnesses the distinction between the two
class predicates, already on families in the prescribed paired variables. 

### `corollary12_of_uniform_P`

 Corollary 1.2. The common threshold covers both matrix families in
characteristic different from two and covers directed Hamiltonian cycles in
characteristic two. The exponent zero is allowed as well. 
