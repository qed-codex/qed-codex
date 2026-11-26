---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotBuildInputs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotBuildInputs.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotBuildInputs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preparing the input tables for the selected slot directory

Four independent one-call phases publish the subdivision lengths. The following
scans write the selected roles, compute the cyclic site successor and clear every
append counter. The old arc and split-width rows precede the newly allocated
tables and survive all seven phases.


### `publishBank`

 Public address and value words for writing one of the four subdivision counts to its
designated cell. 

### `published`

 The single-call report that writes one subdivision count and returns cursor one. 

### `publish_run`

 The four one-call phases restart their local cursor and publish one value each. 

### `roleBank`

 Public layout bit and destination table base for computing the endpoint roles of the four
edge types. 

### `cyclicBank`

 Public lane count, tag count, and destination base for writing the cyclic tag successor of
every packed site. 

### `Reports`

 Reports for the seven input preparation phases, covering four subdivision writes and three
subsequent scans. 

### `Reports.publish`

 One native write report for each of the four subdivision counts. 

### `Reports.roles`

 Reports that populate the eight endpoint role entries for the chosen layout. 

### `Reports.cyclic`

 Reports that write the site reached by advancing the tag at each packed site. 

### `Reports.clear`

 Reports that zero the append counters for the real endpoint owners and the reserved hole
  owners. 

### `Reports.all`

 Preparation reports in order of execution, from the four subdivision writes through the
counter clear. 

### `Reports.final`

 Memory after applying all input preparation reports in order. 

### `Reports.Native`

 All public banks, per-phase fuel and reset cursors, in the planner's visit order. 

### `Reports.Cursors`

 The four publishers return cursor one, and the role, successor, and clear scans return
their respective row counts. 

### `Reports.Native.resources`

 Calls, calls plus external probes, total dispatched instructions, and the
per-call instruction bound for the entire seven-phase preparation program. 

### `preserve_rows`

 Preservation of both previously materialized slot inputs under the
preparation program's frame, including every selected split-width cell. 

### `run`

 The prepared memory supplies both owner workers and all zero append counters.
Every external cell before the role table or beyond the counters retains its
initial value. The older split-width rows can therefore use the same frame. 
