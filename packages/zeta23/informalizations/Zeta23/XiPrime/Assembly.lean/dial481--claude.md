---
{
  "module": "Zeta23/XiPrime/Assembly.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Assembly.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Assembly.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Assembly.lean — composing the ξ′ interface propositions into the fixed-λ theorem.
See Zeta23/XiPrime/Statement.lean for the Props.

  §A1  CoeffMoments ∧ XiTraceTransfer ⟹ GzMoments            (pure eventually-algebra)
  §A2  GzMoments (flat family Pf := fun _ => P) + H-RvM for Z ⟹ the two fixed-λ certificate bounds
       (2 − κ − ε)N ≤ N₀ˢ and (3/2 − κ/2 − ε)N ≤ N_d, for an ABSTRACT Z : ZeroConfig — a copy of
       Zeta23.FinalMult.thmBmult_abstract / thmCmult_abstract with (i) the moments taken as the hypothesis
       GzMoments instead of being derived from ThmTracesHyp + H-EF, and (ii) PaperInputs replaced by the one
       field actually used on the zero side, RiemannVonMangoldt Z (local count ⟹ prop:tail package and NII;
       main ⟹ N → ∞ and the o(N) calculus).  The zero side (BlockInputs, TailInputs, seamA_mult2/3,
       count_certificate, count_certificate_c3) is the tree's, verbatim, generic in Z.
  §A3  The analogue for a height family Pf (e.g. P.atV v), via the Pf-generic (function-abstract)
       count_certificate of CertificateFn, whose proof only ever touches the two real numbers
       rtrace/frobSq of Ĝ(T).
-/
```

 ## §A1. moments of M̂ᵀ + trace transfer ⟹ moments of Ĝ¹ 

### `kappa_nonneg_of_coeffMoments`

 κ in CoeffMoments is automatically ≥ 0: ‖M̂ᵀ‖_F² ≥ 0 and N(T,2T) → ∞ (H-RvM), so (κ+δ)N ≥ 0 for
every δ > 0 at some large T.  (Removes the "0 ≤ κ" side input of gzMoments_of_transfer downstream.) 

### `kappa_nonneg_of_gzMoments`

 same for GzMoments. 

 ## §A2. The fixed-λ certificate bounds from GzMoments, flat family, abstract Z 

### `eventually_tailPackage_of_rvm`

 prop:tail package for Z from the LOCAL COUNT alone (Zeta23.Tail.eventually_tailPackage takes the whole
PaperInputs bundle but uses only RvM.local_count; this is that proof with the bundle opened). 

### `eventually_side_conditions_of_rvm`

 the two zero-side side conditions the endgame needs, from RvM.local_count and the taper facts. 

### `simple_bound_of_gzMoments`

 **(2 − κ − ε)·N(T,2T) ≤ N₀ˢ(T,2T)** at fixed λ ∈ (0,1), flat window, abstract Z, from GzMoments. 

### `dist_bound_of_gzMoments`

 **(3/2 − κ/2 − ε)·N(T,2T) ≤ N_d(T,2T)** at fixed λ ∈ (0,1), flat window, abstract Z, from GzMoments. 

 ## §A3. The fixed-λ certificate bounds from GzMoments for a HEIGHT FAMILY Pf (quartic window etc.)

The window at height T is (Pf T).phi T (Defs.Params.atV realises a profile v on the taper).  The zero side
is consumed per height exactly as in §A2, through the three facts below (pattern:
Zeta23/ThmD/ZeroSideD.lean for P.atD), and the certificate algebra is CertificateFn's function-abstract copy. 

### `WindowZeroSide`

 **The zero-side facts for a height-indexed window family** that the c = 2, 3 seams consume at heights
T → ∞ (the instance for Pf := P.atV vQuartic is built in XiPrime/QuarticWindow.lean from an
Zeta23.AdmWindow instance for φ_v := √(v(u/L))·φ, as ZeroSideD does for φ_D):
  lam_eq, w_eq — the family shares λ and w (hence L, X, d, τ_k) with P;
  poisson      — lem:poisson ★ for the window at height T (ZeroSide.PoissonSq T (Pf T));
  tail         — the prop:tail package for (Pf T) at height T with the standard rate θ₀ ≤ C·l·T^{λ/2−1}
                 (from RvM.local_count of Z and the decay ‖φ̂_v(r−iy)‖ ≤ e^{L/4}‖φ_v″‖₁/|r−iy|², as
                 Tail.TailHyp.tailInputs / ZeroSideD.eventually_tailPackageD);
  a_half       — a(T) = (1/L)∫φ_v² ≥ 1/2 eventually (v ≥ 27/40 on the window suffices for vQuartic). 

### `windowZeroSide_flat`

 the flat family fun _ => P satisfies WindowZeroSide (so §A2 is the special case). 

### `family_tail_package`

 the common o(1) bookkeeping for the tail size B(T) := θ₀(T)/(a(T)L(T)) of a family. 

### `simple_bound_of_gzMoments_family`

 **(2 − κ − ε)·N(T,2T) ≤ N₀ˢ(T,2T)** at fixed λ ∈ (0,1) for a window FAMILY, abstract Z, from GzMoments. 

### `dist_bound_of_gzMoments_family`

 **(3/2 − κ/2 − ε)·N(T,2T) ≤ N_d(T,2T)** at fixed λ for a window FAMILY, abstract Z, from GzMoments. 

 ## §A2′. Instantiation at the zeros of ξ′: FixedLamBounds from the four component Props (flat window) 

### `fixedLam_flat`

 **[XF′ Thm 8.2] at fixed λ, flat window, from the interface Props.**  Every undischarged classical
input is an explicit binder: (F2) hF2, the seam hs, H-RvM for ξ′ hR; the analytic content arrives as the
three interface propositions instantiated at Z := xiDerivZeros hF2 hs and the flat family fun _ => P. 

### `fixedLam_family`

 **[XF′ Thm 8.2] at fixed λ for a window family Pf (e.g. (paramsOf ϱ lam).atV vQuartic) and profile v,
from the interface Props + the family's zero-side facts (`WindowZeroSide`).** 

### `headline_of_strict`

 ε-free decimals from a strict certified inequality at one λ (used by Final.lean with CertFlat /
CertQuartic): if c < 2 − κ and cd < 3/2 − κ/2 strictly and the fixed-λ bounds hold for κ, then
c·N ≤ N₀ˢ and cd·N ≤ N_d eventually. 

 ## §A2″. Interval additivity and the cumulative (0,T] form for the ξ′ configuration
(pattern: Zeta23/Main.lean cumulative_of_dyadic; Zeta23.Assembly.dyadic is generic). 

### `tendsto_Ncount_zero_atTop`

 H-RvM for ξ′ ⇒ N_{ξ′}(0,T) → ∞. 

### `cumulative_of_dyadic`

 dyadic summation for one interval-additive count f against N_{ξ′}. 

### `cumulative_of_fixedLam`

 the fixed-λ pair of ε-bounds on dyadic windows ⇒ the same pair on (0,T]. 

 ## §A4. The Z′ layer: the same assembly at Z := wZeros hZ hs (zeros of W = ζ′ + L₂ζ with |Im| ≥ t₀)
[XF′ §9].  Everything in §A1–§A3 is generic in Z; only the count seam differs (wZeros_N/_N0s/_Nd need
t₀ ≤ T, Statement §6), so the W headline holds for T ≥ max T₀ t₀.  Constants: wCoeffFamily has the same
density D₁, hence the same κ₁(λ, v) and the same certificates CertFlat / CertQuartic. 

### `fixedLam_family_W`

 **[XF′ Thm 9.4] at fixed λ, window family Pf, from the interface Props instantiated at wZeros.** 
