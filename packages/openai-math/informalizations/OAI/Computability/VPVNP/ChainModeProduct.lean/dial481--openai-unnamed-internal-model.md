---
{
  "module": "OAI/Computability/VPVNP/ChainModeProduct.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ChainModeProduct.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ChainModeProduct.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The two live modes in the physical chain contraction

A unit-mode group accepts only zero strings on its incident cuts. An
evaluation-mode group reads a true mode bit on each incident interior cut.
Neighboring groups therefore cannot contribute in different modes to a
nonzero product. The unit-mode product counts the unique all-zero assignment.


### `unitGroupCount`

 The unit group accepts exactly once when both incident cut fields are zero. 

### `evalCutMode`

 The first bit on an interior cut selects evaluation mode. Endpoints carry no bits. 

### `activeCuts`

 Every interior cut has its evaluation-mode bit, the bit at distributed position zero, set
to true. 

### `group_mode_product`

 At fixed cuts every mixed-mode term vanishes, including terms switching
modes across the midpoint. 

### `eval_product_zero_of_inactive`

 A zero evaluation-mode bit on any interior cut kills the whole evaluation product. 

### `sum_groupCount_eq_one_add_eval`

 Summing the physical products counts one unit execution and the full
contraction of evaluation-mode groups. 

### `sum_groupCount_eq_one_add_active`

 The evaluation sum in the live-mode identity can be restricted to cut
assignments with true mode bits on every interior cut. 
