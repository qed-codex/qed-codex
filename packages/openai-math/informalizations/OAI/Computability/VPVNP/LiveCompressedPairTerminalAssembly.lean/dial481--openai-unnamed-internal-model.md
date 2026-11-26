---
{
  "module": "OAI/Computability/VPVNP/LiveCompressedPairTerminalAssembly.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveCompressedPairTerminalAssembly.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveCompressedPairTerminalAssembly.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The compressed pair with the five-stage terminal table

For each selected descriptor branch, the genuine terminal program runs on
the online stage's transferred memory. Its deterministic setup, shared-bit
scan and per-site witnesses give a single branch-indexed equivalence for the
complete eleven-word pair table and its actual dense-counter readback.


### `terminal_tag_fits`

 The outer table already separates enough word values for all 32
terminal-header offsets. 

### `terminal_clock_fits`

 Both nested dispatches leave the private clock needed for the shared
bit phase, including its bounded source-to-physical replay. 

### `terminalBody`

 The static five-worker program for the particular fixed pair. 

### `TerminalBranchData`

 A selected terminal execution uses three forced metadata stages, then a
shared arc phase and a vertex phase for that specific arc assignment. 

### `TerminalBranchData.setup`

 The deterministic terminal prefix on the selected online path's post-memory. 

### `TerminalBranchData.bitPaths`

 The equivalence between the mathematical shared-wire scan paths and the terminal prefix's
  native bit paths. 

### `TerminalBranchData.vertexPaths`

 For each shared-bit path, the equivalence between the sites' witness choices and the
  native vertex paths on that assignment. 

### `TerminalBranch`

 The terminal setup, shared-bit paths, and vertex-path evidence specialized to one selected
descriptor path. 

### `terminalPaths`

 Identify the mathematical terminal data of a descriptor choice with accepted executions of
its actual terminal program. 

### `PhysicalStages.reindexTerminal`

 Combine startup, descriptor choices, and terminal witnesses to identify the full emitted
index with a raw accepted pair path. 
