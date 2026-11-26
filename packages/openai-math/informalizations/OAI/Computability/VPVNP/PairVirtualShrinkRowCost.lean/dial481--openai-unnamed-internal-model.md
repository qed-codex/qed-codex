---
{
  "module": "OAI/Computability/VPVNP/PairVirtualShrinkRowCost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVirtualShrinkRowCost.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVirtualShrinkRowCost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Resource bounds for shrinking rows of an actual virtual pair

The input-length threshold comes before the virtual pair, coefficients
and selected execution. Its wire-width envelope covers every input level.
A shrinking row can add at most a quadratic number of copies of any one
coefficient label. The complete histogram credit fits a machine word.


### `RowBudget`

 Size and cost bounds for selected shrink rows of a virtual pair. They control the block
count, wire widths, available word credit, traversal rates and the number of resident field
copies. 

### `eventually_virtualShrinkRowCost`

 The uniform shrinking allowance on the actual cursor input of each virtual pair. 
