---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapHandlerRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapHandlerRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapHandlerRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executing the selected grid and party handler

The family supplies the descriptor writer and map subroutine links for the
grid row and party recorded at this visit. The call consumes only deterministic
events, reaches the common advance address or a real rejection, and preserves
all other handler registers and every cell outside its workspace.


### `uniform`

 All grid and party cases have a common fixed bound for writer probes and a
common linear bound for the full writer and lowered map clock. 
