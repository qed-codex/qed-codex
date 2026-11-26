---
{
  "module": "OAI/Computability/VPVNP/TensorPowerIncidence.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TensorPowerIncidence.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TensorPowerIncidence.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # An exact-one incidence matrix for tensor powers

One block of columns selects a word at each party. Another block selects a
tuple of digits at each position. Each consistency row counts a true bit on the
word side and a false bit on the tuple side, so exact-one means the bits agree.


### `Col`

 Columns carrying the word and tuple selection flags. 

### `Row`

 A row for each one-hot field and each bit agreement. 

### `incidence`

 The entries for word and tuple columns use opposite polarities on a bit row. 

### `columnWeight`

 A selected word contributes a variable, and a selected tuple contributes a tensor entry. 

### `weightedIncidence_eq_form`

 Summing the weights of all exact-one solutions gives the regrouped tensor power form. 
