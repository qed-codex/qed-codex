---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapHandlerFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapHandlerFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapHandlerFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The physical map handler preserves the DFS stack and role registers

All writable arrays of a prepared map call start above the exclusive end
of the saved stack. Successful visits therefore update only the upper scratch
according to the exact action. Unsuccessful visits execute to a rejecting opcode.


### `Bounds`

 Numerical placement of every interval written by the handler. 

### `Prepared.action_native`

 Run the exact action on the saved scratch. The caller receives its complete
register banks and the lower stack prefix, alongside the actual histogram readback. 
