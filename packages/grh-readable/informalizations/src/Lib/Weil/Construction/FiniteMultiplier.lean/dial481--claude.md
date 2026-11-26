---
{
  "module": "src/Lib/Weil/Construction/FiniteMultiplier.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/FiniteMultiplier.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/FiniteMultiplier.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite Heisenberg datum, its lattice vacuum and the finite multiplier

This file treats the finite part of the standard Heisenberg model on vectors `ι → 𝔸f E` of finite
adeles of a CM field `E`. The elements `j`, `α` and the character `υ` come from `New.WeilData`, and
`New.ψf` is the standard character. We write `Ô` for `New.Ô E`, `ψ₀` for the complex character
`New.stdLattice.selfDualAddChar E`, z ↦ `ψf (j α ᾱ z)`, `x* y` for `star x ⬝ᵥ y`, and `c₀` for the
integral element `WeilData.traceOne` of `E`, which satisfies `c₀ + star c₀ = 1`. This file builds
the finite Heisenberg datum and its vacuum on the standard lattice. It defines the finite multiplier
`Δ_f` through saturating matrices and proves its laws on the finite unitary group `New.Gf`. It also
proves a lemma that fixes a sign by a congruence modulo `4`.

## Main definitions and results

* `New.stdLattice.isVacuum_finVac`: `New.stdLattice.finVac` is a vacuum (`New.Heisenberg.IsVacuum`)
  for `New.stdLattice.finHeisenberg`. The convolution identity follows from
  `New.stdLattice.finVac_add` and the self-duality of the lattice.
* `New.glMultiplier`, `New.glMultiplier_mul_diagGL_mul`: the multiplier on `GL_ι(𝔸_f)` and its value
  in terms of elementary divisors, from which its laws are read off.
* `New.finMultiplier`: its restriction to the finite unitary group `New.Gf`, with
  `New.finMultiplier_inv`, `New.norm_finMultiplier_sq`, `New.upsilon_mul_finMultiplier` and
  `New.finMultiplier_eq_of_supportedOn`.

Notions from other files:
* `New.WeilData`: Weil data on a CM field E with a primitive 5040th root of unity, so that E/E⁺ is
  unramified at the finite places. They consist of ȷ in E with ȷ = −ȷ̄, Im τȷ > 0 for every τ in the
  CM type and (1 − ȷ⁻¹)/2 integral; a finite idele α for which the completed integers Ô are
  self-dual under (z, u) ↦ ψ_f(ȷαᾱzu); and a splitting character υ equal to −1 at uniformisers of
  the places w with w = w̄.
* `New.Heisenberg.IsVacuum`: a vacuum for β and μ is a continuous, integrable, even, real function e
  with e(0) = 1 and ∫ e(z)e(x−y−z)β(z,y)β(z+y,x) dμ(z) = e(y)e(x).

## Relation to the literature

Known; see `Lib.Weil.MixedModel.ZeroTerm` for sources.



## A sign from a real sum of roots of unity over orbits of order four

`New.eq_one_of_apply_apply_eq_neg` determines a sign from a Gauss-type sum by a congruence modulo
`4`.


### `New.eq_one_of_apply_apply_eq_neg`

 Let `X` be a finite abelian group without `2`-torsion and `f : X → X` a map with
`f (f x) = -x`, so that off `0` the orbits of `f` have four points. Let `F : X → ℂ` be invariant
under `f`, with roots of unity as values, `F 0 = 1` and real sum. Let `r ≡ 1` modulo `4`. If
`‖c‖ = 1` and `c * r ^ a = (∑ x, F x) * r ^ b`, then `c = 1`: the sum is `1` plus `4` times an
algebraic integer, which rules out `c = -1`. 


## The standard lattice, the character ψ₀ and the finite Heisenberg datum

* `New.stdLattice.semichar`, `New.stdLattice.finVac`: the function `x ↦ ψ₀ (c₀ x* x / 2)`, and the
  same function set to `0` off the lattice.


 ### The lattice and the character 

### `_root_.New.stdLattice`

 The standard lattice Ô^ι, as an additive subgroup of the finite adelic vectors indexed by ι. 

### `selfDualAddChar`

 The character `z ↦ ψf (j α ᾱ z)` of the finite adeles, with complex values. 

### `traceOneAdele`

 The integer c₀ of the Weil data (c₀ + c̄₀ = 1), viewed as a finite adele of E. 

### `half`

 The number ½, viewed as a finite adele of E. 

### `selfDualAddChar_star`

 Let E be a CM field with Weil data (ȷ = −ȷ̄, finite idele α). Let ψ₀ = `selfDualAddChar E` be
the complex character z ↦ ψ_f(ȷαᾱz) of the finite adeles. Then ψ₀(z̄) = ψ₀(−z) for every finite
adele z, because `ȷ α ᾱ` is purely imaginary. 

### `forall_selfDualAddChar_mul_eq_one_iff`

 The ring `Ô E` of integral finite adeles is its own dual for the pairing
`selfDualAddChar E (z * u)`. 

### `selfDualAddChar_congr`

 If `a = b + (t + star t) + o` with `o` integral, then `selfDualAddChar E` takes the same value
at `a` and `b`: it does not see a trace `t + star t` or an integral summand. 

 ### The vacuum and the Heisenberg datum 

### `semichar`

 For a finite adelic vector x, the complex number ψ₀(c₀ x* x / 2). It equals ψ_f(−y* y / 4) at
y = αx (`New.stdLattice.semichar_eq_ψf`) and is a sign on the lattice Ô^ι. 

### `semichar_eq_ψf`

 Let E be a CM field with Weil data and x a finite adelic vector indexed by ι. Then `semichar x`,
defined as ψ₀(c₀ x* x / 2), equals `ψf (-y* y / 4)` at the rescaled vector `y = α x`. Here `ψf` is
the standard additive character of the finite adeles, α is the finite idele from the Weil data, and
¼ is written as `half * half`. 

### `finVac`

 The finite vacuum: `semichar x = ψ₀ (c₀ x* x / 2)` on the lattice `Ô ^ ι` and `0` off it. 

### `finHeisenberg`

 The Heisenberg datum on finite adelic vectors with bicharacter `β x y = ψ₀ (y* x / 2)`. 


## The twisted lattice indicator as a vacuum

* `New.stdLattice.mem_stdLattice_iff_selfDualAddChar`, `New.integral_selfDualAddChar_stdLattice`:
  the lattice is self-dual for `selfDualAddChar (y* x)`, so `y ↦ selfDualAddChar (x* y)` integrates
  over it to `1` or `0` as `x` lies in it or not.


 ### The lattice and its measure 

### `_root_.New.latticeMeasure`

 The Haar measure on n-tuples of finite adeles of E that gives the lattice Ô^n mass one. 

### `_root_.New.latticeMeasure_stdLattice`

 For a CM field E, the Haar measure `latticeMeasure` on ι-tuples of finite adeles of E, which is
normalised so that Ô^ι has mass one, gives the standard lattice Ô^ι (`stdLattice E ι`) measure 1. 

### `star_mulVec_dotProduct_mulVec`

 An element `g` of the finite unitary group `New.Gf` preserves the form `x* y`. 

### `star_dotProduct_mem`

 For `y` and `z` in the lattice `Ô ^ ι`, the product `z* y` is integral. 

 ### The vacuum and self-duality 

### `semichar_add`

 Let ψ₀(z) = ψ_f(ȷαᾱz) be the self-dual character of the finite adeles
(`New.stdLattice.selfDualAddChar`), and let `c₀` be the integer of the Weil data with c₀ + c̄₀ = 1
(`traceOneAdele`). For finite adelic vectors `x` and `y`, `semichar x * semichar y * β x y = ψ₀ (c̄₀
y* x) * semichar (x + y)`, where `semichar x = ψ₀ (c₀ x* x / 2)` and `β x y = ψ₀ (y* x / 2)` is the
bicharacter of `New.stdLattice.finHeisenberg`. 

### `finVac_add`

 For `y` in the lattice `New.stdLattice E ι` and any `x`,
`finVac x * finVac y * β x y = finVac (x + y)`, where `β` is the bicharacter of
`New.stdLattice.finHeisenberg`. 

### `mem_stdLattice_iff_selfDualAddChar`

 The lattice `Ô ^ ι` is its own dual for the pairing `ψ₀ (y* x)`: `x` lies in it if and only if
the pairing of `x` with every lattice vector `y` is trivial. 

### `_root_.New.integral_selfDualAddChar_stdLattice`

 The integral of `y ↦ selfDualAddChar (x* y)` over the lattice `New.stdLattice E ι`, for
`New.latticeMeasure`, is `1` if `x` lies in the lattice and `0` otherwise. 

### `isVacuum_finVac`

 The function `New.stdLattice.finVac` is a vacuum for the Heisenberg datum
`New.stdLattice.finHeisenberg` with respect to the measure `New.latticeMeasure`. 


## The finite multiplier Δ_f and its laws

The finite part `Δ_f` of the multiplier that normalises the Weil representation. For `g` in
`GL_ι(𝔸_f)` choose `u` with `u Ô^ι = Ô^ι ∩ g⁻¹ Ô^ι`; then `Δ_f g = χ_f (det u)`, where
`χ_f = υ |·|^(-1/2)` and `υ` is the splitting character of the Weil data `New.WeilData`.

* `New.IsSaturating`, `New.IsSaturating.exists_isSaturating`: the relation between `g` and `u`, in a
  form that makes sense over any subring of a ring, and the existence of `u`.
* `New.glMultiplier`, `New.IsSaturating.glMultiplier_eq`, `New.glMultiplier_mul_of_mem`: the
  multiplier on `GL_ι(𝔸_f)`; it does not depend on `u` and is bi-invariant under `GL_ι(Ô)`.
* `New.glMultiplier_mul_diagGL_mul`: its value in terms of the elementary divisors of `g`.

Notions from other files:
* `New.cutGL`: For an idempotent e of the commutative ring A, the endomorphism g ↦ e·g + (1−e)·1 of
  GL_n(A).


 ### Saturating matrices 

### `IsSaturating`

 Units `g`, `u` of a ring satisfy this relation over a subring `S` when `u` and `g u` lie in `S`
and `u⁻¹ = l + m g` for some `l`, `m` in `S`. For matrices and the lattice `Λ` of vectors with
entries in the subring this implies `u Λ = Λ ∩ g⁻¹ Λ`. 

### `IsSaturating.map_of_le_comap`

 A ring homomorphism `f` that maps the subring `S` into `S'` carries a unit `u` that saturates
`g` over `S` (`New.IsSaturating`) to a unit that saturates `f g` over `S'`. 

### `IsSaturating.inv`

 If `u` saturates `g`, then `g u` saturates `g⁻¹`: for lattices, `g (Λ ∩ g⁻¹ Λ) = Λ ∩ g Λ`. 

### `IsSaturating.mul_of_mem`

 If `u` saturates `g`, and `k`, `k'` and their inverses lie in `S`, then `k'⁻¹ u` saturates
`k g k'`. 

### `ideleAbs_locFullIdele`

 The norm of the idele that is `x` at the place `w` and `1` elsewhere
(`New.locFullIdele`) is the absolute value of `x` in the completion at `w`. 

### `IsSaturating.map_evalAt`

 If `u` saturates `b` over integral matrices (`New.IsSaturating`), then at every finite place
`w` the component of `u` saturates the component of `b` over `O_w`. 

### `IsSaturating.v_det_eq`

 Two matrices that saturate the same matrix `x` over the integers `O_w` of the completion at
`w` (`New.IsSaturating`) have determinants of the same valuation. 

### `IsSaturating.mul_of_mem_intGL`

 If `u` saturates `b` over integral matrices and `k`, `k'` lie in `GL_ι(Ô)`, then `k'⁻¹ * u`
saturates `k * b * k'`. 

 ### Elementary divisors 

### `exists_eq_mul_diagGL_mul`

 Elementary divisors over `Ô`: every `g` in `GL_ι(𝔸_f)` is `k * diag(d) * k'` with `k`, `k'` in
`GL_ι(Ô)` and ideles `d i`. 

### `denominatorIdele`

 The denominator of a finite idele `x`: the idele with component `1` where `x` is integral and
`x⁻¹` elsewhere. If `x` has order `μ` at `w`, its denominator has order `max 0 (-μ)` there. 

### `coe_inv_denominatorIdele`

 The inverse of the denominator of `x` is `1` where `x` is integral and `x` elsewhere. 

### `v_denominatorIdele`

 The valuation of the denominator of `x` at `w` is the inverse of `max 1 |x_w|`. 

### `isSaturating_diagGL`

 For finite ideles `d i`, the diagonal matrix of their denominators (`New.denominatorIdele`)
saturates the diagonal matrix of the `d i` over integral matrices (`New.IsSaturating`). 

### `IsSaturating.v_det_eq_prod`

 If `u` saturates `k * diag(d) * k'` over integral matrices, with `k`, `k'` in `GL_ι(Ô)`, then
the valuation of `det u` at `w` is the product of the inverses of `max 1 |(d i)_w|`, which are the
valuations of the denominators of the `d i`. 

 ### The chosen saturating matrix 

### `IsSaturating.exists_isSaturating`

 Let `g` be an invertible `ι × ι` matrix over the finite adeles of the number field `E`. Some
invertible `u` saturates `g` over the matrices with entries in `Ô E` (`New.IsSaturating`): `u` and
`g * u` are integral and `u⁻¹ = l + m * g` for integral `l`, `m`. Thus `u Ô^ι = Ô^ι ∩ g⁻¹ Ô^ι`. 

### `saturatingElem`

 For g in GL_ι(𝔸_f), a chosen u in GL_ι(𝔸_f) that saturates g over integral matrices
(`New.IsSaturating`): u and gu are integral, and u⁻¹ = l + mg for some integral matrices l, m. 

### `IsSaturating.v_det_saturatingElem`

 Let u be the matrix `New.saturatingElem` chosen for b, with uÔ^ι = Ô^ι ∩ b⁻¹Ô^ι. If y saturates
the component of b at w over O_w (`New.IsSaturating`), then det u at w and det y have the same
valuation. 

### `v_det_saturatingElem_eq_one`

 If the component of `b` at `w` is `1`, then the determinant of the matrix `New.saturatingElem`
chosen for `b` has valuation `1` at `w`. 

 ### The multiplier on `GL_ι(𝔸_f)` 

### `chiAdelic`

 The homomorphism x ↦ υ(x)|x|^(−1/2) from the ideles of E to ℂ, with υ the splitting
character and |x| the idele norm. 

### `chiFin`

 The character x ↦ υ(x)|x|^(−1/2) of the finite ideles of E, x being extended by 1 at
infinity. 

### `chiFin_congr`

 The character `χ_f = υ |·|^(-1/2)` of the finite ideles (`New.chiFin`) takes the same value on
two finite ideles that have the same valuation at every finite place. 

### `glMultiplier`

 For g in GL_ι(𝔸_f), Δ_f(g) = χ_f(det u), where u is the matrix `New.saturatingElem` chosen for
g, with uÔ^ι = Ô^ι ∩ g⁻¹Ô^ι. 

### `glMultiplier_mul_of_mem`

 Let `g`, `k`, `k'` be in `GL_ι(𝔸_f)` for the finite adeles of `E`, with `k` and `k'` in the
integral subgroup `GL_ι(Ô)`. Then the multiplier `Δ_f` (`New.glMultiplier`) takes the same value
at `k * g * k'` and at `g`. 

 ### The formula in the elementary divisors, and the laws 

### `glMultiplier_mul_diagGL_mul`

 The multiplier in terms of elementary divisors: if `k`, `k'` lie in `GL_ι(Ô)`, the multiplier of
`k * diag(d) * k'` is the product of `χ_f` at the denominators of the `d i`. As `χ_f` depends only
on orders (`New.chiFin_congr`), this is `∏_w χ_f(ϖ_w) ^ (∑_i max 0 (-μ_{w,i}))`, where `μ_{w,i}` is
the order of `d i` at `w`. 

### `chiFin_denominatorIdele_inv`

 Let `den x` be the denominator of a finite idele `x` (`New.denominatorIdele`). Then
`χ_f (den x⁻¹) = χ_f x * χ_f (den x)` for `χ_f = υ |·|^(-1/2)`: this is the identity
`max 0 μ = μ + max 0 (-μ)` for the orders `μ` of `x`. 

### `chiFin_star`

 The character `χ_f = υ |·|^(-1/2)` of the finite ideles turns the conjugation of `E` into
complex conjugation, as `υ (star x)` is the inverse of `υ x` on the unit circle. 

### `chiFin_denominatorIdele_star`

 For a finite idele `x`, the value of `χ_f = υ |·|^(-1/2)` at the denominator
(`New.denominatorIdele`) of `star x` is the complex conjugate of its value at the denominator of
`x`. 

### `glMultiplier_inv`

 For an invertible matrix `g` over the finite adeles of `E`, Δ_f(g⁻¹) = υ(det g)|det g|^(−1/2)
Δ_f(g), where `chiFin` is the character x ↦ υ(x)|x|^(−1/2) with υ the splitting character of the
Weil data. Here Δ_f(g) = χ_f(det u) (`New.glMultiplier`), where `u` is the chosen matrix with
uÔ^ι = Ô^ι ∩ g⁻¹Ô^ι. 

### `glMultiplier_transposeGL`

 An invertible matrix `g` over the finite adeles and its transpose have the same elementary
divisors, hence the same multiplier `Δ_f` (`New.glMultiplier`). 

### `IsSaturating.glMultiplier_transpose`

 If `u` saturates `b`, then `New.glMultiplier` of the transpose of `b` is also `χ_f (det u)`. 

### `glMultiplier_map_star`

 For `γ` in `GL_ι` over the finite adeles of the CM field `E`, applying the conjugation of `E`
entrywise to `γ` replaces its multiplier Δ_f(γ) (`New.glMultiplier`) by the complex conjugate. Here
Δ_f(γ) = χ_f(det u), where χ_f(x) = υ(x)|x|^(−1/2) (`New.chiFin`) and `u` is the chosen matrix with
uÔ^ι = Ô^ι ∩ γ⁻¹Ô^ι. 

### `glMultiplier_star`

 Let E be a CM field with Weil data and `b` an element of `GL_ι(𝔸_f)`. The multiplier `Δ_f`
(`New.glMultiplier`) of the conjugate transpose `star b` is the complex conjugate of `Δ_f b`. Here
Δ_f(b) = χ_f(det u), where u is the chosen matrix with uÔ^ι = Ô^ι ∩ b⁻¹Ô^ι, χ_f = υ|·|^(−1/2), and
υ is the splitting character of the Weil data. 

### `glMultiplier_mul_of_map_evalAt_eq_one`

 Let `b`, `b'` be invertible `ι × ι` matrices over the finite adeles of `E` such that at every
finite place at least one of them has component `1`. Then the multiplier `Δ_f` (`New.glMultiplier`)
satisfies `Δ_f (b * b') = Δ_f b * Δ_f b'`. Here `Δ_f g = χ_f (det u)`, where `u` is a chosen matrix
with `u Ô^ι = Ô^ι ∩ g⁻¹ Ô^ι`. 

### `reindexGL_blockGL_mem_intGL`

 For a bijection `e : n ≃ ι ⊕ κ` and `x`, `y` in `GL_ι(Ô)`, `GL_κ(Ô)`, the block diagonal
matrix of `x` and `y`, relabelled along `e`, lies in `GL_n(Ô)`. 

### `glMultiplier_fromBlocks`

 For an invertible finite adelic matrix h over the CM field E with Weil data, write
Δ_f(h) = `glMultiplier h`, which is χ_f(det u) for a matrix u with uÔ^ι = Ô^ι ∩ h⁻¹Ô^ι, where
χ_f = υ|·|^(-1/2). Δ_f is multiplicative on blocks: if an invertible finite adelic matrix G is,
after reindexing by a bijection e, block diagonal with invertible blocks g and g′, then
Δ_f(G) = Δ_f(g)Δ_f(g′). 

### `glMultiplier_star_inv_mul`

 Let E be a CM field with Weil data and `b` an element of `GL_ι(𝔸_f)`. Let `Δ_f b` = χ_f(det u),
where u is the chosen matrix with uÔ^ι = Ô^ι ∩ b⁻¹Ô^ι, `χ_f = υ |·|^(-1/2)` on finite ideles
(extended by 1 at infinity), and υ is the splitting character of the Weil data. The product of `Δ_f`
at the conjugate transpose of `b⁻¹` and `Δ_f b` is `‖Δ_f b‖ ^ 2` times the complex conjugate of
`χ_f (det b)`. 

### `glMultiplier_eq_pow_of_local`

 Let `b` in `GL_ι(𝔸_f)` be `1` away from the place `w`, and let `y` saturate the component of
`b` at `w` over `O_w`, so that `det y` has order `n = -log (v (det y))`, which is not negative.
Then `Δ_f b = (υ.atUniformizer w * √q) ^ n`, where `υ.atUniformizer w` is the value of `υ` at a
uniformiser of `w` and `q = w.q` is the size of the residue field. 

### `IsSaturating.setOf_mulVec_mem_stdLattice`

 Let `g`, `u` be invertible `ι × ι` matrices over the finite adeles `𝔸f E`, with `u` saturating
`g` over integral matrices (`New.IsSaturating`): `u` and `g u` have entries in `Ô`, and
`u⁻¹ = l + m g` for some matrices `l`, `m` over `Ô`. Then the vectors `x` of the lattice `Ô^ι`
(`New.stdLattice`) with `g x` in `Ô^ι` are exactly those with `u⁻¹ x` in `Ô^ι`, that is,
`Ô^ι ∩ g⁻¹ Ô^ι = u Ô^ι`. 

### `latticeMeasure_inter_eq_glMultiplier`

 For `g` in `GL_ι(𝔸_f)` with multiplier `Δ_f g` (`New.glMultiplier`), the set of `x` in `Ô^ι`
with `g x` in `Ô^ι` has volume `(‖Δ_f g‖ ^ 2)⁻¹` for `New.latticeMeasure`, the Haar measure giving
the lattice `Ô^ι` mass one. 

### `norm_glMultiplier_sq`

 For an invertible `ι × ι` matrix `γ` over the finite adeles of `E` the squared modulus of the
multiplier `Δ_f γ` (`New.glMultiplier`) is the index of `Ô^ι ∩ γ⁻¹ Ô^ι` in `Ô^ι`, where `Ô^ι` is
the lattice `stdLattice E ι` of integral vectors. 

 ### The multiplier on the finite unitary group 

### `finMultiplier`

 For g in the finite adelic unitary group, Δ_f(g) is `New.glMultiplier` of its underlying
invertible matrix. 

### `finMultiplier_inv`

 Let `g` be in the finite adelic unitary group `Gf E ι`, that is, `g` is in `GL_ι(𝔸_f)` with
`gᴴ g = 1`. The multiplier `Δ_f` (`finMultiplier`, which is `glMultiplier` of the underlying matrix)
satisfies `Δ_f g⁻¹ = conj (Δ_f g)`, the complex conjugate of `Δ_f g`. 

### `IsSaturating.v_det_mul_v_det`

 Let `γ` be in the group `New.Gf E ι` of unitary `ι × ι` matrices over the finite adeles of the
CM field `E` and let `y` saturate `γ` over integral matrices. At every finite place `w` the
valuation of `det γ * det y` is that of the conjugate of `det y`: the elementary divisors of
`γ⁻¹ = γ*` are the conjugates of those of `γ`. 

### `finMultiplier_eq_one_of_mem`

 The multiplier is `1` on the stabiliser `stdLevel E ι` of the standard lattice. 

### `norm_finMultiplier_sq`

 Let E be a CM field with Weil data and g an element of the finite adelic unitary group (gᴴg = 1
in GL_ι(𝔸_f)). Let Δ_f(g) = χ_f(det u), where u is the chosen matrix with uÔ^ι = Ô^ι ∩ g⁻¹Ô^ι,
χ_f = υ|·|^(−1/2), and υ is the splitting character of the Weil data. Then |Δ_f(g)|² equals the
index of Ô^ι ∩ g⁻¹Ô^ι in Ô^ι. 

### `upsilon_mul_finMultiplier`

 Let E be a CM field with Weil data and g an element of the finite adelic unitary group G_f
(matrices g in GL_ι(𝔸_f) with gᴴg = 1). Let Δ_f(g) = χ_f(det u), where u is the chosen matrix with
uÔ^ι = Ô^ι ∩ g⁻¹Ô^ι, χ_f = υ|·|^(−1/2) on finite ideles, and υ is the splitting character of the
Weil data. Then υ(det g)·Δ_f(g) is the complex conjugate of Δ_f(g), where det g is read as an idele
with component 1 at the infinite places. 

### `finMultiplier_eq_of_supportedOn`

 Let E be a CM field with Weil data, S a set of finite places disjoint from its conjugate S̄, and
g an element of the finite adelic unitary group G_f (matrices g in GL_ι(𝔸_f) with gᴴg = 1) whose
component is 1 at every place outside S ∪ S̄. Let `a = cutGL _ g` be the invertible matrix equal to
g at the places of S and to 1 elsewhere. Then `finMultiplier g` (that is, Δ_f of g viewed in
GL_ι(𝔸_f)) equals |Δ_f(a)|² · conj χ_f(det a), where Δ_f(h) = `glMultiplier h` is χ_f(det u) for a
matrix u with uÔ^ι = Ô^ι ∩ h⁻¹Ô^ι, and χ_f = υ|·|^(-1/2) is `New.chiFin`, with υ the splitting
character of the Weil data. 
