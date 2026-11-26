---
{
  "module": "OAI/Computability/VPVNP/PairTraversalCost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalCost.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalCost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native depth-first visits of an ordered placement tree

A node stores the absolute address of its descriptor and the address of
its ordered child list. Visiting a forest pushes the listed children ahead
of the pending suffix. The total number of child reads is the number of
non-root nodes in the forest, even if some addresses recur.


### `VertexTree`

 One node of an actual local expansion, with its ordered placement fiber. 

### `address`

 The absolute DFS node address stored at the root of this selected vertex tree. 

### `preorder`

 All descriptor addresses in the order visited by the downward-growing stack. 

### `rows`

 Contents of the native descriptor table, including the pointer and
count of an empty child list at each leaf. 

### `visits`

 The fixed native traversal executes the serialized placement tree, in
the selected order, in a stack with one word per node. 

### `Visits.cost`

 The DFS control code reads two header words per visit and one word
per child. Its event length also includes the pop, loop, and stack-copy
instructions, and the final empty-stack test. 
