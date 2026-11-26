---
{
  "module": "OAI/Computability/VPVNP/PairSimulationTerminalSplit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalSplit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalSplit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Recovering each terminal stage from an accepted native traversal

Split at the first accepting exit of the currently selected worker.
A worker return stays within the same stage with its exact returned word.
The split preserves the remaining DFS calls, their memory and their bit
strings. Away from the two controller cells the recovered worker can be
replayed as an ordinary RAM segment.


### `Phase`

 All calls of one worker up to and including its accepting exit. 

### `Phase.source_segment`

 Recover the completed original worker, with every header transfer
removed from its output memory and every genuine branch string retained. 
