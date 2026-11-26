---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapOffsets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapOffsets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapOffsets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Advancing the field offsets of one decoded motif copy

Each selected base profile supplies one fixed width for each demand or supply
group. Loading its public width and adding it to the group's offset takes two
private instructions. The finite group list is part of the fixed template.


### `code`

 Load each listed group's public width into `tmp` and add it to the group's offset. 

### `native`

 After one pass over distinct groups, their offset registers contain the
old value plus the selected public width. Registers outside the group list
and the scratch register retain their original values. 
