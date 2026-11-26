---
{
  "module": "Zeta23/XiPrime/Transfer/Inputs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Transfer/Inputs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Transfer/Inputs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

### `QpEntry`

 Q_{kl}(e) := ∫ φ̂(τ−τ_k) φ̂(τ−τ_l) P_e(X; τ) dτ — the P-part Gram entry for an arbitrary coefficient
sequence e : ℕ → ℂ ([XF′ Lemma 6.1]: "Q^{(r)} = the PP-part of the paper's Gram matrix for
coefficients e_r").  ONE parenthesised product under the binder.  Equals
PrimeSide.GentryNu (XiPrime.Pc p.X e) p F k l at p = P.toSetting T, F = P.localFun T, by rfl
(QpEntry_eq_GentryNu below). 

### `QpMat`

 the d×d matrix (Q_{kl}(e))_{0≤k,l<d} as a complex matrix (real entries), same typing as GpC. 

### `deltaKL`

 δ_{kl} := ½ log(τ⋆_{kl}/T)  [XF′ Lemma 6.1]: L⋆^{kl} = L_T + δ_{kl}, δ_{kl} ∈ [0, ½ log 2]. 

### `Reexpansion`

 **The re-expansion input** [XF′ §6], for
F = xiCoeffFamily with e T r N = e_r(N) = Σ_{j<Ω(N)} binom(−(j+1), r) L_T^{−(j+1)−r} [(Λ·log)∗Λ^{∗j}](N)
(supplied by theorem xiReexpansion).
Constants are T-uniform; the δ-range [0, 1/2] ⊇ [0, ½ log 2] ∋ δ_{kl}; sums over N ∈ Finset.Ioc 0 ⌊x⌋₊
(tree convention) for 2 ≤ x ≤ e^{l(T)} ⊇ the only point used downstream, x = X = e^{λl}.
BASE POINT: the expansion is about L_T = ½l + iπ/4 (XiPrime.LT), the ξ′ base —
so this is the right sentence for F = xiCoeffFamily (F.c T N = xiCoeff (LT T) N by rfl) and for nothing else; the
Z′ analogue (real base ½l, Defs.L2star) needs its own structure/consumer (the Z′ Gp1 differs too).  One should not
read 0 ≤ A into this structure: it is derivable from H3 but not carried. 

### `Reexpansion.expand`

 C(N; L_T + δ) − c^{(T)}_N = Σ_{r≥1} e_r(N) δ^r  (absolutely convergent: |δ/L_T| < 1). 

### `Reexpansion.e_one`

 e_r(1) = 0 (the N = 1 frequency does not oscillate; C(1; ·) ≡ 0). 

### `Reexpansion.H1`

 (H1)_r: Σ_{N≤x} |e_r(N)| N^{−1/2} ≤ A (ρ₀/l)^r √x · l. 

### `Reexpansion.H2`

 (H2)_r: Σ_{N≤x} |e_r(N)|² ≤ A (ρ₀/l)^{2r} x l². 

### `Reexpansion.H3`

 (H3)_r: Σ_{N≤x} |e_r(N)|²/N ≤ A (ρ₀/l)^{2r} l² (1 + log x)   ([XF′ §6]: "≤ (c/l)^{2r} c l² L"). 

### `PPUpper`

 **The prop:PP upper bound for general coefficients** (frobSq_Ppart_le; [XF′ Lemma 6.1]):
"Σ_{kl} (Q_{kl})² is bounded by the paper's Prop. PP in its upper-bound form (diagonal +
Montgomery–Vaughan)", through lem_ends_nu for ν = P_e: main T·L·Σ|e|²/N (g ≤ L), then L·Σ|e|²,
the 𝒪₂ term L·S₁², and the r-INDEPENDENT end-effect term L·l·log l·(l + S₁)².  Over abstract taper
data; k,l-sums over Fin p.d (shape of PrimeSide.trGt2A); N-sums over Finset.Ioc 0 ⌊X⌋₊, literally
sumSqDivW / sumSqW / S1 (defeq).  The theorem:
frobSq_Ppart_le (hPP : PPInput) (hMV : MVHilbert C) (hC : 0 < C) (cϱ lam) (hlam : 0 < lam ∧ lam ≤ 1) : PPUpper cϱ lam
(Zeta23/XiPrime/PrimeSide/PPUpper.lean). 
