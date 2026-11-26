---
{
  "module": "Zeta23/ThmD/Functional.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/Functional.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmD/Functional.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmD/Functional.lean — the scale-free variational objects of the paper §7.1 [subsec:MT]:
[eq:cv] the functional c_λ(v), [eq:vstar] the optimal profile v*_λ(s) = cos(√2 λ s) and the
closed-form constant c*_λ = √2 tan ϑ/(1 + ϑ tan ϑ), ϑ = λ/√2.
Pure one-variable calculus: no project imports; consumed by Zeta23/ThmD/Window.lean
(a/b/J of the concrete window) and Zeta23/ThmD/Assembly/Final (the constants of Theorem D).

Convention: we DEFINE cStar in the division-safe sin/cos form
  cStar λ := √2 sin ϑ / (cos ϑ + ϑ sin ϑ)
(the paper's √2 tan ϑ/(1+ϑ tan ϑ) after multiplying through by cos ϑ; equality recorded as
cStar_eq_tan_form).  For 0 ≤ ϑ ≤ 1/√2 < π/2 the denominator is ≥ cos(1/√2) ≥ 3/4 > 0
(cos x ≥ 1 − x²/2), so everything is well-behaved on λ ∈ [0,1].
-/
```

### `theta`

 ϑ := λ/√2  [eq:vstar]. 

### `vStar`

 [eq:vstar]: the optimal window profile v*_λ(s) := cos(√2 λ s)  (scale-free; s ∈ [−1/2, 1/2]). 

### `cStar`

 [eq:vstar]: c*_λ := √2 tan ϑ / (1 + ϑ tan ϑ), written in the division-safe sin/cos form. 

### `cFun`

 [eq:cv]: the scale-free functional
c_λ(v) = λ(∫v)² / (∫v² + λ² ∬|s−s'| v(s)v(s') ds ds'), integrals over [−1/2, 1/2]. 

### `aStar`

 The three moments of v*_λ [eq:abJ] in scale-free form:
a* = ∫v*, b* = ∫v*², J* = ∬|s−s'|v*v*. 

### `HD`

 The Theorem-D lower-bound constants: N₀* rate 2 − 1/c*, N₀ˢ rate 2c* − 1, N_d rate c*. 

 ### Elementary range facts 

### `theta_sq_le`

 on [0, 1/√2] the denominator of cStar is ≥ 3/4  (cos x ≥ 1 − x²/2 and x sin x ≥ 0). 

### `cStar_lipschitzOn`

 Lipschitz bound on [0,1]: |c*_x − c*_y| ≤ 14|x − y| (the constant is crude). 

### `cStar_continuousOn`

 c*_λ is continuous on [0,1] (its denominator is ≥ 3/4 there); this is all the λ → 1⁻ passage needs. 

### `cStar_eq_tan_form`

 c* in the paper's tan form [eq:vstar] (cos ϑ ≠ 0 on the range). 

 ### The moments of v*_λ (elementary trigonometric integrals) 

### `sqrt2_mul_half`

 a* = √2 sin ϑ / λ  (= 2 sin(ω/2)/ω for ω = √2λ = 2ϑ). 

### `bStar_eq`

 b* = 1/2 + sin(2ϑ)/(4ϑ). 

### `hasDerivAt_left`

 antiderivative for the left piece: d/dx [(s−x)sin(ωx)/ω − cos(ωx)/ω²] = (s−x)cos(ωx). 

### `hasDerivAt_right`

 antiderivative for the right piece: d/dx [(x−s)sin(ωx)/ω + cos(ωx)/ω²] = (x−s)cos(ωx). 

### `kernel_eq`

 the inner kernel integral: for s ∈ [−1/2, 1/2],
∫ s' in −1/2..1/2, |s − s'| cos(√2 λ s') = a*/2 + cos ϑ/λ² − cos(√2 λ s)/λ². 

### `jStar_eq`

 The kernel identity behind J*: with β := a*/2 + cos ϑ/λ²,
∬|s−s'| v* v* = β a* − b*/λ². 

### `cFun_vStar`

 [eq:vstar]: c_λ(v*_λ) = c*_λ  (the algebra b* + λ²J* = λ² β a* = ϑ sin ϑ·(√2 sin ϑ/λ·…),
collapsing to √2 sin ϑ/(cos ϑ + ϑ sin ϑ) after cancelling a*). 

 ### The λ = 1 values (the constants of Theorem D) 

### `theta_one`

 HD 1 = 3/2 − (1/√2)·cot(1/√2)  (the paper's 2 − 1/c₁* = 3/2 − 2^{-1/2} cot 2^{-1/2}). 

### `jStar_closed`

 closed form of J* (used by Window.lean's jD_close):
J* = sin(2ϑ)/(8ϑ³) − cos(2ϑ)/(4ϑ²)  (pure algebra from jStar_eq + aStar_eq + bStar_eq,
using λ² = 2ϑ², sin 2ϑ = 2 sin ϑ cos ϑ, cos 2ϑ = 1 − 2 sin²ϑ). 
