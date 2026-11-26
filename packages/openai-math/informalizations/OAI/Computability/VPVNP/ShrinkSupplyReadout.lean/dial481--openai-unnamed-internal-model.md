---
{
  "module": "OAI/Computability/VPVNP/ShrinkSupplyReadout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkSupplyReadout.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkSupplyReadout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading a surviving motif word at its two packed sites

The subdivisions of a surviving wire occupy numbered outgoing arcs at its
source and numbered incoming arcs at its target. Each of the two packed
sites can reconstruct the original word from its own half-wire fields.


### `ShrinkIndex`

 Numbering for the surviving subdivisions and cyclic padding slots. 

### `shrinkOutput`

 The output word network on the numbered lifted arcs of a shrinking step. 

### `localSurvivingSource`

 Concatenate the genuine outgoing slices at the packed source role. 

### `localSurvivingTarget`

 Concatenate the same genuine slices at the packed target role, reading
the incoming half of each arc with its actual lane translation. 

### `localSurvivingSource_eval`

 The local outgoing readout recovers the original motif word. 

### `localSurvivingTarget_eval`

 The local incoming readout recovers the same original motif word. 
