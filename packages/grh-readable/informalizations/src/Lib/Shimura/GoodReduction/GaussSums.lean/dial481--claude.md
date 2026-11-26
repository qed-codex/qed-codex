---
{
  "module": "src/Lib/Shimura/GoodReduction/GaussSums.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/GoodReduction/GaussSums.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/GoodReduction/GaussSums.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Hermitian tori with multiplications, Gauss sums and unfolding of the Poincaré kernel

Let `V / L` be a complex torus with multiplications `F` by a ring `R` with involution and a
polarising hermitian form `B`. The hypothesis `New.ThetaTori.IsHermitianAction` gives the
compatibilities between these data.

## Main definitions and results

* `New.ThetaTori.IsHermitianAction`: `B` is positive hermitian, its Riemann form is integral on `L`,
  `F (star a)` is adjoint to `F a`, and `star β = 1 - β`.
* `New.ThetaTori.IsHermitianAction.isAppellHumbert`: the canonical multiplier
  `New.ThetaTori.IsHermitianAction.multiplier` of `F β` gives Appell–Humbert data.
* `New.ThetaTori.IsHermitianAction.MulKernel`, `New.ThetaTori.IsHermitianAction.card_mulKernel`: the
  kernel `a⁻¹ L / L` of `a ≠ 0` on the torus has order `|det (F a)|²`.
* `New.ThetaTori.IsHermitianAction.normShift_sum_eq_char_smul`: averaging normalised translates over
  this kernel against a character gives an eigenvector.
* `New.ThetaTori.IsHermitianAction.sum_conj_pow_four_eq_sum_pow_four`: a quadratic Gauss sum over
  `κ⁻¹ L / L` has a real fourth power.
* `New.ThetaTori.IsHermitianAction.isSelfAdjoint_quotMean_pow`: the mean of `x ↦ K(c̄ x, c x)` times
  `conj (det c̄)` has a real fourth power; unfolding writes the mean as a Gauss sum times a Gaussian
  integral.

Notions from other files:
* `New.RealComplexForm.riemannForm`: The Riemann form of B: the alternating real form
  E(u, v) = Im(B(u,v) − B(v,u))/(2π).
* `New.ThetaTori.normalizedShift`: The twisted translation `New.RealComplexForm.thetaShift`,
  f ↦ (z ↦ exp(−B(x, z) − B(x, x)/2) f(z + x)), divided by the canonical multiplier at x.
* `New.IsAppellHumbert`: Appell–Humbert data: Re B is symmetric, and on L one has |χ| = 1 and
  χ(l + m) = χ(l)χ(m)·exp(πi E(m, l)), E the Riemann form of B.
* `New.IsAppellHumbert.poincareSeries`:
  K(x, y) = ∑_{l ∈ L} exp(B(x, y − x + l) − B(l,y) − B(l,l)/2)/χ(l), the sum of the terms
  `New.IsAppellHumbert.poincareTerm`.

## Relation to the literature

Known; see `Lib.Shimura.GoodReduction.MultiplicativeNorm` for sources.


 ### Hermitian data and invertibility of multiplications 

### `IsHermitianAction`

 B : LatticeForm L is a positive definite hermitian form on V, ℂ-valued and ℂ-linear in its
second argument, with Riemann form integral on L, the action F of R on the finite-dimensional
complex space V (`FinComplexSpace V`) preserves L with ā adjoint to a, and β̄ = 1 − β. 

### `IsHermitianAction.map_mem`

 Every multiplication `F a` maps the lattice `L` into itself. 

### `IsHermitianAction.conj_symm`

 The form `B` is hermitian. 

### `IsHermitianAction.pos`

 The form `B` is positive definite. 

### `IsHermitianAction.adjoint`

 The adjoint of `F a` for `B` is `F (star a)`. 

### `IsHermitianAction.riemannForm_integral`

 The Riemann form of `B` takes integer values on `L`. 

### `IsHermitianAction.star_eq_one_sub`

 The element `β` and its conjugate add up to `1`. 

### `instance : NeZero (star a)`

 `star a` is nonzero when `a` is. 

### `action_comm`

 The multiplications `F r` and `F s` commute, as `R` is commutative. 

### `action_injective`

 A nonzero element of the domain `R`, finite over `ℤ`, acts injectively on `V`. 

### `action_isInvertible`

 A nonzero element of `R` acts invertibly on the finite-dimensional space `V`. 

 ### Multiplier, normalised translations and kernels 

### `multiplier`

 The canonical multiplier x ↦ exp(πi E(βx, x)) of the hermitian data, where E is the Riemann
form of B. The hermitian data only fix `B`, `F` and `β`. 

### `normShift`

 Normalised translation by x, acting on functions V → ℂ: the twisted translation
`New.RealComplexForm.thetaShift` for B, divided by exp(πi E(βx, x)), E the Riemann form of B. The
hermitian data only fix `B`, `F` and `β`. 

### `divLattice`

 The lattice a⁻¹L: the additive subgroup of the vectors y of V with ay in L, where a acts
through F. The hermitian data only fix `L` and `F`. 

### `MulKernel`

 The kernel a⁻¹L / L of multiplication by a on the torus V/L. 

### `out_mem_iff_eq_zero`

 The chosen representative of a class in a⁻¹L / L lies in L only for the zero class. 

### `riemannForm_apply_beta_eq_sub`

 For hermitian data `h` and the Riemann form `E` of `B`: `E(β u, w) = E(u, w) - E(u, β w)`, so
that `F β` behaves as one half of the identity. 

### `isAppellHumbert`

 For hermitian data `h`, the canonical multiplier of `F β` (`h.multiplier`) and `B` are
Appell–Humbert data (`New.IsAppellHumbert`). 

### `riemannPhase_eq_one`

 Let `x` lie in the dual lattice of `B` (`E(x, l)` is an integer for `l ∈ L`, `E` the Riemann
form) and let `F (star a) y ∈ L`. Then the phase `exp (2πi E(F a x, y))` is `1`. 

### `normShift_normShift_of_mem`

 For `u, w ∈ L` the normalised translations by `u` and `w` compose to that by `u + w`: on `L`
the phase in their composition law is `1`. 

### `normShift_map_out`

 Let `f` be fixed by the normalised translations by `a l`, `l ∈ L`. For `z ∈ a⁻¹ L`, the chosen
representative of the class of `z` in `a⁻¹ L / L` gives the same translate of `f` as `z`. 

### `multiplier_eq_exp`

 The canonical multiplier written with `B` and `F (star β)`, without the Riemann form: it equals
`exp (B x (F (star β) x) - B x x / 2)`. 

### `nsmul`

 Hermitian data stay hermitian data when `B` is multiplied by a positive integer `m`. 

 ### Finite kernels and their eigenvectors 

### `card_mulKernel`

 For hermitian data `h` and a full-rank lattice `L`, the kernel `a⁻¹ L / L` of multiplication by
`a ≠ 0` has order `det (F a) * conj (det (F a))`. 

### `normShift_sum_eq_char_smul`

 Let `h` be hermitian data and `a ≠ 0`. Let `f` be fixed by the normalised translations by `a l`,
`l ∈ L`, let `ξ` be a character of the finite kernel `a⁻¹ L / L`, and let
`s = ∑_k ξ(−k) • (normalised translate of f by a k.out)`, where `k.out` is the chosen
representative of the class `k`; the terms do not depend on that choice. For `y ∈ a⁻¹ L`, the
normalised translation by `a y` multiplies `s` by `ξ(y)`. 


## Gauss sums and the mean of the Poincaré kernel

Here `K = h.isAppellHumbert.poincareSeries` is the Poincaré kernel for the multiplier
`h.multiplier`, and `New.quotMean` is the mean over `V / L` (total mass one).


### `sum_conj_pow_four_eq_sum_pow_four`

 The fourth power of a Gauss sum is real. Let `h` be hermitian data, `κ ≠ 0`, and let `q` be a
function on the finite group `κ⁻¹ L / L` with `q z = exp (B x (F r x))` for every lift `x ∈ κ⁻¹ L`
of `z`. Then the sums of `q` and of its complex conjugate have the same fourth power. 

### `exp_eq_of_mem_lattice`

 For hermitian data `h` and `x, y ∈ L`, the number `B x y - B y x` lies in `2 π i ℤ`, so adding
it does not change an exponential: `s = t + B x y - B y x` gives `exp s = exp t`. 

### `poincareSeries_add`

 For hermitian data `h`, the Poincaré kernel `K` (`h.isAppellHumbert.poincareSeries`) under
translation of its first argument by a lattice vector `l`:
`K(x + l, y) = χ(l)⁻¹ exp (-(B l x + B l l / 2)) K(x, y)`, with `χ = h.multiplier`. 

### `isContPeriodic_poincareSeries`

 For hermitian data `h`, the function `x ↦ K(ā (x + w), a (x + w))` is continuous and
`L`-periodic, where `K` is the Poincaré kernel and `ā = star a`. 

### `exp_mul_sub_eq_of_sub_mem`

 For hermitian data `h` and `κ = c - star c`, let `α = star β * κ - c`. On `κ⁻¹ L` the number
`exp (B x (F (κ * α) x))` depends only on the class of `x` modulo `L`. 

### `hasSum_poincareSeries_mulKernel`

 For hermitian data `h` and `κ = c - star c ≠ 0`, with `α = star β * κ - c`: the Poincaré
kernel `K(c̄ x, c x)` is the sum over `l ∈ L` of the Gauss sums
`∑ z, exp (B z (F (κ α) z)) * exp (B w (F (κ c) w))`, `w = l + x + z`, over representatives `z` of
`κ⁻¹ L / L`. 

### `isSelfAdjoint_quotMean_pow`

 Let `h` say that `B` is a positive definite hermitian form whose Riemann form is integral on the
full-rank lattice `L`, and that `F` is an action of `R` preserving `L` with `F (star a)` adjoint to
`F a` and `star β = 1 - β`. Let `K(x, y) = ∑_{l ∈ L} exp(B(x, y - x + l) - B(l, y) - B(l,
l)/2) / χ(l)` be the Poincaré series of the Appell–Humbert data `h.isAppellHumbert`, and let
`κ = c - star c` be non-zero. Then the mean over `V / L` of `x ↦ K(c̄ x, c x)`, where `c̄ = star c`,
times the complex conjugate of the determinant of `F c̄` on `V`, has a real fourth power. 
