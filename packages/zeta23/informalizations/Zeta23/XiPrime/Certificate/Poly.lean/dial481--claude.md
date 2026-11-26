---
{
  "module": "Zeta23/XiPrime/Certificate/Poly.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Certificate/Poly.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/Certificate/Poly.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/Certificate/Poly.lean — exact rational evaluation of the window integrals for the two
certificate windows ("Certified constants").

  vConv vFlat r = 1 − r,            ∫vFlat = ∫vFlat² = 1,
  vConv vQuartic r = explicit degree-9 polynomial,  ∫vQuartic = 2777/3000,  ∫vQuartic² = 518783/600000,
  jWin (D1trunc 9) 1 vFlat    = 12517210259/88388425125,
  jWin (D1trunc 9) 1 vQuartic = 29965280330934234270211/285991090937677125000000.

Device: a polynomial given by a coefficient list integrates to a finite rational sum
(polyEval / polyInt); every closed form is computer-algebra-generated
and Lean-checked by ring / norm_num.
-/
```

 ### polynomial interval integrals via coefficient lists 

### `polyEval`

 evaluate a coefficient list as a polynomial: Σ_k c[k]·x^k. 

### `polyInt`

 its interval integral: Σ_k c[k]·(b^{k+1} − a^{k+1})/(k+1). 

 ### D1trunc 9 written out 

### `T9`

 the degree-19 polynomial D1trunc 9 with its rational coefficients. 

 ### the flat window 

### `prodFlat`

 coefficients of r ↦ T9(r)·(1 − r). 

### `integral_T9_flat`

 ∫₀¹ D1trunc 9 (r)·(1 − r) dr, exactly. 

 ### the quartic window v(s) = 1 − (7/100)(2s)² − (51/200)(2s)⁴ 

### `convQ`

 closed form of (v⋆v)(r) for the quartic window (degree 9 in r; valid for every real r). 

### `coeffS`

 the coefficients of s ↦ v(s)·v(s+r). 

### `prodQuartic`

 coefficients of r ↦ T9(r)·convQ(r) (degree 28). 

### `integral_T9_quartic`

 ∫₀¹ D1trunc 9 (r)·(v⋆v)(r) dr for the quartic window, exactly. 

 ### positivity / range / continuity facts of the two profiles 

### `vQuartic_ge`

 min over [−1/2,1/2] is 27/40, at the endpoints (v is decreasing in s²). 
