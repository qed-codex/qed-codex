---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Integral/Upper/Separation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Integral/Upper/Separation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Integral/Upper/Separation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Charged finite separation by local Fourier maps

The source is exactly `6 * M` full copies of the shared-first-leg tensor.
The target is the full direct sum of the sector tensors, each multiplied by
a length-`M` pairing on the second and third legs.  Local variables may have
negative weights; after Fourier projection every surviving total weight is
a nonnegative square, so the resulting coefficient array is polynomial.


### `shared`

 The branch labels occur only on the last two legs of the input. 

### `dotPairingX`

 The auxiliary pairing has one coordinate on the first leg. 

### `separated`

 Every branch in this output has its own first-leg space. 

### `phase`

 The integer projected by the finite Fourier average. Labels are numbered
from zero here; translating all four labels by one leaves this phase unchanged. 

### `copyLocal`

 Copy a specified source coordinate with a scalar depending only on the
target coordinate and the source's direct-sum copy number. 

### `restrict_copies`

 Summing the full source copies, rather than target coordinate labels, is
what produces the Fourier average. All three source copy indices must agree. 

### `restrict_scaled`

 Scaling each target coordinate is itself a local linear operation. 

### `fourier_restrict`

 The actual independent local maps give exactly the projected tensor. 

### `squareDegree`

 The degree of a projected monomial, already known to be nonnegative. 

### `separationPolynomial`

 This is a polynomial array even though the individual local weights used
to realize its nonzero evaluations can be negative. 

### `separationPolynomial_constant`

 The zero coefficient is the full direct sum with an auxiliary dot product. 

### `separationPolynomial_eval`

 On the complete projected support, the local weights add to the actual
polynomial degree, including all zero and mismatched coefficients. 

### `separationPolynomial_specializes`

 Every nonzero specialization comes from exactly the charged number of
source copies by three actual local linear maps. 

### `finite_charged_separation`

 The complete finite construction, without a rank or character premise.
The nonzero-evaluation witnesses are restrictions of the full source direct
sum; the constant tensor is itself a full direct sum of products. 
