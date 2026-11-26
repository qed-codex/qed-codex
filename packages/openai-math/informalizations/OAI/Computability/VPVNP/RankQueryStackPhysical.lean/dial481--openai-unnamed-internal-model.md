---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackPhysical.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackPhysical.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackPhysical.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed bit-stack programs for matrix queries

Three shared-bank routines describe the current Schur query and generate its
left and right subqueries. A fourth computes the column index of a tagged
Gram coefficient. Every routine has a fixed table independent of the matrix
dimensions, extension field and degree ranges.


### `gramInput`

 Inputs to the Gram coefficient dispatch, consisting of row indices `i` and `j`, degree `z`,
column count `m`, and four zero words. 

### `decodeGram`

 A valid Gram request contains two row indices and the common column to
read. The remaining descriptor gives the zero coefficient. 

### `Operation`

 The four dispatch operations describe a Schur query, stage either child, or decode a
weighted Gram coefficient. 

### `Operation.tree`

 Register decision tree implementing the chosen dispatch operation. 

### `capacity`

 Shared scratch-register capacity sufficient for each of the four dispatch trees. 

### `widthFactor`

 Uniform factor bounding the word width needed by any of the four dispatch trees. 

### `Operation.machine`

 Compile the operation's decision tree into a bit-stack routine on the shared register bank. 

### `Operation.clock`

 Step bound for executing the operation and writing its six output fields at word width `w`. 

### `Operation.run`

 Execute the complete fixed bit-stack instruction table, including binary
arithmetic, branching and all six register writes. 
