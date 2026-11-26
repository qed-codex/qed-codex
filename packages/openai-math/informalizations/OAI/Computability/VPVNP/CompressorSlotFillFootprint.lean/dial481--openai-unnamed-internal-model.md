---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotFillFootprint.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotFillFootprint.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotFillFootprint.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Probe addresses in the shrinking slot array passes

The append pass reads the owner and count columns and writes the count and row
columns. Scattering the resulting real rows, or the base-mate permutation, reads
the forward column and writes the inverse column. These bounds apply to the
actual chronological event log, so a scheduler can change unrelated control cells
and replay the same native calls.


### `InColumn`

 The half-open physical range of a contiguous column. 

### `AppendReads`

 An address in the owner column or count column that the field append pass may read. 

### `AppendWrites`

 An address in the count column or the rectangular row table that the field append pass may
write. 

### `append_run`

 Native append bounds for a successful partial or complete scan. The guards
on each call suffice for these bounds even with arbitrary starting memory. 

### `scatter_run_bounded`

 Bounds for the native inverse pass with a bounded forward column. The values
may repeat. Each write lies in the disjoint inverse interval, so all remaining
source reads see their initial values. 

### `scatter_run`

 Footprint of the reports returned by `SlotScatter.run`, for any occupied
endpoint embedding. 

### `appendFields`

 In the layout used by the slot builder, the append call's readable interval
ends at the row base, and its writable interval begins after the owner stream. 

### `invertFields`

 Bounds for scattering a rectangular endpoint table with its mathematical
ordering. Only the forward part of the table is needed as input. 

### `invertFields_after_append`

 Scattering immediately after the actual append pass uses the bounded entries
that pass produced. Equality of the native reports identifies its physical output
with the `PreimagesAt` postcondition from `fill_run`. 

### `baseInverse`

 A selected state's forward mate column is a permutation in its canonical
base-port ordering. Its inverse pass reads and writes only those two columns. 

### `selected`

 Read and write bounds for the append and invert phases of an actual shrinking
level. The genuine and dummy reports determine the physical input to append,
including all still-zero counters. The append reports then determine the actual
source rows read by the inversion. 
