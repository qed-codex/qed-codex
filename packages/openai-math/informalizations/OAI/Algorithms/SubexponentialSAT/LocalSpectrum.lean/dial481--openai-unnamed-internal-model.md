---
{
  "module": "OAI/Algorithms/SubexponentialSAT/LocalSpectrum.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/LocalSpectrum.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/LocalSpectrum.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The four-state involution in the interpolation layout

This file constructs the operator rather than assuming a spectral decomposition.
The only characteristic hypothesis on the field is that `2 ≠ 0`.


### `swapPair`

 The local permutation swaps `00` and `11`, fixing `01` and `10`. 

### `localMap`

 Pullback by the actual four-state permutation. 

### `eigenCoordinates`

 Coordinates in the explicit eigenbasis, with the negative vector indexed by `11`. 

### `fromEigenCoordinates`

 Reconstruction from eigenbasis coordinates. 

### `localEigenbasis`

 A genuine basis, not merely a list of candidate eigenvectors. 

### `positiveSpace`

 The positive eigenspace of the actual operator. 

### `negativeSpace`

 The negative eigenspace of the actual operator. 

### `positiveCoordinateEquiv`

 The three coordinates of a positive eigenvector are its values on `00`, `01`, `10`. 

### `negativeCoordinateEquiv`

 A negative eigenvector is determined by its value on `00`. 

### `swapAt`

 Change the bit pair at just one position. 

### `positionMap`

 The actual permutation operator on all assignments of the separate positions. 

### `localKernel`

 Matrix entries of the explicit four-vector basis. 

### `localDualKernel`

 Entries of the inverse change of coordinates. 

### `productKernel`

 Tensoring kernels is the pointwise product of their local entries. 

### `kernelMap`

 Actual linear action of a finite matrix represented by its entries. 

### `productCoordinateEquiv`

 The global coordinate transformation and its inverse are explicit finite sums. 

### `productEigenbasis`

 A genuine basis on all pair assignments, with one local eigenvector chosen per position. 

### `productEigenbasis_eigen`

 The product basis simultaneously diagonalizes every separate-position permutation. 

### `spectatorCoordinateEquiv`

 Add arbitrary unused coordinates by applying the proved product transform separately
on each spectator fiber. 

### `spectatorEigenbasis`

 The full basis, including a separate coordinate vector for each unused-bit assignment. 

### `spectatorPositionMap`

 The actual separate-position permutation leaves all spectator coordinates fixed. 
