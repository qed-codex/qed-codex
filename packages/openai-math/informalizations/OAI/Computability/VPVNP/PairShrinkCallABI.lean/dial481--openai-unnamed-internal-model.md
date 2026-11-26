---
{
  "module": "OAI/Computability/VPVNP/PairShrinkCallABI.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkCallABI.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkCallABI.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Register operands of a selected shrinking map

The locator keeps the old header and the popped node. After the hidden pass
the shared registers also hold the geometry pointer, histogram and the start
of the scratch beyond the leaf verifier stacks. The resident scan supplies
the selected motif ordinal. All descriptor expressions use these six live
words and the external level metadata.


### `hiddenBase`

 First private address after all stacks of capacity `n^40`. 

### `live`

 Register readback for the descriptor and both kinds of gather. The node
arena stride and the hidden slot stride are computed from metadata cell 17. 

### `supply_readback`

 The surviving half-address expression indexes the popped node from the
locator. Its destination is the same surviving interval used by the map. 

### `operand_reads`

 The only external probe in the six live register operands is the
published length at offset 17. 

### `length_published`

 The third DFS payload word copies the original problem length into
the old-level header actually selected by the locator. 

### `length_after_heads`

 The four term and fourteen data-head stores preserve the metadata length
used on entry to the map. 
