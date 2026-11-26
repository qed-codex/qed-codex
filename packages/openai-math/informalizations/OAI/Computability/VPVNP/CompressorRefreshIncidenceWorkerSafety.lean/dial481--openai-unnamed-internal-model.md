---
{
  "module": "OAI/Computability/VPVNP/CompressorRefreshIncidenceWorkerSafety.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshIncidenceWorkerSafety.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshIncidenceWorkerSafety.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Per-call memory regions of refreshed incidence workers

The actual-slot worker reads the scratch directory, ROM or selected supplies
below the output incidence region. Its three writes are in the output
columns. The lane-zero base worker then uses one actual-output read and
three base-column writes inside that same region.


### `interval`

 An inclusive lower bound and exclusive upper bound in the packed allocation. 

### `SlotInvariant`

 Throughout one slot scan, the complete read interval still agrees with
the reference memory at the beginning of that scan. 

### `slot_scan`

 The raw genuine slot reports carry the dense ordinal sequence and their
full footprint before scheduler cells are installed. 

### `slot_valid`

 Replay one complete fixed-slot pass inside a guarded row. The memory may
differ from the reference before the allocation, including the active frame. 

### `base_scan`

 Raw lane-zero scan footprint and completed prefix, independent of the
scheduler's installation of the base worker's public bank. 

### `base_valid`

 The lane-zero base pass preserves its actual columns and its growing
prefix under the scheduler guards, using the same raw report sequence. 
