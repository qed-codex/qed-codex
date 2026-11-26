---
{
  "module": "OAI/Computability/VPVNP/CompressorDemandFootprint.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorDemandFootprint.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorDemandFootprint.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# External addresses read by the motif preparation calls

Every successful execution of the demand-energy scan, the repetition program
and the first-cover search probes only the input demand cells. The proof
tracks the energy scan's advancing cursor and the grid's public offsets and
also applies when comparison arithmetic wraps.


### `demandCell`

 Modular address of an actual demand coordinate. 

### `Footprint`

 All external reads target the input rectangle and no external writes occur. 

### `repetitionMachine`

 Every successful native repetition call, at any fuel and choice input,
probes only the demand cells. 

### `gridMachine`

 Every successful native grid call reads within the same input rectangle. 
