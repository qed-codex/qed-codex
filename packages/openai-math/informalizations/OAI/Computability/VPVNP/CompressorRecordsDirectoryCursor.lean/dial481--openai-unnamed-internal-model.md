---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsDirectoryCursor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsDirectoryCursor.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsDirectoryCursor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Launching the level-zero cursor pass from an initialized directory

The first directory row is produced by the fourteen-write initializer.
The controller snapshots the row, installs the active frame, and launches
the cursor worker at row zero. The last worker call restores the controller
tag while preserving the constructed graph directory.


### `initWords`

 The first scheduler row uses the tag for catalog worker zero. 

### `installed`

 Memory after the cursor initializer writes the first directory row for the specified
radices, degree, width and incidence columns. 

### `row`

 The row object includes the exact reports of the source worker. The
directory dispatcher derives its tag, cursor and operand bank from RAM. 

### `OutsideRow`

 The address lies before the cursor initializer's directory row or at least fourteen words
past its start. 

### `Header`

 The active controller row launches the cursor worker at zero with the exact row count and
public operands for the initial graph. 

### `install`

 The actual initializer produces every operand used by the controller.
The only hypotheses about incoming RAM concern the three controller cells.
Their addresses lie outside the fourteen consecutive writes. 

### `valid`

 Once the controller has read the first row, the guard and parameters
come from its computed frame. Every subsequent reload sees the same values. 

### `row_effect`

 A level-zero row, including its controller launch, has the source
cursor pass's six writes per slot and a fixed dispatcher overhead. 

### `initialize_and_launch`

 Execute the native row producer, launch the controller from the resulting
RAM, run the full incidence scan, and splice any following rows at the exact
post-state. The resulting external memory represents the typed cursor graph. 
