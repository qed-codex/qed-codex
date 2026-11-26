---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Spectrum/Comparison.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Spectrum/Comparison.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Spectrum/Comparison.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Pointwise compactness of the spectrum 

### `points`

 Semiring homomorphisms preserving the order, in the topology of pointwise convergence. 

### `separated`

 If no spectral point realizes the observations, finitely many already
separate them from every point by a positive squared distance. 

 # Absorbing an additive catalyst without order cancellation 

### `absorb`

 Repeating the strict gain pays for an extra factor `D + 1`.
The resulting multiplicative catalyst dominates the unit and works
unchanged for every power. 


# Strict spectral comparison

Adjoin the reversed comparison `y ≤ x` to the order, then identify
mutually comparable elements. Any character of the resulting semiring
would contradict the assumed strict inequality. The additive-state
obstruction gives a strict gain in the quotient. Lifting that comparison
provides the catalyst needed for all powers, with one constant overhead.


### `strictComparison`

 A strict inequality at all spectral points allows a single overhead
independent of the power. 
