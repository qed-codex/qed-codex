---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorRAMDispatch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorRAMDispatch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorRAMDispatch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The evaluator's fixed row dispatch in a live group

The evaluator program is fixed, so its finite row table is part of the
control graph. Register 4 contains the zero-based row number. Each skipped
row costs a test and a decrement. Only two-slot rows execute a choice, with
false selecting the first slot and true selecting the second. A zero-slot
row or an out-of-range row jumps to the rejecting exit.

Registers 5–9 receive the five fields of the chosen instruction. The target
state is assembled from zero and unit increments. Each tape symbol and move
is a single two-bit literal. Consequently the instruction text is fixed
independently of the word width and live window size.


### `literal`

 The four bounded tape fields fit directly in the RAM's literal format. 

### `targetFlow`

 Load a fixed natural number into register 5 using only zero and unit increments. 

### `dispatch`

 The native structured flow compiled from a fixed coefficient machine. 

### `instructionRegs`

 Registers after writing the instruction's five fields. 

### `dispatchBits`

 Nondeterministic input consumed by a successful dispatch. 

### `dispatchBits_injective`

 The consumed RAM bit list uniquely identifies every occupied slot in a given row.
In particular the two copies of a repeated instruction have different encodings. 

### `ticks`

 A trace of the specified number of local instruction steps in the fixed evaluator row
dispatch. 

### `dispatchEvents`

 The exact native trace, including each countdown operation and target increment. 

### `Straight`

 Determinism of the straight-line portion that writes one selected record. 

### `dispatch_exec_iff`

 Successful dispatches are precisely the occupied slots of the indexed
row. This also describes the whole event log and register frame. 

### `dispatch_exec`

 Construct the native execution for a selected table slot. 

### `dispatchEvents_bound`

 The instruction budget is uniform in the word width, input and live window size. 

### `dispatch_rejects`

 A stop row has no successful native execution for any amount of fuel
or any branch stream. This includes out-of-range row indices. 

### `target_exec_iff`

 The fixed natural loader has no other successful execution. 
