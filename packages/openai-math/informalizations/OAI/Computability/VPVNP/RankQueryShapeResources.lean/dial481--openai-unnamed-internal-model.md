---
{
  "module": "OAI/Computability/VPVNP/RankQueryShapeResources.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryShapeResources.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryShapeResources.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Choosing one bit width for both matrix orientations and all Schur roots 

### `shapeBits`

 The largest rectangular prefix in either orientation bounds the
determinant-coefficient scan. The extra unit gives the strict comparison
required when the power of two is attained exactly. 

### `shapeBits_rect`

 A prefix may be read either as a row prefix or as a column prefix
of the transposed matrix. The same depth bound applies in both cases. 

### `shapeBits_minor`

 The constant-polynomial determinant specialization uses degree zero
and the same bound for the minor order and the recursion parameter. 

### `gramWidth_fits`

 These are the three word-fit assumptions shared by the ordinary Schur
root and the weighted Gram descriptor, together with the outer cursor's
width condition. An address kernel can require a larger width. 

### `sliceAddress`

 A single address width accommodates the graded-key enumeration as well
as the two orientations of the Schur rank scanner. 
