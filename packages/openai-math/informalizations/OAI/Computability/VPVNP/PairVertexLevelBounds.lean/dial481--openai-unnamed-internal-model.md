---
{
  "module": "OAI/Computability/VPVNP/PairVertexLevelBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexLevelBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexLevelBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Locating the level of a popped traversal node

The DFS node is a row address. The descending scan accepts the first level
whose published start is at most this address. Its stride quotient recovers
the exact site ordinal, even when other levels contain no rows.


### `layerBase_succ`

 The next prefix base is the exclusive end of this layer's rows. 

### `node_interval`

 The chosen row belongs to its own interval. All earlier exclusive
ends are below or equal to its address and all later starts are strictly above it. 

### `resident_geometry`

 The descending scan begins at the actual last level and uses the published header geometry. 

### `resident_start`

 Every live level has a start cell, including the terminal state. 

### `resident_end`

 The resident count gives the exclusive end for every level. In particular,
the terminal level needs no successor header. 

### `resident_locates`

 Actual header reads give the comparisons of the descending scan and the
machine's unsigned subtraction and division give the exact owner identifier. 
