---
{
  "module": "OAI/Computability/VPVNP/GrassmannFrameDimensions.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrassmannFrameDimensions.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrassmannFrameDimensions.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Dimensions of completed frame blocks

In the frame description of the binary Grassmannian, the two planes share
all completion columns. Their sum contains exactly the completion and both
original blocks. Independence counts the dimensions of all three spans.


### `finrank_completedBlock_range`

 Selecting columns by an injective map gives their count plus the
number of common completion columns as the dimension of the completed block. 

### `finrank_leftBlock`

 Dimension of the completed first block of an independent frame. 

### `finrank_rightBlock`

 Dimension of the completed second block of an independent frame. 

### `sup_frameBlocks`

 The sum of the two completed blocks spans the full frame. 

### `finrank_sup_frameBlocks`

 Dimension of the sum of the two blocks, with their common completion
counted once. 

### `leftPlane`

 The middle-dimensional plane spanned by the first block and the completion. 

### `rightPlane`

 The middle-dimensional plane spanned by the second block and the completion. 

### `hasType_framePlanes`

 The two planes of a completed independent frame have Grassmann type `r`. 
