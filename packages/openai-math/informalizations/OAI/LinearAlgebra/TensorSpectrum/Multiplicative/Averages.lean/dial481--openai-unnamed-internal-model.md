---
{
  "module": "OAI/LinearAlgebra/TensorSpectrum/Multiplicative/Averages.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/Multiplicative/Averages.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/Multiplicative/Averages.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Positive weighted averages of a projective orbit

These elementary finite identities supply the approximate eigenvectors used in
the compactness argument. Every average is a convex combination of actual
members of the invariant set. No fixed-point theorem is assumed here.


### `projectiveOrbit`

 Iteration of the normalized multiplication map, starting at `f₀`. 

### `projectiveMass`

 The unnormalized mass of the `n`th translated function. 

### `projectiveOrbit_normalized`

 Undoing all normalizations in the orbit gives the original translate. 

### `positiveWeightedMean`

 A finite positive weighted mean, with its denominator kept explicit. 

### `positiveWeightedMean_mem`

 Binary convexity suffices for membership of all finite weighted means. 

### `projectiveSum`

 The finite unnormalized power-series sum of the translated coordinates. 

### `projectiveAverage`

 Its normalized mean; its mass denominator is exactly the scalar growth API. 

### `projectiveSum_residual`

 The telescoping identity before dividing by the total weight. 

### `projectiveAverage_residual`

 The sole boundary terms of the normalized approximate-eigenvector equation. 
