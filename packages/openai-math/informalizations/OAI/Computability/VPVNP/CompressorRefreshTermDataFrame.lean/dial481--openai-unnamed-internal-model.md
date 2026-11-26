---
{
  "module": "OAI/Computability/VPVNP/CompressorRefreshTermDataFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshTermDataFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshTermDataFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Scheduler frames for the refresh demand, supply and expander-ROM workers

These three passes read and write inside the packed refresh allocation.
A single tie pass preserves every previously completed demand cell. Supply
visits preserve the term records and advance the supply prefix. Each fixed
ROM row starts at its own edge ordinal and fills the two reverse-edge cells.


### `InArena`

 Addresses from the refresh allocation's start inclusive to its stop exclusive. 

### `Scan`

 The two premises a concrete deterministic source supplies to the guarded
scheduler scan. Native entry is required only at the actual active ordinals. 

### `demandScan`

 One tie's native scan and the exact prefix invariant for all earlier
ties and blocks. Its only read is from a segment column and its only store
lies in the dense demand array. 

### `demand_trace`

 Replay evidence for an actual tie stage, without any prepared scheduler
frame. Its input memory may contain the results of any earlier stages. 

### `supplyScan`

 The actual term-operand reads stay below the selected supply column.
Therefore later visits retain their source values while earlier output
rows stay intact. 

### `supply_trace`

 Replay evidence for the whole dense supply column. 

### `romScan`

 Publication of the two reverse-edge cells for one fixed ROM row. 

### `rom_trace`

 The hardwired ROM stage has exactly one source report, even when its
initial edge ordinal is positive. 
