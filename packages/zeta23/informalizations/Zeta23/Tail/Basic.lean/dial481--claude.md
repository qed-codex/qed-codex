---
{
  "module": "Zeta23/Tail/Basic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Tail/Basic.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Tail/Basic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/Tail/Basic.lean — shared elementary definitions for prop:tail (the paper §4.2).
-/
```

### `distI`

 Distance from γ to the interval I = [T, 2T] (paper: D := dist(γ, I) in the proof of
[prop:tail]); equals 0 for γ ∈ I, T − γ for γ < T, γ − 2T for γ > 2T. 

### `InTail`

 The tail predicate: ordinate γ ∉ I' := (T − D₀, 2T + D₀], D₀ := T^{1/2} [eq:D0].
(Paper: "split the sum [eq:Gdef] over distinct zeros according to whether the ordinate
γ = Re γ_ρ lies in I'"; E is the part with γ ∉ I' [eq:AE]. Note: this includes all
zeros with γ ≤ 0.) 

### `T₀`

 Explicit absolute threshold standing in for "T ≥ T₀" in [prop:tail]. Chosen ≥ 256 ≥ 16π²
(using only π ≤ 4) so that log(4T) ≤ 2·log(T/2π) = 2l (used in the "so that
θ₀ ≤ 32A₀‖ϱ″‖₁² l T^{λ/2−1}" clause); the zero-count estimate needs far less. Any larger
absolute constant would also do. 

### `LocalCount`

 Local zero-count hypothesis of [prop:tail]: "Let A₀ ≥ 1 be an absolute constant such
that N(t+1) − N(t) ≤ A₀ log(t+3) for all t ≥ 0" [Tit86, Thm 9.2], for an abstract family of
ordinates γ : ι → ℝ with multiplicities m : ι → ℕ. We use the two-sided unit-window form
(all real t, bound A₀·log(|t|+3)) as in PaperInputs.RvM.local: it is
equally classical and covers the zeros with γ ≤ 0 — which are in the tail
(paper: "zeros with γ ≤ 0 have D ≥ T and contribute at most ∑_{j≥0} A₀ log(j+4)(T+j)⁻³",
silently using the γ ↦ −γ symmetry and ζ(σ) ≠ 0 for 0<σ<1) — with no separate seam fact.
Stated for finite sub-families so that no summability is presupposed; instantiated from
ZeroConfig + PaperInputs.RvM.local in Zeta23/Tail.lean (LocalCount.ofWindowCount). 
