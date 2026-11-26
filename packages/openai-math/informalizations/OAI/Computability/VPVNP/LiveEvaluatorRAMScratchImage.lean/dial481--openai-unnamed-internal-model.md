---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorRAMScratchImage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorRAMScratchImage.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorRAMScratchImage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Memory images after publishing an evaluator instruction

The native preparation writes the five instruction registers in scratch. A
disjoint configuration still decodes to the same bounded evaluator state.


### `actionAt_scratch`

 The five register values published by preparation constitute the memory
image read by all subsequent scheduled cells. 

### `actionAt_carryRegs`

 Carrying an accepting evaluator publishes state one and four zero tape fields. 

### `actionAt_selectedRegs`

 A selected table slot publishes all five fields of that instruction. 

### `ConfigAt.after_scratch`

 Configuration and scratch can be allocated in either order. The fit
bounds ensure that neither block wraps in machine-word arithmetic. 
