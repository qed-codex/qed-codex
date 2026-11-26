---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/TensorSpectrum.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/TensorSpectrum.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/TensorSpectrum.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Tensor eigenbases for the multicolor register swap

The finite change of basis is constructed from invertible local kernels. This
module then specializes it to the actual register swap and transports it to the
joint fiber of universal types; multiplicities count those actual basis labels.


### `productKernel`

 Pointwise tensor product of local change-of-basis entries. 

### `productCoordinateEquiv`

 Explicit mutually inverse finite tensor transforms. 

### `productBasis`

 A genuine basis of the full function space on assignments of local states. 

### `productBasis_eigen`

 If the local kernel is an eigenkernel, the genuine product basis has the
same eigenvalue under a change at one position. 

### `spectatorCoordinateEquiv`

 Apply the tensor change of basis independently on each spectator fiber. 

### `spectatorBasis`

 Include a separate coordinate vector for every assignment of the untouched registers. 

### `JointBasisIndex`

 Labels of the genuine joint eigenbasis. The spectator includes the
non-head color of the pinned slot and all unused slot words. 

### `jointEquivPairs_jointSwap`

 The actual register swap becomes a change of just one local pair under
the joint-fiber decomposition. 

### `negativePositions`

 Negative signs are indexed by the local labels strictly below the diagonal. 

### `spectatorCard`

 Integer multiplicity of all untouched registers, including the pinned slot color. 

### `card_jointWeight`

 Exact dimensions of the weight spaces of the actual tensor eigenbasis. 

### `weightedTail`

 The integer tail, with both local eigenspace multiplicities retained. 

### `card_joint_via_multiplicities`

 The total number of actual coordinates has the same spectator factor as
the weight-space count; hence the normalized weight distribution is binomial. 

### `jointWeightProbability`

 The uniform probability of a weight among the actual joint eigenbasis labels. 

### `jointWeightProbability_eq_swapProbability`

 Spectator coordinates cancel from the normalized, exact weight count. 

### `jointWeightProbability_eq_binomial`

 The actual basis weight law is Bin(Q-1,(r-1)/(2r)), counted with multiplicity.
This is an identity of rational probabilities, not a calculation in the field. 
