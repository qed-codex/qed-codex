---
{
  "module": "OAI/Computability/VPVNP/PairTraversalControllerInputs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalControllerInputs.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalControllerInputs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading traversal workers from the resident terminal header

The cursor layer precedes the outputs of the chosen compression passes. Each
output layer uses its producing pass's preimage directory and the DFS bases
of that pass's input and output states. Tags refer to the output state's
producing role, including the final state.


### `terminalHead`

 The last 32 words of the pair's square workspace are the terminal header. 

### `terminalHead_eq_nat`

 The word address equals the natural square-workspace formula whenever
the public address width fits the shift and the 32-word header fits the square. 

### `terminalField`

 Read a terminal-header field at its machine-word offset in the supplied external memory. 

### `levelHead`

 Compute the physical head of level j from the first-level word and the level pitch saved in
the terminal header. 

### `levelField`

 Read a selected level-header field using the terminal header's runtime level geometry. 

### `siteCount`

 The input site's count comes from its first pass, or from the terminal
site count when there are no passes. Later counts come from their producer. 

### `tagParams`

 Assemble the four role-tag parameters from the terminal displacement, current row base, row
pitch, and stored producing role. 

### `leafParams`

 Read the initial row base and row pitch for writing cursor leaf rows. 

### `fiberParams`

 Fiber worker for pass `i` writes the rows of state `i+1`. 

### `Fiber`

 A fiber is the tagged output together with the corresponding raw
placement directory's six public words. 

### `fiberWorkers`

 Chronological translation of tagged output levels into native row workers. 

### `fiberWorkers_at`

 The `i`-th fiber connects states `i` and `i+1`. The last fiber uses
its output state header by precisely the same formula. 

### `rowWorkers`

 The full schedule has one leaf worker before the fiber workers. 

### `Resident`

 Physical header cells for one finished compressor branch. Addresses here
are ordinary natural addresses, independent of the controller's word arithmetic. 

### `RowAt`

 Lookup of a row worker supplies its exact count and public operand bank. 

### `Schedule`

 The controller has one pair of row/tag stages per state level. Every
admitted ordinal selects the exact chronological worker and role. 

### `levelFibers`

 The typed directory list keeps the address of every occurrence of a
selected level, even when two levels have equal mathematical data. 

### `selectedJobs`

 Exactly the worker list executed by the selected traversal-arena build. 

### `selected_schedule`

 Physical fields for the initial state and each selected pass provide all
the operands of the native workers, with the precise chronological schedule. 

### `selected_resident_of_directory_fields`

 Read the public placement words from the real directory for each
occurrence of a selected pass. The count cells are identified with the
mathematical site counts by that directory's old/new count witnesses. 

### `selected_schedule_of_directory_fields`

 The physical directory fields select exactly the workers of the reference
arena construction, including the final output layer. 
