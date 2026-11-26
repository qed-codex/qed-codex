---
{
  "module": "src/Lib/SiegelWeil/OneVector/FinitePlaceDensity.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/OneVector/FinitePlaceDensity.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/OneVector/FinitePlaceDensity.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Local measure bounds and local densities at a finite place

Local measure estimates at a finite place, and Fourier inversion for local densities near a
hermitian quadric. A finite place `New.Floors.IntegralPlace A` is a place `New.Floors.Place A` (a
ring with involution, Haar measure, modulus `modulus`, character `ψ`, an element `τ` with
`τ + star τ = 1`, a skew unit δ = `skewUnit` and a Haar measure ν = `skewMeasure` on the skew
elements) with a compact open ring of integers `R` of volume `1`.

## Main definitions and results

* `New.Floors.IntegralPlace.exists_content`, `New.Floors.IntegralPlace.contentIndex`: the content of
  a vector with a unit entry, and its index.
* `New.Floors.IntegralPlace.lintegral_contentIndex_pow_le`: if `New.idealZeta integers μ ≤ 2` and
  the dimension is large enough, the integral of a power of the index of a block of coordinates over
  the vectors v with βv integral is at most `New.idealZeta integers μ` times a power of
  `(modulus β)⁻¹`.
* `New.Floors.IntegralPlace.topEichler`, `New.Floors.IntegralPlace.orbitPoint_topEichler`: an
  explicit isometry `g` of `T.splitGram` with `FloorGroups.orbitPoint 𝔰.top g` (that is `g⁻¹ z` for
  the last frame vector `z`) equal to `e`. With `l` the index of `z`, it is built from a vector `u`
  such that h(u, y) = `y l` for all `y` and `u l = 0`. The equation holds if h(e, e) = h(z, z) and
  `e l` is a unit.
* `New.Floors.IntegralPlace.ascConv_mconv_unfolding`: the mass of a coset of the congruence subgroup
  `New.unitaryLevel`.
* `New.Floors.IntegralPlace.setIntegral_eq_slab`,
  `New.Floors.Place.IsDisintegration.setLIntegral_slab`: orthogonality of characters reduces the cut
  double integral to the mass of a slab, and that mass is an integral of masses of quadrics.
* `New.Floors.IntegralPlace.integral_skewMeasure_eq_toReal_lintegral`,
  `New.Floors.IntegralPlace.enorm_localDensity_le`: let `f ≥ 0` be continuous of compact support.
  Let `J` be hermitian, let the measures `l b` on the quadrics disintegrate Haar measure along
  `x ↦ x* J x` (`New.Floors.Place.IsDisintegration`), and let `ψ` be trivial on traces. If the outer
  integral converges absolutely, the local density of `f` at `δ⁻¹ t` is the integral of `f` against
  `l t`. Its norm is always at most this integral.

Notions from other files:
* `New.Shape.Form.splitGram`: The Gram matrix of ϱ hyperbolic planes and a middle space with Gram
  matrix T: identity blocks pair the first and last ϱ indices, T is the middle block, all else is
  zero.
* `New.idealZeta`: The ideal zeta sum ∑ [R : I]^(−s) over the ideals I of finite index in R, for a
  natural number s, with values in [0, ∞].
* `New.Shape.BesselIndex`: The index set of the basis e₁, …, e_ϱ, x_i (i in κ), z, e*₁, …, e*_ϱ.

## Relation to the literature

Known; see `Lib.SiegelWeil.OneVector.SiegelClassSum`, `Lib.Adelic.Adeles.Basic` and
`Lib.Adelic.Witt.IwasawaDecomposition` for sources.


### `IntegralPlace`

 A finite place: a place `A` with its ring of integers `integers`, the subring `O` of the
semilocal field `A`. The subring `integers` is open and compact of volume `1`, is stable under
conjugation and locally a valuation ring (`New.IsAdelic`), and is self-dual for the character `ψ`.
The data of the place are normalised to `integers`: the element `element` of trace `1` is integral,
`skewUnit` is a unit of `integers`, the Plancherel constant `kernelBound` is `1`, and the skew
elements of `integers` have `skewMeasure` `1`. The modulus `modulus x` is the inverse of the
generalised index of `x integers` in `integers`. 

### `IntegralPlace.element_mem`

 The element `element` of trace `1` is integral. 

### `IntegralPlace.skewUnit_mem`

 The skew unit is integral. 

### `IntegralPlace.skewUnit_inv_mem`

 The inverse of the skew unit is integral. 

### `IntegralPlace.kernelBound_eq_one`

 The bound in the Plancherel kernel is `1`. 

### `IntegralPlace.skewMeasure_setOf_mem`

 The integral skew elements have measure `1`. 

### `IntegralPlace.self_dual`

 The ring of integers `R = O` is self-dual for `ψ`: the character `r ↦ ψ (r * a)` is trivial on
  `R` if and only if `a ∈ R`. 

### `IntegralPlace.modulus_eq_inv_genIndex`

 The modulus `modulus x` is the inverse of the generalised index of `x integers` in
  `integers`. 

### `integers`

 The ring of integers of the finite place: the compact open subring O of A. 

### `data_normalised`

 The data of a finite place are normalised to its ring of integers: `element`, `skewUnit` and its
inverse are integral, `kernelBound` is `1`, and the integral skew elements have measure `1`. 

 ### Volumes of fractional ideals and lattices 

### `volume_setOf_mul_mem`

 For a unit `u` of `A`, the set `u⁻¹ R` has volume `(modulus u)⁻¹`, where `R` is the ring of
integers (the subring `O`) and `modulus` the modulus of the place `P`. 

### `exists_ideal_cardQuot_eq`

 For a unit `c` of `A` that lies in `R`, the set `c R` is an ideal of `R` of finite index
`(modulus c)⁻¹`. 

### `skewMeasure_setOf_mul_mem`

 For a self-adjoint unit `u`, the skew elements of `u⁻¹ O` have measure
`modulus u ^ (-1 / 2)`. 

### `isOpen_isCompact_volume_intVectors`

 The lattice of integral vectors is open and compact, of volume `1`. 

### `modulus_le_volume`

 A set that contains `u R` has volume at least `modulus u`. 

### `modulus_le_one`

 A unit of `A` that lies in `R` has modulus at most `1`. 

### `unitaryLevel_open_compact`

 The principal congruence subgroups `unitaryLevel integers g J` (the `k` with `k`, `k⁻¹` and
`g⁻¹ (k - 1)` integral) of the unitary group `U J` of the matrix `J` are open for every unit `g`,
and the one of level `1` is compact. 

### `modulus_det_eq_one`

 The determinant of a matrix in `GL(R)` has modulus `1`. 

 ### The content of a vector 

### `exists_content`

 Content: if some entry of `p` is a unit of `A`, there are a unit `t` of `A` and a row `r` over
`integers` with `r ⬝ᵥ p = t` such that `c • p` is integral exactly when `t * c ∈ integers`. 

### `contentIndex`

 The volume of the set of c in A with cp integral if the entry p_i is a unit of A, and ∞
otherwise. 

### `measurable_contentIndex`

 The content index at `i` is a measurable function of the vector. 

### `lintegral_contentIndex_pow_le`

 Let ζ_O(μ) ≤ 2, V ∈ GL_ι(O), β a unit, and single out the coordinates indexed by κ of Vᴴw,
through σ. Suppose |κ| = s + k with k ≥ μ, and put d = |n| + k, so that d = |ι| − s. The integral of
the s-th power of the content index (`New.Floors.IntegralPlace.contentIndex`) of these coordinates
over the w with βw integral is at most ζ_O(μ)·md(β)^(−d), where md is the modulus, O is the ring of
integers, GL_ι(O) is `intGL ι integers` and ζ_O is `New.idealZeta integers`. 

 ### Eichler maps to the last frame vector 

### `topEichlerMatrix`

 Let `z` be the last frame vector, `l` its index, `h` the form and `v = e - z`. This is the
matrix of the scaled Eichler map `1 + u h(v, ·) - (e l)⁻¹ (v + s u) h(u, ·)` along `u`, where
`s = h(v, e) - τ (h(e, e) - h(z, z))` and `τ = P.element`. It is the identity if `e l` is not a
unit. 

### `gram_topEichlerMatrix`

 If pairing with `u` under the Gram matrix `T.splitGram` reads the coordinate at the last frame
vector `z` and this coordinate of `u` is zero, the scaled Eichler map attached to `e` along `u` is
an isometry of `T.splitGram`. 

### `topEichler`

 The scaled Eichler map along `u` attached to `e`, as an element of the unitary group. 

### `coe_topEichler`

 The matrix of `topEichler` is `topEichlerMatrix`. 

### `topEichler_mem_floorGroup`

 If the entries of `e` of floor below `𝔰.ϱ` vanish, the scaled Eichler map along `u` attached to
`e` fixes every basis vector of floor below `𝔰.ϱ`. 

### `orbitPoint_topEichler`

 The scaled Eichler map takes `e` to `z` if `e` has the norm of `z` and its coordinate at `z` is
a unit. 

### `topEichler_single`

 The scaled Eichler map attached to the last frame vector `z` itself is the identity. 

### `measurable_topEichler`

 The scaled Eichler map depends measurably on `e`. 

### `continuousAt_topEichler`

 The scaled Eichler map along `u` depends continuously on `e` at every point `e` such that
inversion is continuous at its entry at the last frame vector `z`. 

 ### Cosets of congruence subgroups 

### `intUnits`

 The group of units of R, as a subset of A. 

### `measurableSet_exists_mul_mem_level`

 For a subgroup `S`, the set `S K c⁻¹` is measurable, where `K` is the congruence subgroup of
level `g`. 

### `ascConv_mconv_unfolding`

 Unfolding at a finite place: let η be the ascending convolution `ascConv heisenbergMeasure j` of
the measures on the first `j` Heisenberg groups, K the congruence subgroup of level `g`, θ an
s-finite measure and c an element of the unitary group. Then (η∗θ)(K c⁻¹) = η(K)·θ(N K c⁻¹), with
N = `unipotentBelow j` the unipotent group on the floors below `j`. 

 ### Fourier inversion for local densities 

### `IntegralPlace.psi_skew_eq_one_iff`

 Duality on the skew elements. Let `u` be a hermitian unit, `y` hermitian, and `ψ` trivial on
traces. Then `b ↦ ψ (e b y)` is trivial on the skew `b` with `u b` integral if and only if `u⁻¹ δ y`
is integral, that is, lies in the ring of integers `O` of the place. Here `e = P.element`,
`e + ē = 1` and `δ = P.skewUnit`. 

### `IntegralPlace.setIntegral_eq_slab`

 Orthogonality of characters. Integrate `∫ f(x) ψ(e b (x* J x − α)) dx` over the skew elements
`b` with `u b` integral, with respect to `P.skewMeasure`. The result is the `P.skewMeasure`-measure
of these `b` times the mass of `f` on the slab where `u⁻¹ δ (x* J x − α)` is integral. Here `f ≥ 0`
is continuous of compact support, `J`, `u` and `α` are hermitian, `ψ` is trivial on traces,
`δ = P.skewUnit` is the skew unit of the place, `e = P.element` with `e + ē = 1`, and integral means
in the ring of integers `O` of the place. 

### `Place.IsDisintegration.setLIntegral_slab`

 Let the family `l` of measures on the quadrics, indexed by skew elements, disintegrate Haar
measure along `x ↦ x* J x`, let `δ = P.skewUnit` and let `t` be skew. For continuous `f ≥ 0`, the
mass of `f` on the slab where `c δ (x* J x - δ⁻¹ t)` is integral is the integral of the masses of
`f` on the quadrics with index `t + b`, over the skew `b` with `c b` integral. 

### `IntegralPlace.tendsto_average_skew`

 The mean of a continuous function over the skew elements `t + b` with `b ∈ y ȳ O` tends to its
value at `t` as the unit `y` tends to zero. The factor, the measure of the `b` with `y ȳ b ∈ O`, is
the inverse of the measure of the skew elements of `y ȳ O`. 

### `IntegralPlace.integral_skewMeasure_eq_toReal_lintegral`

 Fourier inversion for local densities. Let the measures `l b`, indexed by skew `b`, disintegrate
Haar measure along `x ↦ x* J x` for a hermitian `J`, let `ψ` be trivial on traces, and let `f ≥ 0`
be continuous of compact support. Put `δ = P.skewUnit` and let `t` be skew. If the function
`b ↦ ∫ f(x) ψ(e b (x* J x - δ⁻¹ t)) dx` is integrable on the skew elements, its integral, the
density of `f` at `δ⁻¹ t`, is the integral of `f` against `l t`. Here `e = P.element` and
`e + ē = 1`. 

### `IntegralPlace.enorm_localDensity_le`

 The density of `f ≥ 0` has norm at most the integral of `f` over the quadric. If the outer
integrand is not integrable, the left side is zero by convention.

This is a one-sided form of Fourier inversion for the fiber integrals of a hermitian form at finite
places: an upper bound in norm, for continuous `f ≥ 0` of compact support, rather than an
equality. 

### `integral_eq_mul_of_section`

 For s-finite, translation-invariant measures `μ` on `X` and `ν` on `Y` (additive groups, with
`ν` also invariant under negation), let measurable maps `ι : Y → X` and `p : X → Y` satisfy
`p (ι y + x) = y + p x`, and let `K` be a measurable set with `ν K = 1`. If
`f (ι y + x) = c x * a (y + p x)` whenever `p x ∈ K`, then `∫ f ∂μ` equals the product of `∫ c ∂μ`
over `p ⁻¹' K` and `∫ a ∂ν`. 
