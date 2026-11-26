---
{
  "module": "OAI/Computability/VPVNP/PairTerminalPrefixWorker.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalPrefixWorker.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalPrefixWorker.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Live terminal-prefix instruction table

The terminal header is recovered from the workspace and size exponent in the
eleven public operands. Every active call takes its width and prefix table
heads from that header, advances one arc, and returns the successor ordinal.
The closing call publishes the role-table displacement and accepts.


### `header`

 Terminal header at the high end of the pair workspace. 

### `data`

 Width-array head, prefix-array head, and running-total address loaded from the terminal
header for the prefix worker. 

### `instruction`

 The 41 native instructions that recover the terminal header, process one arc's width, or
publish the closing displacement. 

### `table`

 Resizable terminal prefix worker table, assembled at six-bit word width with entry at
instruction zero. 

### `activeReport`

 Report for arc ordinal i. It writes the current total into that arc's prefix cell, adds the
arc width, and returns the next ordinal. 

### `closeReport`

 Final prefix report that adds the accumulated terminal width to the DFS row count, stores
the role-table displacement, and accepts. 

### `active`

 Exact native execution of the one-arc visit. 

### `close`

 Exact native execution of the terminal role-offset publication. 
