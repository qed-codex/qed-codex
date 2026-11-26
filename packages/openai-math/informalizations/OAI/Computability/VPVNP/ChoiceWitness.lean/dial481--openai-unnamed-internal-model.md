---
{
  "module": "OAI/Computability/VPVNP/ChoiceWitness.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ChoiceWitness.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ChoiceWitness.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Canonical accepting-path witnesses

For the counting polynomial in §1.1 of *VP and VNP differ over every field*, we use
one Boolean choice for every machine step. This is the combinatorial counting identity
that lets the VNP summand verify one candidate path deterministically.


### `acceptsChoices`

 One choice bit per step. A single transition consumes zero, and an early halt
accepts only the all-zero unused suffix. The two instructions in a branch have
separate bits even when they induce the same successor configuration. 

### `reject`

 Enter rejection without further tape operations. 

### `choiceStep`

 Consume a single witness bit. Invalid choices enter the rejecting state, which is
absorbing. An accepting halt survives precisely the zero padding of a canonical witness. 

### `acceptsChoices_succ`

 Consuming the leading bit agrees with one deterministic machine transition. 

### `acceptsChoices_eq_foldl`

 The final state of the fixed-length simulation determines the verifier's answer. 

### `paths_eq_sum_choices`

 Counting accepting strings of fixed length recovers the number of accepting paths
of the encoded machine within the step bound, with each halted path counted once. 

### `paths_eq_card_choices`

 The cardinality form of the fixed-length witness identity. 

### `verifiesInput`

 A candidate for the coefficient indexed by `x` consists of one bit per clock tick. 

### `acceptingCount_eq_card_witnesses`

 The number of canonical witnesses is the coefficient `U_n(x)` from equation (1.1). 

### `acceptingCount_eq_sum_witnesses`

 The Boolean witness sum gives the same coefficient in every target semiring. 
