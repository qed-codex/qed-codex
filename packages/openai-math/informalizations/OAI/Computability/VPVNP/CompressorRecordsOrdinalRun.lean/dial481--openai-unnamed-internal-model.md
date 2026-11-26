---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsOrdinalRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsOrdinalRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsOrdinalRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Ordinal worker scans inside the guarded compressor dispatcher

A worker may return a dense ordinal, a strided address, or another
computed cursor. At each genuine source call its result advances to the
next cursor and its writes preserve the active frame and control cells.
These properties turn the raw segment into the guarded trace used by
the online launcher, while retaining the worker's own graph invariant.


### `ControlCell`

 Mutable control cells and every word read from the active worker frame. 

### `Preserved`

 The two memories agree on the stage tag, ordinal, row count, and the active frame's
stopping cursor and parameter words. 

### `validTrace`

 Check all dispatch guards from a genuine raw execution. The ordinal
invariant may describe already written fields as well as future inputs.
Every control cell has its initial value at the end of the scan. 

### `row_valid`

 Specialization to an already prepared physical directory row. 
