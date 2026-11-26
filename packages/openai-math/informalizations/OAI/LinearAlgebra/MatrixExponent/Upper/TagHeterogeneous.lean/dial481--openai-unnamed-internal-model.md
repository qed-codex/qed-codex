---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Upper/TagHeterogeneous.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Upper/TagHeterogeneous.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Upper/TagHeterogeneous.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Heterogeneous shared-first-leg tensors

Padding a branch adds only zero coordinates. The extra uniform labels used by
the separation construction are removed by actual independent local maps.
The first leg is shared throughout; no direct-sum additivity is used here.


### `sharedTwo`

 Two heterogeneous branches with one common first coordinate. 

### `padLeft`

 Zero extension into the left summand on the last two legs. 

### `padRight`

 Zero extension into the right summand on the last two legs. 

### `ofTensor_padLeft`

 Zero padding is an equivalence under mutual actual restriction. 

### `ofTensor_padRight`

 Right zero padding also has explicit inclusion and projection maps. 

### `maskedFamily`

 Keep just one matched pair of sectors in a common ambient tensor. 

### `ofTensor_shared_maskedFamily`

 Redundant labels are removed by selecting each coordinate's own sector;
the reverse maps are the corresponding zero extensions. 

### `twoLabel`

 A two-sector label independent of the coordinate inside the sector. 

### `twoFamily`

 Both branches now use the same ambient last two legs. 

### `sharedThree`

 Three heterogeneous branches, still sharing one first leg. 

### `threeFamily`

 The three padded branches used by the uniform tag theorem. 

### `triplingMiddleTensor`

 The middle polynomial branch keeps its original first-leg reversal. 

### `triplingSectorTensor_eq_sharedThree`

 The actual polynomial sector assembly is exactly a heterogeneous shared
tensor; in particular all six mismatched sector blocks remain zero. 

### `ofTensor_tripling_uniform`

 This is the exact uniform-tag input representing the three-sector
polynomial degeneration, with a literal common first-input space. 
