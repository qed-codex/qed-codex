---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackEngineRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackEngineRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackEngineRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Execution and space of the physical Schur continuation control 

### `runSpace`

 The call-stack cap counts the nested tagged field strings in each history.
One bounded transition accounts for the private working space between calls. 

### `eval_run`

 Transfer a capped abstract execution to the finite bit-stack program. 

### `eval_root`

 Run the supplied matrix coefficient query from its root to a native scalar
on the output port. The entire physical return stack has been emptied. 
