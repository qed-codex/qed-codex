---
{
  "module": "OAI/Computability/VPVNP/PairTraversalRoles.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalRoles.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalRoles.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Routing local vertex visits by their actual compressor pass

A cursor input is visited as a leaf. Each later descriptor belongs to the
output of a particular selected shrinking or refresh pass. Its tag comes from
that pass's origin before the state and its term are erased to a history.
The resulting tagged layers retain the same order and placement fibers as the
selected local parsers used by the native depth-first traversal.


### `Role`

 The three cases of a vertex visit. 

### `Role.code`

 Numerical DFS dispatch tag, assigning zero to a cursor leaf, one to a shrink, and two to a
refresh. 

### `TaggedLayer`

 Row identifiers and the visit operation for one layer. 

### `TaggedLayer.layer`

 The selected DFS layer of site rows and their child ordinals. 

### `TaggedLayer.role`

 Producing role used to dispatch visits to the rows of this tagged layer. 

### `layerBase`

 Header bases in the tag table use the exact prefix of selected output sizes. 

### `Reads`

 Tags live at a fixed public offset from descriptor headers. 

### `ofOrigin`

 Pattern-match on the actual scheduled pass, including its input state and
proof that it is the corresponding shrinking or refresh operation. 

### `tagLevel`

 Recover a selected output layer's role from the origin of its elementary compression pass. 

### `selected`

 One tag per physical layer. The initial layer is the cursor. Subsequent
layers are indexed by the real, branch-specific `SelectedLevel` records. 

### `selected_layers`

 Dropping just the tag gives precisely the layers consumed by the selected
parsers, including every old-site identifier in the order of the true fiber. 

### `reads_selected_level`

 Reading a concrete output tag routes to the selected shrink or refresh pass
that supplied that position's kernel reader. 

### `reads_cursor`

 The cursor leaves always select the initial-vertex reader. 
