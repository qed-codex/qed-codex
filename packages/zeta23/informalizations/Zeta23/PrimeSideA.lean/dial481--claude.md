---
{
  "module": "Zeta23/PrimeSideA.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideA.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideA.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

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


# Prime side, part A — paper §5 [sec:prime]:  [prop:trace], [lem:ends], [eq:Msplit], [prop:mumu], [prop:cross]

Seam with `PrimeSideB.lean` ([prop:PP], [thm:traces]): see the header of
`Zeta23/PrimeSideA/Defs.lean`.  Everything here is ζ-free: the zeros never
appear in §5 ("In this section the zeros play no role", §5); `N(T,2T)` enters [prop:trace]
only through [eq:muints] + [eq:RvM], which we take as hypotheses on an abstract real `N`.

## Shape of the results
All error terms are explicit inequalities, uniform in `T`:
  `∃ C, EventuallyAt cϱ lam (fun p F => |lhs p F − main p F| ≤ C * err p)`
where `EventuallyAt cϱ lam P` means: there is `T₀` such that `P p F` holds for every parameter set
`p` with `p.lam = lam`, `T₀ ≤ p.T` and every taper datum `F` satisfying `LocalHyps cϱ p F`.
So `C` and `T₀` may depend on `c_ϱ`, on the constants inside H-Γ/H-cheb, and on `λ` — the paper
has `C` depending on ϱ only and `T₀ = T₀(λ)` (§5.5); ours is the (weaker, sufficient at fixed λ)
reading.  This is a deviation from the paper.

## Hypotheses consumed (all proved elsewhere in the repository; none is a Lean axiom)
* `Zeta23.GammaFacts` (H-Γ [eq:mufacts]+[eq:muints]) and `Zeta23.ChebyshevMertens` (H-cheb
  [lem:cheb]) — Zeta23/Hypotheses.lean, verbatim (fields of `PaperInputs`).
* `LocalHyps cϱ p F` — taper/test-family facts [eq:psidef], [eq:abdef], [eq:gbounds], [eq:Phi2FT],
                      `∫φ̂² = 2πaL`, `Φ(0) = aL`, `∫Φ² = 2πbL`;
                      [lem:poisson] (★); [eq:PiPfacts] for Π_X;
                      parameter regime [eq:wrange], `0<λ≤1`.


 ## [prop:trace]  (§5.2) 

### `prop_trace_mu`

 **[prop:trace], μ-form** (the paper's proof, §5.2, before [eq:muints] is invoked):
`L·tr G̃ = aL² ∫_T^{2T} μ + O(L²√X + L l)`, divided by `L` and with `l ≤ L√X/λ`:
`|tr G̃ − aL ∫_T^{2T} μ| ≤ C · L√X`. 

### `prop_trace`

 **[prop:trace]** (§5.2, verbatim): `tr G̃ = aL·N(T,2T) + O(L√X)`.
Here `N` is an abstract real standing for `N(T,2T)` and the two hypotheses are exactly what the
paper's proof uses to pass from `∫_T^{2T}μ` to `N(T,2T)`: [eq:muints] (field `int_mu` of
`Zeta23.GammaFacts`) and [eq:RvM] `N(T,2T) = Tℓ₁/2π + O(l)` with constant `A` (hypothesis `hRvM`). 

 ## [lem:ends]  (§5.3), with [eq:Kdef], [eq:trG2int], [eq:Kbounds] 

 ## [eq:Msplit]  (§5.4) 

### `eq_Msplit`

 **[eq:Msplit]** (§5.4, verbatim):
`𝓜 = 𝓜[μ,μ] + 𝓜[P_X,P_X] + 2𝓜[μ,P_X] + 2𝓜[μ,Π_X] + 2𝓜[P_X,Π_X] + 𝓜[Π_X,Π_X]`,
valid because `𝓜[·,·]` is a symmetric bilinear form (`Φ²` even) and all six densities are
continuous on the compact square `I×I` (so every integral is a genuine Lebesgue integral). 

 ## [prop:mumu]  (§5.4) 

 **[prop:mumu]**, first form (§5.4, verbatim): `𝓜[μ,μ] = 2πbL ∫_T^{2T} μ² + O(l² log L)`.
(The second form `= (bLTℓ₁²/2π)(1+O(l⁻²)) + O(l² log L)` follows with [eq:muints] and is taken in
PrimeSideB.)  We write `log L` as in the paper; note `log L ≤ log l` since `λ ≤ 1`. 

 ## [prop:cross]  (§5.4) 

### `prop_cross_muPi`

 **[prop:cross] (ii)** (§5.4): `𝓜[μ,Π_X] ≪ l L √X`.  Proof (§5.4): `0<μ≤l` and
`|Π_X| ≤ 3√X/T` on `I`, inserted into the sup-bound: `≤ l·(3√X/T)·T·2πbL ≤ 6π·lL√X`. 

### `prop_cross_PPi`

 **[prop:cross] (iii)** (§5.4): `𝓜[P_X,Π_X] ≪ L X`.  Proof (§5.4): `|P_X| ≤ √X` (H-cheb) and
`|Π_X| ≤ 3√X/T` on `I`: `≤ √X·(3√X/T)·T·2πbL ≤ 6π·LX`. 

### `prop_cross_PiPi`

 **[prop:cross] (iv)** (§5.4): `𝓜[Π_X,Π_X] ≪ L X / T`.  Proof (§5.4): `|Π_X| ≤ 3√X/T` on
`I` twice: `≤ (3√X/T)²·T·2πbL ≤ 18π·LX/T`. 


## Contents
Proved in this file:
* eq_Msplit — [eq:Msplit]
* prop_cross_muPi / _PPi / _PiPi — [prop:cross] (ii)(iii)(iv)
* prop_trace_mu, prop_trace — **[prop:trace]** (μ-form and the paper's aL·N(T,2T) + O(L√X) form)
Proved in child files, imported here:
* prop_mumu      — [prop:mumu]     — Zeta23/PrimeSideA/MuMu.lean
* prop_cross_muP — [prop:cross](i) — Zeta23/PrimeSideA/CrossMuP.lean
* lem_ends       — [lem:ends]      — Zeta23/PrimeSideA/Ends.lean

