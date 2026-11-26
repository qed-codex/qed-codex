---
{
  "module": "OAI/Computability/VPVNP/PairSimulationRoutePrepare.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRoutePrepare.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRoutePrepare.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preparing the routing checker from the private DFS arguments

A leaf enters with a decoded cursor, site and descriptor address. Fourteen
instructions copy the coordinates, compute the descriptor's argument base,
and read the three geometry words in the operand cache. Fifteen arithmetic
instructions compute the successor and sorting widths and the four buffer
bases. Every instruction contributes one tick.


### `Field`

 Public pointers to the argument arena and the private geometry cache. 

### `Stage`

 The labels of the operand fetches and the arithmetic sequence. 

### `ticks`

 Number of native private instructions before the first route test. 

### `portBase`

 Host-word address of the first bit of a stored half-wire. 

### `instruction`

 The leaf, route and public banks can be embedded at any host indices. 

### `Linked`

 Every setup instruction is present at its designated machine label. 

### `Ready`

 Native operands at entry, after the leaf address decoder. 

### `resident_of_stored`

 Word addresses used by the checker read the four consecutive packet intervals. 

### `resident_cursorPacket`

 After a stored DFS packet, the checker reads its independently supplied
half-wire bits. The DFS stack below the scratch boundary can have arbitrary contents. 

### `run`

 The linked code enters the scheduler with all coordinates, widths and
private bases initialized and preserves every register outside its routing bank. 
