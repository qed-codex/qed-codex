---
{
  "module": "OAI/Computability/VPVNP/TensorPowerCNF.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TensorPowerCNF.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TensorPowerCNF.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Weighted literal encoding of a tensor power

The input gives one sequence of binary digits per party. Word flags select
one variable at each party and digit-tuple flags select one coefficient per
copy of the tensor. The CNF has exactly one satisfying extension of each input.


### `Digit`

 A block of `b` bits selecting a local basis index in one tensor factor. 

### `Word`

 The `h` successive local index blocks selected by one party in the tensor power. 

### `form`

 The multilinear form of the tensor power, grouping copies at each party. 

### `width`

 Number of bits including the two families of flags. 

### `formula`

 All word and tuple match tests. 

### `weights`

 Each bit weight is either a scalar or one variable. 

### `weightedCNF_formula`

 The weighted satisfying-assignment polynomial is exactly the tensor power form. 
