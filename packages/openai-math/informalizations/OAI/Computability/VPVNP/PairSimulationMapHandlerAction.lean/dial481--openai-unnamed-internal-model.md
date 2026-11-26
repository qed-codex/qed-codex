---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapHandlerAction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapHandlerAction.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapHandlerAction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Deterministic actions of selected grid and party handlers

An action depends on the recorded motif entry, the six descriptor operands,
external memory and the incoming upper scratch. It is defined at exactly the
successful entries. The chronological trace includes the external reads of the
argument writer and all ticks of the initialized and lowered map.


### `successEvents`

 The typed field bits fix all map branch lengths, while the six operands
and external memory fix the precise read addresses and returned words. 

### `successEvents_readsFrom`

 All external reads in the full visit belong to the descriptor expressions. 

### `action`

 The selected occurrence either rejects or returns its native trace and
complete outgoing scratch to the enclosing map loop. 

### `action_some_iff`

 A successful action returns precisely the chronological trace and the
prescribed update of the incoming upper scratch. 
