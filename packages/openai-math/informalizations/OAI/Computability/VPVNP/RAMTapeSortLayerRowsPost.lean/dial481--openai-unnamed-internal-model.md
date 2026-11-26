---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortLayerRowsPost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortLayerRowsPost.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortLayerRowsPost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Installing a record comparison in the row traversal

The partner offset and decision bits produced by the address routine satisfy
the record routine's input conditions. A comparison changes the pending
output, exchange streams and flags. The traversal retains its binary and
unary row indices for the subsequent increment.


### `prepared_ready`

 The address computation has prepared all record operands and scratch stacks. 

### `row_run`

 Install a record routine's execution on the layer ports. The next row
will see the selected record and flags at the heads of their reverse streams. 
