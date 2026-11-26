---
{
  "module": "Zeta23/Assembly.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Assembly.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Assembly.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Part of the Zeta23 formalization of
  "More than two thirds of the zeros of the Riemann zeta function lie on the critical line".
-/
```


# §4 "The counting inequalities" and §6 "Proofs of Theorems A, B, C" — assembly

Reference: the paper, labels `prop:zeroside-rank`, `eq:zeroside-rank`,
`prop:zeroside`, `eq:zeroside`, `eq:zeroside2`, and `sec:proofs` (proofs of `thm:A`, `thm:B`, `thm:C`).

Design:
* Parts A–E of this file are **ζ-free and Defs-free**: theorems about Hermitian matrices
  (Part A, consuming the `RHLinalg` §3 lemmas) and about real numbers / explicit real
  functions (Parts B–E).  Every analytic or combinatorial input produced elsewhere
  (prop:block — `ZeroSide.lean`; prop:tail — `Tail.lean`; thm:traces — `PrimeSideTemp.lean`'s
  `TracesBounds`; Riemann–von Mangoldt and the local count — `Hypotheses.lean`; taper facts —
  `Taper.lean`) enters as an explicit, named hypothesis whose docstring quotes the paper label.
* Part F instantiates A–E with the concrete objects of `Defs.lean`: `thmA_abstract`, `thmB_abstract`,
  `thmC_abstract` (Theorems A–C at fixed `λ < 1` for an abstract `ZeroConfig`, taking prop:block / prop:tail /
  the H-EF bridge / [eq:abdef] / thm:traces as named inputs).
* Error terms are explicit inequalities with named constants throughout Parts A–D; filters /
  `Tendsto` appear only in the final `ε`-wrappers (Part E).

## Units (paper §4, [eq:AE], [eq:hatunits])

Three normalisations of the same real-symmetric `d × d` matrix occur:
* `G` [eq:Gdef];
* `G̃ = G / L`, `Ã = A / L`, `Ẽ = E / L` ("tilde units") — lem:weyl and lem:CS are applied to
  `G̃ = Ã + Ẽ` with threshold `θ = θ₀ ≥ ‖Ẽ‖` (prop:zeroside);
* `Ĝ = G / (a L²)`, `Â`, `Ê` ("hat units", [eq:hatunits]) — lem:ranktrace is applied to `Â = P + Q`
  **only** in these units (paper, after prop:zeroside-rank: "Lemma lem:ranktrace is not
  scale-invariant: it must be applied in the units (eq:hatunits), in which tr P ≤ N_on(I′)").
The two systems meet only through the explicit conversion of Part D,
`tr Ĝ = tr G̃ /(aL)`, `‖Ĝ‖_F² = tr G̃² /(aL)²` (paper §6, first line of the proof of Thm A), and the
taper constant `a` must cancel in `tr Ĝ = N + O(√X / a)`.

Scalar field: `ZeroSide.lean` works over `ℂ` (the inertia argument lives on `ℂ^d`); Part A is kept
`RCLike`-generic like `RHLinalg` and is instantiated at `ℂ` in Part F.


 ## Part A.  Matrix-level counting inequalities (paper §4, "The counting inequalities") 

### `posIndex_le_rank`

 For any Hermitian matrix, `n₊(A) ≤ rank A` (positive eigenvalues are nonzero eigenvalues).
Used in prop:zeroside: "`n₊^θ(G̃) ≤ n₊(Ã) ≤ rank Ã ≤ #𝒵(I′)`". 

### `zeroside_rank_core`

 **prop:zeroside-rank, first assertion** (the paper, `prop:zeroside-rank`):
"`s₁ + s₂ ≥ 4 tr Â − 2 N(I′) − ‖Â‖_F²`".

Stated over the abstract output of prop:block(ii) — `Â = P + Q`, `P ⪰ 0`, `rank P ≤ r`
(paper: `r = s₁+s₂`), `tr P ≤ N_on(I′)`, `Q` Hermitian with `n₊(Q) ≤ b` (paper: `b = p`) — together
with the counting fact `N_on(I′) + 2p ≤ N(I′)` ([eq:Ncount] and the line after it).  Proof exactly as
in the paper: lem:ranktrace at `c = 2` (`RHLinalg.rank_trace_ineq_two`) gives
`r ≥ 2 tr P + 4 tr Q − 4b − ‖P+Q‖_F² = 4 tr Â − 2(tr P + 2b) − ‖Â‖_F²`, and `tr P + 2b ≤ N(I′)`.

UNITS: hat units `Â = A/(aL²)` only [eq:hatunits]. 

 ### Frobenius-norm bookkeeping

`RHLinalg.frobSq A = Re tr(Aᴴ A)`.  We identify it with the square of Mathlib's (scoped) Frobenius
norm, to get the triangle inequality `‖Ĝ − Ê‖_F ≤ ‖Ĝ‖_F + ‖Ê‖_F` used in prop:zeroside-rank. 

### `frobSq_eq_norm_sq`

 `RHLinalg.frobSq A = ‖A‖_F ²` (Mathlib's Frobenius norm, scoped instance). 

### `norm_eq_sqrt_frobSq`

 `‖A‖_F = √(frobSq A)`. 

### `frobSq_sub_le`

 Triangle inequality in the form used by prop:zeroside-rank:
`‖G − E‖_F² ≤ (‖G‖_F + ‖E‖_F)²`, written with `frobSq` and `√`. 

### `four_tr_sub_frobSq_perturb`

 **prop:zeroside-rank, perturbation step** (proof of `prop:zeroside-rank` in the paper):
"`Â = Ĝ − Ê` with `|tr Ê| ≤ ‖Ê‖₁` and `‖Â‖_F ≤ ‖Ĝ‖_F + ‖Ê‖_F ≤ ‖Ĝ‖_F + ‖Ê‖₁`, so …
`4 tr Â − ‖Â‖_F² ≥ 4 tr Ĝ − ‖Ĝ‖_F² − O(θ₀ L⁻¹ (1 + ‖Ĝ‖_F))`".

Here the `O(·)` is made explicit: with `B ≥ 0` any common bound for `|tr Ê|` and `‖Ê‖_F`
(prop:tail supplies `B = ‖Ê‖₁ ≤ 2θ₀/L`), the loss is exactly `B (4 + 2‖Ĝ‖_F + B)`.
UNITS: hat units. 

### `zeroside_core`

 **prop:zeroside, [eq:zeroside]** (the paper's `prop:zeroside`): "For every `θ ≥ θ₀`,
`s₁ ≥ 2 n₊^θ(G̃) − N(I′)` and `#𝒵(I′) ≥ n₊^θ(G̃)`."

Inputs, as in the paper's proof: lem:weyl (`RHLinalg.weyl_posIndexAbove_le`, needs
`|λᵢ(Ẽ)| ≤ θ` for all `i`, which is `‖Ẽ‖ ≤ θ₀ ≤ θ`), prop:block(i) (`n₊(Ã) ≤ s₁+s₂+p`,
`rank Ã ≤ #𝒵(I′)`), and [eq:Ncount] (`N(I′) ≥ s₁ + 2s₂ + 2p`).
UNITS: tilde units `G̃ = Ã + Ẽ`. 

### `posIndexAbove_congr`

 `posIndexAbove` depends only on the matrix, not on the particular Hermitian-ness proof
(convenience for rewriting `G̃ = Ã + Ẽ`). 

### `nplus_lower`

 **[eq:nplus-lower]** (proof of `thm:B` in the paper): lem:CS (`RHLinalg.cauchySchwarz_count`)
applied to `R = G̃`, `θ = θ₀`: if `tr G̃ > θ₀ d` then
`n₊^{θ₀}(G̃) ≥ (tr G̃ − θ₀ d)² / tr G̃²`.  (`d = Fintype.card n`; `tr G̃² = ‖G̃‖_F² = frobSq G̃` for
Hermitian `G̃`.  This is `cauchySchwarz_count` verbatim, re-exported under the paper's equation
name.)  UNITS: tilde units. 

 ## Part B.  The functions `H`, `F` and the `λ₁` versus `λ` step (paper [eq:Fdef], §6)

Vocabulary from `Zeta23/Defs.lean`: `l T = log(T/2π)`, `ell1 T = l T + 2 log 2 − 1`, `Hfun`, `Ffun`,
`P.L T = P.lam * l T`, `P.lam1 T = P.L T / ell1 T`. 

### `c₀`

 The constant `c₀ := 2 log 2 − 1 = ℓ₁ − l` (paper §1 Notation / [eq:RvM]); `0 < c₀ < 1`. 

### `lam1_eq`

 `λ₁ = λ l / (l + c₀)` — unfolded form of `Params.lam1` [eq:ratio]. 

### `lam1_le`

 `0 ≤ λ − λ₁`, i.e. `λ₁ ≤ λ` (paper §6: "`0 ≤ λ − λ₁ ≤ λ/l`"), for `l > 0`, `λ ≥ 0`. 

### `sub_lam1_le`

 `λ − λ₁ ≤ λ / l` (paper §6); indeed `λ − λ₁ = λ c₀/(l + c₀)` with `c₀ < 1`. 

### `Hfun_lam1_ge`

 **`H(λ₁) ≥ H(λ) − 1/(λ l)`** (the paper §6, proof of Thm A: "Since `H′(x) = x⁻² − 1/3 ∈ (0,∞)`
is decreasing on `(0,1]` and `0 ≤ λ − λ₁ ≤ λ/l`, we have `H(λ₁) ≥ H(λ) − 1/(λl)`").
We prove it via the exact identity `H(λ) − H(λ₁) = c₀/(λ l) − (λ − λ₁)/3` and `c₀ = 2 log 2 − 1 < 1`.
(Note `λ₁ = L/ℓ₁ ≠ λ`.) 

### `Ffun_sub_le`

 Lipschitz bound for `F` on `[0,1]`: `F(y) − F(x) ≤ y − x` for `0 ≤ x ≤ y ≤ 1`
(paper: "`F′(x) = (1−x²/3)/(1+x²/3)² ∈ (0,1]` on `[0,1]`"), proved by algebra. 

### `Ffun_lam1_ge`

 **`F(λ₁) ≥ F(λ) − 1/l`** (the paper §6, proof of Thm B: "`F′(x) = (1−x²/3)/(1+x²/3)² ∈ (0,1]`
on `[0,1]` and `0 ≤ λ − λ₁ ≤ 1/l`, so `F(λ₁) ≥ F(λ) − 1/l`"). 

### `Hfun_ge_near_one`

 `sup_{λ<1} H(λ) = 2/3`, in the quantitative form used for the `λ → 1⁻` step:
for `λ ∈ [1/2, 1]`, `H(λ) ≥ 2/3 − (5/3)(1 − λ)`. 

### `Ffun_ge_near_one`

 For `λ ∈ [0, 1]`, `F(λ) ≥ 3/4 − (1 − λ)` (for the `λ → 1⁻` step of Thm B/C). 

 ## Part C.  §6 at fixed `T`: the explicit inequality for Theorem A

All quantities are real numbers attached to one fixed `T` (and fixed `λ`, `ϱ`); every error term is
explicit.  Dictionary (paper ↔ arguments): `N = N(T,2T)`, `NII = N(I′∖I) := N(T−D₀,T) + N(2T,2T+D₀)`,
`N0star = N₀*(T,2T)`, `s12 = s₁ + s₂`, `trGh = tr Ĝ`, `frGh = ‖Ĝ‖_F²`, `trAh = tr Â`,
`frAh = ‖Â‖_F²`, `B` = the prop:tail bound for `|tr Ê|` and `‖Ê‖_F` (`≤ 2θ₀/L`). 

### `N0star_lower_explicit`

 **[eq:zeroside-rank] made explicit** (the paper `prop:zeroside-rank`, second assertion):
"`N₀*(T,2T) ≥ 4 tr Ĝ − ‖Ĝ‖_F² − 2N(T,2T) − O(θ₀L⁻¹(1+‖Ĝ‖_F) + D₀ l)`", here with the `O(·)`
replaced by the explicit `3 N(I′∖I) + B(4 + 2‖Ĝ‖_F + B)`.
Inputs: `hcount` = "`s₁+s₂ ≤ N₀*(T,2T) + N(I′∖I)`"; `hcore` = `zeroside_rank_core` with
`N(I′) = N(T,2T) + N(I′∖I)`; `hpert` = `four_tr_sub_frobSq_perturb`. 

### `N0star_lower_H`

 **§6 proof of Thm A, the "`(H(λ₁) − O(𝓔′_T)) N`" line made explicit.**
With `cλ := 1/λ₁ + λ₁/3` (so `4 − cλ − 2 = H(λ₁)`), if `|tr Ĝ − N| ≤ R₁`
("`tr Ĝ = N + O(√X/a)`") and `‖Ĝ‖_F² ≤ cλ N + R₂` ("`‖Ĝ‖_F² ≤ (1/λ₁+λ₁/3)N(1+O(𝓔′_T))`"), then
`N₀*(T,2T) ≥ H(λ₁) N − [4R₁ + R₂ + 3N(I′∖I) + B(4 + 2√(cλ N + R₂) + B)]`. 

 ## Part D.  Unit conversion `Ĝ ↔ G̃` and the trace inputs
(paper §6, proof of Thm A, first lines: "In the units (eq:hatunits), `tr Ĝ = tr G̃/(aL)` and
`‖Ĝ‖_F² = tr G̃²/(aL)²`. By Proposition prop:trace, `tr Ĝ = N + O(√X/a)` … (note that the taper
constant `a` cancels). By (eq:tr2) … `‖Ĝ‖_F² ≤ … = (1/λ₁ + λ₁/3) N (1 + O(𝓔′_T))`") 

### `tilde_eq`

 `G̃ = L⁻¹ • G` with the scalar written as a real cast. 

### `hat_eq`

 `Ĝ = (aL²)⁻¹ • G` with the scalar written as a real cast [eq:hatunits]. 

### `hat_eq_smul_tilde`

 `Ĝ = (aL)⁻¹ • G̃`: hat units are tilde units divided by `aL` ([eq:hatunits] vs [eq:Gdef]). 

### `rtrace_hat`

 "`tr Ĝ = tr G̃ /(aL)`" (paper §6). 

### `frobSq_hat`

 "`‖Ĝ‖_F² = tr G̃² /(aL)²`" (paper §6), with `tr G̃² = ‖G̃‖_F²`. 

### `rtrace_tilde_Gp`

 The prime-side trace computed entrywise: `rtrace (G̃ᵖʳⁱᵐᵉ) = P.trGtilde T`
(Defs: `trGtilde := L⁻¹ Σ_k G_{kk}`). 

### `frobSq_tilde_Gp`

 The prime-side Frobenius norm computed entrywise: `frobSq (G̃ᵖʳⁱᵐᵉ) = P.trGtildeSq T`
(Defs: `trGtildeSq := (L⁻¹)² Σ_{k,l} G_{kl}²`). 

### `trGhat_sub_N_le`

 **"`tr Ĝ = N + O(√X/a)` (note that the taper constant `a` cancels)"** (paper §6 / prop:trace).
From [eq:tr1] first form `|tr G̃ − a L N| ≤ C·L·√X`:
`|tr G̃/(aL) − N| ≤ C √X / a` — the main term is exactly `N`, independent of `a`. 

### `mainTr2_hat_identity`

 The algebra behind "`‖Ĝ‖_F² ≤ (T/(2πLa²))(ℓ₁² + L²/3)(1+O(𝓔′)) = … = (1/λ₁ + λ₁/3) N (1+O(𝓔′))`":
`(aL)⁻² · (TL/2π)(ℓ₁² + L²/3) = a⁻² · (1/λ₁ + λ₁/3) · (Tℓ₁/2π)` exactly, where `λ₁ = L/ℓ₁`. 

### `frobGhat_le`

 **"`‖Ĝ‖_F² ≤ (1/λ₁ + λ₁/3) N (1 + O(𝓔′_T))`" made explicit.**  From [eq:tr2] (second form,
upper half) `tr G̃² ≤ (1 + C𝓔)(TL/2π)(ℓ₁² + L²/3)` and Riemann–von Mangoldt in the form
`Tℓ₁/2π ≤ N + R_N` [eq:RvM], with `K := (1 + C𝓔)/a²` and `cλ := 1/λ₁ + λ₁/3`:
`‖Ĝ‖_F² = tr G̃²/(aL)² ≤ cλ N + cλ((K − 1) N + K R_N)`.  (The second summand is the explicit `R₂`.) 

 ## Part E.  The asymptotic wrappers (the only place filters appear)

E1: the explicit error of Parts C–D is `o(N)` given the growth facts;  E2: `o(N)` error ⇒ `ε`-form;
E3: `λ → 1⁻`;  E4: dyadic summation `N₀*(T,2T) ⇒ N₀*(T)` (paper §6, end of proof of Thm A). 

### `eps_form_of_isLittleO`

 E2. An `o(N)` error term yields the `ε`-form. 

### `err_isLittleO`

 E1. The explicit error term of `N0star_lower_H` is `o(N)`, given:
`N → ∞`; `R₁, R₂, N(I′∖I) = o(N)`; `B → 0`; `cλ = 1/λ₁ + λ₁/3` eventually in `[0, K]`. 

### `eps_form_sup_half`

 **sup over λ ∈ [1/2, 1)** (the common `λ → 1⁻` step): if the `ε`-form holds with constant `c(λ)`
for every `λ ∈ [1/2, 1)` and `C − η ≤ c(λ)` for some such `λ`, for every `η > 0`, then it holds with constant `C`. 

### `exists_lam_near_one`

 a point of `[1/2, 1)` within `δ` of `1`. 

### `eps_form_twoThirds`

 E3. The `λ → 1⁻` step: if for every `λ ∈ [1/2, 1)` the `ε`-form holds with
constant `H(λ)`, then it holds with constant `2/3 = sup_{λ<1} H(λ)`. 

### `eps_form_threeQuarters`

 Same for `F`: constant `3/4 = sup_{λ<1} F(λ)` (Thm C), given the `ε`-forms with `F(λ)`. 

### `eps_form_half`

 Same for `2F − 1`: constant `1/2 = sup_{λ<1} (2F(λ) − 1)` (Thm B). 

### `dyadic`

 E4. **Dyadic summation** (the paper §6, end of the proof of Thm A: "the statement for
`N₀*(T)/N(T)` by summing over dyadic intervals: given `ε>0` choose `T₁` with
`N₀*(t,2t) ≥ (2/3−ε)N(t,2t)` for `t ≥ T₁`; for `T ≥ 2T₁` and `J` maximal with `T2^{−J} ≥ T₁`,
`N₀*(T) ≥ Σ_{j=1}^{J} N₀*(T2^{−j},T2^{−j+1}) ≥ (2/3−ε)(N(T)−N(T2^{−J})) ≥ (2/3−ε)N(T) − O_ε(1)`.")
Abstract form: `f, g` interval-additive and nonnegative, `g(0,T) → ∞`. 

 ## Part F.  Instantiation with the concrete objects of `Defs.lean`

F2: growth lemmas for the explicit functions `l, L, X` and for `N(T,2T)` under H-RvM;
F3: `thmA_abstract` — Theorem A at fixed `λ < 1` for an abstract `ZeroConfig`, from the named inputs. 

### `tendsto_l_atTop`

 `l(T) = log(T/2π) → ∞`. 

### `tendsto_L_atTop`

 `L = λ l → ∞` for `λ > 0`. 

### `log_eq_l_add`

 `log T = l T + log 2π` for `T > 0`. 

### `eventually_log_le_two_l`

 `log T ≤ 2 l T` eventually. 

### `tendsto_Tl_atTop`

 `T l(T) → ∞`. 

### `eventually_N_ge`

 H-RvM ⇒ `N(T,2T) ≥ T l /(4π)` eventually.  ([eq:RvM]: `N = Tℓ₁/2π + O(log T)`, `ℓ₁ ≥ l`.) 

### `eventually_N_le`

 H-RvM ⇒ `N(T,2T) ≤ T l` eventually. 

### `tendsto_N_atTop`

 H-RvM ⇒ `N(T,2T) → ∞`. 

### `isLittleO_N_of_isLittleO_Tl`

 `T l = O(N)` under H-RvM, so `o(T l) ⊆ o(N)`. 

### `isLittleO_l_Tl`

 `l = o(T l)`. 

### `isLittleO_log_Tl`

 `log T = o(T l)`. 

### `isLittleO_sqrt_mul_l_Tl`

 `√T · l = o(T l)`. 

### `sqrtX_eq`

 `√X = (T/2π)^{λ/2}` ("`X = e^L = (T/2π)^λ`", §1 Notation). 

### `isLittleO_sqrtX_Tl`

 `√X = (T/2π)^{λ/2} = o(T l)` for `λ ≤ 1` (indeed for `λ < 2`). 

### `tendsto_theta_over_L`

 `l · T^{λ/2−1} / L = T^{λ/2−1}/λ → 0` (the size of `θ₀/L`, prop:tail). 

### `eventually_clam_bounds`

 `cλ = 1/λ₁ + λ₁/3` is eventually in `[0, 2/λ + 1/3]` (since `λ/2 ≤ λ₁ ≤ λ ≤ 1` once `l ≥ c₀`). 

### `tendsto_a_one`

 `a → 1` from [eq:abdef] `1 − 2w/L ≤ a ≤ 1` and `L → ∞`. 

 ### F0.  Window bookkeeping for an abstract `ZeroConfig` (interval additivity; the four
"set-level" facts of prop:zeroside-rank / prop:zeroside:
`s₁+s₂ ≤ N₀*(T,2T) + N(I′∖I)`, `s₁ ≤ N₀ˢ(T,2T) + N(I′∖I)`, `#𝒵(I′) ≤ N_d(T,2T) + N(I′∖I)`,
`N(I′) = N(T,2T) + N(I′∖I)`, where `N(I′∖I) := N(T−D₀,T) + N(2T,2T+D₀)`). 

### `N_add`

 Interval additivity of `N` (with multiplicity). 

### `Nd_add`

 Interval additivity of `N_d`. 

### `N0star_add`

 Interval additivity of `N₀*`. 

### `N0s_add`

 Interval additivity of `N₀ˢ`. 

### `NIprime_eq`

 "`N(I′) = N(T,2T) + N(I′∖I)`" (proof of prop:zeroside-rank). 

### `s1_add_s2_eq`

 `𝒮₁ ∪ 𝒮₂ = 𝒵(I′) ∩ {β = 1/2}` (every zero has `m_ρ ≥ 1`), hence
"`s₁ + s₂` = number of distinct on-line zeros with ordinate in `I′`" `= N₀*(T−D₀, 2T+D₀)`. 

### `s1_add_s2_le`

 "`s₁ + s₂ ≤ N₀*(T,2T) + N(I′∖I)`" (proof of prop:zeroside-rank). 

### `s1_le`

 "`s₁ ≤ N₀ˢ(T,2T) + N(I′∖I)`" (proof of prop:zeroside); `s₁ = N₀ˢ` over `I′` by definition. 

### `card_ZIprime_le`

 "`#𝒵(I′) ≤ N_d(T,2T) + N(I′∖I)`" (proof of prop:zeroside). 

 ### F1.  Fixed-`T` assembly with the concrete matrices `Ĝ = P.hat T (Z.Gz P T)` etc.

The inputs from prop:block (ZeroSide.lean) and prop:tail (Tail.lean) are packaged as the two
Prop-structures below, whose fields are exactly the statements those files announce; they are
discharged in those files' instantiation sections. 

### `seamA`

 **Seam A — [eq:zeroside-rank], explicit, for the concrete matrices.**  For `T ≥ 0`, with
`Ĝ := P.hat T (Z.Gz P T)`, `B₀ := θ₀/(aL)`, `N(I′∖I) = NII Z T`:
`4 tr Ĝ − ‖Ĝ‖_F² − 2N(T,2T) − 3N(I′∖I) − B₀(4 + 2‖Ĝ‖_F + B₀) ≤ N₀*(T,2T)`. 

### `seamA_BC`

 **Seam A for Theorems B, C — [eq:zeroside2], for the concrete matrices.**  For `T ≥ 0` and
`θ ≥ θ₀`: `2 n₊^θ(G̃) − N(T,2T) − 2N(I′∖I) ≤ N₀ˢ(T,2T)` and `n₊^θ(G̃) − N(I′∖I) ≤ N_d(T,2T)`. 

### `seamB`

 **Seam B — the trace inputs in hat units, for the concrete matrices**, given the H-EF bridge
`Z.Gz P T = P.Gp T` (zero side = prime side, [eq:Gdef] "the two expressions agreeing by
Proposition prop:EF"), [eq:tr1]/[eq:tr2] at height `T` with constants `C₁, C₂`, and [eq:RvM] at `T`
in the form `Tℓ₁/2π ≤ N + R_N`:
`|tr Ĝ − N| ≤ C₁√X/a` (the taper constant cancels in the main term) and
`‖Ĝ‖_F² ≤ cλ N + cλ((K−1)N + K R_N)`, `K = (1 + C₂𝓔_T)/a²`, `cλ = 1/λ₁ + λ₁/3`. 

 ### F3.  Theorem A at fixed `λ < 1` for an abstract zero configuration

The theorems are proved over an abstract error function `Err` (only: eventually nonnegative and
`→ 0`) in place of the concrete `Params.calE` — the `_err` versions below — so that alternative
prime-side chains (e.g. an MV-free one with an enlarged error) plug in directly; the
`calE` statements are kept as specializations. 

### `isLittleO_of_tendsto_zero_mul`

 little-o from a factor tending to zero. 

### `isBigO_one_of_abs_le`

 `O(1)` from an eventual absolute bound. 

### `isLittleO_of_bdd_mul`

 `O(1) · o(N) = o(N)`. 

### `thmA_abstract_err`

 **Theorem A at fixed `λ ∈ (0,1)`, for an abstract zero configuration** ([thm:A] with
§6's proof, in `ε`-form):
for every `ε > 0`, `N₀*(T,2T) ≥ (H(λ) − ε) N(T,2T)` for all `T ≥ T₀`.

Genuine hypotheses: the published inputs `H : PaperInputs Z` (only H-RvM is used directly here;
the others enter through the inputs below) and the thm:traces package
`hTr : ThmTracesHyp P Z`.
Named inputs:
`hBlock` (prop:block, ZeroSide), `hTail`/`hθ₀` (prop:tail, Tail), `hNII` (boundary count
`N(I′∖I) ≪ D₀ l`, Tail), `hGzGp` (the H-EF bridge `G^{zero} = G^{prime}`, [eq:Gdef]), `ha` ([eq:abdef],
Taper), `hcalE` (`𝓔_T → 0`, PrimeSideB). 

### `thmA_abstract`

 **Theorem A at fixed `λ ∈ (0,1)`, abstract zero configuration** — the `Err := P.calE`
specialization of `thmA_abstract_err`. 

 ### F4.  Theorems B and C at fixed `λ < 1` for an abstract zero configuration
(the paper §6, proofs of thm:B and thm:C: [eq:nplus-lower] + [eq:zeroside2]) 

### `isHermitian_ofReal_smul`

 A real-scalar multiple of a Hermitian matrix is Hermitian. 

### `Gp_isHermitian`

 The prime-side matrix `G^{prime}_{kl} = ∫ φ̂(τ−τ_k)φ̂(τ−τ_l)ν_X(τ)dτ` is real symmetric, hence Hermitian
(paper [eq:Gdef]: "The second expression shows that `G` is real symmetric"). 

### `eventually_calE_nonneg`

 `𝓔_T ≥ 0` eventually (all three summands are nonnegative once `L > 0`, `l ≥ 1`, `T > 0`). 

### `Ffun_bounds`

 `0 ≤ F(x) ≤ 1` for `0 ≤ x ≤ 1` (indeed `F(x) ≤ x`). 

### `nplus_ge_explicit`

 The algebra of [eq:nplus-lower]: with `Q := (tr G̃)²/tr G̃²` and `x := θ₀ d / tr G̃`,
"`n₊^{θ₀}(G̃) ≥ (tr G̃ − θ₀ d)²/tr G̃² = Q (1 − x)²`" `≥ Q − 2xQ`; combined with [eq:ratio]
`|Q − F(λ₁)N| ≤ C𝓔F(λ₁)N` this gives `n₊^{θ₀}(G̃) ≥ F(λ₁)N − [C𝓔F(λ₁)N + 2x(1+C𝓔)F(λ₁)N]`. 

### `thmBC_core_err`

 **Theorems B and C at fixed `λ ∈ (0,1)`, for an abstract zero configuration — common core.**
There is `R = o(N)` with, eventually in `T`:  `(2F(λ) − 1)N − 2R ≤ N₀ˢ(T,2T)` and
`F(λ)N − R ≤ N_d(T,2T)`  (paper §6, proofs of thm:B, thm:C: prop:tail `θ₀ ≪ lT^{λ/2−1}`, prop:trace
`tr G̃ ≫ dl` hence `tr G̃ > θ₀d`, lem:CS + [eq:ratio] ⇒ [eq:nplus-lower], then [eq:zeroside2] and
`F(λ₁) ≥ F(λ) − 1/l`).  Same displayed inputs as `thmA_abstract` (without `ha`). 

### `thmBC_core`

 `thmBC_core`, the concrete-rate wrapper: `Err := P.calE`
(the `Err`-parametric generalization is `thmBC_core_err` above). 

### `thmB_abstract`

 **Theorem B at fixed `λ ∈ (0,1)`, abstract zero configuration** (the paper [thm:B], `ε`-form):
`N₀ˢ(T,2T) ≥ (2F(λ) − 1 − ε) N(T,2T)` for `T ≥ T₀`. 

### `thmC_abstract`

 **Theorem C at fixed `λ ∈ (0,1)`, abstract zero configuration** (the paper [thm:C], `ε`-form):
`N_d(T,2T) ≥ (F(λ) − ε) N(T,2T)` for `T ≥ T₀`. 

 ### F5.  `𝓔_T → 0` (paper [thm:traces]: "`𝓔_T ≪_λ w/L + T^{λ−1} log l` (λ<1), `≪ w/L + log l/l` (λ=1)") 

### `X_le_T`

 `X = (T/2π)^λ ≤ T` once `T ≥ 2π` (for `λ ≤ 1`). 

### `calE_tendsto_zero`

 **`𝓔_T → 0`** as `T → ∞`, for fixed `0 < λ ≤ 1` and fixed `w ≥ 0`
(`𝓔_T := w/L + (l²+X) log l/(Tl) + T^{λ/2−1}`, [thm:traces]).  Bound used:
`𝓔_T ≤ w/L + (log T)²/T + log l/l + T^{λ/2−1}` for `T ≥ 2π`, `l ≥ 1`. 
