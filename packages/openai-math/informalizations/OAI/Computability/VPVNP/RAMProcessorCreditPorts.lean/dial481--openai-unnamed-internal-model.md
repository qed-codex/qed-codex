---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorCreditPorts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorCreditPorts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorCreditPorts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Ports for the private interpreter's call credits and probe timestamps

The public unary tallies are copied anew for each call. The global cap and
remaining allowance stay binary. The saved start cost and the ordinal are
the two per-call words needed for a chronological probe record.


### `Port`

 Stack names for public and remaining credits, the binary global cap, probe timestamps and
scratch space for copying and arithmetic. 

### `budget_injective`

 The six-port charge routine is installed at the budget ports. 

### `bank`

 Encode the current credit state in its stacks, with unary public allowances, binary cap and
the saved start and ordinal bit strings. 

### `install_budget_bank`

 The charge routine affects only the six installed counters and scratch.
The public tallies, saved start and ordinal are kept in the caller's frame. 
