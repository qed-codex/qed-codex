---
{
  "module": "OAI/Computability/VPVNP/PlacedTensorComposition.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PlacedTensorComposition.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PlacedTensorComposition.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Composing placements of tensor legs

Regrouping factors twice gives the same tensor as placing them along the
composite map. The identity places each original leg back at its own
party, and the inclusion into `Option J` adds a singleton center leg.


### `placeTensor_comp_mutual`

 Two successive placements induce a canonical bijection of the grouped local bases. 

### `placeTensor_id_mutual`

 Placing a tensor at its original parties simply relabels its bases. 

### `placeTensor_some_mutual`

 Placing the old parties by the canonical injection into `Option` is the
trivial extension of the tensor at the added party. 
