---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotFinish.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotFinish.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotFinish.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Building the selected shrinking state's incidence directory

One native run produces the sorted endpoint and base tables. The following
three scans invert and lift the base matching, and a final scan gathers the
selected split widths. All six output columns use the exact canonical port
numbers of the next compressor state.


### `Passes`

 Reports for the nine passes that build the endpoint tables, lift the base matching, and
gather the next state's widths. 

### `Passes.slots`

 Reports for the five passes that order endpoint fields and recover the base matching and
  displacements. 

### `Passes.mates`

 Reports for inverting the base matching and writing the two directions of actual port
  incidence. 

### `Passes.widths`

 Reports that gather the selected split widths for actual outgoing slots, including zero
  widths for dummy slots. 

### `Passes.all`

 All slot, mate, and width reports in the order their workers execute. 

### `Passes.final`

 Memory after applying the slot passes, the mate passes, and the final width scan. 

### `Passes.Native`

 The three groups of reports arise from native slot, mate, and width executions on
successive memory states. 

### `Passes.Cursors`

 The slot and mate scans reach their prescribed stops and the width scan returns the actual
port count. 

### `from_prepared`

 All nine passes on a prepared shrinking level. The final representation
feeds the ordinary incidence API and retains the source arrays. 
