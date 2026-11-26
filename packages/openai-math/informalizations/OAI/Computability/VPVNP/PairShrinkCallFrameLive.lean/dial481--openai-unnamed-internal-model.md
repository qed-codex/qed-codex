---
{
  "module": "OAI/Computability/VPVNP/PairShrinkCallFrameLive.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkCallFrameLive.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkCallFrameLive.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Shrink-map operands from the native private geometry

The terminal startup stores the pointer at the live length and the cache,
length and histogram at offsets 8, 9 and 11. The hidden handoff and the map
reload use these four cells, possibly at different points of the traversal.


### `Stored`

 Private geometry read by the two native handoffs. 

### `of_fields`

 Both the startup `Result` and the geometry segment's `Ready` expose
this pointer and the twelve fields in its actual outgoing private memory. 

### `of_run`

 Concrete initial private geometry of a completed frame program. 

### `of_readback`

 Rewrite the runtime region to the selected terminal row layout. 

### `Stored.transfer`

 Only the geometry pointer and its three live fields need to survive the
private packet writes between startup and the handoffs. 

### `handoff`

 Reading the geometry in the hidden handoff and then in the map reload
sets the two concrete registers required by the party publication theorem. 
