---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkAllocatedTables.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkAllocatedTables.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkAllocatedTables.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Separate AB, surviving-width and ordered-slot tables in the physical block

The block calendar builds the AB intersections before its four surviving
role scans. Each table has its own advised base address. The incidence
directory, endpoint lists, and both kinds of interval descriptors are
readable in the same final memory.


### `width_at_eq`

 The requested width-table base is used exactly when the preceding
resident fields fit below it. 

### `Resident`

 Readbacks inherited by the AB and surviving-width workers from the
term, placement and preimage passes. 

### `ABFields`

 Every assigned bundle's final bank stores the intersections between its old thick fields
and new AB pieces in the prescribed orders. 

### `TablesRun`

 The successive reports of the AB phase and both output phases. 

### `TablesRun.intersections`

 Reports emitted by the initial AB intersection scans before construction of the surviving
  and ordered-slot tables. 

### `TablesRun.remainder`

 The remaining shrinking passes after the AB intersections, including their final memory. 

### `TablesRun.postAB`

 Replay the intersection reports on the input memory to obtain the starting memory of the
remaining passes. 

### `TablesRun.reports`

 The complete report sequence, with the AB intersection scans followed by the remaining
table-building passes. 

### `TablesRun.final`

 The final memory of the remaining passes after the AB, surviving-width and ordered-slot
tables have been built. 

### `CompleteTables`

 The chronological AB and remaining passes build all three tables, preserve memory outside
the AB bank during its construction, and replay to the claimed final memory. 

### `CompleteTables.cost`

 The number of calls and probes includes the native AB work, all four
role scans, and the complete ordered-slot passes. 

### `withAB`

 Run the actual AB source visits, then the native surviving-role and slot
workers. The source memory may already contain the hidden history records.
Only established readbacks of its existing columns and selected terms are
needed. All three output tables are built from those inputs. 
