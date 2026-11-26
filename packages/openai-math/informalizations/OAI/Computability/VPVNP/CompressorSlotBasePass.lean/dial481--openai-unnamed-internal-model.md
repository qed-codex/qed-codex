---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotBasePass.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotBasePass.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotBasePass.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Scanning two output tables of the compressed base graph

The worker at cursor `i` writes the destination base arc and lane displacement
into separate tables. Outside their completed prefixes, all input words retain
their initial values. This lets one lift a single native call to a full scan
with an exact calls-plus-probes count.


### `Visit`

 Execution of one call under the frame left by all preceding calls. 

### `FilledRun`

 The two completed tables, persistent state, and resource use of a scan. 

### `run`

 Successive calls fill both disjoint output intervals in cursor order. 
