---
{
  "module": "OAI/Computability/VPVNP/TensorRestrictionSpectrum.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TensorRestrictionSpectrum.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TensorRestrictionSpectrum.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Spectral points on the semiring of tensor restriction classes

A spectral point is constant on each class of mutually restricting tensors.
Its real values define a monotone semiring homomorphism on the quotient.
Conversely, monotonicity bounds the values of such a homomorphism below by
zero, so its evaluations on tensor representatives form a spectral point.


### `ofSpectralPoint`

 Real-valued evaluation of a spectral point on restriction classes. 

### `toSpectralPoint`

 Evaluate a monotone real-valued semiring homomorphism on tensor representatives. 

### `spectralPointEquiv`

 The two descriptions of the tensor spectrum agree point by point. 

### `charZeroOfSpectralPoint`

 One spectral point distinguishes every pair of distinct natural-number classes. 
