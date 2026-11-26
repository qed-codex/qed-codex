---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsOnline.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsOnline.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsOnline.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native online descriptor program

Stage zero launches the freshly constructed row. The data workers come
next, followed by the calendar and the row recipes. A data worker's
closing call returns to the calendar. A recipe's accepting call returns
to stage zero, which snapshots its actual output row. The calendar is the
only accepting terminal stage of the scheduled path.


### `Config`

 The finite plan of row-building recipes for the initial and repeated phases, together with
the number of levels advanced by each block. 

### `Config.levelsPerBlock`

 How many level headers the calendar advances when it moves to the next block. 

### `Config.recipes`

 The recipe and its register count at each initial or repeated phase, producing a
  directory row of the catalog's fixed arity. 

### `N`

 Total number of linked online stages, including a launcher, the data workers, a calendar
and the row recipes. 

### `calendar`

 Build the planner calendar for this configuration using the catalog's row pitch and the
configured number of levels per block. 

### `launchIndex`

 Stage zero, where the controller snapshots the directory row and launches its data worker. 

### `workerIndex`

 The linked stage of a data worker, immediately following the launcher in catalog order. 

### `calendarIndex`

 The stage after the data-worker bank that selects the next planner recipe. 

### `recipeIndex`

 The linked stage of a row-building recipe, numbered after the calendar. 

### `slots`

 The stage slots and their operand mappings, ordered as launcher, data workers, calendar and
row recipes. 

### `tables`

 Embed each stage's instructions into the online program's shared register bank and public
operand table. 

### `handoff`

 The continuation on stage acceptance. A completed worker goes to the calendar and a
completed recipe goes to the launcher. 

### `template`

 The fixed online RAM template linking the widened stage tables with their accepting
handoffs. 

### `program`

 Instantiate the linked online stages with the runtime workspace ports and stage-tag
address. 

### `linked`

 Wrap a source-stage report in the online dispatcher's events and apply the accepting
handoff for its stage. 

### `phaseIndex`

 Identify a recipe's configuration index with its slot in the constructed planner calendar. 

### `calendar_call`

 One real calendar call selects the next row recipe in the shared tag
cell and returns the header pointer to it. 

### `recipeSource`

 The accepting source report of a row recipe, using the write events computed from the block
header state and entry memory. 

### `recipe_call`

 A fixed recipe runs on the returned header pointer and transfers to the
row launcher. 

### `launch_call`

 Stage zero loads the currently addressed row and installs its worker's
parameter frame. 

### `closedSource`

 The data worker's closing source report, including the active-frame loads for its bound and
parameters before acceptance. 

### `calendarReport`

 The linked calendar report dispatching the recipe for the specified phase. 

### `recipeReport`

 The linked report of a recipe that writes its row and hands control to the launcher. 

### `launchReport`

 The linked controller report that installs the newly prepared row and dispatches its data
worker. 

### `activeReport`

 Wrap one successful data call with its active-frame loads and the online stage dispatch. 

### `stopReport`

 The linked closing report at the worker's exclusive bound, handing control back to the
calendar. 

### `workerRows`

 Wrap the worker reports in execution order, advancing the source memory after each call so
the next frame is read from its actual entry memory. 

### `worker_segment`

 Run all the source calls of a data worker, acknowledge its stop, and
continue at the calendar tag. Each read of the bounded frame uses the
memory left by the preceding source call. 

### `calendarMemory`

 Memory after calendar dispatch has written the selected recipe's stage tag. 

### `rowInput`

 Memory after the selected recipe writes its row at the computed address and sets the
launcher tag. 

### `preparation`

 The calendar dispatch, recipe execution and worker launch reports that precede the data
calls of one online row. 

### `prepare_segment`

 Execute the calendar, its selected recipe, and the launcher, then enter
the data worker selected by the computed row. The launcher reads the
actual output memory of the selected recipe. 

### `rowLog`

 All reports for one online row, including preparation, the ordered data calls and the
closing return to the calendar. 

### `post`

 The row's final worker memory with the stage tag set to resume the calendar. 

### `rowChoices`

 The complete choice-stream list for the row, with empty streams for its three preparation
calls and its closing call. 

### `row_segment`

 A complete phase begins and ends at the calendar. The original source
call sequence consumes exactly its own branch choices. The recipe and row
launcher operate on the memory computed by the preceding phase. 

### `row_cost`

 Total calls plus probes for one online phase, charged against the raw
worker calls and the native row expression's metadata reads. 

### `row_effect`

 Actual linked reports have the same memory and next state as the
continuation supplied to the phase composition theorem. 

### `computed_ready`

 From a recipe's actual destination and field values, the launcher
installs the computed start, stop and parameters. Address separation
protects the row and the two controller counters through the tag transfer. 
