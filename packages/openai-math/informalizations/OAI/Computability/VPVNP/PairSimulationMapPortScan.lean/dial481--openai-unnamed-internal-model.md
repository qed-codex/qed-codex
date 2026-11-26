---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapPortScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapPortScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapPortScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A private directory scan comparing all incident selector fields

Each directory cell points to the beginning of a port's selector suffix.
The enclosing loop reads that pointer and compares the suffix to the same
anchor, carrying the difference mask across ports. The anchor and directory
may overlap any of the input fields because every memory access is a read.


### `innerRegs`

 The comparison loop uses the first seven of the directory scanner's registers. 

### `instruction`

 Registers 7 through 10 hold the directory cursor, its exclusive end,
the first selector bit of the anchor, and the common selector length. 

### `Linked`

 The fixed outer code invokes the same inner loop for every directory entry. 

### `Preserved`

 The port-directory scan writes the directory cursor and six inner-loop registers. 

### `Agrees`

 All words of every selected slice equal the corresponding words of the anchor. 

### `run`

 The loop walks the pointer table and branches to its declared success
or failure label. Its fixed trace length applies on malformed words too. 
