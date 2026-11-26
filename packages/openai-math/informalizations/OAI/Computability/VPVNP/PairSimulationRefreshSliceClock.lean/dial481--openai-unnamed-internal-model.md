---
{
  "module": "OAI/Computability/VPVNP/PairSimulationRefreshSliceClock.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRefreshSliceClock.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRefreshSliceClock.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading and copying external segments at a refreshed port

The refresh directory stores widths and offsets in separate columns. Both local
directions use the same native copy code with their own column bases. Its six setup
instructions address the columns, read the interval and prepare the private copy.
The final loop test is executed even for an empty segment.


### `instruction`

 Registers 0–4 use the private-copy ABI. Registers 5–7 hold the segment
ordinal and the two directory column heads. 

### `Linked`

 At the six supplied program counters the machine executes the refreshed segment's setup,
reading width and offset from their columns and entering the private copy loop. 

### `copyRegs`

 Restrict the segment setup's eight-register allocation to the first five registers used by
the private copy loop. 

### `headerEvents`

 The six setup events for one refreshed segment, including reads at the width and offset
column heads plus the segment ordinal and the values returned there. 

### `segmentEvents`

 Trace for one refreshed segment from its two directory reads through the last copy-loop
test. It costs seven events plus five per bit and makes exactly two external probes. 

### `execute_header`

 Read the two actual cells and prepare the source, destination and end operands. 

### `execute_segment`

 Exact native run for the independently supplied half-word at one port. 

### `portTrace`

 Physically addressed traces for all segments in either local direction, including
the diagonal port. The bit index type is the length word read from that direction. 

### `execute_port`

 The native copy consumes the physical interval addressed by the port trace.
The header ABI takes the two column heads and the source-major port ordinal. 

### `incident_clock`

 The refresh kernel takes the outgoing and incoming segments independently. 
