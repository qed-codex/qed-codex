---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapWorkspaceLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapWorkspaceLayout.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapWorkspaceLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Consecutive scratch regions for a native map call

The live histogram and operand fields may be at different addresses from one
call to the next. Above their exclusive ends the caller reserves space for
the port directory, the fixed argument descriptor, the selector ordinals, and
the output labels. The two copy arrays have the same capacity.


### `descriptorBase`

 Reserve the two possible ends of each supply edge before the argument descriptor. 

### `ordinalBase`

 The selector ordinals start immediately after the fixed descriptor. 

### `scratchRegions`

 The label array follows the reserved selector-ordinal array. 

### `scratchEnd`

 Exclusive end of the label array, including its unused reserved capacity. 

### `descriptorWord_lt`

 The descriptor has a distinct address for each argument, strictly before
the first scratch ordinal. 

### `scratchRegions_ordered`

 All writable map arrays are separated for any supplied operand bases whose
ends and the live histogram precede the directory. 

### `scratchWorkspace`

 The natural layout supplies the workspace of the actual native map program,
including all selector-dependent reads on unsuccessful choices. 

### `liveDirectory`

 Above field and histogram starts at most `n ^ 5`, leave room for a payload
of at most `n` bits and every selector suffix of at most `n` copies. 

### `liveWorkspace`

 The same capacity, fixed before the branch, constructs workspaces for all
map inputs of these numerical sizes. No equality of the proposed total widths
with the selected payload is required. 
