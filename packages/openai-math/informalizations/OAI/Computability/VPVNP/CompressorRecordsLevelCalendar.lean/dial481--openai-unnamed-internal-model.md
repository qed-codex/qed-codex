---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsLevelCalendar.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsLevelCalendar.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsLevelCalendar.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Online controller for repeated descriptor phases

The finite controller contains the planner tags for an initial sequence and
for one compression block. On each entry it reads the current ordinal and
the total number of phases. A quotient and remainder recover the current
block and its phase. The controller writes the planner tag and returns the address of the
current block header. The subsequent row launch increments the ordinal.
At the total it accepts. The same finite instruction table serves every block count.


### `Calendar`

 The initial and repeated tags are operands in the program text. 

### `Calendar.initial`

 Planner tags visited once before the first repeated compression block. 

### `Calendar.block`

 Planner tags traversed in order for each repetition of a compression block. 

### `Calendar.rowPitch`

 Words reserved per directory row when locating the level headers after the directory. 

### `Calendar.levelsPerBlock`

 Number of level-header strides from the start of one compression block to the next. 

### `Calendar.size`

 Number of distinct phase slots in the initial sequence and one copy of the repeated block. 

### `Calendar.total`

 Number of scheduled phases for the given block count, including the initial phases exactly
once. 

### `Calendar.phase`

 Convert a chronological ordinal to a finite phase slot, using the remainder within the
repeated block after the initial sequence. 

### `Calendar.level`

 The zero-based block number containing a repeated phase, with initial phases assigned to
block zero. 

### `Calendar.planner`

 The planner tag at a phase slot in the concatenation of the initial sequence and one
repeated block. 

### `PCs`

 Number of native calendar instruction labels, with 31 shared rows and three lookup rows per
phase slot. 

### `literalWidth`

 Enough bits to represent the tags, phase indices, row pitch and number
of levels per block. The level size is read from RAM. 

### `table`

 Finite instruction table that reads the current ordinal, locates its block header and
dispatches its planner, or accepts at the schedule end. 

### `machine`

 Instantiate the level calendar's instruction table at the chosen word width and five public
operands. 

### `closedReport`

 The accepting calendar report after reading the ordinal and total phase count, with no
continuation state. 

### `header`

 Level headers immediately follow the directory with one fixed-pitch row
per ordinal. The planner receives the address of the current header. 

### `dispatchReport`

 Planner tag and current header selected by the cursor calculation. 

### `execute_closed`

 The capacity test consumes two reads and accepts at or beyond the
exclusive bound. Nonempty branch strings are rejected. 

### `execute_dispatch`

 The ordinal selects a planner from the finite program text. The bound, ordinal and level-stride
reads are followed by the planner tag write. The return word points
to the current header for the planner to read on the next call. 

### `recipeCalendar`

 Stage zero launches the row, the next stages are the data workers,
and the calendar follows them. The recipe tags follow the calendar in
initial-then-block order. 

### `execute_active`

 For every block count and every active ordinal the phase index exists.
The read-only phase table has only one copy of the repeated block. 

### `dispatch_effect`

 The selected recipe sees the original ordinal and directory. There are
three reads, one tag write, and zero nondeterministic choices. 

### `dispatch_ordinal`

 The planner can emit row `o` and the row launcher can read that same
row. The launcher subsequently advances the ordinal. 

### `header_address`

 The level pointer is an exact natural RAM address when the header fits.
The word before the directory stores the number of words in one level. 

### `execute_block`

 For each block below the repetition bound, each slot dispatches to
its own compiled recipe and receives that block's header. 

### `execute_at_total`

 When the last row launcher has advanced the ordinal to the prescribed
total, the next calendar call terminates after two reads. 
