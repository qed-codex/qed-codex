---
{
  "module": "Zeta23/Taper/Gevrey.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Taper/Gevrey.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Taper/Gevrey.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/Taper/Gevrey.lean — Gevrey-class taper profiles (items P1–P4 below).

PURPOSE.  The family / q-aspect version of the theorem (paper rem:otherL (iii): "requires a different (Gevrey-class)
taper in prop:tail") needs a profile ϱ with sup|ϱ^{(k)}| ≤ B·A^k·k^{sk} (all k ≥ 1) for some s > 1.  We fix s = 2 and the
explicit profile built from Mathlib's Real.expNegInvGlue g(x) = exp(−1/x) (x>0), 0 (x≤0):
   θ(x) := g(x)·g(1−x)   (a bump on (0,1)),      ϱ₂(x) := (∫_0^x θ) / (∫_0^1 θ).
CONTENTS (all tools exist in Mathlib):
 (P1) gevrey_expNegInvGlue : ∀ k ≥ 1, ∀ x, |iteratedDeriv k expNegInvGlue x| ≤ (18/e)^k · k^(2k).
      Route: for x > 0, expNegInvGlue =ᶠ[𝓝 x] (fun t => (G t).re) with G z := Complex.exp (−1/z) holomorphic on ℂ∖{0};
      real/complex iterated derivatives agree (induction with HasDerivAt.real_of_complex + EventuallyEq.iteratedDeriv_eq);
      Cauchy's estimate Complex.norm_iteratedDeriv_le_of_forall_mem_sphere_norm_le on the circle |z − x| = x/2, where
      Re(1/z) = Re z/|z|² ≥ 2/(9x) so ‖G z‖ ≤ exp(−2/(9x)); then k!·(x/2)^{−k}·exp(−2/(9x)) ≤ k!·(9k/e)^k ≤ (9/e)^k k^{2k}·(k!/k^k)
      (sup_t t^k e^{−2t/9} = (9k/(2e))^k).  For x < 0 all derivatives vanish (eventually 0); x = 0 by continuity of
      iteratedDeriv k (expNegInvGlue is C^∞: Real.expNegInvGlue.contDiff).
 (P2) gevrey_mul : Leibniz (norm_iteratedFDeriv_mul_le / iteratedDeriv version): (G_s) for f,h with (A,B) ⇒ (G_s) for f·h
      with (2A, B²), using j^{sj}(k−j)^{s(k−j)} ≤ k^{sk} and Σ_j C(k,j) = 2^k.
 (P3) theta, rhoTwo : definitions; rhoTwo is a TaperProfile (monotone: θ ≥ 0; = 0 / = 1 outside (0,1); C^∞, indeed C³ as
      TaperProfile wants) and iteratedDeriv (k+1) rhoTwo = iteratedDeriv k θ / ∫θ.
 (P4) gevreyProfile_rhoTwo : GevreyProfile 2 (36/e) (2·e^8) rhoTwo   (∫_0^1 θ ≥ e^{−8}/2 since θ ≥ e^{−8} on [1/4,3/4]).
Downstream: a Gevrey tail lemma gives TailInputs with
θ₀ = η/L once (wD₀/A)^{1/2} ≥ c₁^{−1}[L/2 + log d + …]; nothing else in §2.2/§4 changes (c_ϱ finite).
-/
```

### `GevreyProfile`

 Gevrey-s derivative bounds in the (weaker-than-usual) form
sup|ϱ^{(k)}| ≤ B·A^k·k^{sk} for all k ≥ 1, on top of the paper's TaperProfile and C^∞. 

### `theta`

 the bump θ(x) = g(x) g(1−x), g = expNegInvGlue. 

### `Theta`

 its primitive Θ(x) = ∫_0^x θ. 

### `rhoTwo`

 the Gevrey-2 profile ϱ₂ = normalized primitive of θ. 

 ### (P1) Gevrey-2 bounds for exp(−1/x) via Cauchy's estimate 

### `G`

 holomorphic extension of exp(−1/x). 

### `gR`

 real restriction. 

### `norm_iteratedDeriv_G_le`

 Cauchy's estimate for G on the circle |z − x| = x/2. 

### `pow_mul_exp_neg_le`

 elementary: u^k e^{−u} ≤ (k/e)^k for u ≥ 0, k ≥ 1. 

### `cauchy_bound_le`

 the numeric step: k!·e^{−2/(9x)}·(x/2)^{−k} ≤ (18/e)^k k^{2k}. 

### `gevrey_expNegInvGlue`

 **(P1)** Gevrey-2 bound for exp(−1/x): |g^{(k)}(x)| ≤ (18/e)^k k^{2k} for all k ≥ 1 and all real x
(Cauchy's estimate for G(z) = exp(−1/z) on the circle |z − x| = x/2, where ‖G‖ ≤ exp(−2/(9x))). 

 ### bounds for g and g(1−·) with the convention gb 0 = 1 

 ### θ 

### `abs_iteratedDeriv_theta_le`

 Leibniz ⇒ |θ^{(k)}| ≤ (36/e)^k k^{2k}. 

 ### Θ = primitive of θ 

### `Theta_one_ge`

 ∫_0^1 θ ≥ e^{−8}/2 (θ ≥ e^{−8} on [1/4, 3/4]). 

 ### ϱ₂ 

### `gevreyProfile_rhoTwo`

 **(P4)** ϱ₂ is a Gevrey-2 taper profile with explicit constants (A, B) = (36/e, 2e^8):
the input needed by the family/q-aspect tail lemma. 
