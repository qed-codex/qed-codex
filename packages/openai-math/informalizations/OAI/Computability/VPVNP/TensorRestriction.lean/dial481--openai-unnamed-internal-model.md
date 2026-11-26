---
{
  "module": "OAI/Computability/VPVNP/TensorRestriction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TensorRestriction.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TensorRestriction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Tensor classes modulo mutual restriction

Each class retains its concrete restriction comparisons. The smaller class
is the demand and the larger class is the supply. Direct sums and products
descend to the quotient because independent local maps act on both factors.


### `restrictionSetoid`

 Identifying exactly those tensors that restrict to each other. 

### `RestrictionClass`

 The restriction classes used to form the semiring of Section 2. 

### `ofTensor`

 Map a concrete tensor to its equivalence class under mutual restriction by local linear
maps. 
