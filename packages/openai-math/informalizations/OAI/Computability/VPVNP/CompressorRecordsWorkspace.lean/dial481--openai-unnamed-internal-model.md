---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsWorkspace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsWorkspace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsWorkspace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The pair workspace as the compressor scheduler's native parameter bank

Public word two of the eleven-word pair ABI points to the workspace.
Its first six words supply the scheduler's parameters. The following three
words hold its tag, ordinal and row count. The active frame occupies the
next maximum-arity-plus-one words. One reserved word separates the frame
from the directory.


### `ports`

 Locate the scheduler's active frame, directory, ordinal, row count, and tag relative to the
pair workspace base, allowing room for the maximum worker arity. 

### `bank`

 The six public scheduler pointers stored in the workspace header. The internal scheduler
tag and its stage linker share one tag cell. 

### `Installed`

 The header's two tag parameters refer to the same external cell. 

### `table`

 The only public operand accessed by the enclosing frame loader is word two. 

### `report`

 Prefix a scheduler report with the events that load its six parameter words from the
workspace header. 

### `execute_dispatch_of`

 A successful scheduler report with its exact branch stream lifts at a cost of
six external reads and eighteen private ticks. 

### `offset`

 Offsets from the workspace base stored in the header. The last two cells
are control words initialized to zero. Row count at offset eight comes from
the level-directory constructor. 

### `headerWord`

 Value installed in one of the first eight workspace cells. The first six hold scheduler
pointers, followed by the initial zero tag and ordinal. 

### `initTable`

 One native call installs the six pointers and resets the scheduler's tag
and ordinal. Its accepting exit allows the outer linker to enter the next stage. 

### `initMachine`

 Instantiate the header initializer at the chosen word width using the pair ABI's public
words and maximum worker arity. 

### `initReport`

 Accepting initialization report recording eight header writes to install the scheduler
pointers and reset its tag and ordinal. 

### `execute_init`

 The initializer executes exactly one deterministic accepting history at every
sufficient instruction cap. 

### `init_cell`

 The eight contiguous installed words, including the two mutable control cells. 

### `init_installed`

 The scheduler sees the computed pointer bank on its very first call. 

### `Installed.preserve`

 Reuse of the header on later calls only requires that the six pointer cells
retain their values. The internal tag and ordinal may change on every row. 

### `execute_initialized`

 Consecutive native initialization and dispatch, using the memory left by the
initializer. The input row count and all precomputed directory entries may already
be present when initialization starts. 

### `calendarStart`

 After installing the workspace, the online scheduler begins at the calendar
stage whose tag follows the `d` data-worker tags. 

### `calendarReport`

 Accepting report for starting the calendar stage, with four private ticks and a write of
tag `d+1` at workspace offset six. 
