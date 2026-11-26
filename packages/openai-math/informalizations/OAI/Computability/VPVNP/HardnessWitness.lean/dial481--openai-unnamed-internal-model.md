---
{
  "module": "OAI/Computability/VPVNP/HardnessWitness.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HardnessWitness.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HardnessWitness.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Eliminating Boolean witness substitutions in a weighted CNF

A selected flag can carry both a scalar and a variable. Its duplicate in the
augmented formula accounts for the variable while the original carries the scalar.
For a witness variable the added implication excludes precisely the assignments
where that variable specializes to zero.


### `augmentedWeight`

 Projection weights on the three blocks of bits. An original flag carries
its scalar, its duplicate carries its formal variable, and the witness is unweighted. 

### `assignments`

 Reindex a payload assignment by its witness, flags, and copies of the flags. 

### `sum_witnessValue_weightedCNF`

 After summing the Boolean witnesses, a product with one scalar and one
optional variable per selected flag has a CNF presentation with projection weights. 
