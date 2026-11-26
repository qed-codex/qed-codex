---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/LocalSpectrum.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/LocalSpectrum.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/LocalSpectrum.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Spectrum of a swap of two finite ordered registers

The alphabet size is unrestricted relative to the characteristic.  The only
field assumption beyond `Field K` is `2 ≠ 0`.  Basis labels on or above the
diagonal are positive; labels strictly below the diagonal are negative.


### `swapMap`

 The actual permutation operator on functions on two registers. 

### `eigenCoordinates`

 Diagonal entries are fixed; each unordered off-diagonal pair supplies a sum
coordinate and a difference coordinate. 

### `eigenCoordinates_swap`

 Conjugating the actual swap gives a diagonal sign operator. 

### `swapEigenbasis`

 The sum/difference construction is a genuine basis over every field with `2 ≠ 0`. 

### `linearMap_apply_eq_sum`

 The matrix-entry formula for a finite linear map, used to verify both kernel inverses. 

### `positiveSpace`

 These are the eigenspaces of the actual permutation operator. 

### `spaces_isCompl`

 The two actual eigenspaces form a direct sum of the full register space. 
