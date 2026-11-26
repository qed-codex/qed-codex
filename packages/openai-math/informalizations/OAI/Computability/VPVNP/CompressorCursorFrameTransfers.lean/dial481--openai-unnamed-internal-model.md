---
{
  "module": "OAI/Computability/VPVNP/CompressorCursorFrameTransfers.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorCursorFrameTransfers.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorCursorFrameTransfers.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Cursor-frame startup across external stage transfers

The row-count call, raw parameter writer, framed loader and bank copy enter in
state zero. At each accepting exit the stage linker writes the next stage number
below the workspace. The loader's read transcript uses the memory left by both
the raw writer and its transfer.


### `Trace`

 Reports of the four accepting components before their transfer instructions. 

### `Trace.row`

 Report computing and storing the descriptor calendar's row count. 

### `Trace.raw`

 Report writing the raw cursor parameters into the startup workspace. 

### `Trace.loaded`

 Report loading the raw frame and computing the cursor's derived operands. 

### `Trace.copied`

 Report copying the completed cursor operands into the persistent frame. 

### `Trace.postRow`

 Memory after the row-count report and the transfer to stage one. 

### `Trace.postRaw`

 Memory after the raw cursor parameters are published and control advances to stage two. 

### `Trace.postLoad`

 Memory after the parameter loader runs and control advances to stage three. 

### `Trace.post`

 Memory after the persistent frame copy and the transfer to stage four. 

### `trace`

 Construct the four cursor-frame reports using the memory produced by each preceding tagged
transfer. 

### `Runs`

 The four calls and the memory passed to the stride calculator. 

### `run`

 From any external memory, the four native components and their transfers
leave both cursor banks populated, the calendar count intact, and stage four selected. 
