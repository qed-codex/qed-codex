---
{
  "module": "OAI/Computability/VPVNP/PairTraversalTerminalBootstrap.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalTerminalBootstrap.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalTerminalBootstrap.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Terminal pair bootstrap after the descriptor calendar

The first and last stored traversal-row bases give the exact accumulated row size.
A single fixed eleven-operand burst reads the persistent level headers and the last
auxiliary descriptor, initializes the terminal header and leaves every other cell intact.


### `operand`

 Workspace base, grammar counter base, address width, auxiliary shadow and grammar length. 

### `shadowSpan`

 The histogram begins after all reserved auxiliary fields, including both padded exterior cuts. 

### `address`

 The terminal bootstrap header begins 32 words before the end of the square workspace of
radix two to the address exponent. 

### `calculation`

 Initialize all twenty-one public terminal header fields. The phase and both counters
start at zero. The final-width pass subsequently supplies the total and role offset. 

### `table`

 The fixed table has no dependence on the input size or the selected compression branch. 

### `cost`

 Native instruction cost of the terminal bootstrap's compiled header calculation at the
chosen descriptor shape and record capacity. 

### `report`

 The bootstrap worker's report contains the calculation's external events and closes without
a successor state. 

### `execute_table`

 The table accepts exactly the empty choice string, from every incoming persistent state. 

### `Header`

 Stored values needed at the calendar's terminal exit. `priorWords` counts all
traversal rows strictly before the final level, with their fixed row stride. 

### `Header.priorWords`

 Total words occupied by all DFS row layers before the final layer. 

### `Header.vertices`

 Number of final base vertices before expanding their lane assignments. 

### `Header.lanes`

 Number of lane assignments per final base vertex. 

### `Header.degree`

 Number of numbered final outgoing slots per site. 

### `Header.widthHead`

 Head of the final outgoing arc-width column used by the terminal prefix scan. 

### `Header.incomingHead`

 Head of the inverse incidence column used to gather the incoming final half-wires. 

### `Header.prefixBase`

 Base address of the terminal prefix array used to locate each final arc's shared bits. 

### `Header.baseRadix`

 Saved initial base radix used by the terminal cursor-leaf decoder. 

### `Header.laneRadix`

 Saved initial lane radix used by the terminal cursor-leaf decoder. 

### `atCell`

 Read the external cell at a natural base and offset after conversion to the runtime word
address. 

### `Ready`

 The physical workspace, level geometry, row counts, final incidence heads, and saved
radices have the values required by terminal bootstrap. 

### `Header.sites`

 Total number of final sites, including every combination of base vertex and remaining lane
assignment. 

### `Header.rowWords`

 Total words reserved for DFS rows, including the final sites at their capacity-plus-two
word pitch. 

### `values`

 The 21 terminal bootstrap header words computed from the descriptor layout, selected final
state, row geometry, and public shadow data. 

### `native`

 The one-shot native table is ready for a terminal phase linker. It performs a fixed
number of probes and ticks and does not use a choice bit. 
