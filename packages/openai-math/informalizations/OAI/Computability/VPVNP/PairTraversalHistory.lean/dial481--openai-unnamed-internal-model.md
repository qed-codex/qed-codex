---
{
  "module": "OAI/Computability/VPVNP/PairTraversalHistory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalHistory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalHistory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Placement histories in the native descriptor traversal

On each selected shrinking or refresh term, the children of an output
vertex are exactly the placed old vertices, in the actual reader's order.
The following construction retains these vertices recursively down to
the routed cursor input. The depth-first code visits the resulting tree
in that order, using the stored row addresses of the selected stages.


### `RowPointers`

 The header address and child-list pointer at each stage of a chosen history. 

### `rowsAt`

 Child IDs in the stored order, with their absolute addresses in the preceding layer. 

### `leafTree`

 A cursor leaf tree with the supplied node and source pointers and an empty family of
children. 

### `chainTrees`

 Build the selected final vertex tree by following each term's actual
finite placement fibers. The initial vertices may already carry subtrees. 

### `chainTrees_length`

 Every visit consumes one of the vertex occurrences counted in
Theorem 7.1. Field and map occurrences may increase that count further. 

### `leafTree_rows`

 The cursor leaves have an empty list in the first descriptor layer. 

### `selectedTraversal`

 On every selected branch, the native DFS log reads at most three
words and uses at most fifteen word instructions per vertex occurrence,
plus the empty-stack test. The ordered node sequence is the actual
placement tree of that branch. 
