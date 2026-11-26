---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorAdviceFrameStore.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorAdviceFrameStore.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorAdviceFrameStore.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Writing an advice frame with reserved holes

Register 22 points at the first frame word and register 1 holds the stride.
A present slot writes its source register, while a hole leaves memory intact.
Both advance the cursor by the same stride.


### `storeFlow`

 A static schedule of register stores and holes. 

### `storeRegs`

 Advance the frame-writing cursor once per slot, including reserved holes, to obtain the
registers after publication. 

### `frameMemory`

 The memory after writing each present register word into its frame slot and advancing over
reserved holes. 

### `storeEvents`

 The chronological frame writes and cursor-advance ticks for the given slot assignment. 

### `store_exec`

 Exact registers, external memory and events after the fixed instruction schedule. 

### `naturalMemory`

 The natural-address version of the same sequence, using the fixed entry
bank for all source registers. 

### `frameMemory_outside`

 Words outside the frame survive every write. 

### `frameMemory_at`

 A written slot reads back its entry register, while a hole reads back the entry memory. 
