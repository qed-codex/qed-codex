---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafFieldCopy.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafFieldCopy.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafFieldCopy.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Moving a logical-order half-wire field into a private bit stack

The selected half-wire is stored in increasing logical order. A stack grows
upwards with its first logical bit at the highest occupied address. This
fixed five-row fragment therefore advances the source and retreats the
destination. Missing chain endpoints use the same loop with a zero source.


### `word`

 Encode a natural address in a machine word. 

### `Source`

 Read a resident half-wire cell or supply the clamped zero bit. 

### `Source.value`

 Word returned by this source at the current cursor. 

### `instruction`

 Source cursor, destination base, exclusive destination cursor, unit, temporary. 

### `Linked`

 The host instruction table contains the five-row descending copy loop. 

### `place`

 Write a bit list into private stack memory with its head at the highest address. 

### `Result`

 Exact native result, with the unrelated registers and cells framed. 
