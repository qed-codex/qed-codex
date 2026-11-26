---
{
  "module": "OAI/Computability/VPVNP/CompressorCalendarArenaTransfers.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorCalendarArenaTransfers.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorCalendarArenaTransfers.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Starting the history arena and calendar across pair-linker calls

After the cursor parameters have been copied to the active frame, four native
calls compute the level stride, publish the history arena and traversal
bounds, install the pointer bank, and arm the calendar. The external tag is
updated after each accepting call.


### `Trace`

 The four startup reports that install the descriptor stride, history arena, scheduler bank
and calendar arm. 

### `Trace.stride`

 Report of the worker that publishes the descriptor stride. 

### `Trace.arena`

 Report of the worker that computes the history arena base from the calendar and level
  dimensions. 

### `Trace.bank`

 Report of the worker that initializes the scheduler operand bank. 

### `Trace.arm`

 Report of the worker that arms the online calendar. 

### `Trace.postStride`

 Memory after applying the stride report and transferring control to stage five. 

### `Trace.postArena`

 Memory after publishing the history arena base and transferring control to stage six. 

### `Trace.postBank`

 Memory after the scheduler bank is initialized and control advances to stage seven. 

### `Trace.post`

 Memory after the calendar is armed and the stage tag advances to eight. 

### `trace`

 Construct the four startup reports chronologically, using each tagged transfer's output
memory for the next worker. 

### `Runs`

 Each startup worker executes at the specified clock and stage entry, producing the
corresponding report of the trace. 

### `run`

 At entry, both cursor banks and the natural row count come from the
preceding four linked calls. The layout and word bounds certify every
address used in the history-arena header. 
