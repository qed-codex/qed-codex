---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapDriverFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapDriverFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapDriverFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Register preservation across all selected row calls

The controller can carry an arbitrary collection of exterior registers
through dispatch, the selected row and the label store. A later width check
or histogram flush may therefore use operands prepared before the copy loop.


### `Saved`

 All the saved registers retain their initial words. 

### `OutsideWrites`

 The four registers modified by the driver's own instructions are excluded.
The selected rows supply their own preservation proof. 

### `FramedRows`

 The row contract with a register frame carried from an arbitrary initial state. 

### `FramedRowsWith`

 Exact row calls preserving a chosen exterior register set. 

### `native_framed`

 Both the complete label slice and all exterior operands are available
on entry to the linked final-width checker. 
