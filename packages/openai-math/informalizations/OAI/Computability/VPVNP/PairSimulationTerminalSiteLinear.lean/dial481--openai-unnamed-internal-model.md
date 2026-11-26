---
{
  "module": "OAI/Computability/VPVNP/PairSimulationTerminalSiteLinear.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalSiteLinear.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalSiteLinear.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Straight-line rows for initializing a final site's private DFS stack 

### `Reg`

 Logical registers for the terminal-site entry code, partitioned into nine DFS slots, eleven
saved bootstrap slots and three working slots. 

### `dfs`

 Selects a DFS register in the site-entry bank. The bootstrap uses this bank to set the
stack top and end for the pending root visit. 

### `saved`

 Selects a bootstrap register holding values needed by later stages, including the site
ordinal, root descriptor and endpoint table addresses. 

### `work`

 Selects one of the three working registers available for intermediate site-entry
calculations such as header offsets and the root row address. 

### `Line`

 One straight-line operation on the symbolic site-entry registers. Operations include public
and state inputs, word arithmetic, external reads and private loads or stores. 

### `Line.emit`

 Translates one symbolic line to a native RAM instruction using the supplied physical
registers, public ports and successor label. 

### `eval`

 Evaluate a straight-line fragment with the same address reads and private stores as the RAM. 

### `linear_walk`

 Execute the emitted rows at arbitrary labels, leaving the live bank and
private memory computed by `eval`. 
