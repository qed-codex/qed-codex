---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Integral/Upper/TagTensorWords.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Integral/Upper/TagTensorWords.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Integral/Upper/TagTensorWords.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Coefficient tensor words and matched-label restrictions

Tensor powers of a shared-first-leg tensor have one branch for each word.
The regrouping below preserves all coefficients, including the zero
coefficients between different words. Selecting words by an injection is an
actual local restriction. Multiplicativity is then applied to the actual
tensor product represented by each word.


### `sharedLabels`

 A shared-first-leg tensor with an arbitrary finite label type. 

### `tensorWord`

 One actual tensor factor per position, without identifying positions or
discarding any coefficients. 

### `wordBranch`

 A word specifies which branch occupies each tensor position. 

### `joinCoordinates`

 Put a word of labels and a word of coordinates back into coordinate pairs. 

### `power_shared_pullback`

 Regrouping the second and third coordinates of the full tensor power
produces exactly the shared tensor of word branches. 

### `restricts_power_shared_words`

 The regrouping is implemented by three actual coordinate pullbacks. 

### `ofTensor_shared_words`

 The regrouping is invertible, so it also identifies the tensor classes. 

### `shared_injective_pullback`

 An injection on branch labels preserves the equality test between labels. 

### `restricts_shared_injective`

 Selecting any set of matched labels is an actual local restriction. 

### `restricts_power_shared_selected`

 This target uses the precise `Fin M` shared tensor accepted by the charged
separation construction. The label map may enumerate any selected word set. 

### `restricts_power_shared_fiber`

 In particular, the words in a count fiber can be retained together. 

### `restricts_power_shared_fiber_enumeration`

 Every finite enumeration of a count fiber provides the exact input needed
by charged separation, with multiplicity equal to the number of selected words. 

### `headTailCoordinates`

 Split off the first tensor position, leaving every remaining coordinate. 

### `ofTensor_tensorWord`

 The class of a coefficient tensor word is the product of the factor
classes. This is proved by actual invertible coordinate regroupings. 

### `map_wordBranch`

 A character evaluates a word branch as the finite product of the values
of the chosen branches; there is no separate multiplicativity assumption. 

### `map_wordBranch_of_mem_fiber`

 Every word in a fixed count fiber has the same character value. 
