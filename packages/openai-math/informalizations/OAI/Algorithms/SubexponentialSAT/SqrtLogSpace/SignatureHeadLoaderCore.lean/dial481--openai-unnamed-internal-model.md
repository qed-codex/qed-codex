---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SignatureHeadLoaderCore.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SignatureHeadLoaderCore.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SignatureHeadLoaderCore.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The fixed head-loader table uses the actual integer entry program. Its
physical matrix view follows LeafHeadSetupProgramHead/MatrixRun exactly, while
its controller emits one matrix and never constructs assignment tables. 

### `masters`

 Exactly the physical source words read by head selection and native
integer entries. Unrelated arithmetic scratch is deliberately excluded. 

### `rawOutputs`

 Raw matrix output; the old bucket output21 is never selected. 

### `localCommand`

 The low bank computes a single actual head; output668 is the full shifted
matrix. Raw669 is cleared before returning to the signature iterator. 

### `stage_trace_bound`

 A local polynomial run gives a polynomial bound for every paid stage,
including input copies, dirty work-bank clearing, and output copies. 

### `raw_eval`

 Paid raw-matrix staging, with its exact physical output and caller frame.
The native specialization below discharges the entry contract. 

### `shift_prepared`

 Exact projection into the 17-stack preprocessing machine. 

### `shift_eval`

 Paid shift staging reads the physically emitted signed rows. 

### `localResult`

 State of the paid one-head loader, before its high-bank export. 

### `localBudget`

 The budget includes every stage and the final raw-word clear. 

### `localResult_frame`

 Every persistent protected source except the head outputs and matrix
output668 is retained by the local loader. 

### `localResult_head`

 The selected head identifiers, size, mask and factor context survive
both matrix stages in their original dedicated tapes. 

### `localResult_nonoutput_length`

 Non-output stacks never grow across reloads, including dirty arithmetic
scratch. This endpoint fact prevents retained storage from compounding across
an exponential number of generator calls. 

### `shifted_matrix_word_length`

 The retained shifted matrix has D rows and every original head column.
Its size depends on physical coefficient word lengths, not their integer values. 

### `shiftedMatrix_typed`

 The physical shifted rows retain every incidence and the exact emitted
column order, including empty matrices and empty heads. 

### `localResult_retained_bound`

 A fixed output envelope is reused at every head reload; caller storage
enters only through max, not through a recurrent enlargement. 

### `localResult_work_empty`

 Every physical raw-matrix work tape is blank at the loader boundary. 

### `localResult_temporary_empty`

 The paid staging copy temporary is restored to blank. 

### `leafRegs`

 The final leaf ABI reserves the high query controls; only16 registers are
used by the loader and its paid copies. 

### `leaf_eval`

 A successful native head reload is promoted to the exact final40-register
leaf ABI, including all address and matrix copying instructions. 

### `command_run_space`

 The native local execution and both paid ABI transfers share this exact
halted trace. Every stack is charged at every prefix of the complete loader. 

### `leaf_run_space`

 The same run and bound after register widening to the actual leaf ABI.
The caller's all896 stacks are included; only the unused registers are framed. 

### `lowResult_low`

 Exporting the matrix preserves all other retained low-bank outputs. 

### `leaf_head_outputs`

 All four head descriptors are returned by the concrete40-register loader.
In particular the all-false size word counts every selected ambient ID. 

### `importAddressFrom`

 A fixed alternate address tape supports reverse head visits without
changing the DFS's retained address845. 

### `programFromLabels`

 The fixed loader's label count is named so callers do not repeatedly
normalize the full structured command merely to compare program types. 

### `commandFrom_run_space`

 Reverse visitation has the same paid-copy and native-loader budget. 

### `leafInputFrom`

 The actual lower input reached after the paid address copy. 

### `exportedState_wordBound`

 Export copies into the destination already emptied by address setup. 

### `MasterFrame.trans`

 Retained source equality composes between concrete call boundaries. 

### `leafOutputFrom_registers`

 The fixed16-register loader leaves every higher caller register intact. 

### `leafOutputFrom_matrix`

 The whole shifted matrix is returned on its dedicated physical tape. 
