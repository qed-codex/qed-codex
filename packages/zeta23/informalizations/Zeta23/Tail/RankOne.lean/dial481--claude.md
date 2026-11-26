---
{
  "module": "Zeta23/Tail/RankOne.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Tail/RankOne.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Tail/RankOne.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/Tail/RankOne.lean — the linear-algebra step of [prop:tail] (the paper §4.2):
eigenvalue bounds for a (possibly infinite) sum of rank-one matrices m_ρ u_ρ u_ρᵀ.


Paper, verbatim (proof of [prop:tail]): "Since E = ∑_{γ∉I'} m_ρ u_ρ u_ρᵀ and
‖uuᵀ‖ = ‖u‖₂², ‖E‖ ≤ ∑_{γ∉I'} m_ρ ‖u_ρ‖₂²  [eq:Enormsum]" … "The trace-norm bound follows
from the same chain, since ‖uuᵀ‖₁ = ‖u‖₂² as well".

Design (avoiding Schatten-norm machinery): the trace norm of a Hermitian
matrix is DEFINED here as traceNorm hE := ∑ᵢ |λᵢ(E)|, and the operator-norm bound is
delivered in the shape RHLinalg.weyl_posIndexAbove_le consumes, namely ∀ i, |λᵢ(E)| ≤ θ.
Both follow from one inequality, traceNorm hE ≤ ∑_ρ c_ρ ‖u_ρ‖₂², proved directly in the
eigenbasis: λᵢ = vᵢ* E vᵢ = ∑_ρ c_ρ ⟨vᵢ,u_ρ⟩⟨v̄ᵢ,u_ρ⟩, |⟨vᵢ,u_ρ⟩⟨v̄ᵢ,u_ρ⟩| ≤ (|⟨vᵢ,u_ρ⟩|² +
|⟨vᵢ,ū_ρ⟩|²)/2, and Parseval ∑ᵢ|⟨vᵢ,w⟩|² = ‖w‖² for the unitary eigenvector matrix.
NOTE u_ρ u_ρᵀ (Matrix.vecMulVec u u), NOT u_ρ u_ρ*: the u_ρ = (φ̂(γ_ρ − τ_k))_k are complex
for off-line zeros and the paper's E is complex-symmetric termwise; Hermitian-ness of the
total (from the ρ ↦ 1−ρ̄ symmetry) is taken as the hypothesis hE.
-/
```

### `traceNorm`

 Trace norm ‖E‖₁ of a Hermitian matrix, DEFINED as ∑ᵢ |λᵢ(E)| (= sum of singular values
for Hermitian E). Paper: "the trace norm ‖Ê‖₁" in [prop:tail]; consumed in
[prop:zeroside-rank] via |tr Ê| ≤ ‖Ê‖₁ and ‖Ê‖_F ≤ ‖Ê‖₁ (both proved below). 

### `abs_rtrace_le_traceNorm`

 |tr E| ≤ ‖E‖₁ (used in [prop:zeroside-rank]: "|tr Ê| ≤ ‖Ê‖₁"). 

### `frobSq_le_traceNorm_sq`

 ‖E‖_F² ≤ ‖E‖₁² (used in [prop:zeroside-rank]: "‖Â‖_F ≤ ‖Ĝ‖_F + ‖Ê‖_F ≤ ‖Ĝ‖_F + ‖Ê‖₁"). 

### `abs_eigenvalues_le_traceNorm`

 Every |λᵢ(E)| is at most ‖E‖₁ (so a trace-norm bound is also an operator-norm bound in
the shape RHLinalg.weyl_posIndexAbove_le wants). 

### `mul_le_half_sq_add_sq`

 ab ≤ (a² + b²)/2. 

### `traceNorm_le_of_hasSum_vecMulVec`

 **[eq:Enormsum], trace-norm form.** If a Hermitian matrix E is the convergent sum
∑_ρ c_ρ · u_ρ u_ρᵀ (c_ρ ≥ 0, u_ρ ∈ ℂⁿ, vecMulVec u u = u uᵀ — no conjugation) and
∑_ρ c_ρ ‖u_ρ‖₂² converges to S, then ‖E‖₁ = ∑ᵢ|λᵢ(E)| ≤ S.
Paper: "‖uuᵀ‖ = ‖u‖₂²" and "‖uuᵀ‖₁ = ‖u‖₂² as well". 

### `abs_eigenvalues_le_of_hasSum_vecMulVec`

 **[eq:Enormsum], operator-norm form** (the shape RHLinalg.weyl_posIndexAbove_le wants):
under the same hypotheses every eigenvalue satisfies |λᵢ(E)| ≤ S, i.e. ‖E‖ ≤ S.
Paper: "‖E‖ ≤ ∑_{γ∉I'} m_ρ ‖u_ρ‖₂²". 
