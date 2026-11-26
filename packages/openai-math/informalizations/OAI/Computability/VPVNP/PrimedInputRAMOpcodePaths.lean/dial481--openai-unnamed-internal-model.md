---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMOpcodePaths.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMOpcodePaths.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMOpcodePaths.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native path correspondence for the physical primed input passes

Each data call reads three supplied cut lengths before performing its scheduled item.
The physical machine may take extra private steps. Across the entire input stage its
branch choices, returned cursors and final memory agree with the schedule.


### `execute_extra_choices`

 A successful call consumes its entire choice stream. Appending an unused
nonempty suffix to that same stream therefore rejects. 

### `PhysicalSchedule`

 Local contract of the physical input-stage machine. Only prescribed input
streams need to be checked; exact use of bits rules out any other path. 

### `PhysicalSchedule.report`

 Native report for one scheduled data call at the given incoming memory and choice bit. 

### `PhysicalSchedule.last`

 Native report for the halt call at the cursor just beyond the final data item. 

### `MatchedReports`

 Agreement of two native histories, including their extra cut-length probes.
A returning data call incurs three extra probes; the terminal call incurs none. 

### `run_matched`

 Run the physical and scheduled interpreters on the same sequence of streams.
They reject together, or return matching histories, from any valid cursor. 

### `accepts_iff`

 Physical acceptance and schedule acceptance coincide before imposing budgets. 

### `generated`

 A complete physical run for every bit assignment, with its exact final memory
and exact calls-plus-probes cost, including the terminal call. 

### `accepted_cost`

 For any accepting run, the interpreter's own reports carry the exact total
cost and respect the six-unit call bound. 

### `pathEquiv`

 Identity on the supplied per-call branch streams. Both the total budget and
the individual-call budget refer to the actual reports returned by each program. 
