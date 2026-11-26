---
{
  "module": "OAI/Computability/VPVNP/PairSimulationShrinkGatherMatrix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationShrinkGatherMatrix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationShrinkGatherMatrix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Running one selected party gather and its matrix in the same machine

The operand gather reads the selected stage and produces its exact scratch
update. The grouped matrix tests those fields, updates the histogram, and
returns to the row increment. A failed test rules out every returning burst.


### `gatheredAction`

 Prepend the selected party's gather trace to a successful matrix action on the
gathered scratch. A rejected matrix entry yields `none`. 

### `gathered_native`

 The actual installed gather, descriptor writer and selected matrix act on
a typed job and private packets with independent lower stack and scratch words. 
