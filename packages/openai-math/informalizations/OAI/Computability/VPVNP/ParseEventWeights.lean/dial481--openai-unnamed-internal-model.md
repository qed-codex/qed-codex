---
{
  "module": "OAI/Computability/VPVNP/ParseEventWeights.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseEventWeights.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseEventWeights.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Weights of the interval events in an ordered parse

Each production occurrence contributes its grammar scalar. Each leaf also contributes
its input value. The interval coordinate distinguishes repeated occurrences of the same
production. Consequently a product over the finite event table counts these repetitions
with the same multiplicity as the recursive parse weight.


### `eventScalar`

 Scalar of a terminal or binary production. A binary coordinate outside the
layer or split bounds of the grammar receives zero. 

### `ParseEvent.leafVariable`

 Optional variable supplied by a leaf production. 

### `ParseEvent.leafValue`

 A terminal contributes its input value, and a binary production contributes one. 

### `prod_eventScalar`

 Multiplying the selected production scalars recovers the recursively defined
parse weight, independently of the left endpoint of the root interval. 

### `prod_leafValue`

 The product of the leaf inputs over the event table is the product of the
parse's left-to-right list of leaves. 

### `prod_eventWeights`

 Local scalar and leaf factors can be multiplied at each selected event. 

### `eval₂_eq_sum_eventWeights`

 Evaluating the grammar is a sum of products over canonical finite event tables. 

### `eval_eq_sum_eventWeights`

 The formal state polynomial is the weighted sum of its finite event tables. 

### `witnessValue_eval_eq_sum_eventWeights`

 In the Boolean witness sum, an output variable remains formal and a witness
variable contributes its chosen bit as a field constant at each leaf. 
