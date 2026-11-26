---
{
  "module": "OAI/Computability/VPVNP/PairSimulationTerminalRootGatherCode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalRootGatherCode.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalRootGatherCode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Relocatable terminal endpoint gather

Each incoming slot first reads its matching outgoing slot. Both passes then
read the width and exclusive prefix of that outgoing slot and copy the
corresponding shared wire words to the site's private argument buffer.


### `Reg`

 Symbolic register names shared with the site bootstrap. The gather maps the first nine
names to its own temporaries, the next eleven to saved fields and the final three to DFS
registers. 

### `Line`

 Straight-line instruction format used for the gather's initialization and per-slot
directory reads. 

### `tmp`

 Names one of the nine gather temporaries used for wire addresses, the private destination,
and slot loop bounds. 

### `save`

 Names a bootstrap register from which the gather reads the site ordinal, root, slot counts
or endpoint array heads. 

### `bootLines`

 Twelve instructions that load the private argument stride, compute the root's destination
address and set the first slot, exclusive limit and unit increment for the outgoing scan. 

### `headerLines`

 Reads a slot's width and exclusive prefix to compute its source interval in the wire bank.
The incoming pass first reads the matched outgoing slot from the inverse incidence table. 

### `PC`

 Labels for gather initialization and the two slot scans. Each pass has a loop test,
directory reads, a wire-copy loop and a slot increment, with a cursor reset between passes. 

### `firstHeader`

 Index of the first directory instruction for a slot in the selected scan direction. 

### `blockPC`

 Extends the labels of a straight-line gather block by one position holding its
continuation, so the last instruction can target the next phase. 

### `rows`

 Emits the gather instruction at a symbolic label. The outgoing pass resets the slot cursor
for the incoming pass, which transfers to the supplied continuation after its last slot. 

### `bitRegs`

 Assigns the first five gather temporaries to the endpoint copy loop as source cursor,
exclusive end, destination cursor, unit increment and transfer word. 

### `Linked`

 Requires the machine to contain every gather instruction at its assigned label, with the
specified register bank and final continuation. 

### `regMap`

 Resolves gather register names into the segment's nine private temporaries, the eleven
saved bootstrap registers and the first three host DFS registers. 

### `segment`

 Finite vertex-image segment for gathering the terminal root's endpoint packet. It enters at
initialization and allocates nine private temporaries for both scan directions. 

### `Saved`

 Saved fields read by this segment. The private geometry pointer and
stride are initialized by the previous stage. 

### `Frame`

 Register frame for a gather run. The two configurations agree on the persistent word and on
every register outside the nine gather temporaries. 

### `Prefix`

 For any remaining fuel and choice bits, execution from the initial configuration produces
the given event prefix followed by the continuation from the final configuration on the
same external memory. 
