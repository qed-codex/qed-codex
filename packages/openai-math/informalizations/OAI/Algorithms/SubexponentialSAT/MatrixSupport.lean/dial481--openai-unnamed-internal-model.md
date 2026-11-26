---
{
  "module": "OAI/Algorithms/SubexponentialSAT/MatrixSupport.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/MatrixSupport.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/MatrixSupport.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The far-support property of the interpolation matrices

The bit permutations and the products of (1 - J_l) / 2 are constructed
explicitly.  The support conclusion is derived from their sublist expansion.


### `agreements`

 Agreements compare the column head against the row's selected slot. 

### `swapPositions`

 Apply the local 00 ↔ 11, 01 ↦ 01, 10 ↦ 10 permutation at each selected position. 

### `swapPositions_sdiff`

 Multiplying the full permutation by an omitted subset cancels those positions. 

### `applySwaps`

 Ordered application of the position involutions. 

### `agreements_card_le`

 Any possible agreements are in the omitted set, together with position t. 

### `differenceProduct`

 The actual ordered product of Id - J_l, acting by pullback. 

### `projectorProduct`

 The product of the normalized projectors (Id - J_l) / 2. 

### `differenceProduct_expansion`

 Full expansion: one term for each choice of the permutation part of a factor. 

### `projectorProduct_expansion`

 The normalized expansion is valid even when some coefficients cancel. 

### `activePositions`

 The full permutation at t acts at every other position. 

### `delta`

 A column basis vector, in function coordinates. 

### `elementaryProjector`

 Elementary symmetric sum of degree j in the actual normalized projectors. 

### `matrixEntry`

 Equation (5.4), evaluated on the column basis vector indexed by y.
The outer full permutation is pullback by swapPositions.


### `applySwaps_agreements_card_le`

 Every subword of omitted flips leaves all other positions complemented. 

### `projectorProduct_delta_eq_zero`

 Each elementary projector term has far support after the full permutation. 

### `matrixEntry_support`

 The far-support conclusion for the actual matrix formula, with no
assumption on the coefficients or on whether expansion terms cancel. 

### `jointMatrix`

 The matrix on the joint fiber used by the universal-block construction. 

### `permutationLinear`

 The permutation operator associated with any set of positions. 

### `differenceLinear`

 Linear-map presentation of the ordered product of Id - J. 

### `projectorLinear`

 A linear map for a product of normalized projectors. 

### `matrixLinear`

 The endomorphism in (5.4), before restriction to the joint fiber. 

### `extendJoint`

 Extend a vector on the joint fiber by zero, using its coordinate basis. 

### `jointMatrix_mulVec`

 Matrix-vector multiplication is exactly the concrete projector action.
This supplies the bridge needed for a spectral proof of the rank bound.


### `jointSwap`

 The actual position involution restricted to the joint fiber. 

### `extendJoint_swap_eigen`

 A simultaneous eigenvector on the fiber extends to one on the full type space. 

### `projectorLinear_cons`

 The scaled product definition is precisely the product of normalized factors. 

### `projectorProduct_eigen`

 Eigenaction of an ordered product of the normalized projectors. 

### `matrixEigenvalue`

 Eigenvalue obtained by multiplying the position eigenvalues and evaluating
the elementary symmetric polynomial on (1 - sign) / 2. 

### `matrixLinear_eigen`

 Simultaneous position eigenvectors are eigenvectors of the constructed map. 

### `jointMatrix_eigen`

 Concrete matrix eigenaction on the joint fiber.  No eigenvalue or
support conclusion is assumed; only the individual position actions are given. 
