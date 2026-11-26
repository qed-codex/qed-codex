---
{
  "module": "OAI/Computability/VPVNP/CompressorCurrentGraph.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorCurrentGraph.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorCurrentGraph.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The current graph at a selected compression boundary

A boundary carries the actual terminal scalars and the packed incidence
columns of its current state. The initial position count is retained at
level zero. Publishing the next header preserves the current graph's old
incidence columns, even at the first shrinking substep.


### `Startup`

 The part of the initial physical header used at subsequent levels. 

### `Current`

 The current level's terminal scalars, pointer bank and packed incidence represent its
state, with the startup data still present at level zero. 

### `column_range`

 Every occupied column word lies between the end of this level's header
and the beginning of its scratch arrays. 

### `Current.publish`

 The stored current state supplies the source data of all three physical
header bursts. The old graph and the new head bank coexist in their output. 

### `startupCell`

 All first-level cells needed from startup, including the saved length and
the immutable descriptor arena end. 

### `graphCell`

 The six scalar words and the two families of pointers that describe a
current graph. The remaining header words hold local traversal metadata. 

### `Current.successor`

 Replaying the post-header kernels may install the next graph's incidence
columns and traversal metadata. Only its scalar words, pointers and six
startup words are needed to reconstruct the full current boundary. 
