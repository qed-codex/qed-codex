---
{
  "module": "OAI/Computability/VPVNP/CompressorSourceLaunch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSourceLaunch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSourceLaunch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The physical launch certificate for the current script phase 

### `evaluated`

 Actual stage operands depend on the current memory. Choice strings and
the worker's private clock are supplied by the source scan. 

### `launch_of_evaluation`

 Public field evaluation is all that a typed source stage needs to supply
to identify its computed runtime launch. 

### `worker_eq_phase`

 A valid row at a script visit has the worker tag selected by that visit.
This equality is recovered from the prepared memory even when the source scan
is empty. 
