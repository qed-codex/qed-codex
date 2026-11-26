---
{
  "module": "OAI/Computability/VPVNP/SlotGreedyScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotGreedyScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotGreedyScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The indexed greedy scans for Appendix C

An indexed base admits deterministic choices of all colors and offsets.
Each scan visits the base in increasing index order. It stores one label
per vertex and selects the first index outside the bounded list of
forbidden values at that vertex. The two scans provide the first local
record construction in Appendix E of *VP and VNP differ over every field*.


### `tagIncrement`

 The list of increments in Appendix C's `Lₓ`: zero and the tag
displacements of all the outgoing slots. Repeated values are harmless. 

### `ValidTagOffsets`

 The tag exclusions imposed at both incidences of each arc in Appendix C. 

### `firstMissing`

 Take the least candidate index absent from the forbidden list. 

### `orderedUpdate`

 One visit updates just the selected vertex of the partial label table. 

### `colorForbidden`

 The colors currently stored at the outgoing and incoming neighbors of a vertex, indexed by
direction and slot number. 

### `chooseColor`

 Least permissible color at a vertex of a partially filled table. 

### `orderedColor`

 Select a proper coloring by visiting the indexed base once, reading
only colors at the two lists of neighboring endpoints. 

### `TagTests`

 Indices for the forbidden-tag tests, recording an incident arc and either one local
increment or a pair of endpoint increments. 

### `tagForbidden`

 Compute the excluded tag for one incident-arc test from its displacement and the specified
increments, using the neighboring tag assignment in the two-endpoint case. 

### `chooseTag`

 Choose the least indexed tag outside the forbidden list for the current vertex and partial
tag assignment. 

### `orderedTagOffsets`

 Select tag offsets in one indexed base scan. Every step examines a
list of at most `2d((d+1)+(d+1)²)` forbidden indices, counting duplicates. 
