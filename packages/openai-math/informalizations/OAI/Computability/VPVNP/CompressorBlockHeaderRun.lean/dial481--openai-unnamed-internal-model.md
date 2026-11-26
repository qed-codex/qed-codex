---
{
  "module": "OAI/Computability/VPVNP/CompressorBlockHeaderRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockHeaderRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockHeaderRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Chronological publication of selected compressor level headers

The input header of each substep begins in terminal format. The first visit
relabels it in place using the selected pass. The second visit computes the
output state's terminal scalars. The third visits the new header and writes
its incidence and table pointers using the initial level's capacities.


### `header`

 The machine-word address of the start of level `i`. 

### `scalarPorts`

 Public operand bank for a scalar publisher, with the destination header in operand zero. 

### `headPorts`

 Public operand bank for the pointer publisher, carrying the destination header and the
first level header. 

### `published_of_present`

 The pass origin identifies the lane count remaining in the actual output
state. This converts six natural scalar loads to the consumer's typed header. 

### `scalarReport`

 Report of the native six-scalar publisher. Its result is the next cursor
relative to the supplied source, even when source and destination coincide. 

### `headReport`

 The pointer publisher's report for level `i`, evaluated at cursor zero in the supplied
memory. 

### `HeadsRun`

 Physical effects of the incidence/table pointer visit. 

### `inputRow`

 Scalar formula converting the input's terminal header to the selected pass's header format. 

### `outputRow`

 Scalar formula advancing from the selected pass's header format to the successor's terminal
format. 

### `inputMemory`

 Memory after relabeling the input level's scalar header in place. 

### `outputMemory`

 Memory after the input relabel and the publication of the successor's terminal scalars. 

### `finalMemory`

 Memory after both scalar visits and the successor's incidence and table pointer
publication. 

### `Substep`

 All three reports execute with the actual post-memory of their predecessor.
The published input fields express the selected pass, and the output's terminal
fields can serve as the input of the next substep. 

### `Substep.before`

 All completed earlier levels and the schedule directory keep their exact
word values throughout this three-visit substep. 

### `Substep.firstScalarTail`

 Immutable scalar cells beyond the six mutable fields survive all three
visits. These include the saved parameter bank and the arena-base word. 

### `Substep.cursorFrame`

 The original eight cursor parameters stay available at the first header
even when the current substep relabels level zero itself. 

### `reports`

 The three chronological reports for a selected substep, each computed from the preceding
visit's output memory. 

### `initialMemory`

 Memory after the level-zero scalar publisher reads the cursor frame and initializes the
first header. 

### `initialFinal`

 Memory after the initial scalars and level-zero incidence and table pointers have been
published. 

### `Initial`

 The first two raw workers in the initial calendar sequence. They install
level zero's terminal scalars and heads and retain its eight cursor parameters. 

### `rawCall`

 Evaluate the actual visit's operand bank and starting cursor, then enter
its native worker. All operand expressions use this visit's entry memory. 

### `Substep.visits`

 The three native executions use exactly the public operands and cursors of
the compiled block plan. The two directory control cells lie before the level
headers and survive the preceding raw visits. 

### `Initial.cursor`

 After the two initialization reports, the third visit reads the eight
immutable parameter words from the first header. Its bound and its eleven
public operands are exactly those of the native cursor-incidence scan. 

### `OneCall`

 A one-call deterministic source scan in the compiled visit's own operand
bank. The report and the memory for its successor are retained by SourceWalk. 
