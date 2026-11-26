---
{
  "module": "src/Lib/Shimura/ComplexTheta/AppellHumbertData.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/ComplexTheta/AppellHumbertData.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/ComplexTheta/AppellHumbertData.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Theta functions on complex tori: Appell–Humbert data and factors of automorphy

This file defines theta functions on a finite-dimensional complex vector space `V` for a subgroup
`L` and a form `B`. The form has type `ThetaTori.LatticeForm L`, which is `RealComplexForm V`
tagged with `L` and imposes no condition. `B` is real linear in the first argument and complex
linear in the second, and is not assumed hermitian. The file also defines the Riemann form
`E = New.RealComplexForm.riemannForm B`, Appell–Humbert data, twisted translations and the dual
lattice, and proves their first properties. Under the assumption that `L` is a full lattice, it
treats factors of automorphy, positive Riemann forms and theta functions without zeros. Below,
`𝐞 t` is `exp (2πi t)` (`New.coe_fourierChar_eq_exp`).

## Main definitions and results

* `New.RealComplexForm.thetaSpace`: the entire `f` with
  `f (z + l) = χ l * exp (B l z + B l l / 2) * f z` for `l ∈ L`. Products and powers of theta
  functions are theta functions (`New.thetaSpace.mul`, `New.thetaSpace.pow`).
* `New.IsAppellHumbert`: Appell–Humbert data; then `riemannForm B` is integral on `L`
  (`New.IsAppellHumbert.le_dualLattice`).
* `New.RealComplexForm.thetaShift`: translation by `a` twisted by `exp (-(B a z + B a a / 2))`. Two
  of these commute, for Appell–Humbert data, up to `𝐞 (E u v)`
  (`New.IsAppellHumbert.thetaShift_comm`). Those by vectors of the dual lattice
  `New.RealComplexForm.dualLattice` preserve, for such data, the theta functions
  (`New.IsAppellHumbert.thetaShift_mem_of_mem_dualLattice`).

## Relation to the literature

Known; see `Lib.Shimura.ComplexTheta.DimensionFormula` for sources.



## Theta functions, Riemann forms and Appell–Humbert data

The definitions (theta functions, the Riemann form, Appell–Humbert data, twisted translations and
the dual lattice) and their first properties.


### `FinComplexSpace`

 A finite-dimensional complex normed space. 

### `RealComplexForm`

 The continuous complex-valued forms B(u, v) on V that are real-linear in u and
complex-linear in v. 

### `abbrev`

 The subgroup `L` of `V` is a lattice of full rank: it is discrete and spans `V` over the
reals. 

### `ThetaTori.LatticeForm`

 The type `New.RealComplexForm` V of forms on V, tagged with a subgroup L of V (the lattice).
`New.RealComplexForm.thetaSpace` and `New.RealComplexForm.dualLattice` read L from the type. No
condition is imposed. 

 ### Definitions 

### `RealComplexForm.pullForm`

 The pull-back (u, v) ↦ B(φu, φv) of the form B along the complex-linear map φ. 

### `RealComplexForm.thetaSpace`

 The space of theta functions of type (B, χ) for L: entire f on V with
f(z + l) = χ(l)·exp(B(l,z) + B(l,l)/2)·f(z) for l in L. 

### `RealComplexForm.riemannForm`

 The Riemann form of B: the alternating real form E(u, v) = Im(B(u,v) − B(v,u))/(2π). It is
additive in B, as a map from forms to real bilinear forms on V. 

### `RealComplexForm.riemannPhase`

 The complex number exp(2πi E(u, v)) of modulus one, where E is the Riemann form
`New.RealComplexForm.riemannForm` of B. 

### `IsAppellHumbert`

 Appell–Humbert data: Re B is symmetric, and on L one has |χ| = 1 and
χ(l + m) = χ(l)χ(m)·exp(πi E(m, l)), E the Riemann form of B. 

### `IsAppellHumbert.re_symm`

 The real part of B is symmetric. 

### `IsAppellHumbert.norm_eq_one`

 The multiplier χ has absolute value 1 on L. 

### `IsAppellHumbert.semicharacter`

 χ is a semicharacter of L for the Riemann form E of B:
  χ(l + m) = χ(l) χ(m) exp(π i E(m, l)). 

### `IsPosRiemann`

 The Riemann form E of B is positive: E(u, iu) > 0 for every u ≠ 0. 

### `IsPosRiemann.riemannForm_pos`

 E(u, iu) > 0 for every u ≠ 0. 

### `RealComplexForm.thetaShift`

 The twisted translation by `a`, a complex-linear map on all functions `V → ℂ`:
`thetaShift B a f z = exp (-(B a z + B a a / 2)) * f (z + a)`. The factor is the inverse of the
exponential in `New.RealComplexForm.thetaSpace`, so for `a ∈ L` it multiplies a theta function by
`χ a`. 

### `RealComplexForm.dualLattice`

 The dual of L for the Riemann form E of B: the v in V with E(v, l) an integer for all l in
L. 

### `differentiable_of_symm`

 A form B with B(u, v) = B(v, u) is complex linear in both arguments, hence holomorphic. 

### `eq_zero_of_forall_fourierChar_eq_one`

 A real linear form φ with 𝐞(φ x) = 1 for every x is zero. 

### `isPosRiemann_of_re_pos`

 If Re B(u, u) > 0 for every u ≠ 0, the Riemann form of B is positive. 

### `IsAppellHumbert.poincareTerm`

 The term exp(B(x, y − x + l) − B(l,y) − B(l,l)/2)/χ(l) of the Poincaré series at (x, y), for
l in L. The unnamed argument is the Appell–Humbert data (B, χ), for dot notation. 

### `IsAppellHumbert.poincareSeries`

 The Poincaré series K(x, y) = ∑_{l ∈ L} exp(B(x, y − x + l) − B(l,y) − B(l,l)/2)/χ(l) of
Appell–Humbert data (B, χ). 

### `mem_thetaSpace_iff`

 Membership in the space of theta functions of type (B, χ), written out. 

### `apply_add_of_mem_thetaSpace`

 The automorphy law of a theta function of type (B, χ) at `z + l`, for `l` in `L`. 

 ### Consequences of the Appell–Humbert conditions 

### `IsAppellHumbert.sub_eq_riemannForm`

 As `Re B` is symmetric, `B u v - B v u` is purely imaginary, equal to `2πi E(u, v)`. 

### `IsAppellHumbert.thetaShift_thetaShift`

 For Appell–Humbert data (`B`, `χ`) on `L`, the twisted translation
`thetaShift B a f z = exp (-(B a z + B a a / 2)) * f (z + a)` by `v` followed by the one by `u`
equals `exp (π i E(u, v))` times the twisted translation by `u + v`. Here E is the Riemann form of
`B`, and the identity holds for every function `f : V → ℂ`. 

### `IsAppellHumbert.add`

 The sum of the forms and the product of the multipliers of two Appell–Humbert data are again
Appell–Humbert data. 

### `IsAppellHumbert.neg`

 If `(B, χ)` are Appell–Humbert data, then so are `(-B, χ⁻¹)`. 

### `IsAppellHumbert.nsmul`

 If `(B, χ)` are Appell–Humbert data, then so are `(n • B, χ ^ n)`. 

### `IsAppellHumbert.mul_riemannPhase`

 Multiplying `χ` by the unitary character `l ↦ exp (2πi E(l, a))`, with `E` the Riemann form of
any `C` (by default `B`), keeps the Appell–Humbert conditions. 

### `IsAppellHumbert.thetaShift_comm`

 For Appell–Humbert data, two twisted translations commute up to the phase 𝐞(E(u, v)). 

### `IsAppellHumbert.le_dualLattice`

 For Appell–Humbert data, L lies in its dual lattice: the Riemann form is integral on L. 

### `IsAppellHumbert.exp_riemannForm_pow_eq_one`

 For Appell–Humbert data, if n • a and m • b lie in L, then exp(πi E(a, b)) is a root of unity
of order dividing 2nm. 

### `IsAppellHumbert.exp_mul_mem_thetaSpace`

 If `(B, χ)` and `(B', χ')` are Appell–Humbert data with the same Riemann form and the same
multiplier on `L`, then multiplication by `exp ((B' z z - B z z) / 2)` turns theta functions of the
first type into theta functions of the second. 

 ### Translates, products and powers of a theta function 

### `IsAppellHumbert.thetaShift_add_eq_smul_of_mem`

 On a theta function, adding a lattice vector `l` to `u` changes the translation by `u` only by
a scalar. 

### `IsAppellHumbert.thetaShift_mem`

 For Appell–Humbert data (B, χ) for a subgroup `L` of the complex space `V`, the translate by
`a ∈ V` of a theta function is a theta function for the multiplier `l ↦ χ l * exp (2πi E(l, a))`. 

### `IsAppellHumbert.thetaShift_mem_of_mem_dualLattice`

 For Appell–Humbert data, the twisted translation by a vector a of the dual lattice maps theta
functions of type (B, χ) to theta functions of the same type. 

### `IsAppellHumbert.thetaShiftEnd`

 Let (B, χ) be Appell–Humbert data and `a` a vector in the dual lattice of L. This is the twisted
translation `New.RealComplexForm.thetaShift` by `a`, as an endomorphism of the theta functions of
type (B, χ). 

### `thetaSpace.mul`

 The product of theta functions of types `(B, χ)` and `(B', χ')` is a theta function of type
`(B + B', χ * χ')`. 

### `thetaSpace.pow`

 The `n`-th power of a theta function of type `(B, χ)` is one of type `(n • B, χ ^ n)`. 


## Factors of automorphy, positive Riemann forms and theta functions without zeros

`L` is a full lattice in a finite-dimensional complex space `V`, and the form `B` is real-linear in
the first variable and complex-linear in the second.

* `New.exists_factor_of_automorphy`: if `f` has no zero and each quotient `w ↦ f (l + w) / f w` has
  constant logarithmic derivative, then for some `B` with symmetric real part
  `f (z + l) = f z * exp (B l z) * f l / f 0`.
* `New.IsPosRiemann.isDualFamily`: for a positive Riemann form `E` the characters
  `x ↦ exp (2πi E(x, a))`, `a` in the dual lattice, separate the points of `V ⧸ L`.
* `New.IsAppellHumbert.eq_exp_of_ne_zero`: a theta function without zeros is
  `f 0 * exp (B z z / 2)`.


### `exists_factor_of_automorphy`

 Let f : V → ℂ have no zero, and for each l in the lattice L let the quotient w ↦ f(l + w)/f(w)
have as logarithmic derivative a constant complex-linear form. Then there is a form B, real-linear
in the first variable and complex-linear in the second, such that (a) f(z + l) =
f(z)·exp(B(l, z))·f(l)/f(0) for l in L and z in V, and (b) the real part of B is symmetric. 

### `instance : CompactSpace (V ⧸ L.toAddSubgroup)`

 The torus `V ⧸ L` is compact, as `L` is a full lattice. 

 ### Positive Riemann forms and the dual lattice 

### `IsPosRiemann.nondegenerate`

 A positive Riemann form (instance `hp`) is nondegenerate. 

### `IsPosRiemann.eventually_add_neg`

 Positivity of the Riemann form is an open condition on `B`: if the Riemann form of `B` is
positive (instance `hp`), so is that of `B - A` for every `A` near `0`. 

### `IsAppellHumbert.isFullRankLattice_dualLattice`

 If the Riemann form of `B` is positive (instance `hp`), the dual lattice
`New.RealComplexForm.dualLattice` is a full lattice in `V`. 

### `IsPosRiemann.isDualFamily`

 For a positive Riemann form `E` of `B` (instance `hp`), `a ↦ (x ↦ exp (2πi E(x, a)))` embeds the
dual lattice in the unitary characters of `V ⧸ L`, and these characters separate the points of
`V ⧸ L`. 

 ### Theta functions on complex lines 

### `IsAppellHumbert.isCompact_range_norm_thetaShift`

 Let (B, χ) be Appell–Humbert data (instance `hB`) and f a theta function of that type
(hypothesis `hf`). Then the values ‖thetaShift u f 0‖ = |exp(−B(u, u)/2)·f(u)|, for u in V, form a
compact set. 

### `IsAppellHumbert.apply_smul_of_nonpos`

 Let f be a theta function (hypothesis `hf`) for Appell–Humbert data (B, χ) (instance `hB`) on
the full lattice L in V. If the Riemann form E of B satisfies E(u, iu) ≤ 0, then
f(tu) = exp(t²B(u, u)/2)·f(0) for every complex t. 

### `IsAppellHumbert.eq_exp_of_ne_zero`

 If a theta function f (hypothesis `hf`) for Appell–Humbert data (B, χ) (instance `hB`) has no
zero on V, then the Riemann form of B vanishes identically, χ is 1 on L, and
f(z) = f(0)·exp(B(z, z)/2) for all z. 
