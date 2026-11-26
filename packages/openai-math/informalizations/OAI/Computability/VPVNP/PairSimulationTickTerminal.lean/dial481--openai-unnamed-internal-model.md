---
{
  "module": "OAI/Computability/VPVNP/PairSimulationTickTerminal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTickTerminal.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTickTerminal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Uniqueness of the tick count at a terminal instruction

Starting at the same native configuration, two runs consisting entirely of
local ticks take the same number of ticks to reach a terminal instruction.


### `ticks_terminal_unique`

 Two tick prefixes from one configuration that end in rejection or a
finished call have the same length and the same terminal configuration. 
