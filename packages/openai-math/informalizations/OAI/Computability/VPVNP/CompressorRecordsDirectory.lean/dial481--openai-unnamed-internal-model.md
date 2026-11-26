---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsDirectory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsDirectory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsDirectory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native execution of a level-major descriptor directory

Every row supplies a worker tag, a starting cursor, an exclusive stop, and
a fixed-pitch parameter bank. The dispatcher executes the controller, then
the chosen worker for all its data calls, and then returns to the controller.
The row theorem composes an actual verified source run with any remaining
directory. Its cost is linear in the source calls plus probes and the row
count, with constants fixed by the catalog.


### `levelOrdinal`

 A fixed number of pass slots per level. An optional initial segment,
such as the level-zero cursor construction, precedes the repeated levels. 

### `address`

 Natural address of a field in the fixed-pitch directory, indexed by row ordinal and field
offset. 

### `table`

 A descriptor program with one finite table independent of the number
of repetitions, directory rows, address width, and live input length. 

### `program`

 The native program that dispatches between the fixed-arity directory controller and the
catalog's data workers. 

### `rowBase`

 The current directory row's word address, computed from the published directory base, row
ordinal and catalog arity. 

### `launchReport`

 The linked controller report that snapshots the active row and starts its selected worker
at the stored cursor. 

### `terminalReport`

 The linked accepting controller report emitted when the directory ordinal has reached the
total row count. 

### `prepared`

 Memory after the controller launches an active row, with its worker operands and stop bound
installed in the active frame. 

### `start`

 The worker's initial cursor, read from offset one of the current directory row. 

### `bound`

 The worker's exclusive stopping cursor, read from offset two of the current directory row. 

### `words`

 The public parameter words of the selected worker, read in order immediately after the
row's stop bound. 

### `launch_effect`

 Internal controller memory effects and the precise next cursor. 

### `FrameFits`

 Separation of the active parameter bank from the two mutable control
cells. The controller snapshots the full source row before writing the bank. 

### `Row`

 One scheduled worker invocation. Its operand words, starting state,
and bound are read from its row in the entry memory. 

### `Row.input`

 Entry memory in which the directory controller finds the row and reads its operands. 

### `Row.worker`

 Catalog index of the worker selected for this row. 

### `Row.fuel`

 Instruction fuel supplied to each call of the row's source worker. 

### `Row.choices`

 The ordered choice-bit streams supplied to the source worker's data calls. 

### `Row.reports`

 The source worker reports for the row's data calls, in execution order. 

### `choicesWithControl`

 Surround the worker choice streams with empty streams for the controller launch and closing
call. 

### `dataMemory`

 Memory passed to the first worker data call after the controller has installed this row's
active frame. 

### `endMemory`

 Memory after replaying all source worker reports from the prepared data memory. 

### `post`

 Memory after the row finishes and restores the controller stage tag to zero. 

### `log`

 The complete linked report list for a directory row, from the controller launch through all
data calls and the closing handoff. 

### `Valid`

 The active row starts under the controller tag, has positive fuel, and its source reports
form an actual run respecting the loaded frame and cursor bound. 

### `capNeeded`

 A per-call fuel bound covering the controller, the row's source worker and active-frame
loads, and the outer stage dispatch. 

### `segment`

 From controller entry through the full original pass and its handoff.
The tail can itself start another pass with newly computed parameters. 

### `cost`

 Exact source and scheduler charges through one full row, including the
controller launch, active data calls, and the empty-choice closing call. 

### `finalMemory`

 Memory at the terminal controller, after the last worker handoff. 

### `Valid`

 Compatibility at every native row boundary, with directory exhaustion
checked at the terminal controller. A worker may write later rows. 

### `run`

 The native full directory run accepts these exact streams and computes
the indicated reports for all the selected rows. 

### `cost_bound`

 The total linked charge depends only on native source charges and
the row count. The constants depend on the fixed worker catalog. 
