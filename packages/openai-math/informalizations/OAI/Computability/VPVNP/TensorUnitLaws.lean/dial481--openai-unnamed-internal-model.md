---
{
  "module": "OAI/Computability/VPVNP/TensorUnitLaws.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TensorUnitLaws.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TensorUnitLaws.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Tensor identities under mutual local restriction

Regrouping or permuting tensor factors only relabels their local bases.
The diagonal with empty bases represents zero under local restriction.


### `tensorProduct_unit_mutual`

 The simple tensor is the multiplicative unit up to local restriction. 

### `tensorProduct_assoc_mutual`

 Reassociating three tensor factors preserves the local restriction class. 

### `tensorProduct_comm_mutual`

 Swapping the two factors preserves the local restriction class. 

### `directSum_zero_mutual`

 The empty diagonal is the additive unit up to local restriction. 

### `restricts_zero`

 Every tensor restricts to the empty diagonal. 

### `zero_restricts_iff`

 The empty diagonal restricts exactly to tensors with zero coefficient array. 

### `tensorProduct_zero_mutual`

 The tensor product with the empty diagonal has zero coefficient array. 
