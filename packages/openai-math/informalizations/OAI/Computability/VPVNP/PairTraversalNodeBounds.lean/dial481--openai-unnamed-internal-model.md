---
{
  "module": "OAI/Computability/VPVNP/PairTraversalNodeBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalNodeBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalNodeBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Addresses of the selected placement trees

The leaf and intermediate layers occupy consecutive row intervals in increasing
stage order. Every header read in a final vertex's preorder lies below the end
of these layers. A stored child pointer recovers the exact address of its row
in the preceding layer when the table fits in memory.


### `endPos_fold`

 Advancing the base through the same rows as the builder gives the sum
of the preceding layer sizes. 

### `layerNode_bounds`

 Every row in a layer after the preceding layers has its header inside the
allocated descriptor interval. 

### `Layer.ChildrenIn`

 The site identifiers of the later layer are row indices in the earlier layer. 

### `chainLayers_childrenIn`

 The child-index range property holds at every pair of consecutive selected layers. 

### `childWords_val`

 Reading a row's child pointer words gives exactly the preceding-layer
row addresses in order, including when the row has no children. 

### `chain_childWords_val`

 Specialize exact child pointer decoding to any consecutive layers in
the actual parser chain, without assuming a bound on the raw child indices. 

### `chainTrees_below`

 The precise upper end of the forest after storing the remaining stages. 

### `chainForest_below`

 Start the forest with one leaf at each actual initial site. 

### `selectedTrees`

 Actual placement trees visited after building this branch's row directory. 

### `selectedTrees_below`

 Every visited node lies strictly below the exclusive end of the actual
descriptor region of the selected branch. 
