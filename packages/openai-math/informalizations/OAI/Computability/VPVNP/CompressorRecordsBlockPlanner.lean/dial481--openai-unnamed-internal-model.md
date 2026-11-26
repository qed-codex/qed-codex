---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsBlockPlanner.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsBlockPlanner.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsBlockPlanner.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Compiling a finite block of native scans

Each phase contains its worker and exactly the expressions for that worker's
public bank. The phase's position in the program determines the tag written
by its planner. The initial sequence and one complete block determine the
instruction table. The number of repeated blocks enters through the runtime
row count.


### `Visit`

 One scheduled scan, pairing its worker with expressions for the initial cursor, exclusive
stopping cursor, and public operands. 

### `Visit.worker`

 The native pass selected for this scan and the arity of its operand bank. 

### `Visit.initial`

 Expression giving the state word passed to the worker at the start of the scan. 

### `Visit.stop`

 Expression giving the exclusive end cursor at which this worker's scan finishes. 

### `Visit.params`

 An operand expression for each public input of the selected worker. 

### `Visit.ofPhase`

 Combine a native pass with the cursor and operand expressions from a phase of matching
arity. 

### `ops`

 Build a scheduled visit for a straight-line stack-RAM worker, with its result register,
cursor bounds, and public operands. 

### `copy`

 Move a verified scratch column to the next level's published incidence directory. 

### `publish`

 Publish a single fixed subdivision or header field in the current level. 

### `Script`

 The finite visits needed to run the initial scans once and a block of scans repeatedly,
with the level advance per block. 

### `Script.levelsPerBlock`

 Number of descriptor levels advanced by each complete repetition of the block. 

### `Script.initial`

 The visits executed once before the first repeated block. 

### `Script.block`

 The ordered visits that make up one repetition of the scheduled block. 

### `size`

 Number of visit positions in the initial sequence followed by one block. 

### `visit`

 Look up a visit in the concatenated indexing of initial phases and block phases. 

### `catalog`

 The native worker at each of the script's visit positions. 

### `phase`

 Each occurrence gets its own finite worker label, even when several
occurrences run the same native table on different operands. 

### `plan`

 Compile the visit recipes and block level advance into the online scheduler's
configuration. 

### `program`

 Instantiate the online scheduler for this script on the supplied workspace ports. 

### `cursor`

 Runtime cursor parameters are produced before the first calendar visit.
They occupy eight persistent scalar cells in the initial level. This bank
survives subsequent launches that overwrite the active frame. 
