---
{
  "module": "OAI/Computability/VPVNP/PairTraversalRootAddress.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalRootAddress.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalRootAddress.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Root row of a selected placement tree

The selected tree ends at the row numbered by its final state's site order.
The terminal bootstrap publishes the base of that layer and its row stride
in header cells 6 and 15. Their native multiply-add recovers the same address.


### `selectedTrees_address`

 Every final site has its root in the last row layer at its actual numerical ordinal. 

### `selectedTrees_address_ofHeader`

 The terminal gather computes the selected root using the live last-layer base
and row stride. Fit of the selected arena suffices for the native multiply-add. 

### `selectedTrees_address_ofBootstrap`

 The physical header fields published by the selected terminal bootstrap supply
both address operands of the root gather. 

### `VertexEntry.gather_root`

 At the physical vertex entry, the root gather reads the row for the
selected final site from the bootstrap fields preserved by the linked stages. 
