---
{
  "module": "OAI/Computability/VPVNP/PairTerminalPrefixBudget.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalPrefixBudget.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalPrefixBudget.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Communication budget of the live terminal-prefix worker

The final outgoing directory has one entry for each slot of each final site.
The prefix stage visits exactly those entries and makes one closing call.
Including fixed linker costs on every call, these reports fit every positive
fraction of the live group's communication allowance uniformly over branches.


### `arc_count_positions`

 The physical outgoing-arc directory has one entry for each site and slot. 

### `eventually_budget`

 A common size threshold gives both the per-burst allowances and the
total charge bound, including the linker margin on the closing report. 
