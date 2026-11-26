---
{
  "module": "Zeta23/Final.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Final.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Final.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/Final.lean — the headline theorems.

  "More than two thirds of the zeros of the Riemann zeta function lie on the critical line",
   Theorems A, B, C — ε-forms.

Each theorem's TYPE in the first section displays the inputs as separate named hypotheses:
  hEF  : EF.EF_lit zetaZeroConfig        — Weil's explicit formula, literature form [eq:EFstd]
                                           ([IK04, Thm 5.12] for ζ), over ζ's nontrivial zeros;
  hRvM : RiemannVonMangoldt zetaZeroConfig — [eq:RvM] + local count N(t+1)−N(t) ≤ A₀ log(|t|+3);
  hMV  : ∃ C > 0, MVDiag C                — Montgomery–Vaughan weighted Hilbert inequality, literature
                                           (y = x) form [MV74, Thm 2]; the paper's bilinear [lem:MV] is
                                           derived (Zeta23.MVHilbert_of_diag);
  hΓ   : GammaFacts                        — Stirling-type facts for μ [eq:mufacts], [eq:muints].
Nothing else: the Chebyshev–Mertens bounds [lem:cheb] are proved (Zeta23.Cheb.chebyshevMertens), the
paper's spectral form of the explicit formula [eq:EF] is derived from hEF (Zeta23.EF), the taper profile
is Mathlib's Real.smoothTransition (Zeta23.stdProfile), the ζ-facts (analytic order, functional-equation
symmetry, local finiteness) are proved (Zeta23.zetaSeam), and thm:traces [thm:traces] is
Zeta23.PrimeSide.thm_traces (the versions with thm:traces as an explicit hypothesis are
Zeta23.thmA_of_traces etc. in Zeta23/Main.lean). Later sections discharge the hypotheses
hMV, hΓ, hRvM and hEF one by one, ending with the unconditional forms.

