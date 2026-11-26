---
{
  "module": "OAI/Computability/VPVNP/ShiftedBlocks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShiftedBlocks.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShiftedBlocks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Assembly of the shifted crossing blocks

Appendix B indexes a block by the particle number and the two doubled source
energies. We extend both factors of each cut by zero at incompatible source
indices, concatenate their intermediate coordinates, and remove the integral
pairing by its inverse. Each cut retains its own set of intermediate states.


### `CrossingState`

 The nonempty source states of doubled energy at most `H`. 

### `CrossingBlock`

 The first coordinate is the particle number minus one. The other coordinates
are the doubled energies of the two operator indices. 

### `sourceGrade`

 The doubled energy of a crossing source state, viewed as a grade between zero and the
cutoff. 

### `blockPoleDegree`

 The exponent of the multiplier `(z - w)^L` for this block. For an inhabited block it is the
sum of the two source energies minus one. 

### `isBlockRow`

 A source state belongs to the row block when its particle number and doubled energy agree
with the first source index of the block. 

### `isBlockColumn`

 A source state belongs to the column block when its particle number and doubled energy
agree with the second source index of the block. 

### `BlockRows`

 The source states with the particle number and row energy specified by the crossing block. 

### `BlockColumns`

 The source states with the particle number and column energy specified by the crossing
block. 

### `BlockCoordinates`

 Each intermediate coordinate retains its block and its binomial index. 

### `BlockDecomposition`

 The local decomposition on the block tagged by `t`. It uses the two opposite
orders of the input and output state, with the binomial index ranging to its
actual pole degree. 

### `assembleCrossingBlocks`

 Concatenate the local factorizations and apply the inverse of the signed
integral pairing. The first summand factors on `(i, α) | (j, β)` and the second
on `(i, β) | (j, α)`. 

### `CrossingCutoff`

 Finite-mode states of doubled energy at most `B`. 

### `finiteShiftedCrossing`

 Integral crossing at a fixed energy cutoff and shift. The finite-mode
window contains the coefficient of both products, and the sizes of the two
intermediate spaces retain the signs of the shift. 
