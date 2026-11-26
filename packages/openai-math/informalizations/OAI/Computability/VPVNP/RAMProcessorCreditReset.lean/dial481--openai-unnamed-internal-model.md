---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorCreditReset.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorCreditReset.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorCreditReset.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Resetting the private interpreter's call credits

The reset copies the two public unary allowances and snapshots the cumulative
cost. A second scan of the cost word supplies the width for the zero probe
ordinal. Each scan restores its source and clears the previous destination.


### `resetCredits`

 Install the public budgets and record the start of this call. 

### `resetFrame`

 Only the two per-call allowances, start cost and probe ordinal are replaced. 

### `resetCredits_framed`

 Exact running time on a caller's frame. Empty, partially used, and
full destination stacks are all permitted. 

### `resetCredits_run`

 Starting a call reloads the full fuel and call budgets, records the old
cumulative cost, and initializes the ordinal to the width-correct zero. 
