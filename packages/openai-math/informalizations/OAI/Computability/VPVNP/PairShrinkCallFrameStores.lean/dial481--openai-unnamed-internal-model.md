---
{
  "module": "OAI/Computability/VPVNP/PairShrinkCallFrameStores.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkCallFrameStores.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkCallFrameStores.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Private geometry through the two shrinking stores

The vertex invariant gives the geometry pointer and the cache, length and
histogram words. Child packets occupy argument slots below the geometry.
Absorbed-wire stores occupy private slots beyond the leaf stacks.


### `of_vertex`

 Read the four live private cells directly from the scratch invariant
carried at each pending vertex. 

### `Stored.children`

 The old children use real nodes below the region's exclusive node
bound, and all of their packet intervals begin above the geometry pointer cell. 

### `Stored.hidden`

 The hidden store starts beyond the entire geometry directory. Its
computed interval fits also cover zero-width absorbed rows. 
