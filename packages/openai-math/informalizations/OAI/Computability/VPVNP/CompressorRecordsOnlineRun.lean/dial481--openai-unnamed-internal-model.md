---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsOnlineRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsOnlineRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsOnlineRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Chronological execution of the online descriptor program

Each selected phase contributes the actual branch stream of its worker.
The row input is computed by the recipe in the memory left by the
preceding phase. One final empty-choice calendar call accepts at the
exclusive ordinal bound. The total work bound uses the maximum number
of metadata reads among the fixed recipes.


### `Step`

 The recipe and data worker on this actual path. 

### `Step.phase`

 Index of the row recipe chosen by the calendar at this step's ordinal. 

### `Step.row`

 The selected worker's directory row, including its entry memory, fuel, branch streams and
  source reports. 

### `Step.Valid`

 Each phase starts from actual RAM and has enough private fuel to
evaluate its recipe and to execute each source call. 

### `Valid`

 The next phase is verified in the previous worker's computed post-memory. 

### `finalMemory`

 Follow the scheduled rows in order and return the memory left when the last worker hands
control back to the calendar. An empty run returns its entry memory. 

### `reports`

 Concatenate the planner, launch, worker and stop reports for each row in its entry memory,
then append the calendar's closing report. 

### `choices`

 Supply empty branch streams for row preparation and stopping, the worker's own streams for
its data calls, and one final empty stream for calendar acceptance. 

### `execute`

 Run the fixed instruction table from the calendar through the terminal
accept. Each phase may depend on choices made inside all earlier workers. 

### `effect`

 The full reports leave exactly the memory of the last data worker
after its return to the calendar, and the final call halts. 

### `maxReads`

 Uniform metadata-read bound depends only on the finite set of recipes. 

### `sourceCost`

 Sum the number of source-worker calls and their memory probes over all selected rows,
before charging for calendar and dispatch work. 

### `cost_bound`

 Source calls and probes are charged with a catalog-wide constant. Each
scheduled row also pays for the calendar, recipe, frame launch, and closing
call. The final calendar call costs four units including its dispatch read. 

### `remaining`

 Number of rows still to be launched from this calendar memory. 

### `exists_valid`

 A per-phase construction can generate the entire path from its current
descriptor memory. It suffices to construct the next source row, preserve
the construction invariant, and account for the single ordinal increment. 

### `exists_run`

 Acceptance, exact path choices, final invariant and work bound follow
from the next-row construction without a precomputed directory of rows. 
