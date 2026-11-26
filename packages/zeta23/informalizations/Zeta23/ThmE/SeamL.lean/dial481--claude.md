---
{
  "module": "Zeta23/ThmE/SeamL.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/SeamL.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/SeamL.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmE/SeamL.lean — discharging the L(s,χ)-seam obligations of Zeta23.ThmE.LSeam from Mathlib.
Mirror of Zeta23/ZetaReflect.lean + Zeta23/Statement/Seam.lean for a primitive Dirichlet character
χ mod q, q > 1.

Paper [thm:E] proof (ii), verbatim: "the multiset of zeros of L(s,χ) is invariant under ρ ↦ 1−ρ̄
with multiplicities (functional equation χ ↔ χ̄ composed with conj L(conj s, χ) = L(s, χ̄)), all
zeros have 0<β<1, and N_χ(t+1) − N_χ(t) ≪_q log(t+3)".  These are CLASSICAL facts about L(s,χ),
not paper inputs.  χ̄ = χ⁻¹ for ℂ-valued characters (`MulChar.star_eq_inv`).

Contents:
  • `LFunction_conj`  :  L(s̄, χ) = conj L(s, χ⁻¹)  (Schwarz reflection; Dirichlet series on
    Re s > 1 + identity theorem on ℂ — L is ENTIRE for χ ≠ 1, so no pole bookkeeping);
  • `analyticOrderAt_LFunction_conj`  :  conjugation order transport (via the generic
    `Zeta23.analyticOrderAt_conj_conj` of ZetaReflect.lean);
  • `rootNumber_ne_zero`  :  W(χ) ≠ 0, derived from the functional equation + L(2,χ) ≠ 0
    (no Gauss-sum evaluation needed);
  • `analyticOrderAt_LFunction_one_sub`  :  order transport through
    `IsPrimitive.completedLFunction_one_sub` (Γ-factor and prefactor nonvanishing in the strip);
  • `L_reflect_zero`, `L_mult_reflect`, `LSeam.one_le_mult_holds`, `LSeam.finite_window_holds`,
    and the package `LSeam_of : 1 < q → χ.IsPrimitive → LSeam χ`.
-/
```

 ### 0. Generalities 

### `ne_one_of_primitive`

 A primitive character mod q > 1 is nontrivial. 

 ### 1. Schwarz reflection:  L(s̄, χ) = conj L(s, χ⁻¹) 

### `LFunction_conj`

 **Schwarz reflection for Dirichlet L**: `L(s̄, χ) = conj L(s, χ⁻¹)` (everywhere; χ ≠ 1). 

 ### 2. Order transport under conjugation 

 ### 3. The Γ-factor and the FE prefactor in the strip 

### `completed_eq_gamma_mul_L`

 `Λ = γ·L` on the right half plane (`q > 1`), as an eventual equality near strip points. 

### `rootNumber_ne_zero`

 **W(χ) ≠ 0** for primitive χ mod q > 1 — derived from the functional equation and
L(2,χ) ≠ 0 (no Gauss-sum input). 

 ### 4. Order transport through the functional equation 

### `analyticOrderAt_LFunction_one_sub`

 For `w` in the open strip: `ord_{1−w} L(·,χ) = ord_w L(·,χ⁻¹)`. 

 ### 5. The LSeam fields 

### `L_mult_reflect`

 multiplicity invariance under `ρ ↦ 1 − ρ̄`. 

### `L_reflect_zero`

 zero-set invariance under `ρ ↦ 1 − ρ̄`. 

### `LSeam_one_le_mult`

 H-fin for L(s,χ). 

### `LSeam_finite_window`

 local finiteness of the zeros of L(·,χ) in ordinate windows. 

### `LSeam_of`

 **The seam, discharged**: a primitive χ mod q > 1 satisfies all four LSeam obligations. 
