---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsSchedule.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsSchedule.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsSchedule.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A fixed dispatcher for the compressor descriptor passes

The controller occupies tag zero. A worker has a finite native table and
its own public parameter format. On each worker call the active frame
supplies an exclusive cursor bound followed by the parameters. At the
bound the stage linker writes tag zero and returns to the controller. Thus
level counts and pass repetitions change memory and cursors while the
dispatcher table is fixed.


### `Pass`

 A worker with its actual finite register and parameter arities. 

### `Pass.pcs`

 Number of instruction labels in the pass’s native RAM table. 

### `Pass.regs`

 Number of private registers available to instructions in this pass. 

### `Pass.params`

 Number of public operand words expected by the native pass. A scheduled call loads these
  words from the active frame after the stop word. 

### `Pass.table`

 The pass’s native instruction table, indexed by its own instruction labels, private
  registers, and public operands. 

### `Catalog`

 An indexed family of native passes. The dispatcher assigns the pass at index `i` to tag `i
+ 1` and reserves tag zero for the controller. 

### `cursorPass`

 Native pass that writes six cursor-incidence entries for one outgoing port and returns the
next port index in register zero. 

### `refreshPass`

 Native pass that writes a segment’s outgoing and incoming offsets and incoming width,
updates the bundle total, and returns the next segment index. 

### `cursorRefresh`

 Small concrete catalog used to link the initial cursor and refresh scans. 

### `arity`

 Maximum number of public operands among the catalog’s passes, or zero for an empty catalog.
This fixes the width of the directory’s parameter bank. 

### `field`

 The bounded-table library numbers its exclusive stop last. A directory
frame places it first, followed by the worker's original public words. 

### `worker`

 Wrap a native pass in a frame loader and a cursor guard. Its sole public word points to the
frame, whose first word is the exclusive stop and whose remaining words supply the pass
operands. 

### `stopWord`

 Limit and original public words in the order seen by the running worker. 

### `parameters`

 Read native operand `j` at active-frame offset `j + 1`, immediately after the exclusive
stop stored at offset zero. 

### `workerReport`

 Report for an active worker call. The frame loads and three cursor-guard ticks precede the
native pass events, and the call returns the native result. 

### `Ports`

 Shared public words of the enclosing stage linker. The internal tag is
separate from the enclosing live program's stage tag. 

### `Ports.activeFrame`

 Base address of the active worker frame, which stores the exclusive cursor bound followed
  by the worker’s public operands. 

### `Ports.directory`

 Base address of the descriptor directory from which the controller loads each scheduled
  row. 

### `Ports.ordinal`

 Address of the control cell holding the index of the next directory row to launch. 

### `Ports.rows`

 Address of the cell holding the directory row count. The controller finishes when the
  ordinal reaches this count. 

### `Ports.tag`

 Address of the internal dispatch tag. Zero selects the controller and tag `i + 1` selects
  worker `i`. 

### `Ports.data`

 The five shared public words in operand order are the active-frame base, directory base,
ordinal address, row-count address, and dispatch-tag address. 

### `Slot`

 A stage is widened only after its operand format and optional frame loader
have been chosen. This keeps the original worker register budgets independent. 

### `Slot.publicIndex`

 Selects the shared public word for each operand of the slot. The controller uses all five
  words in order, and a framed worker uses only the active-frame base. 

### `slots`

 Assign the controller to slot zero and the framed, guarded version of catalog pass `i` to
slot `i + 1`. 

### `tables`

 Widen a slot’s native table to the largest register count among all slots and map its
public operands into the dispatcher’s five shared words. 

### `handoff`

 The controller explicitly writes the computed worker tag and returns
its initial cursor. An accepting worker transfers back to the controller. 

### `template`

 The linked dispatcher table for the controller and catalog workers. Accepting a worker
transfers control to slot zero, while accepting the controller finishes the schedule. 

### `machine`

 Instantiate the linked dispatcher at word width `w` with the five port words and
`ports.tag` as the address from which the linker reads the active slot. 

### `worker_active`

 One successful call of a source worker inside the actual finite
descriptor dispatcher. Its incoming tag and guard are read from RAM. 

### `worker_stop`

 The single empty-choice call at the exclusive bound transfers back to
the controller, which can select another pass or the next level. 

### `controller_call`

 Any successful call of the controller is also a native call in the
descriptor dispatcher. The controller's accepting exit terminates the schedule. 

### `activeLinkedReport`

 Tagged reports of active data calls and of the single closing call. 

### `closedLinkedReport`

 Report of the closing call at or beyond worker `i`’s exclusive bound. It reads the dispatch
tag and frame, writes tag zero, and returns cursor zero to the controller. 

### `closedLinkedReport_effect`

 Finishing a pass writes precisely the internal controller tag and returns
cursor zero. There are two tag probes plus one read per active-frame word. 

### `Ready`

 Active-frame and dispatcher cells that must survive an ordinary pass. 

### `ValidTrace`

 Each source report is below the stop and returns a new cursor. At the
end the native guard observes the stop. This allows arbitrary cursor steps. 

### `linkedRows`

 Wrap each active source report in its dispatcher report in execution order. The frame for
each call is read from the memory left by the preceding source events. 

### `linkedRows_cost`

 Exact total charge of the linked data calls in an active source trace. 

### `linkedPass_cost`

 Exact cost through the handoff, excluding the controller call that
prepared this row. A zero-length scan still executes its closing call. 

### `worker_segment`

 Execute a verified source pass inside the finite dispatcher, consume its
closing call, and resume any remaining level schedule at controller tag zero.
The frame is loaded once per call, independently of the source's private work. 
