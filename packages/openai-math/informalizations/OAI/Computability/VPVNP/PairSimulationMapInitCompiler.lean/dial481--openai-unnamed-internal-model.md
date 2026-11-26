---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapInitCompiler.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapInitCompiler.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapInitCompiler.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Register recipes reading the private call descriptor

The existing straight-line recipe compiler assigns disjoint outputs and
reuses a bounded scratch bank. For a map call its loads read private memory
at addresses computed from the live descriptor pointer. Every instruction
therefore contributes one tick and both memories are preserved.


### `memory`

 The recipe evaluator uses natural addresses while the private memory accepts words. 

### `instruction`

 Retarget the compiler's read instruction to the private memory of the current call. 

### `Linked`

 Installation condition for the private descriptor initializer. At each indexed program
counter the machine contains the compiled assignment with the next index as its successor. 

### `native`

 Load a complete finite output vector from a private descriptor. The number of
ticks depends solely on the chosen recipes. Outside registers and all cells survive. 
