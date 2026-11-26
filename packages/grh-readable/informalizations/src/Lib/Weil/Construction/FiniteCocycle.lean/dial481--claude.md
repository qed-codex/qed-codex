---
{
  "module": "src/Lib/Weil/Construction/FiniteCocycle.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/FiniteCocycle.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/FiniteCocycle.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The finite cocycle as a finite Gauss sum, and its triviality

This file treats the matrix action of the finite unitary group `New.Gf` on the finite Heisenberg
datum `New.stdLattice.finHeisenberg` of vectors `ι → 𝔸f E`, with vacuum `New.stdLattice.finVac` and
multiplier `New.finMultiplier`. We write `Ô` for `New.Ô E`, `ψ₀` for
`New.stdLattice.selfDualAddChar E`, `x* y` for `star x ⬝ᵥ y`, and `c₀` for `WeilData.traceOne`.
The double integral in the resulting cocycle is a finite Gauss sum, and the cocycle equals `1`.

## Main definitions and results

* `New.stdLattice.exists_gauss_sum_finProjAction`: the double integral in the cocycle is a Gauss sum
  over a finite module over `New.Ô`, the ring of integral finite adeles.
* `New.stdLattice.mem_cocycleRadical`: the cocycle is `1` at all `g` and `s`.
* `New.finAction`: the same action with cocycle `1`, as used for the adelic Weil representation.

Notions from other files:
* `New.WeilData`: Weil data on a CM field E: ȷ in E with ȷ = −ȷ̄, a finite idele α for which Ô is
  self-dual under (z, u) ↦ ψ_f(ȷαᾱzu), and a splitting character υ.
* `New.Heisenberg.IsVacuum`: a vacuum for β and μ is a continuous, integrable, even, real function e
  with e(0) = 1 and ∫ e(z)e(x−y−z)β(z,y)β(z+y,x) dμ(z) = e(y)e(x).
* `New.Heisenberg.MultiplierAction`: an action of G on W that preserves β and μ. It comes with a
  continuous multiplier Δ: G → ℂ such that Δ(1) = 1, Δ(g⁻¹) = conj Δ(g) and Δ(g)Δ(h)Δ((gh)⁻¹) ∬
  e(hx)e(ghy)β(x,y)e(x+y) = c(g,h).
* `New.stdLattice.finVac`: the function `ψ₀ (c₀ x* x / 2)` on the lattice `Ô ^ ι` and `0` off it.
* `New.finMultiplier`: for g in `New.Gf`, Δ_f(g) = χ_f(det u) with uÔ^ι = Ô^ι ∩ g⁻¹Ô^ι and
  χ_f = υ|·|^(−1/2).

## Relation to the literature

Known; see `Lib.Weil.MixedModel.ZeroTerm` for sources.



## The finite cocycle as a finite Gauss sum

The vacuum `New.stdLattice.finVac` vanishes off the standard lattice. So the integrand of the double
integral that defines the cocycle lives on a compact module, where it is invariant under an open
submodule.


### `finProjAction`

 The matrix action of the finite unitary group on the finite Heisenberg datum (β x y = ψ₀(y*
x / 2); vacuum `finVac` = ψ₀(c₀ x* x / 2) on Ô^ι and `0` off it; `latticeMeasure` the Haar measure
giving Ô^ι mass one), with multiplier `New.finMultiplier`, paired with its cocycle
`finProjAction.1`, for which the cocycle identity holds by definition. 

### `cocycleIntegrand_eq`

 The integrand of the double integral in the cocycle at `(g, s)`, made of the vacuum `finVac`
(ψ₀(c₀ x* x / 2) on Ô^ι, `0` off it) and the bicharacter `β` of `finHeisenberg`, is
`selfDualAddChar E (c̄₀ y* x)`, with `c₀ = traceOneAdele`, if `x + y`, `s x` and `g s y` lie in the
standard lattice, and `0` otherwise. 

### `selfDualAddChar_traceOne_dot_congr`

 Let `(x₁, x₂)` and `(y₁, y₂)` be pairs whose sums and whose images under `(s, g s)` lie in the
standard lattice, and which differ by lattice vectors. Then `selfDualAddChar E (c̄₀ x₂* x₁)` and
`selfDualAddChar E (c̄₀ y₂* y₁)` agree. 

### `cocycleSubmodule`

 The pairs `(x, y)` of finite adelic vectors such that `x + y`, `s x` and `g s y` lie in the
lattice `Ô^ι`, as an `Ô E`-submodule. The integrand of the cocycle at `(g, s)` lives on it
(`New.stdLattice.cocycleIntegrand_eq`). 

### `measureReal_prod_inter_cocycleSubmodule`

 For the square of the Haar measure `latticeMeasure E ι`, which gives Ô^ι mass one, the pairs
`(x, y)` in `Ô^ι × Ô^ι` that lie in `cocycleSubmodule g s` (that is, `x + y`, `s x` and `g s y` are
again in `Ô^ι`) have volume `(‖Δ s‖ ^ 2)⁻¹ * (‖Δ (g * s)‖ ^ 2)⁻¹`, with `Δ = finMultiplier`. 

### `finMultiplier_mul_smul_mul_eq`

 In the product of multipliers on the left of the Gauss sum identity
`New.stdLattice.exists_gauss_sum_finProjAction`, the volume factors
`(‖Δ s‖ ^ 2)⁻¹ * (‖Δ (g * s)‖ ^ 2)⁻¹` cancel against `Δ x * Δ x⁻¹ = ‖Δ x‖ ^ 2` for `x = s` and
`x = g * s`, with `Δ = finMultiplier`: only `Δ g` and the factor `z` remain. 

### `exists_gauss_sum_finProjAction`

 The cocycle as a finite Gauss sum. For `g`, `s` in the finite unitary group there are a finite
module `Q` over the ring `Ô E` of integral finite adeles, in the larger of the universes `u_1` of
`E` and `u_2` of `ι`, and a function `γ` from `Q` to the finite adeles with the following
properties. Take the cocycle `c = finProjAction.1` of the matrix action of `Gf E ι` on the finite
Heisenberg datum, the multiplier `Δ = finMultiplier` (`glMultiplier` of the underlying invertible
matrix) and the character `ψ₀ = selfDualAddChar E`, z ↦ ψ_f(ȷαᾱz). Then (a)
`c g s * Δ s⁻¹ * Δ (g * s)` is the sum of `ψ₀ (γ q)` over `Q` times `Δ g`; and for all `t` in `Ô E`
and `q` in `Q`, (b) `γ (t • q)` and `star t * t * γ q` have the same value under `ψ₀`, and (c)
`t • q = 0` if the matrix `t • s⁻¹` has entries in `Ô E`. 


## Triviality of the finite cocycle

* `New.stdLattice.finProjAction_cocycle_eq_one_of_mem`: the cocycle at `(g, s)` is `1` when `s` lies
  in the stabiliser `New.stdLevel` of the standard lattice.

The `s` at which the cocycle is `1` for all `g` form a subgroup,
`New.Heisenberg.IsVacuum.cocycleRadical`. It contains `New.stdLevel`, so only `s` supported on one
pair of conjugate places remain. The cocycle has absolute value `1`, and
`New.stdLattice.exists_gauss_sum_finProjAction` turns it into a Gauss sum. At a split place `w`,
where one may assume `s⁻¹` integral at `w`, all terms of this sum are `1`. At a place fixed by
conjugation `New.eq_one_of_apply_apply_eq_neg` fixes the sign.


### `finProjAction_cocycle_eq_one_of_mem`

 The finite cocycle is `1` at `(g, s)` when `s` lies in the stabiliser `New.stdLevel` of the
standard lattice. 

### `norm_cocycle_eq_one`

 The finite cocycle has absolute value one, as the operators of the action are isometries. 

### `finMultiplier_div_nonneg_of_isSplit`

 For `a`, `s` supported on a split place `w` and its conjugate, `Δ a / Δ (a * s) / Δ s⁻¹` is
nonnegative, that is real and `≥ 0` in `ComplexOrder`, with `Δ = finMultiplier`: the phase of
`Δ x` is a character of the determinant of `x` at `w`. 

### `exists_finMultiplier_eq_neg_pow`

 Let `x` be an element of the finite adelic unitary group `Gf E ι` (matrices g over the finite
adeles with gᴴg = 1) supported on an inert place `w`: `w` is fixed by conjugation, and `x` has
component 1 at every other place. If the residue field of `w` has `w.q = r ^ 2` elements, then the
multiplier Δ_f(x) (`New.finMultiplier`) is a power of `-r`, as the splitting character `υ` of the
Weil data is `-1` at the uniformiser. 

### `eq_one_of_gauss_sum_of_inert`

 Let `w = star w` be an inert place with `w.q = r ^ 2` residue field elements, `r ≡ 3` modulo
`4`. Let `Q` be a finite `Ô E`-module killed by `idem (star {w})ᶜ`, the idempotent that is `1` off
`w = star w` and `0` at it. Let `γ` be hermitian-quadratic modulo the kernel of the character
`selfDualAddChar E`. If `‖c‖ = 1` and `c * (-r) ^ k` is the Gauss sum of `γ` times `(-r) ^ m`,
then `c = 1`. 

### `mem_cocycleRadical`

 **The finite cocycle is trivial**: `finProjAction.1 g s = 1` for all `g`, `s` in the finite
unitary group. It is stated as membership of `s` in `New.Heisenberg.IsVacuum.cocycleRadical` for the
action `New.stdLattice.finProjAction`, the subgroup of the `s` with `finProjAction.1 g s = 1` for
every `g`, so that the proof may argue on generators. Forming that subgroup needs
`finProjAction.1 g 1 = 1` for all `g`. This follows from
`New.stdLattice.finProjAction_cocycle_eq_one_of_mem`, since `1` lies in `New.stdLevel`.

A special case of the splitting of the Weil representation over unitary groups (Kudla) at the finite
places, for one explicit normalisation on the finite vacuum. 

### `_root_.New.finAction`

 The matrix action of the finite adelic unitary group on the finite Heisenberg datum with
multiplier `New.finMultiplier`, together with the fact that its cocycle is identically 1. 
