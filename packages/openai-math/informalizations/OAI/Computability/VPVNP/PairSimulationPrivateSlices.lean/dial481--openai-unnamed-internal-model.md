---
{
  "module": "OAI/Computability/VPVNP/PairSimulationPrivateSlices.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationPrivateSlices.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationPrivateSlices.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading slice records inside a final-site call

The setup reads the length at frame address plus two before using either
offset. A positive length selects the source and target offset reads,
adds these to the supplied private field bases and enters the copy loop.
An empty intersection returns immediately.


### `instruction`

 Registers 0–4 share the copy-loop ABI. The sixth register is the
external address of the first offset and is preserved. 

### `Linked`

 The machine contains the eleven slice-setup instructions that check the length, return for
an empty slice, or apply both offsets and enter the copy loop. 

### `copyRegs`

 Restrict the slice-setup register allocation to the first five registers shared with the
private copy loop. 

### `headerEvents`

 Exact header trace. Empty records read only the length cell. 

### `ReadPrefix`

 The header contains local instructions and external reads only. 

### `HeaderResult`

 The header exit and its copy operands. On the empty branch the offsets
need no values, so the input field bases stay available. 

### `execute_header`

 Execute the length-first header read and pass the resulting registers to
the linked copy or to the empty-slice continuation. 

### `frameEvents`

 A zero-length frame returns directly. A nonempty frame also executes
the full private-copy loop after its three header reads. 

### `execute_frame`

 Read a completed frame and copy its declared bits. Fit, source contents
and forward-copy overlap conditions are needed only for positive lengths.
Outside its destination interval the entire private memory is preserved. 
