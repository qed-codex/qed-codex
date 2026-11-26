---
{
  "module": "Zeta23/XiPrime/Hardy/ZFunction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/ZFunction.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Hardy/ZFunction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Hardy/ZFunction.lean — Hardy's Z-function and [XF′ (Z3)]:  Z′(t) = i e^{iϑ(t)} W(½+it)
(branch-free construction).
  G(t) := Γℝ(½+it) (≠ 0),  e(t) := G(t)/‖G(t)‖  (this IS the classical e^{iϑ(t)}: |χ(½+it)| = 1 and
  χ = conj G/G, so e² = 1/χ, e(0) = 1, e(−t) = conj e(t));  ZC(t) := e(t)·ζ(½+it) ∈ ℂ;  hardyZ t := Re ZC(t).
We PROVE: ZC(t) is real (so hardyZ t = ZC t); HasDerivAt ZC (i·e(t)·W(½+it)) t for t ≠ 0 [(Z3)], via
e′/e = i·Re(Γℝ′/Γℝ)(½+it) = i·L₂(½+it); hence the stationary points of Z at height t ≠ 0 are exactly the zeros
of W on the critical line, and Z′(t) = 0 ≠ Z″(t) ⟺ the zero ½+it of W is simple; hence the literal Z′ form of the
W headline (the corollary itself is stated in Final.lean from ncard_simpleStationaryZ).
-/
```

### `instContinuousSMulRealComplexZ`

 ContinuousSMul ℝ ℂ is not found by instance search in this closure. 

 ## 1. The phase e(t) = e^{iϑ(t)} and Hardy's Z 

### `sline`

 the critical line parametrisation s(t) = ½ + it. 

### `Gfun`

 G(t) := Γℝ(½ + it). 

### `ephase`

 e(t) := G(t)/‖G(t)‖ = e^{iϑ(t)}, ϑ = the Riemann–Siegel theta function (branch-free definition). 

### `ZC`

 Hardy's function as a complex number: Z(t) := e^{iϑ(t)} ζ(½+it). 

### `hardyZ`

 **Hardy's Z-function** Z : ℝ → ℝ (the real part of ZC; ZC is real, ZC_im below). 

### `chiFE_sline`

 χ(½+it) = conj G(t)/G(t). 

### `ephase_sq`

 e(t)² = 1/χ(½+it). 

### `conj_ZC`

 **Z is real**: conj ZC(t) = ZC(t). 

 ## 2. Derivatives: e′/e = i·Re(Γℝ′/Γℝ)(½+it) = i·L₂(½+it) 

### `gG`

 g(t) := (Γℝ′/Γℝ)(½+it). 

### `hasDerivAt_ephase`

 **e′ = i·Re(g)·e**. 

### `L2_sline`

 L₂(½+it) = Re (Γℝ′/Γℝ)(½+it) ∈ ℝ  [XF′ (Z3)], t ≠ 0. 

### `hasDerivAt_ZC`

 **[XF′ (Z3)]  Z′(t) = i e^{iϑ(t)} W(½+it)**, t ≠ 0. 

### `hasDerivAt_dZC`

 the derivative of i·e·W(½+it). 

 ## 3. Real derivatives of Z and the dictionary with zeros of W 

### `im_deriv_eq_zero`

 a complex-valued function of a real variable with identically zero imaginary part has real derivative. 

### `dZC_im`

 Z′(t) as a complex number is i e W(½+it) (which is therefore real). 

### `deriv_hardyZ_eq_zero_iff`

 **Z′(t) = 0 ⟺ W(½+it) = 0** (t ≠ 0). 

### `deriv_hardyZ_eventuallyEq`

 deriv hardyZ agrees with Re(i e W(½+i·)) near any t ≠ 0. 

### `deriv2_hardyZ_ne_zero_iff`

 **at a zero of W on the line: Z″(t) ≠ 0 ⟺ W′(½+it) ≠ 0**. 

### `wMult_eq_one_iff`

 simple zero of W ⟺ W = 0 and W′ ≠ 0 (W analytic off ℝ). 

 ## 4. The Z′ form of the headline 

### `simpleStationaryZ`

 the stationary points of Z in (T, 2T] with Z″ ≠ 0, as a set of reals. 

### `image_simpleStationaryZ`

 **dictionary**: for T > 0, t ↦ ½+it maps simpleStationaryZ T bijectively onto the simple zeros of W on the
critical line with height in (T, 2T]. 
