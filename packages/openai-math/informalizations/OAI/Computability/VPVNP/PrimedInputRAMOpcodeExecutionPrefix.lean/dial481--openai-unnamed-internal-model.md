---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMOpcodeExecutionPrefix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMOpcodeExecutionPrefix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMOpcodeExecutionPrefix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Transferring the physical input prefix to the grammar phase

The data calls of Section 11 return after the second pass with the assembled memory.
They can be used in a larger program whose data calls are linked to the same opcodes
and whose terminal cursor enters the parser. The residual stream of parser calls is
arbitrary and is passed unchanged to that cursor.


### `ReturningCalls`

 Data calls of an enclosing program. Its phase transition can continue in the grammar
parser, and the extra private ticks of its dispatch may differ from the standalone RAM. 

### `ReturningCalls.report`

 Report of one input-stage call in the enclosing program, indexed by the scheduled item,
  incoming memory and supplied bit. 

### `reportList`

 Per-item reports before a continuation takes control. 

### `dataReports`

 Reports of successive returning input-stage calls, threading each item's memory update into
the next call. 

### `prefix_endState`

 The actual data reports, taken without the halt, end at the first parser cursor. 

### `splice`

 Any enclosing burst program with the physical data-call implementations can resume
at cursor `M`. Its exit behavior and its remaining private branch streams are unrestricted. 

### `recover`

 Conversely, every accepting execution of the enclosing program must pass all the
input cursors with their prescribed branch streams. Its suffix starts at the grammar
cursor, consumes the remaining streams, and finishes with an accepting halt. 

### `choices_of_length`

 If exactly the data calls have returned, every choice list must have the
scheduled shape, even when the later program rejects. 

### `dataReports`

 Reports for the specified physical data calls in order, using the memory produced by each
preceding item. 

### `returningCalls`

 Keep the per-cursor implementations and leave the terminal call to the enclosing
program. 

### `prefix_endState`

 The actual data reports, taken without the halt, end at the first parser cursor. 

### `splice_data`

 Any enclosing burst program with the physical data-call implementations can resume
at cursor `M`. Its exit behavior and its remaining private branch streams are unrestricted. 

### `recover_data_prefix`

 Conversely, every accepting execution of the enclosing program must pass all the
input cursors with their prescribed branch streams. Its suffix starts at the grammar
cursor, consumes the remaining streams, and finishes with an accepting halt. 

### `run_data`

 The generated native data calls without the halt. 

### `cursorBits`

 Extend the internal assignment to every cursor; only owner positions consume these bits. 

### `input_prefix`

 Generated data-call prefix for the actual, finite opcode table. Its cost omits the
terminal call, and its return cursor and memory are ready for the parser. 
