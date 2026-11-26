---
{
  "module": "OAI/Computability/VPVNP/StarEmbedding.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StarEmbedding.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StarEmbedding.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Embedded old tensor classes

Adjoining the trivial center leg preserves parallel products and reflects
local restrictions. The old factors in a monomial of Theorem 2.4 can thus
be multiplied in the old party set, then embedded as one tensor class.


### `embedOldClass`

 Embedding an old tensor induces a multiplicative map on restriction
classes which also preserves zero. 

### `embedOldClass_le_iff`

 Embedding a trivial center leg preserves and reflects restriction. To
reflect a restriction, contract the demand with the unit covector and pull
it back to the singleton center basis of the supply. 

### `embedOldClass_injective`

 Adjoining a trivial leg is faithful on tensor restriction classes. 

### `ofTensor_tensorPowerFin`

 The concrete product indexed by `Fin n` represents the `n`-th power
in the semiring of restriction classes. 