Counting functions (Zeta23/Statement.lean): Ncount T₁ T₂ = N(T₁,T₂) with multiplicity (analytic order of
riemannZeta), N0star = N₀* (on the line, distinct), N0simple = N₀ˢ (on the line, simple), Ndist = N_d
(distinct), all over nontrivial zeros ρ (ζ ρ = 0, 0 < Re ρ < 1) with T₁ < Im ρ ≤ T₂.
-/
```

### `PaperInputs.of_literature`

 PaperInputs from the literature trust base: literature EF, RvM, MV74 in diagonal form, Γ-facts. 

### `thmA`

 **Theorem A** [thm:A]: "liminf_{T→∞} N₀*(T,2T)/N(T,2T) ≥ 2/3" — for every ε > 0 and all large T,
at least (2/3 − ε) of the nontrivial zeros of ζ with T < Im ρ ≤ 2T, counted with multiplicity, are
accounted for by DISTINCT zeros on the critical line:  (2/3 − ε)·N(T,2T) ≤ N₀*(T,2T). 

### `thmA_cumulative`

 **Theorem A** [thm:A], cumulative: "liminf_{T→∞} N₀*(T)/N(T) ≥ 2/3", N(T) := N(0,T). 

### `thmA_lam`

 **Theorem A at fixed λ ∈ (0,1)** [thm:A]: N₀*(T,2T) ≥ (H(λ) − ε) N(T,2T), H(λ) = 2 − 1/λ − λ/3
(the paper's c(λ)·loglogT/logT absorbed into ε). 

### `thmB`

 **Theorem B** [thm:B]: "at least half of the zeros are simple and on the critical line":
(1/2 − ε)·N(T,2T) ≤ N₀ˢ(T,2T) for T ≥ T₀(ε). 

### `thmB_cumulative`

 **Theorem B** [thm:B], cumulative: "liminf_{T→∞} N₀ˢ(T)/N(T) ≥ 1/2". 

### `thmB_lam`

 **Theorem B at fixed λ** [thm:B]: N₀ˢ(T,2T) ≥ (2F(λ) − 1 − ε) N(T,2T), F(λ) = λ/(1+λ²/3). 

### `thmC`

 **Theorem C** [thm:C]: "liminf N_d(T)/N(T) ≥ 3/4" — distinct zeros: (3/4 − ε)·N(T,2T) ≤ N_d(T,2T). 

### `thmC_cumulative`

 **Theorem C** [thm:C], cumulative: "liminf_{T→∞} N_d(T)/N(T) ≥ 3/4". 

### `thmC_lam`

 **Theorem C at fixed λ** [thm:C]: N_d(T,2T) ≥ (F(λ) − ε) N(T,2T). 

 ## Three-hypothesis forms: H-MV is a theorem (Zeta23.MV.mv_hilbert — the weighted Hilbert
inequality of Montgomery–Vaughan 1974, proved outright). 

### `PaperInputs.of_three`

 PaperInputs from (literature EF, RvM, Γ-facts) only: cheb and MV are theorems. 

### `thmA₃`

 **Theorem A**, three hypotheses (EF_lit, RvM, Γ): (2/3 − ε)·N(T,2T) ≤ N₀*(T,2T). 

### `thmA₃_cumulative`

 **Theorem A** cumulative, three hypotheses. 

### `thmB₃`

 **Theorem B**, three hypotheses: (1/2 − ε)·N(T,2T) ≤ N₀ˢ(T,2T). 

### `thmB₃_cumulative`

 **Theorem B** cumulative, three hypotheses. 

### `thmC₃`

 **Theorem C**, three hypotheses: (3/4 − ε)·N(T,2T) ≤ N_d(T,2T). 

### `thmC₃_cumulative`

 **Theorem C** cumulative, three hypotheses. 

 ## Two-hypothesis forms: H-Γ is a theorem (Zeta23.gammaFacts; proved via
digamma partial fractions + vertical Stirling + FTC). 

### `PaperInputs.of_two`

 PaperInputs from (literature EF, RvM) only: cheb, MV and Γ are theorems. 

### `thmA₂`

 **Theorem A**, two hypotheses (EF_lit, RvM): (2/3 − ε)·N(T,2T) ≤ N₀*(T,2T). 

### `thmA₂_cumulative`

 **Theorem A** cumulative, two hypotheses. 

### `thmB₂`

 **Theorem B**, two hypotheses: (1/2 − ε)·N(T,2T) ≤ N₀ˢ(T,2T). 

### `thmC₂`

 **Theorem C**, two hypotheses: (3/4 − ε)·N(T,2T) ≤ N_d(T,2T). 

### `thmB₂_cumulative`

 **Theorem B** cumulative, two hypotheses. 

### `thmC₂_cumulative`

 **Theorem C** cumulative, two hypotheses. 

 ## One-hypothesis forms: H-RvM is a theorem given the proved Γ-facts
(local count + folded argument principle + Backlund; Zeta23/RvM/*). 

### `riemannVonMangoldt_zeta`

 **H-RvM for ζ, unconditionally** (from the RvM development and the proved Γ-facts). 

### `PaperInputs.of_EF`

 PaperInputs from the literature explicit formula ALONE. 

### `thmA₁`

 **Theorem A** [thm:A], single hypothesis — Weil's explicit formula for ζ in literature form
[eq:EFstd] is the ONLY assumption: for every ε > 0 and all large T, at least (2/3 − ε) of the
nontrivial zeros of ζ in (T, 2T], counted with multiplicity, are matched by distinct zeros ON the
critical line:  (2/3 − ε)·N(T,2T) ≤ N₀*(T,2T). 

### `thmA₁_cumulative`

 **Theorem A** cumulative, single hypothesis: liminf N₀*(T)/N(T) ≥ 2/3. 

### `thmB₁`

 **Theorem B** [thm:B], single hypothesis: (1/2 − ε)·N(T,2T) ≤ N₀ˢ(T,2T) (simple AND on-line). 

### `thmB₁_cumulative`

 **Theorem B** cumulative, single hypothesis. 

### `thmC₁`

 **Theorem C** [thm:C], single hypothesis: (3/4 − ε)·N(T,2T) ≤ N_d(T,2T) (distinct zeros). 

### `thmC₁_cumulative`

 **Theorem C** cumulative, single hypothesis. 

 ## Unconditional forms: the explicit formula is a theorem
(Zeta23.WeilEF.EF_lit_zetaZeroConfig — Weil/Riemann–von Mangoldt explicit formula for ζ,
literature form [eq:EFstd], proved from Mathlib's functional equation by contour integration).
These are the headline statements of the formalization: no hypotheses at all. 

### `zetaEF`

 **Weil's explicit formula for ζ**, re-exported. 

### `paperInputs_zeta`

 The paper's full input package, unconditionally. 

### `thmA₀`

 **Theorem A** [thm:A], UNCONDITIONAL: for every ε > 0, for all large T, at least (2/3 − ε) of the
nontrivial zeros of Mathlib's riemannZeta with T < Im ρ ≤ 2T, counted with multiplicity, are matched
by distinct zeros on the critical line:  (2/3 − ε)·N(T,2T) ≤ N₀*(T,2T). 

### `thmA₀_cumulative`

 **Theorem A**, cumulative, UNCONDITIONAL: liminf_{T→∞} N₀*(T)/N(T) ≥ 2/3. 

### `thmB₀`

 **Theorem B** [thm:B], UNCONDITIONAL: at least (1/2 − ε) of the zeros are simple AND on the line. 

### `thmB₀_cumulative`

 **Theorem B**, cumulative, UNCONDITIONAL. 

### `thmC₀`

 **Theorem C** [thm:C], UNCONDITIONAL: at least (3/4 − ε) of the zeros are distinct. 

### `thmC₀_cumulative`

 **Theorem C**, cumulative, UNCONDITIONAL. 

### `thmA₃_N0`

 a fortiori (paper [thm:A]: "and a fortiori N₀(T) ≥ (2/3 − o(1))N(T)"): the WITH-multiplicity
on-line count also carries the 2/3 proportion. From thmA₃ and N₀* ≤ N₀ ([eq:trivialchain]). 

### `thmB₃_Nsimple`

 a fortiori (paper [thm:B]: "consequently also Nˢ(T) ≥ (1/2 − o(1))N(T)"): simple zeros
anywhere in the strip. From thmB₃ and N₀ˢ ≤ Nˢ ([eq:trivialchain]). 

### `thmA₀_N0`

 a fortiori: the on-line count WITH multiplicity. 

### `thmB₀_Nsimple`

 a fortiori: simple zeros anywhere in the strip. 

### `thmA_ofInputs`

 Same as thmA but from the bundled paper-form inputs (PaperInputs) rather than the literature
trust base. 
