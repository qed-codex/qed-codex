---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Rectangle/Threshold.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Threshold.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Rectangle/Threshold.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Optimizing the amount trimmed from the logarithmic output lengths 

### `maximum`

 The maximum includes the boundary case of no trimming. 


# The harmonic threshold

The logarithms of the outer lengths are trimmed by fixed amounts.
All three logarithms may have errors tending to zero, as happens
when rounding the lengths to integers.


### `shifted_threshold_limit`

 At inner exponent `xy`, the excess over output area is of order
`1/k` or smaller. The limit includes the untrimmed case. 

### `exp_shifted_threshold_limit`

 The derivative of the exponential gives the same scaled limit even
when the excess vanishes infinitely often. 

### `shifted_surplus_limit`

 Normalize by the untrimmed output area. This version allows arbitrary
sequences of logarithmic side lengths with the stipulated shifts. 
