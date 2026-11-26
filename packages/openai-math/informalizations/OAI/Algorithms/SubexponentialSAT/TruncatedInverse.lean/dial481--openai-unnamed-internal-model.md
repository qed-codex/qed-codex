---
{
  "module": "OAI/Algorithms/SubexponentialSAT/TruncatedInverse.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/TruncatedInverse.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/TruncatedInverse.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Explicit finite geometric inversion and local CRT factors

The inverses in this file are finite polynomial expressions. Scalar inverses are
input data with multiplication certificates; no Bézout coefficients are chosen.


### `geometricLoop`

 A single-recursion loop retaining its current power and geometric sum.
Each iteration invokes its multiplication and addition functions once. 

### `geometricLoop_denote`

 Semantic correctness requires only operation-preservation by `denote`;
the executable representation itself need not satisfy semiring equalities. 

### `geometricLoopWithCost`

 Instrument the same loop with the scalar-operation counters returned by
its concrete arithmetic routines. Previous states are evaluated once. 

### `geometricLoopWithCost_cost_le`

 The counter bound comes from the costs of the operations actually called
at each earlier state, rather than an annotation on the result. 

### `geometricLoop_size_le`

 A uniform size bound for every stored power and partial geometric sum.
For dense polynomials, `size` is coefficient-list length. 

### `denseGeometricWithCost`

 Dense coefficient-list implementation of the stored-power geometric loop. 

### `denseInverseWithCost`

 The scalar inverse `a` is supplied explicitly. Its negation is computed
by one counted multiplication, and all polynomial operations are list routines. 

### `denseFactorsWithCost`

 Build the repeated linear factors with one counted negation multiplication
per retained node. Repeated factors reuse the computed coefficient. 

### `denseTermWithCost`

 One CRT summand. Every computed polynomial is bound once and reused. 

### `denseCRTWithCost`

 The complete dense-list CRT loop, including the costs of every term and
the final coefficient-wise summation. Scalar inverse inputs `a` are explicit. 

### `cofactorLength`

 Explicit polynomials bounding the sizes and counters in the CRT loop. 

### `trunc_eq_modByMonic`

 Coefficient truncation and monic remainder are the same operation. 

### `rawInverse`

 The untruncated finite geometric inverse expression. 

### `inverse`

 The inverse represented by exactly its first `D` coefficients. 

### `inverse_correct`

 Only the supplied constant inverse is used. This works in positive
characteristic and in rings with zero divisors. 

### `correctedJet`

 Multiply a jet by the inverse, keeping precisely the local order. 

### `localFactor`

 The other nodes' factors, expressed in node `i`'s local coordinate. 

### `reconstruct`

 Explicit Hermite reconstruction. Local corrections are truncated before
shifting back, so no final polynomial division is required. 

### `reconstruct_eq`

 Correct local data reconstruct the original polynomial by the proved
degree bound and CRT injectivity, using the explicit geometric formula. 

### `constantInverse`

 Form the required scalar inverse directly from the supplied inverses of
the node differences. 

### `denseInverse_cost_le`

 A genuine coefficient-ring operation bound for the instrumented inverse.
`L` is any positive bound on the input coefficient-list length. 

### `denseCRT_correct`

 The complete executable dense-list algorithm recovers the polynomial.
The supplied scalar inverse certificates are the sole inverse-related input. 
