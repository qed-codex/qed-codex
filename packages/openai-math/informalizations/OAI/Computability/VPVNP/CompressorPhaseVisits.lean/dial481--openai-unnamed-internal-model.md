---
{
  "module": "OAI/Computability/VPVNP/CompressorPhaseVisits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorPhaseVisits.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorPhaseVisits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Charged native directory scans on a selected compression branch

A phase may dispatch one flat scan or use short rows for each site of a
fixed kind. The two forms have different launch counts. The scope indexes
the actual base, slots, motifs or resulting sites of the selected kernel.
The directory bound charges launches, closing calls and the final controller
as well as every original data call, even for empty scans.


### `Scope`

 Objects traversed by the native workers at a single level. 

### `Scope.count`

 Number of objects in the phase's scope for the selected pass, using its base, sites, slots,
or motifs as appropriate. 

### `Phase`

 A fixed scan prescription. `perObject` counts data calls at each
physical object or the full work of its short rows. 

### `Phase.scope`

 Set of objects over which this native phase is scheduled. 

### `Phase.perObject`

 Bound on worker visits charged to each object in the phase's scope. 

### `Phase.weight`

 Per-object charge including the worker visit budget and two calls for entering and closing
a row. 

### `Plan`

 Native pass families of the fixed finite block. 

### `Plan.shrink`

 List of native phases assigned to each shrinking substep of a block. 

### `Plan.refresh`

 List of native phases assigned to the degree refresh at the end of a block. 

### `Plan.phases`

 Recover the phase list appropriate to the origin of the actual state pass. 

### `Plan.levelRate`

 Largest total phase weight among the refresh and all indexed shrinking passes. 

### `calls`

 Number of charged calls in a row list, adding launch and close to each row's data-report
count. 

### `Rows`

 Either a whole-phase cursor scan, or an ordered family of short row
groups. In the second form each group pays its own launches and closes. 

### `Rows.log`

 Chronological directory rows of a phase, either one flat scan or the concatenation of its
per-object rows. 

### `LevelRows`

 Each occurrence has its own physical memory and worker. The two
ordinals distinguish equal phase sizes and repeated equal input states. 

### `levelLog`

 Directory log for the phases of one selected level, numbered from phase zero at that level. 

### `levelLogs`

 Concatenate the directory logs of successive selected levels while advancing the level
index. 

### `branchRows`

 Chronological rows on the selected branch, including the level-zero
cursor initialization in `initial`. 

### `directory_run`

 Run the linked table on a physically valid directory and charge all
returned reports, including launch, stop and terminal controller. 
