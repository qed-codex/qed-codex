---
{
  "module": "Zeta23/Hypotheses/GzGp.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Hypotheses/GzGp.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Hypotheses/GzGp.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/Hypotheses/GzGp.lean — the H-EF bridge between the two expressions of [eq:Gdef]:  Z.Gz P T (zero side, Σ_ρ m_ρ φ̂(γ_ρ−τ_k)φ̂(γ_ρ−τ_l))
                  = P.Gp T  (prime side, ∫ φ̂(τ−τ_k)φ̂(τ−τ_l)ν_X(τ)dτ),
"the two expressions agreeing by Proposition [prop:EF]" — here: by hypothesis H-EF applied to
f = f_k, g = f_l, using h_{f_k}(z) = φ̂(z − τ_k) and "since φ̂ is real on ℝ we have
conj φ̂(conj z) = φ̂(z)" ([subsec:family] after [eq:fk]).
What this does and does not test: it checks the paper's internal consistency between [eq:Wdef],
[eq:fk], [eq:Gdef] and the form of [eq:EF] (conjugations, shifts, realness, support, X = e^L);
it does not test the 2π/sign normalisation inside ν_X, because [eq:EF] enters as the hypothesis
H-EF in the paper's own form — that normalisation is tested in Zeta23/ExplicitFormula.lean
(literature form ⇒ ExplicitFormulaPaper).
Taper regularity (φ ∈ C², supp φ ⊆ [−L/2, L/2]; Zeta23/Taper.lean) enters as
hypotheses. Helper lemmas are namespaced Zeta23.GzGp to avoid clashing with Zeta23/Taper.lean's
Params.phiHat_conj / Params.phiHat_ofReal (same statements; proved here independently so
this file depends only on Zeta23.Hypotheses).
-/
```

### `phi_neg`

 φ is even: φ(−u) = φ(u)  ([subsec:family]: "φ ∈ C_c³(ℝ) is even"). 

### `paperFT_fk`

 h_{f_k}(z) = φ̂(z − τ_k)  ([subsec:family] after [eq:fk]). 

### `phiHat_conj`

 "since φ̂ is real on ℝ we have conj φ̂(conj z) = φ̂(z)", in the form φ̂(conj z) = conj φ̂(z);
uses only that φ is real-valued and even. 

### `phiHat_ofReal`

 φ̂ is real on the real axis: φ̂(r) = φ̂_ℝ(r). 

### `fk_contDiff`

 f_k ∈ C² given φ ∈ C² (as a ℂ-valued function). 

### `fk_tsupport`

 supp f_k ⊆ supp φ ⊆ [−L/2, L/2]. 

### `Gz_eq_W`

 Zero side: G_{kl} [eq:Gdef, 1st expr] is literally W(f_k, f_l) [eq:Wdef]. No hypotheses. 

### `EFrhs_eq_Gp`

 Prime side: the [eq:EF] right-hand side at (f_k, f_l) is literally G_{kl} [eq:Gdef, 2nd expr].
No hypotheses. 

### `ZeroConfig.Gz_eq_Gp`

 **The H-EF bridge** [eq:Gdef]: the zero-side and prime-side matrices agree, given H-EF, L > 0,
φ ∈ C² and supp φ ⊆ [−L/2, L/2] (the last two are taper facts, Zeta23/Taper.lean). 

### `ZeroConfig.summable_Gsummand`

 Also: under H-EF the zero-side entries are (absolutely) summable — needed to write E = G − A as
the sum over zeros with γ ∉ I' . 
