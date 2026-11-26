---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorChoices.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorChoices.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorChoices.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Generating the bounded private-choice stream

One accepting computation of the site validator consumes exactly one finite
list of guessed bits. This table generates each list up to the public bound
once. The budget is a unary stack. After the stop choice the routine drains
the remaining budget deterministically, with the same instruction count on
every path. The continuation receives the complete guessed list.


### `State`

 Finite controls for choosing a bounded private stream and draining the remaining budget. 

### `routine`

 Generate each allowed bit list once and pass it to the continuation. 

### `words`

 Lists are grouped by the last chosen bit, which is at the bottom of the
generated stack. 

### `count`

 Exact CPS count, with the budget and output ports explicit in the caller. 

### `allStops_iff`

 Every generator branch spends exactly the same prefix cost. The remaining
budget suffices exactly when the continuation stops on each permitted list. 
