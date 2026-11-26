---
{
  "module": "OAI/Computability/VPVNP/PairTraversalSelectedOrder.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalSelectedOrder.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalSelectedOrder.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The order of placement fibers throughout a selected compressor branch

The shrink and refresh readers both enumerate children in the numerical order
of the preceding state. Joining procedures and repeating the compression block
preserve these orders along each branch of the selected kernel history.


### `OrderedChildren`

 Every child list uses the restriction of the numbering at its input layer. 

### `PassOrders`

 The local descriptor uses the actual child, outgoing, and incoming orders of its source state. 

### `ExecutionOrders`

 Orders at all stages and all choices of this execution. 

### `execute_readerOrders`

 The actual slot orders on both sides of every visit, through all
repetitions of the shrinking and degree-refresh block. 

### `selectedParsers_ordered`

 In the actual repeated compressor, each local reader visits old positions in the
same order as a scan by their numerical identifiers. 
