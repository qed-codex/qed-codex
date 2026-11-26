---
{
  "module": "OAI/Computability/VPVNP/LiveFirstTailBudget.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveFirstTailBudget.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveFirstTailBudget.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The transcript budget of the initialized first tail group

The first nonempty evaluator group executes the header, both routers, the
initial state writer, the packing and input stages, and one terminal
transition. The outgoing gather allowance also pays for the last sentinel
when this is the only tail group. The common outside-work bound therefore
provides the budget for every accepting continuation from the midpoint.


### `cost`

 The specific amount charged by the post-initialization count theorem,
including the header and mode router. 

### `cost_le_actualBound`

 The physical route budget is covered by the common outside-work bound
with the ordinary outgoing-gather allowance. 

### `eventually_countCaps`

 The site exponent is chosen before the length threshold. For every
bounded advice prefix, the ordinary per-call cap and the full initialized
group budget then hold simultaneously. 
