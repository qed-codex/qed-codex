---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafIncidentTable.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafIncidentTable.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafIncidentTable.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The fixed instruction image and virtual clock of the incident loader


### `PC`

 Standalone machine states, including the return location. 

### `rowPC`

 Numerical instruction address for an incident-loader label. 

### `returnPC`

 Numerical address of the standalone accepting return. 

### `template`

 The same opcode image is instantiated at every host word width. 

### `ticks_le`

 A numerical bound on the actual native instruction count that is
independent of the four supplied half-wire strings. 

### `ticks_le_of_budget`

 The loader occupies at most a fifth-power portion of the live private
clock for the parameters of the virtual auxiliary processor. 
