---
{
  "module": "OAI/Computability/VPVNP/TensorDistributivity.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TensorDistributivity.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TensorDistributivity.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Direct sums and products up to local restriction

Relabeling local bases lets us permute and regroup direct summands, and distribute
a tensor product over a direct sum. Pure coordinate blocks carry the entries of
their summands and mixed blocks vanish.


### `sum_assignment_cases`

 An assignment to disjoint local bases lies in one block at every party, or uses both. 

### `directSum_assoc_mutual`

 Regrouping the three coordinate blocks at every party preserves the tensor. 

### `directSum_comm_mutual`

 Swapping the left and right local blocks interchanges the summands. 

### `tensorProduct_directSum_mutual`

 Local distribution of product coordinates over a disjoint union gives
mutual restrictions for the distributive law. 
