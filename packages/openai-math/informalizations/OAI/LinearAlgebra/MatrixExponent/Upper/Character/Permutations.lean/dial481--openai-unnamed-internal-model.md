---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Upper/Character/Permutations.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Upper/Character/Permutations.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Upper/Character/Permutations.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Permuting the three actual tensor legs

The two adjacent swaps act on coefficient arrays and on their actual local
restriction witnesses. Their quotient actions preserve the semiring operations.
The six induced characters therefore remain normalized restriction-monotone
characters; their six values form a multiset invariant under either swap.


### `permuteHom`

 All six permutations, in the order `id, XY, YZ, XY·YZ, YZ·XY, XY·YZ·XY`. 

### `Character.permuted`

 Composing an actual tensor character with any of the six leg permutations
again gives a normalized monotone semiring character. 

### `permuteSwapXY`

 Right multiplication of the six leg permutations by the first swap. 

### `permuteSwapYZ`

 Right multiplication of the six leg permutations by the second swap. 

### `Character.sixValues`

 Multiplicities are retained even when different permutations have equal
character values. 

### `swapXY_polynomialTensor`

 Swapping the two polynomial inputs is a literal coefficient reindexing. 

### `Character.permuted_dotX`

 Each of the three singleton-leg orientations occurs exactly twice among
the first-leg pairings evaluated by the six permuted characters. 
