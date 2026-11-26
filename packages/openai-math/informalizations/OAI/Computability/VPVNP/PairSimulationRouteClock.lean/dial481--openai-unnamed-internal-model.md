---
{
  "module": "OAI/Computability/VPVNP/PairSimulationRouteClock.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRouteClock.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRouteClock.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Clock for the native cursor routing checks

The scheduler visits one successor field per cursor bit and at most one sort
field per phase and step. Each resident word takes at most thirteen ticks.
The processor's bounds on bucket size and word width put the entire scan,
including its field setup and final decision, within the stated clock.


### `scheduler_le`

 The successor loop, nested sort loop and final decision fit within the
routing allowance on both live and virtual processors. 
