---
{
  "module": "src/Lib/Shimura/GoodReduction/MultiplicativeNorm.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/GoodReduction/MultiplicativeNorm.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/GoodReduction/MultiplicativeNorm.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Good reduction of theta tori from shift bounds on kernels of multiplications

The file gives a criterion for the main condition of good reduction of a torus `V / L` with
multiplications `New.ThetaTori.IsHermitianAction`. The condition
(`New.ThetaTori.HasMultiplicativeNorm`) is that the sup norm of sizes of theta functions is
multiplicative at the valuation `v`. The tool is a shift bound: `A.HasShiftBound v w C` (`w` has
the constant `C` in degree `A`) says `φ y ^ 2 ≤ C * ⨆ x, φ x * φ (x + w)` for all sizes `φ` of theta
functions of degree `A` and all torsion points `y`. Constants are obtained on the kernels of
multiplications `c` and descend along `c`, which gives multiplicativity.

## Main definitions and results

* `New.ThetaTori.IsHermitianAction.hasShiftBound_one_of_ker`: under arithmetic conditions on `c`,
  its kernel has the constant `1`.
* `New.ThetaTori.IsHermitianAction.hasShiftBound_of_torsionAction`,
  `New.ThetaTori.IsHermitianAction.eventually_hasShiftBound`: a constant descends along `c`; some
  constant exists.
* `New.ThetaTori.IsHermitianAction.hasMultiplicativeNorm_of_frequently_hasShiftBound`: if such `c`
  have arbitrarily small inverses, `New.ThetaTori.HasMultiplicativeNorm` holds.
* `New.ThetaTori.hasMultiplicativeNorm_of_expanding`: the multiplicative norm from arithmetic
  conditions on `R`, `B` and `p`.
* `New.ThetaTori.ThetaTorus.hasGoodReduction_and_val_card_eq_one`: let `v` be a valuation on `ℂ`
  whose valuation ring receives `𝓞 E` compatibly with `Φ v₀`, over a prime that is good for `D`.
  Then a theta torus has good reduction for `v`, and the order of `D.dualTorsion` is a unit.

Notions from other files:
* `New.ThetaTori.IsHermitianAction.multiplier`: The canonical multiplier x ↦ exp(πi E(βx, x)) of the
  hermitian data, where E is the Riemann form of B.
* `New.ThetaTori.HasGoodReduction`: a polarisation whose dual lattice is mapped into the lattice by
  a `v`-unit, a level `r > 1` that is a `v`-unit, and a multiplicative sup norm of theta functions
  on the torsion points.

## Relation to the literature

Known result: Good reduction of unitary PEL abelian varieties, in analytic form without toric
degeneration. Suppose a torus with polarisation prime to p has non-unit multipliers that expand
arbitrarily, divide a power of p and are prime to their conjugates, and whose conjugates have unit
determinant on the Lie algebra. Then the supremum of a valuation of theta values at torsion points
is multiplicative. Source: K.-W. Lan, Elevators for degenerations of PEL structures, Math. Res.
Lett. 18 (2011); R. Kottwitz, Points on some Shimura varieties over finite fields, J. Amer. Math.
Soc. 5 (1992), §5 (division algebra case); for the CM case B. Conrad, Semistable reduction for
abelian varieties (notes), Prop. 6.3, after Serre and Tate, Ann. of Math. 88 (1968).



## Shift bounds on kernels of multiplications and the multiplicative norm

Conventions: `h.normShift x` is translation of functions by `x` with the factor of automorphy of
`B`, divided by the multiplier `h.multiplier x`; `h.MulKernel c` is `c⁻¹ L / L`. The size
`New.ThetaTori.LatticeForm.sizeAt` of `f` at a torsion point `x` is `v (exp (-B x x / 2) * f x)`.
`New.ThetaTori.LatticeForm.sizes` is the set of sizes of theta functions of a given degree `B`, for
every multiplier `χ` such that `(B, χ)` is of ample type (`New.ThetaTori.IsAmpleType`:
Appell–Humbert data with positive Riemann form, `χ` of finite order on `L`).


### `torsionAction`

 The action of `a` on the points of `V` of finite order modulo `L`: `x ↦ F a x`, again of finite
order because `F a` preserves `L`. 

 ### Normalised translations, sizes and torsion points 

### `normShift_comm`

 The commutator of the normalised translations by `x` and `y` is `exp (2 π i E(x, y))`, where
`E` is the Riemann form of `B`. 

### `sizeAt_add`

 The size of `f` at the sum of torsion points `x` and `w` is the valuation of the value at `0` of
the normalised translate of `f` by `w` and then by `x`. 

### `mem_torsionPoints`

 A point `a` of `c⁻¹ L` (the vectors that `F c` maps into `L`) has finite order modulo `L`. 

### `torsionAction_surjective`

 For `c ≠ 0`, multiplication by `c` maps the points of finite order modulo `L` onto
themselves. 

### `normShift_comp_inverse_eq`

 Let `d = star c`. Translating `f ∘ F c ∘ (F d)⁻¹` by `d w` gives the translate of `f` by `c w`,
composed with `F c ∘ (F d)⁻¹`. 

 ### The theta identity and the kernel of a multiplication 

### `averagedPullback`

 The averaged pull-back along `c` and `d`: the operator sending `t : V → ℂ` to the sum, over the
classes `z` of `d⁻¹ L / L` (with chosen representatives `z.out`), of the normalised translates of
`t ∘ F c ∘ (F d)⁻¹` by `d z`. 

### `averagedPullback_mem_thetaSpace`

 Let `d = star c`. The averaged pull-back of a theta function with the canonical multiplier is
again one. 

### `averagedPullback_normShift_of_mem_dualLattice`

 Let `d = star c`, and let `c` and `d` act as the identity on the dual lattice modulo `L`. For
`a` in the dual lattice and a theta function `t` with the canonical multiplier, the averaged
pull-back of the normalised translate of `t` by `a` is the normalised translate by `a` of the
averaged pull-back of `t`. 

### `exists_averagedPullback_eq_smul`

 Let `d = star c`, and let `c` and `d` act as the identity on the dual lattice modulo `L`. The
averaged pull-back acts on the theta functions with the canonical multiplier as a scalar. 

### `exists_sum_normShift_eq_smul`

 Let `d = star c` with `c` and `d` non-zero, and let `c` and `d` act as the identity on the dual
lattice modulo `L`. There is a number `μ` such that (a) `μ` is the order of `d⁻¹ L / L` times the
mean over `V / L` of `x ↦ K(d x, c x)`, with `K` the Poincaré kernel (a sum over `L`, a theta
function with the canonical multiplier in its second variable, of mean `1` on the diagonal); (b) for
every theta function `t` with the canonical multiplier, the sum over `z ∈ d⁻¹ L / L` (with chosen
representatives `z.out`) of the normalised translates of `t ∘ F c ∘ (F d)⁻¹` by `d z` is `μ • t`. 

### `sum_normShift_eq_zero`

 Let `h` be a hermitian action of `R` on `V/L` (`B` positive definite hermitian with Riemann form
E integral on `L`, `F` preserving `L` with `star` giving adjoints, `star β = 1 - β`). Let `c` and
`d = star c` be coprime and non-zero, with `F d a - a ∈ L` for every `a` in the dual lattice of `B`.
Let `t` be a theta function of type (`B`, χ), where χ is the canonical multiplier x ↦ exp(πi E(βx,
x)), and let `z ≠ 0` lie in the kernel of `d` on `V/L`. Write `normShift x` for the twisted
translation by `x` divided by exp(πi E(βx, x)). Then the sum of
`normShift (F c k.out) (normShift (F c z.out) t)` over `k` in the kernel of `c` on `V/L` vanishes at
every point `x`. 

### `poincareSeries_eq_conj_poincareSeries_star`

 The Poincaré kernel `K` of the canonical multiplier (`poincareSeries`, a sum of `poincareTerm`
over the lattice) at `(c x, star c x)` is the complex conjugate of its value at
`(star c x, c x)`. 

### `exists_theta_identity`

 The theta identity. Let `d = star c` with `c` and `d` non-zero and `c ≠ d`, let `c` and `d` be
coprime, and let both act as the identity on the dual lattice modulo `L`. Then there is `μ` with
`μ ^ 8 = det (F d) ^ 8`, that is, `μ` is the determinant of `d` up to an eighth root of unity, such
that for every theta function `t` with the canonical multiplier the sum over `z ∈ d⁻¹ L / L` of the
normalised translates of `t ∘ F c ∘ (F d)⁻¹` by `d z` is `μ • t`. 

### `_root_.Valuation.map_sub_one_pow_le_of_pow_eq_one`

 Let `v` be a valuation on `ℂ` with values in `ℝ≥0`, let `p` be a prime and `ζ` a `p ^ n`-th root
of unity. Then `v (ζ - 1) ^ p ^ n ≤ v p`. 

### `_root_.NNReal.sq_le_of_le_max_sqrt_mul`

 If `S ≤ max (√T) (ρ * S)` in `ℝ≥0` with `ρ < 1`, then `S ^ 2 ≤ T`. 

### `mul_normShift_eq_mul_normShift_sub_sum`

 Let `d = star c`, let `μ` be the scalar of the theta identity `identity`, let `f` be a theta
function with the canonical multiplier and let `c g ∈ L`. Write `T(x, y)` for the value at `0` of
the normalised translate of `f` by `x` and then by `y`. Then `μ` times the value at `0` of the
normalised translate of `f` by `d q` equals `μ * T(d g, d q)` minus the sum over `z ∈ d⁻¹ L / L`
(with chosen representatives `z.out`) of `(B.riemannPhase (c g) (c z) - 1) * T(c z, c q)`. 

### `hasShiftBound_one_of_ker`

 The constant `1` on the kernel of `c`. Let `c ≠ 0` and `d = star c` be distinct and coprime and
act as the identity on the dual lattice of `B` modulo `L`; let `p` be a prime with `v p < 1`, let
`det d` have valuation `1`, and let `B - A` have a positive Riemann form. Then every torsion point
`w` with `c w ∈ L` and `p ^ n w ∈ L` has the constant `1` in degree `A`, meaning
`(sup φ) ^ 2 ≤ ⨆ x, φ x * φ (x + w)` (`x` over torsion points) for the size function `φ`, taken with
`v`, of every twisted theta function of degree `A`. 

 ### The contraction argument 

### `isHermitianAction_pullForm`

 The pull-back `c^* B` of `B` along the action of `c ≠ 0` (the form `B.pullForm (F c)`) is again
a hermitian form for the action of `R`, with the same `β`. 

### `hasShiftBound_of_torsionAction`

 Descent along `c ≠ 0`. Say that a torsion point `x` has the constant `C` in degree `A` (a form
on `V`) when `A.HasShiftBound v x C` holds: for the size function `φ` (taken with `v`) of every
twisted theta function of degree `A`, `(sup φ)² ≤ C · sup_y φ(y) φ(y + x)`, with `y` running over
the torsion points. Suppose the torsion points `y` with `c y ∈ L` have the constant `1` in every
degree, and `c^* B - A` has a positive Riemann form, where `c^* B` is the pull-back
`B.pullForm (F c)`; then for a torsion point `w`, if `c w` (that is `h.torsionAction c w`) has the
constant `D` in degree `B`, `w` has the constant `D / v (#(c⁻¹ L / L)) ^ 2` in degree `A`. 

### `eventually_hasShiftBound`

 Let `h` be a hermitian action of `R` on `V/L`: `B` is positive definite hermitian with Riemann
form integral on the full lattice `L`, each `F a` preserves `L` with `F (star a)` adjoint to `F a`,
and `star β = 1 - β`. Here `A.HasShiftBound v y C` means that for the size function φ of every
twisted theta function of degree `A`, (sup φ)² ≤ `C` · sup_x φ(x) φ(x + `y`), with x over the
torsion points. Suppose that arbitrarily close to `0` there are continuous linear maps `e` with
`F c (e x) = x` for some `c ≠ 0` in `R`, such that `A.HasShiftBound v y 1` holds for every form `A`
and every torsion point `y` with `F c y ∈ L`; then for every torsion point `w`,
`B.HasShiftBound v w C` holds for all sufficiently large `C`. 

### `hasMultiplicativeNorm_of_frequently_hasShiftBound`

 The contraction. Suppose that arbitrarily close to `0` there are linear maps `e` with (a) `e`
right inverse to the action `F c` of some `c ≠ 0` in `R`, and (b) every torsion point `y` with
`c y ∈ L` has the constant `1` in every degree (`A.HasShiftBound v y 1` for every form `A`: for the
size function `φ` of each twisted theta function of degree `A`, `(sup φ)² ≤ sup_x φ(x) φ(x + y)`
over torsion points `x`). Then `HasMultiplicativeNorm v L` holds: for any two forms and twisted
theta functions `f`, `g` of those degrees, the sup norm (with respect to `v`) of `f g` is the
product of the sup norms of `f` and `g`. 

### `_root_.New.ThetaTori.hasMultiplicativeNorm_of_expanding`

 The multiplicative norm from expanding multiplications. Let `R`, a domain of characteristic zero
and finite over ℤ, act on `V / L` with the hermitian data `h`. Let `p` be a prime with `v p < 1`,
and let `n`, prime to `p`, map the dual lattice of `B` into `L`. Suppose every neighbourhood of `0`
holds a right inverse of `F c` for some `c ∈ R` that is not a unit, is prime to `star c`, divides a
power of `p` and has `v (det (F (star c))) = 1`. Then `V / L` has good reduction at `v` in analytic
form. For any degrees and any sizes φ, ψ of twisted theta functions f, g of those degrees, the sup
norm (on torsion points) of φψ, the size of fg, is the product of the sup norms. 

 ## Good reduction of a theta torus over a good prime 

### `New.ThetaTori.ThetaTorus.riemannForm_smul_add_pullForm`

 The average `(x.automorphyForm + i^* x.automorphyForm) / 2` of the form of the theta torus `x`
over multiplication by `i` has the same Riemann form as `x.automorphyForm`. 

### `New.ThetaTori.ThetaTorus.isHermitianAction_smul_add_pullForm`

 The average `(x.automorphyForm + i^* x.automorphyForm) / 2` of the form of the theta torus `x`
over multiplication by `i` is a hermitian form for the action `x.intAction` of `𝓞 E`, with
`β = D.β`. 

### `New.ThetaTori.ThetaTorus.hasGoodReduction_and_val_card_eq_one`

 Let `ρ` map `𝓞 E` into the valuation ring of `v`, agreeing with `Φ v₀`, and let the prime of
`𝓞 E` below the maximal ideal of the valuation ring be good for `D`. Then the theta torus `x` has
good reduction for `v` (`New.ThetaTori.HasGoodReduction` for `x.automorphyForm`, `x.multiplier` and
`D.paddedNorm`), and the order of `D.dualTorsion` has valuation `1`. 
