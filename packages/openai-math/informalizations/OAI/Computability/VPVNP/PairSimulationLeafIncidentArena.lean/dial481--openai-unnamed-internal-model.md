---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafIncidentArena.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafIncidentArena.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafIncidentArena.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Supplying the four private half-wire buffers of a DFS node

The parent stores one packed array at the interval indexed by the
descriptor address. The loader reads its four occupied arc slots in
their numerical order. Initializing other stack ports preserves these
cells when the node arena and stack arena are disjoint.


### `sourceBase`

 The four source addresses inside the selected node's private argument packet. 

### `stored_after_scalars`

 Scalar stack initialization leaves every independent half-wire bit
available at its original node-arena address. 

### `stored_leaf`

 A stored packet read from DFS scratch remains valid in the represented
scalar bank that immediately precedes the incident copy. 

### `stored_leaf_regions`

 In the physical regions of a leaf the whole argument packet precedes
every stack, so its bits survive scalar initialization without a per-port
separation hypothesis. 
