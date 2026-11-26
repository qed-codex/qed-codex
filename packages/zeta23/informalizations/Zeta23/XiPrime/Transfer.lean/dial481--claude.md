---
{
  "module": "Zeta23/XiPrime/Transfer.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Transfer.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Transfer.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Transfer.lean — ξ′: **XiTraceTransfer** [XF′ Lemma 5.1 + Lemma 6.1].
The target is Zeta23.XiPrime.XiTraceTransfer (XiPrime/Statement.lean §4).

THE STATEMENT PROVED.  In hat units M ↦ M/(aL²), with
  Ĝ¹  := hat (Z.Gz (Pf T) T)                 — zero-side Gram matrix of the configuration Z,
  M   := (Pf T).Gp1 T                          — entry-dependent main term (coefficients C(N; L⋆^{kl})),
  Mᵀ  := (Pf T).GpC T (F.c T)                  — fixed-coefficient prime-side matrix (c^{(T)}_N),
for every δ > 0, eventually in T:
  |tr Ĝ¹ − tr M̂ᵀ| ≤ δ·N(T,2T)   and   ‖Ĝ¹‖_F² ≤ (1+δ)‖M̂ᵀ‖_F² + δ·N(T,2T).

ROUTE.  Write G = Mᵀ + D + E with E := G − M ("entry errors", [XF′ Lemma 5.1]) and D := M − Mᵀ
("entry dependence", [XF′ Lemma 6.1]).  Both are HatNegligible (|tr Â| ≤ ηN and ‖Â‖_F² ≤ η²N for
every η > 0 eventually), and Transfer/Abstract.lean §E turns that into the two displayed lines
(xiTraceTransfer_of_negligible — pure algebra, no analytic input).
  • E (§2): XiEF gives ‖E_{kl}‖ ≤ C T^{−δ}(1/max(1,Δ_{kl}²) + 1/T), Δ_{kl} = (k−l)h; the lattice sum
    Σ_l (1/max(1,Δ²))² ≤ 8(1 + 1/h) (Abstract §D) and d ≤ LT/2π, a ≥ a₀, N ≥ Tl/4π give
    |tr Ê| ≪ T^{1−δ}/L = o(N), ‖Ê‖_F² ≪ T^{1−2δ}/L² = o(N).
  • D (§3): M_{kl} − Mᵀ_{kl} = Q_{kl}(C(·; L_T+δ_{kl}) − c^{(T)}), Q_{kl}(e) := ∫ φ̂_k φ̂_l P_e (the P-part
    Gram entry, linear in e), δ_{kl} = ½ log(τ⋆_{kl}/T) ∈ [0, ½ log 2].  The re-expansion
    C(N; L_T+δ) − c_N = Σ_{r≥1} e_r(N) δ^r separates the (k,l)-dependence: D = Σ_r Δ^{(r)} ∘ Q(e_r);
    Minkowski over r (Abstract §B) with ‖Q(e_r)‖_F² ≤ A (ρ₀/l)^{2r} (aL²)² T l gives
    ‖D̂‖_F² ≪ T/l = o(N); for the trace, the diagonal formula Q_{kk}(e) = 2Σ_N A_φ(log N) N^{−1/2}
    Re(e_N N^{−iτ_k}), Abel summation in k (weights δ_k^r monotone) and the Dirichlet-kernel bound
    A_φ(y)|Σ_{k<K} e^{iτ_k y}| ≤ L²/(2 log 2) give |tr D| ≪ L²√X·l^{O(1)}, |tr D̂| = o(N).

INPUTS of the theorem xiTraceTransfer_of (§5), all named hypotheses:
  P.Valid, P.lam < 1, (Pf T).lam = P.lam ∧ (Pf T).w = P.w   (height-indexed window family over fixed (λ, w);
                                   λ < 1 is needed: PPUpper's r-independent end-effect term is o(N) iff λ < 1)
  LocalHypsCore cϱ ((Pf T).toSetting T) ((Pf T).localFun T) for T ≥ T₁   (taper facts of the window family)
  GammaFacts                       (μ-integrability, to split the prime-side entry)
  ∃ a₀ > 0, ∀ᶠ T, a₀ ≤ (Pf T).a T  (hat units divide by aL²)
  RiemannVonMangoldt Z             (only N(T,2T) ≥ Tl/4π eventually, Assembly.eventually_N_ge)
  XiEF Z Pf                        (Statement.lean §4; only the entrywise norm bound is used)
  0 ≤ ρ₀, Reexpansion F e ρ₀ A T₀  ([XF′ §6] e_r(N), the δ-expansion identity, H1–H3-type bounds)
  PPUpper cϱ P.lam                 (frobSq_Ppart_le, [prop:PP] upper bound, general coefficients)
-/
```

 ## §1. HatNegligible and the algebraic reduction 

### `HatNegligible`

 a height-indexed matrix family A_T is negligible in hat units against N(T,2T):
for every η > 0, eventually |tr Â_T| ≤ η N and ‖Â_T‖_F² ≤ η² N. 

### `HatNegligible.add`

 HatNegligible families form an additive class. 

### `HatNegligible.congr`

 a family congruent to a HatNegligible one is HatNegligible. 

### `xiTraceTransfer_of_negligible₁`

 **the algebra, one piece**: if G − Mᵀ is HatNegligible then XiTraceTransfer holds. 

### `xiTraceTransfer_of_negligible`

 **[XF′ Lemma 5.1 + 6.1 ⇒ XiTraceTransfer], the algebra**: if both E = G − M and D = M − Mᵀ are
HatNegligible then XiTraceTransfer holds. 

 ## §2. [XF′ Lemma 5.1]: the entry errors E = G¹ − M are HatNegligible 

### `fam_L`

 scalars of the family that depend only on (λ, T) agree with those of P. 

### `entryError_bounds`

 **[XF′ Lemma 5.1] at fixed T** (explicit): from the entrywise bound of XiEF,
|tr E| ≤ d·C T^{−δ}(1 + 1/T)  and  ‖E‖_F² ≤ 2(C T^{−δ})²(8d(1 + 1/h) + d²/T²). 

### `rtrace_hat'`

 rtrace / frobSq in hat units. 

### `hatNegligible_of_entryBound`

 **[XF′ Lemma 5.1], for any entrywise main term** M_T with the XiEF/WEF error shape:
‖G_{kl} − M_{kl}‖ ≤ C T^{−δ}(1/max(1,Δ²_{kl}) + 1/T) for T ≥ T₀  ⇒  G − M is HatNegligible. 

### `hatNegligible_entryError`

 **[XF′ Lemma 5.1]**: from XiEF, E = G¹ − M is HatNegligible. 

 ## §3. [XF′ Lemma 6.1]: the entry dependence D = M − Mᵀ is HatNegligible 

### `Lstar_eq_LT_add`

 L⋆(τ⋆) = L_T + ½ log(τ⋆/T) for T, τ⋆ > 0. 

### `d_mul_hgrid_le`

 d·h ≤ T (d = ⌊LT/2π⌋, h = 2π/L). 

### `deltaKL_mem`

 0 ≤ δ_{kl} ≤ 1/2 for grid indices 0 ≤ k, l < d. 

### `deltaKL_diag_monotone`

 k ↦ δ_{kk} = ½ log(τ_k/T) is monotone. 

### `tendsto_lpow_mul_X_div`

 l^n · X / T → 0 for λ < 1 (X = (T/2π)^λ, l = log(T/2π)). 

### `ReexpansionAt`

 **base-generic re-expansion input** (the five fields of Transfer/Inputs.lean's Reexpansion with the base
point Λ₀(T) and the frozen coefficients c(T) as parameters): ξ′ is Λ₀ = LT, c = xiCoeffFamily.c (Reexpansion.toAt);
Z′ is Λ₀ = ½l, c = wCoeffFamily.c (Transfer/W.lean). 

### `ReexpansionGeom`

 the GEOMETRIC form actually consumed by the proof of Lemma 6.1 (derived in §4 from ReexpansionAt +
PPUpper; kept separate so that the analytic argument does not depend on the producers' exact shapes).
For T ≥ T₀ and r ≥ 1, with X = X(T), l = l(T), ρ = ρ₀/l, L = L(T), and the P-part Gram sums over the
window data of Pf T:  the expansion of C(N; L_T+δ) − c_N on δ ∈ [0,1/2] for N ≤ X;  e_r(1) = 0;
S₁(e_r; X) ≤ A ρ^r √X·l;   Σ_{k,l<d} Q_{kl}(e_r)² ≤ A ρ^{2r}·L⁴ T l² + A·L³ l⁴ (1 + X)
(the second, r-independent term is the end-effect term of PPUpper; it is o((aL²)² N) iff λ < 1). 

### `Gp1_sub_GpC_apply`

 the entries of D = M − Mᵀ are P-part entries of the coefficient DIFFERENCES (μ, Π_X cancel). 

### `hatNegligible_of_geom`

 **[XF′ Lemma 6.1], base-generic engine**: a matrix family D whose entries are the P-part entries of the
coefficient differences C(·; Λ₀(T)+δ_{kl}) − c(T) is HatNegligible, given the geometric re-expansion input at Λ₀. 

### `hatNegligible_entryDependence`

 **[XF′ Lemma 6.1]** for ξ′: D = M − Mᵀ (Gp1 vs GpC, base L_T) is HatNegligible. 

 ## §4. Glue: ReexpansionAt + PPUpper ⇒ ReexpansionGeom 

### `reexpansionGeom_of`

 Reexpansion + PPUpper ⇒ the geometric form, with
A' = 4·max(C,1)·max(A,1)² and T₀' large (L ≥ 1, l ≥ max(1,ρ₀), 2 ≤ X ≤ T, T past all thresholds). 

 ## §5. The main theorem of this file 

### `xiTraceTransfer_of`

 **XiTraceTransfer** [XF′ Lemma 5.1 + Lemma 6.1] from the named inputs. 

 ## §6. The flat-window instance (Pf := fun _ => P): the family hypotheses discharged from the tree 

### `xiTraceTransfer_of_flat`

 **XiTraceTransfer for the flat window family** Pf = fun _ => P: the taper facts (PrimeSide.localHypsEventually
+ LocalHyps.toCore) and a ≥ 1/2 (Params.half_le_a) come from the tree, so only the genuine inputs remain. 
