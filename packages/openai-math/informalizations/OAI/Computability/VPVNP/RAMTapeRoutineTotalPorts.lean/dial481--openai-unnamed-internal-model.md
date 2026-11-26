---
{
  "module": "OAI/Computability/VPVNP/RAMTapeRoutineTotalPorts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeRoutineTotalPorts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeRoutineTotalPorts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# All-branch stopping bounds for framed stack routines

Installing an injective port map preserves each stack transition and both branches of every
choice. The same residual fuel is passed to the continuation, with the local outputs written
back into the caller's untouched frame.


### `allStopsFrom_onPorts`

 Transport the continuation predicate through the installed ports, at any control label. 

### `allStops_onPorts`

 The local machine starts with exactly the caller's stacks at its named ports. 
