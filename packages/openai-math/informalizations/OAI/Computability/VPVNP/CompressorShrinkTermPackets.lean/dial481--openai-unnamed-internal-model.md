---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkTermPackets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkTermPackets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkTermPackets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The two term-selection packets in the shrinking block calendar

The ordered packets correspond to the actual gather and selection visits
of the block planner. Each packet records the source program, complete
branch tapes, successor ordinals, and external read and write bounds.


### `Stage`

 The two native stages of term preparation, gathering AB/CD demand widths and selecting a
term for each motif. 

### `order`

 Run the demand gather before the term selector so the selector sees the completed dense
pairs. 

### `visit`

 The planned gather or selector visit at its position in the shrinking substep's term
window. 

### `bank`

 The public operands of the demand gather or motif selector, using the actual pair bank or
the dense demand and term-table heads. 

### `choices`

 An empty tape per gather row, or the encoded selected term's tape per dense motif for the
selector. 

### `source`

 Running the selected worker with its physical bank from cursor zero on the given tapes
yields the indicated reports. 

### `readable`

 The allowed external read region for gathering demands or reading the dense demands and
selected term records. 

### `writable`

 The gather's output pair region or the selector's ten-word term rows, according to the
phase. 

### `probeRate`

 The per-motif probe bound for a term packet, four for gathering or the term-reader bound
for two demands and eight supplies. 

### `PacketRun`

 The physical gather or selection run with its tapes, cursor sequence, motif report count,
memory footprint and probe bound. 

### `packets`

 The calendar's actual visits form one chronological two-packet
execution. The final snapshot retains the graph input, all six sorted
columns, and the selected descriptor of every motif. 
