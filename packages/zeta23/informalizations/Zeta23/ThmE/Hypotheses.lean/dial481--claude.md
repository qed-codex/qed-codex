---
{
  "module": "Zeta23/ThmE/Hypotheses.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/Hypotheses.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/Hypotheses.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmE/Hypotheses.lean — Theorem E (Dirichlet L-functions), the χ-dependent densities and the
published inputs restated for L(s,χ).

Canonical text: the paper §7.2 [subsec:dirichlet], [thm:E] and its proof, items (i)–(iii), VERBATIM:
"(i) Explicit formula: with κ = (1−χ(−1))/2, Proposition prop:EF holds for
 W_χ(f,g) := Σ_ρ m_ρ h_f(γ_ρ) conj(h_g(conj γ_ρ)) (zeros of L(s,χ)) with ν_X replaced by
 ν_{X,χ} := μ_χ + P_{X,χ},  μ_χ(τ) := (1/2π)[log(q/π) + Re Γ′/Γ(1/4 + κ/2 + iτ/2)],
 P_{X,χ}(τ) := −(1/π) Re Σ_{n≤X} Λ(n)χ(n) n^{−1/2−iτ}, and no pole term (Π_X ≡ 0); the derivation of
 Appendix A applies to [IK04, Theorem 5.12] for L(s,χ). Since ν_{X,χ} is real, G is again real
 symmetric. (ii) Zero side: the multiset of zeros of L(s,χ) is invariant under ρ ↦ 1−ρ̄ with
 multiplicities (functional equation χ ↔ χ̄ composed with conj L(conj s,χ) = L(s,χ̄)), all zeros have
 0<β<1, and N_χ(t+1) − N_χ(t) ≪_q log(t+3); Section 4 is otherwise verbatim. (iii) Prime side:
 |Λ(n)χ(n)| = Λ(n)·1_{(n,q)=1}, so Lemma lem:cheb holds for these coefficients with O_q(·) errors
 (finitely many primes removed); … μ_χ = (1/2π) log(q|τ|/2π) + O(τ⁻²) satisfies (eq:mufacts)–(eq:muints)
 with ℓ₁ replaced by ℓ_{1,χ} := log(qT/2π) + 2log2 − 1, and λ₁ = L/ℓ_{1,χ} → λ as q is fixed."

This file is ζ-free AND L-free: it defines the densities μ_χ, P_{X,χ}, ν_{X,χ}
as explicit real functions of (κ, q, the coefficient character values) and states the hypotheses
for an ABSTRACT `ZeroConfig`; only `Zeta23/ThmE/Statement.lean` mentions Mathlib's
`DirichletCharacter.LFunction`.  Everything the paper derives from these inputs is proved in the sibling files;
this file only states the inputs.
-/
```

 ## 1. The χ-dependent scalars and densities  ([thm:E] proof (i), (iii)) 

### `ell1q`

 `ℓ_{1,χ} := log(qT/2π) + 2 log 2 − 1`  ([thm:E] proof (iii)); for q = 1 this is `Zeta23.ell1`. 

### `muq`

 `μ_χ(τ) := (1/2π)[log(q/π) + Re Γ′/Γ(1/4 + κ/2 + iτ/2)]`  ([thm:E] proof (i)), as a function of the
parity `κ ∈ {0,1}` (`κ = (1−χ(−1))/2`) and the modulus `q`.  For `κ = 0, q = 1` this is `Zeta23.mu`
(since log(1/π) = −log π).  Γ′/Γ = `Complex.digamma`. 

### `PXc`

 `P_{X,χ}(τ) := −(1/π) Re Σ_{n≤X} Λ(n) χ(n) n^{−1/2−iτ}`  ([thm:E] proof (i)), as a function of the
coefficient sequence `c n = χ(n)` (values of the character on ℕ).  Sum over `Finset.Ioc 0 ⌊X⌋₊` as in
`Zeta23.PX`; for `c ≡ 1` this is `Zeta23.PX` since Re n^{−iτ} = cos(τ log n). 

### `nuXc`

 `ν_{X,χ} := μ_χ + P_{X,χ}`, "and no pole term (Π_X ≡ 0)"  ([thm:E] proof (i)). 

### `CoeffOK`

 Admissible coefficient sequences for modulus q ([thm:E] (iii)): unimodular-or-zero character
values, vanishing off (n,q) = 1.  (For χ primitive, c n = χ(n) qualifies.) 

### `CoeffUnimodular`

 Unimodular coefficient sequences: additionally `‖c n‖ = 1` exactly on `(n,q) = 1`, `n > 0`
(true for a primitive χ).  Needed wherever the main term is TWO-sided ([prop:PP]'s diagonal uses
`|χ(n)|² = 1`); the four upper-bound statements only need `CoeffOK`. 

 ## 2. The published inputs, restated for L(s,χ)  (abstract zero configuration Z) 

### `ExplicitFormulaPaperChi`

 **H-EF(χ), paper form** ([thm:E] proof (i) applied to [prop:EF]/[eq:EF]): for f,g ∈ C_c²(ℝ) with
supports in [−L/2, L/2],  W_χ(f,g) = ∫_ℝ h_f(τ) conj(h_g(τ)) ν_{X,χ}(τ) dτ, X = e^L, with the zero sum
absolutely convergent and the integrand integrable (same shape as `Zeta23.ExplicitFormulaPaper`, whose
ν_X is replaced by ν_{X,χ}). 

### `RiemannVonMangoldtChi`

 **H-RvM(χ)**: `N_χ(T,2T) = (T/2π) ℓ_{1,χ} + O_q(log T)` ([thm:E] intro sentence with (iii)'s ℓ_{1,χ};
classical, [Dav00 §16]) and the local count `N_χ(t+1) − N_χ(t) ≪_q log(|t|+3)` ([thm:E] proof (ii)),
two-sided as in `Zeta23.RiemannVonMangoldt`. Constants may depend on q (q is fixed in [thm:E]). 

### `GammaFactsChi`

 **H-Γ(χ)**: "μ_χ = (1/2π)log(q|τ|/2π) + O(τ⁻²) satisfies (eq:mufacts)–(eq:muints) with ℓ₁ replaced
by ℓ_{1,χ}" ([thm:E] proof (iii)) — the nine fields of `Zeta23.GammaFacts` for `muq κ q` and `ell1q q`. 

### `ChebyshevMertensCoprime`

 **The Chebyshev–Mertens bounds for the coefficients Λ(n)χ(n)** ([thm:E] proof (iii): "|Λ(n)χ(n)| =
Λ(n)·1_{(n,q)=1}, so Lemma lem:cheb holds for these coefficients with O_q(·) errors (finitely many
primes removed)").  Since only |a_n| enters, and |χ(n)| ≤ 1, the UPPER bounds of [lem:cheb] hold
verbatim; the two-sided [eq:cheb2] asymptotics need the (n,q)=1 restriction.  Stated here in
hypothesis shape (cf. `Zeta23.Cheb.chebyshevMertens`). 

### `PaperInputsChi`

 The published inputs for Theorem E at parity κ, modulus q, coefficient character values c,
for an abstract zero configuration Z (analogue of `Zeta23.PaperInputs`). 

 ## PXc unfolding lemmas (shared by the Theorem E prime-side files) 

### `natCast_cpow_neg_half_sub_I_mul`

 `n^{−1/2−iτ} = n^{−1/2}·e^{−iτ log n}` for `n ≥ 1`. 

### `exp_neg_I_mul_ofReal`

 `e^{−iθ} = cos θ − i sin θ`, real θ, cast form. 

### `PXc_eq_sum_cos_sin`

 `P_{X,χ}` as a real sum of phase-split cosines/sines, coefficients `(c n).re, (c n).im`:
`P_{X,c}(τ) = −π⁻¹ Σ_{n≤X} Λ(n) n^{−1/2} ((c n).re·cos(τ log n) + (c n).im·sin(τ log n))`. 

 ## Uniform-constant ("Bounded") variants, for the hybrid range [rem:otherL](i):
same fields as `GammaFactsChi` / `ChebyshevMertensCoprime`
but with every existential constant replaced by the given bound, so families of characters can
carry ONE constant uniformly in q. 

### `GammaFactsChiBounded`

 `GammaFactsChi` with all constants bounded by `C` (and all thresholds by `C`). 

### `GammaFactsChiBounded.toGammaFactsChi`

 forgetting the uniformity. 

### `ChebyshevMertensCoprimeBounded`

 `ChebyshevMertensCoprime` with both constants bounded by `B`. 

### `ChebyshevMertensCoprimeBounded.toChebyshevMertensCoprime`

 forgetting the uniformity. 
