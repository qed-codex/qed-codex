---
{
  "module": "Zeta23/Analytic/RectangleLogDeriv.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Analytic/RectangleLogDeriv.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Analytic/RectangleLogDeriv.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Residue calculus on rectangles beyond one simple pole.
Used for the weighted contour integral ∮ H·Λ'/Λ and for the Riemann–von Mangoldt count
N(T₁,T₂) = (1/2πi)∮ Λ'/Λ.

* `residueTheorem_finset`: f holomorphic on Rectangle z w minus a finite set S of interior points, with
  f − A p/(s − p) bounded near each p ∈ S  ⟹  RectangleIntegral' f z w = Σ_{p∈S} A p.
  (Induction on S: subtract one principal part, remove the singularity, recurse.)
* `rectangleIntegral'_mul_logDeriv` (the "argument principle with weight"): f, g analytic on a
  neighbourhood of each point of Rectangle z w, f ≠ 0 on the border, Z = the (finite) zero set of
  f in the rectangle  ⟹  RectangleIntegral' (g · f'/f) z w = Σ_{ρ∈Z} ord_ρ(f) · g(ρ).
* `finite_zeros_rectangle`, `rectangleIntegral'_mul_logDeriv'`: the zero set is finite; self-contained form.
-/
```

### `residueTheorem_finset`

 **Residue theorem on a rectangle for finitely many simple poles.** 

### `finite_zeros_rectangle`

 The zero set of a function analytic on a neighbourhood of every point of a rectangle and
nonvanishing at one of its points is finite. 

 ## Meromorphic version: finitely many zeros AND poles inside the rectangle

Intended for f = completedRiemannZeta (simple poles at 0 and 1, residues ∓1):
(1/2πi) ∮ g·(f'/f) = Σ_{zeros ρ} ord_ρ(f)·g(ρ) − Σ_{poles p} m_p·g(p).
A pole of order m at p is witnessed elementarily by  (s − p)^m · f(s) → c ≠ 0  (s → p, s ≠ p),
which is the shape of Mathlib's `completedRiemannZeta_residue_one` (m = 1). 

### `rectangleIntegral'_mul_logDeriv_of_poles`

 **Weighted argument principle with poles.** f analytic on a neighbourhood of every point of
the closed rectangle except at the finitely many interior points P, where (s − p)^{m p} f(s) → c_p ≠ 0;
g analytic on a neighbourhood of every point; f ≠ 0 on the border; Z = zero set of f in the
rectangle (off P). Then (1/2πi)∮ g·f'/f = Σ_{ρ∈Z} ord_ρ(f) g(ρ) − Σ_{p∈P} m_p g(p). 

### `rectangleIntegral'_mul_logDeriv`

 **Weighted argument principle on a rectangle.** For f, g analytic on a neighbourhood of every
point of the closed rectangle, f nonvanishing on its border, and Z the zero set of f in the
rectangle (as a Finset):  (1/2πi) ∮ g·(f'/f) = Σ_{ρ ∈ Z} ord_ρ(f)·g(ρ). 

### `rectangleIntegral'_mul_logDeriv'`

 **Weighted argument principle, self-contained form**: as `rectangleIntegral'_mul_logDeriv`, with
the finite zero set produced rather than supplied. 
