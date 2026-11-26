---
{
  "module": "OAI/Computability/VPVNP/HardnessWitnessCNF.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HardnessWitnessCNF.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HardnessWitnessCNF.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Copying selection flags and testing witness bits

The augmented formula contains the original selection flags, a second copy of
each flag and one bit per witness variable. Each selected event labelled by a
witness variable forces the corresponding witness bit to be true.


### `width`

 The augmented formula has the original `k` flags, their `k` copies, and one Boolean
variable for each witness coordinate. 

### `slots`

 The three disjoint blocks of Boolean slots. 

### `augment`

 Lift all original clauses, constrain the copied flags, and add witness implications. 

### `Compatible`

 Each selected flag with a witness label has a true bit for its label. 

### `satisfies_augment`

 Satisfiability of the augmented formula separates into the original clauses,
equality of every copy with its flag, and the witness implications. 

### `literalCount_augment_le`

 Each original flag contributes at most six literals to the augmented CNF. 
