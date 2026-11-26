---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafIncidentLoad.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafIncidentLoad.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafIncidentLoad.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Loading a selected incident field from the four resident cursor arcs

The direction and selected arc are finite control. The source offset, length,
four half-buffer bases and descending destination cursor are runtime words.
An endpoint selects the zero source. The local program never consults a
global wire assignment.


### `baseReg`

 First five operands are shared with the descending field mover, then
length, arc offset, and the two outgoing and two incoming buffer bases. 

### `copyRegs`

 Registers of the field mover inside the incident-loader register file. 

### `mode`

 Select resident input for an available port and zeros at a missing endpoint. 

### `sourceAddress`

 Private address of a field within its half-wire buffer. 

### `prepare`

 The two address setup rows followed by the five-row move loop. 

### `Stored`

 All four resident half-wire arrays encode their declared bits. 

### `Field`

 The selected consecutive bits of one port, or zeros when that port is absent. 

### `Result`

 State and continuation of a completed native field copy. 

### `copy_run`

 Copy or clamp the chosen whole field. This theorem accounts for both
address setup instructions, every bit movement and the terminal test. 
