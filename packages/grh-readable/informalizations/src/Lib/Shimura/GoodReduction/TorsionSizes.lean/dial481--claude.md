---
{
  "module": "src/Lib/Shimura/GoodReduction/TorsionSizes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/GoodReduction/TorsionSizes.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/GoodReduction/TorsionSizes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Sizes of theta functions at torsion points: products, bounds and shift bounds

Theta functions (`New.RealComplexForm.thetaSpace`) on a complex torus `V / L`, measured at the
torsion points by a valuation `v` on `ℂ`. The degree is a form `B` (a `LatticeForm L`: it has
complex values B x y, and degrees are added and scaled by reals) with Appell–Humbert data
`New.IsAppellHumbert` and Riemann form `New.RealComplexForm.riemannForm`;
`New.RealComplexForm.thetaShift` is translation with the exponential factor that keeps the degree.
The size `New.ThetaTori.LatticeForm.sizeAt` of `f` at a torsion point `x` is
`v (exp (-B x x / 2) * f x)`, and `New.ThetaTori.LatticeForm.sizes` is the set of all sizes of
degree `B`, over all multipliers χ of finite order with `New.ThetaTori.IsAmpleType`. Roots of unity
have valuation `1`, so sizes are periodic and do not see these multipliers.

* `New.ThetaTori.mul_shift_mem_sizes`: products of sizes with torsion translates of sizes are sizes.
* `New.ThetaTori.bddAbove_of_mem_sizes`, `New.ThetaTori.IsAmpleType.thetaNorm_pos`: sizes are
  bounded, and the sup norm of `f ≠ 0` is positive.
* `New.ThetaTori.eq_zero_of_torsionPoints`: a holomorphic function that vanishes at all torsion
  points is zero.
* `New.ThetaTori.LatticeForm.HasShiftBound`: the bound `φ ^ 2 ≤ C * ⨆ x, φ x * φ (x + w)`. It passes
  from `B` to `B'` when the Riemann form of `B - B'` is positive
  (`New.ThetaTori.LatticeForm.HasShiftBound.of_isPosRiemann_sub`), and with `C = 1` it compares
  products of translates (`New.ThetaTori.mul_le_iSup_of_hasShiftBound`).

Notions from other files:
* `New.IsPosRiemann`: The Riemann form E of B is positive: E(u, iu) > 0 for every u ≠ 0.
* `New.RealComplexForm.dualLattice`: The dual of L for the Riemann form E of B: the v in V with E(v,
  l) an integer for all l in L.

## Relation to the literature

Known; see `Lib.Shimura.GoodReduction.MultiplicativeNorm` for sources.


 ### Definitions 

### `torsionPoints`

 The ℤ-submodule of the vectors a of V with na in L for some n ≠ 0: the preimage in V of the
torsion subgroup of V/L. 

### `IsAmpleType`

 (L, B, χ) is an Appell–Humbert datum (the Riemann form E of B is integral on L, and χ is a
nonvanishing multiplier on L) with positive Riemann form, and χ has finite order on L: χⁿ = 1 there
for some n ≠ 0. 

### `IsAmpleType.finite_order`

 The multiplier `χ` has finite order on `L`. 

### `LatticeForm.sizeAt`

 The size of f at a vector x of V of finite order modulo L: the value
v(exp(−B(x, x)/2)·f(x)). 

### `LatticeForm.thetaNorm`

 The sup norm of f in degree B: the supremum of its sizes `New.ThetaTori.LatticeForm.sizeAt` over
all torsion points of V/L. 

### `LatticeForm.sizes`

 The sizes of degree B: the functions `New.ThetaTori.LatticeForm.sizeAt` of f on the torsion
points of V/L, for f a theta function of type (B, χ) (f is holomorphic, and for l in L, f(z + l) is
χ(l) times an exponential factor fixed by B, times f(z)), with any χ such that
`New.ThetaTori.IsAmpleType` holds for B and χ (a twisted theta function of degree B). 

### `LatticeForm.sizes.of_mem_thetaSpace`

 For `f` in `B.thetaSpace χ` with `IsAmpleType B χ`, the function `B.sizeAt v f` belongs to
  `LatticeForm.sizes`. 

### `HasMultiplicativeNorm`

 The analytic form of good reduction of V/L at v: for all degrees B, C and all sizes φ, ψ of
these degrees (sizes of twisted theta functions f, g), the sup norm of the product φψ, the size of
fg, is the product of the sup norms. 

### `HasGoodReduction`

 The conditions of `New.ThetaTori.IsAmpleType`, plus three more. Some natural N with v(N) = 1
maps the dual lattice of L into L. The level r > 1 has v(r) = 1. The sup norm is multiplicative
(`New.ThetaTori.HasMultiplicativeNorm`). 

### `HasGoodReduction.dual_torsion`

 Some natural number of valuation `1` multiplies the dual lattice of `L` into `L`. 

### `HasGoodReduction.val_eq_one`

 The level `r` has valuation `1`. 

### `HasGoodReduction.one_lt`

 The level `r` is at least `2`. 

### `HasGoodReduction.hasMultiplicativeNorm`

 The sup norm of theta functions on the torsion points is multiplicative. 

### `LatticeForm.HasShiftBound`

 For the size function φ of every twisted theta function of degree B, (sup φ)² ≤ C · sup_x
φ(x) φ(x + w), x over the torsion points. 

 ### Products, translates and periodicity of sizes 

### `_root_.New.IsAppellHumbert.valuation_exp_riemannForm`

 Let `B` carry an Appell–Humbert datum (`New.IsAppellHumbert`), with Riemann form `E`. At torsion
points `a`, `b` the number `exp (π i E(a, b))` is a root of unity, so it has valuation `1`. 

### `_root_.New.IsAppellHumbert.sizeAt_thetaShift`

 The size at `x` of the translate `B.thetaShift w f` is the size of `f` at `x + w`, for torsion
points `w`, `x`. 

### `factorsThrough_mkQ_of_mem_sizes`

 Sizes are periodic modulo `L`: a size `φ` of degree `B` takes the same value at two torsion
points with the same class in `V ⧸ L`. 

### `mul_shift_mem_sizes`

 Let `φ` and `ψ` be sizes of degrees `B` and `B'`. For every torsion point `w` the function
`x ↦ φ x * ψ (x + w)` is a size of degree `B + B'`. 

 ### Finiteness and density of torsion points 

### `finite_range_nsmul_torsion`

 A function on the torsion points that depends only on the class modulo `L` takes finitely many
values on the points `x` with `n • x ∈ L`, for `n ≠ 0`. 

### `isCocompact_of_isFullRankLattice`

 A full-rank lattice `L` in `V` is cocompact: some compact set meets every coset of `L`. 

### `eq_zero_of_small_mesh`

 A continuous function that vanishes on lattices of arbitrarily small mesh is zero: suppose that
for linear maps `d` arbitrarily close to `0` there is a left inverse `c` of `d` such that `f`
vanishes on the preimage of `L` under `c`. Then `f = 0`. 

### `eq_zero_of_torsionPoints`

 A holomorphic function `f` on `V` that vanishes at all torsion points of `V / L` is zero. 

### `LatticeForm.HasShiftBound.of_doubling`

 A fixed point argument for the constant in `New.ThetaTori.LatticeForm.HasShiftBound`, for a
family of degrees `B i` with translations `w i`. Suppose that some constant `D₀` serves every
`B i` with `w i`, and that whenever a constant `D` serves every `B i` with `w i`, the constant
`D * C` serves every `B i + B i` with `w i`. Then `C` serves every `B i` with `w i`. 

### `bddAbove_of_mem_sizes`

 Let `L` be a full lattice in a finite-dimensional complex space `V`, and let `v` be an
ℝ≥0-valued valuation on ℂ. A size φ of degree `B` is the function `sizeAt` of `f` on the torsion
points of `V/L`, where `f` is a theta function of type (`B`, χ) for some χ with `IsAmpleType B χ`.
Every such φ is bounded above. 

### `mul_le_iSup_of_hasShiftBound`

 Let `L` be a full-rank lattice in `V`, `v` a valuation on ℂ, `x`, `y`, `w` torsion points, and
φ, ψ sizes of degrees `B`, `B'` (`sizes`: functions x ↦ v(exp(−B(x, x)/2)·f(x)) on the torsion
points, for f a twisted theta function of degree B). Suppose every size ρ of degree B + B' satisfies
(sup ρ)² ≤ sup_z ρ(z)·ρ(z + (y − x − w)), which is `HasShiftBound` for y − x − w with C = 1. Then
φ(x)ψ(y) ≤ sup_z φ(z)ψ(z + w). 

### `IsAmpleType.thetaNorm_pos`

 The sup norm `B.thetaNorm v f` of a nonzero theta function `f` of type `(B, χ)` is positive. 

### `LatticeForm.HasShiftBound.of_isPosRiemann_sub`

 Let L be a lattice of full rank in the finite-dimensional complex space V, let (L, B, χ) satisfy
`New.ThetaTori.IsAmpleType`, and let the Riemann form of B − B' be positive. If the bound of
`New.ThetaTori.LatticeForm.HasShiftBound` for w with constant C holds for the sizes of all theta
functions of type (B, χ), then it holds in degree B'. 

### `IsAmpleType.eventually_isPosRiemann_smul_sub`

 Let (L, B, χ) satisfy `New.ThetaTori.IsAmpleType`. For every form A and all large enough m,
m ≠ 0 and the Riemann form of m • B − A is positive. 
