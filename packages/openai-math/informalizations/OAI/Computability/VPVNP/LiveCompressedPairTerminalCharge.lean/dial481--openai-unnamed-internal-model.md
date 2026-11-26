---
{
  "module": "OAI/Computability/VPVNP/LiveCompressedPairTerminalCharge.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveCompressedPairTerminalCharge.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveCompressedPairTerminalCharge.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Communication of the five native terminal stages

The final outgoing-arc prefix scan, tagged history-directory construction,
shared-bit guesses, and vertex evaluations all run on the same selected
network. This calculation includes the closing reports and the two complete
passes over the history directories, including their repeated operand reads.


### `terminalCoefficient`

 Fixed coefficient for the initial header, both row-building passes,
the wire-prefix and shared-bit scans, and all vertex reports. 

### `terminal_source_charge`

 Bound the actual bootstrap, wire-prefix, history-table, final-bit and
per-vertex report lists by the compressed branch's geometric charge. The
history constructor supplies its two-pass charge and the vertex routines
supply their own occurrence-by-occurrence charges. 

### `terminal_source_rows`

 The local cap on the same chronological reports, including both
guard closures and all external reads from the history directories. 
