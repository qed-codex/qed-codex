---
{
  "module": "src/Lib/Weil/Periods/DescentVanishing.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/DescentVanishing.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/DescentVanishing.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Vanishing theta descents for unitary groups: Fourier coefficients and periods

This file defines the predicate `New.SiegelWeil.DescentsVanish`, the vanishing of all theta descents
of a function on `U(V)(𝔸)` to `U(W)(𝔸)` for data that are vacua above given places. It studies the
Fourier coefficients of theta lifts between unitary groups along the centre of the unipotent
radical. These coefficients are written as sums over rational frames. Then, for an invertible Gram
matrix, Witt's theorem writes them as integrals modulo a stabiliser.

## Main definitions and results

* `New.SiegelWeil.DescentsVanish`: the descents of `Y` vanish for all data that are vacua above the
  places of `S`.
* `New.Space.Splitting.centreCoeff_integral_eq_tsum`: the coefficient at `j β` keeps the frames `x`
  with Gram matrix `β`.
* `New.SiegelWeil.integral_blockEmb_eq_zero_of_descentsVanish`: split `V = V″ ⊕ V°` into blocks of
  ranks `n₁` and `n₂`. Let `o₁` be the frame of `V″` and `I(h)` the period over `[U(V°)]` of the
  right translate by `h`. The vanishing of a Fourier coefficient of the descents makes `I`, times a
  weight, orthogonal to every additive character of the frame `h⁻¹ o₁` that ignores its components
  at the places of `T` and their conjugates, hence, by Stone–Weierstrass, to every continuous
  function of these characters. On the support of the weight `I` is such a function, so it vanishes
  there.

Notions from other files:
* `New.𝒮`: the Banach space of data on which the Weil representation of a hermitian space acts;
  `New.Space.projOn` projects it on the vectors that are vacua above a set of finite places and
  their conjugates.
* `New.pairTheta W V a b f`: the theta kernel on `U(W)(𝔸) × U(V)(𝔸)` of a datum `f` on `Hom(W, V)`,
  twisted by the characters `a`, `b` of `U(1)`. `New.pairThetaKer` bundles it, and `New.Space.lift`
  for `(pairThetaKer W V a b).swap` integrates a function on `U(V)(𝔸)` against it.
* `New.Space.Splitting.radicalCentre`: the parametrisation of the centre of the unipotent radical by
  adelic `p × p` matrices; `centreCoeff T F g` is the mean of `ψ (tr (T M)) * F (z M * g)` over the
  `M` modulo rational matrices, `z` being this parametrisation.
* `New.WeilData.upsilonU1`: the restriction of the splitting character υ to the norm-one ideles.

## Relation to the literature

Known result: Fourier coefficients of theta lifts as periods over stabilisers. Here a single
non-degenerate coefficient of a theta lift to a split unitary group is unfolded once by Witt's
theorem. Hence a form on the definite U(n) orthogonal to the theta kernels of the split space has
zero period over the complementary unitary group. Source: P. Walls, The theta correspondence,
periods of automorphic forms and special values of standard automorphic L-functions, arXiv
1501.01565 (2015), Prop. 2.1.1; S. Rallis, On the Howe duality conjecture, Compositio Math. 51
(1984) 333–399.


 ## Vanishing of descents 

### `DescentsVanish`

 All descents of `Y` from `U(V)` to `U(W)` vanish, for the data that are vacua above the places
of `S` and their conjugates: for every datum `f` on `Hom(W, V)` fixed by the projection `projOn S`,
the function `g ↦ ∫ θ_f(g, h) Y(h) dh` on `U(W)(𝔸)` is zero. The integral is over the adelic
quotient `[U(V)]`, and `θ_f` is the theta kernel of the pair twisted by `a (det h)`, for the
character `a` of `U(1)`. No twist in `g` is taken: it would only multiply a descent by a character
of `det g`. 

### `DescentsVanish.comp_mul_right`

 Translations: let `Y` be an automorphic function on `U(V)(𝔸)` whose descents to `U(W)` vanish
for data that are vacua above `S`. If `h₀` is integral (lies in `localIntGL m w`) at every place `w`
of `S`, then the descents of the right translate of `Y` by `h₀` vanish as well. 

### `DescentsVanish.of_schrodingerOp`

 To show that all descents of `Y` by data that are vacua off a set `Σ` of places vanish, it is
enough to test special data. Here `V` is definite, `A` is a set of finite places disjoint from its
conjugate, and `Σ = A.conjClosure` consists of the places of `A` and their conjugates. For a
Schwartz–Bruhat function `Ψ` above `A`, the operator `schrodingerOp A Ψ` is the combination of
finite Heisenberg operators with which `Ψ` acts on the data. The special datum of `(P, Ψ)` applies
it to the vacuum `vacElem` of `Hom(W, V)`, and then integrates (`integrated`) the real Heisenberg
operators against the Fock vector `polyVector _ P` of the polynomial `P`, with the signs
`realSigns E (homSigns s 1)` of the coordinates at infinity. 


## Fourier coefficients of a theta integral via rational frames

Fourier coefficients of the theta lift of `y` from `U(V)` to `U(W)`, where `W` has the splitting `D`
(`New.Space.Splitting`) with isotropic frames of rank `p`. The element `j` of `E` is the imaginary
element of `New.WeilData`.


### `instance (priority`

 A monoid that acts on columns acts on matrices, column by column. 

### `_root_.New.U.smul_matrix_eq_mul`

 The unitary group acts on frames by matrix multiplication. 

### `_root_.New.Space.ratStabilizer`

 The rational stabiliser of a rational frame `x`: the image in `U(V)(𝔸)` of the group of the
rational points `γ` of `U(V)` with `γ x = x`. 

### `_root_.New.Space.mem_ratStabilizer`

 The elements of the rational stabiliser of `x` are the images of the rational points of the
unitary group that fix `x`. 

### `_root_.New.Space.gram_eq_iff_mem_orbit`

 Witt's theorem for frames: if the rational frame `x` has invertible Gram matrix for the form
`V.J`, the rational frames with the same Gram matrix are those whose orbit under the rational
unitary group `U V.J` contains `x`. 

### `radicalCentre_apply`

 By definition `radicalCentre z` is the element `radicalElement` of the unipotent radical with
zero vector and central part `-2 j z`. 

### `hasSum_thetaTerm`

 The theta kernel of the datum `f` at `(g, h)` is the sum of its terms `D.thetaTerm` over the
rational frames `x`, where `D` is the splitting of `W`. 

### `thetaTerm_radicalCentre_mul`

 Multiplying `g` on the left by the central unipotent element `radicalCentre z` multiplies the
term of the frame `x` in the theta kernel by `ψ (tr (-j β z))`, where `β` is the Gram matrix of `x`
and `ψ` the standard additive character of the adeles. 

### `thetaTerm_mul_ratEmbed_mul`

 For `y` left invariant under the rational points `V.Γ`, the term of the frame `x` in the theta
kernel at `(g, h)`, times `y h`, does not change when `(x, h)` is replaced by `(γ x, γ h)` with `γ`
rational. 

### `fixesLeft_thetaTerm_mul`

 For `y` left invariant under the rational points `V.Γ`, the term of the frame `x` in the theta
kernel, times `y`, is left invariant under the rational stabiliser of `x`. 

### `integral_pairTheta_radicalCentre_mul`

 Let `y` be continuous on `U(V)(𝔸)`, and let the terms of the theta kernel at `g` be absolutely
integrable against `y`. Then the theta lift of `y` at `radicalCentre z * g` is the sum over all
rational frames `x` of `ψ (tr (-j β(x) z))` times the integral over `[U(V)]` of the term of `x` at
`g` against `y`, where `β(x)` is the Gram matrix of `x`. 

### `centreCoeff_integral_eq_tsum`

 Let `D` split `W`, and take the theta kernel of the datum `f` twisted by the characters `a`,
`b`. Let `y` be continuous on `U(V)(𝔸)`, and let the terms of the kernel at `g` be absolutely
integrable against `y` (`HasIntegrableTerms`). Then the Fourier coefficient along the centre of the
unipotent radical, at `j β` and `g`, of the theta lift of `y` is the sum, over the rational frames
`x` with Gram matrix `β`, of the integrals over `[U(V)]` of the term of `x` times `y`. Here `j` is
the imaginary element of `E` given by `WeilData`. 

### `centreCoeff_eq_integral_ratStabilizer`

 Unfolding. Let `y` be continuous on `U(V)(𝔸)` and left invariant under the rational points, and
let the terms of the theta kernel at `g` be absolutely integrable against `y`. Let `x` be a rational
frame with invertible Gram matrix `β`. Then the term of `x` times `y` is integrable modulo the
rational stabiliser of `x`, and its integral is the Fourier coefficient along the centre of the
unipotent radical, at `j β` and `g`, of the theta lift of `y`. 

### `centreCoeff_eq_integral_stabilizer`

 Unfolding, for a subgroup `S` of `U(V)(𝔸)` that consists of the rational points fixing the
rational frame `x₀`. Let `x₀` have invertible Gram matrix `β`, let `y` be continuous and left
invariant under the rational points, and let the terms of the theta kernel at `g` be absolutely
integrable against `y`. Then the term of `x₀` times `y` is left invariant under `S` and integrable
modulo `S`, and its integral is the Fourier coefficient at `j β` and `g` of the theta lift of
`y`. 


## Vanishing of periods over a block subgroup

`stdSpace E n` is the definite space with Gram matrix `1`, and `(stdSpace E n).Γ` is its group of
rational points. `(stdSpace ..).quotMeasure` is the measure on the quotient by it. `New.G.blockEmb`
is the block-diagonal embedding of `U(n₁) × U(n₂)` in `U(n)`. The three groups are those of `V″`,
`V°` and `V = V″ ⊕ V°`.

The Fourier coefficient at the unit matrix is unfolded and integrated over `[U(n₂)]`
(`DescentsVanish.integral_frameChar_mul_blockPeriod_eq_zero`). Then the datum is varied, and the
Stone–Weierstrass theorem replaces the characters `ψ_u` by a continuous function `χ` of them that
equals the complex conjugate of the period wherever `frameWeight` is nonzero, so
`frameWeight · |I|²` has integral zero.


### `exists_continuousMap_comp_eq`

 A continuous function `f` on a compact space that depends only on the image under a continuous
map `p` to a normal Hausdorff space is a continuous function of `p`. 

### `firstFrame`

 The matrix whose columns are the basis vectors of the first block of the splitting
`n₁ ⊕ n₂ ≃ n`. In the comments below this frame is written `o₁`. 

### `movedFrame`

 The frame `h⁻¹ o₁`, where `o₁` stands for `firstFrame E o`. 

### `secondBlock`

 The embedding `h₂ ↦ diag(1, h₂)` of the unitary group of the second block of the splitting
`n₁ ⊕ n₂ ≃ n` in that of the whole space. 

### `blockPeriod`

 The period `I(h) = ∫ Y(diag(h₁, h₂) h) dh₂` over the adelic quotient `[U(n₂)]`, for a fixed
`h₁`. 

### `frameChar`

 The value `ψ_u(x) = ψ(δ ∑ u_{ij} x_{ij})` at a frame `x`, with `ψ` the standard additive
character, `δ = invDifferentIdele E` an idele whose finite part generates the inverse different, and
the components of the sum at the places of `T` and their conjugates replaced by zero. 

### `frameWeight`

 The weight `vac[α₀ x] = |e(α₀ x)|²` of a frame `x`, with `e = vacuumFn` the vacuum function on
adelic vectors and `α₀ = scaleIdele E`. It is called the slice of the vacuum below: up to a nonzero
constant, it is what the vacuum datum contributes to the term of a frame in the theta kernel. 

### `blockEmb_mul_firstFrame`

 The block-diagonal element `diag(g₁, g₂)` acts on the frame `o₁` of the first block through
`g₁`. 

### `mem_range_secondBlock`

 The stabiliser of the frame `o₁` is the second block: `g` fixes the first `n₁` basis vectors if
and only if it is `diag(1, v)` for some `v` in `U(n₂)(𝔸)`. 

### `movedFrame_secondBlock_mul`

 The frame `h⁻¹ o₁` does not change when `h` is multiplied on the left by the second block. 

### `comap_Gamma_secondBlock`

 An element of `U(n₂)(𝔸)` is rational if and only if its image in `U(n)(𝔸)` is rational. 

### `blockEmb_eq_secondBlock_mul`

 `diag(h₁, h₂) = diag(1, h₂) diag(h₁, 1)`. 

### `inv_blockEmb_mul_secondBlock_mul`

 The second block commutes with `diag(h₁, 1)⁻¹`. 

### `frameWeight_ne_zero_iff`

 The slice `frameWeight x = vac[α₀ x]` of the vacuum is not zero exactly when all entries of `x`
have integral finite part. 

### `exists_movedFrame_eq`

 If the slice `frameWeight` of the vacuum is not zero at the frame `h⁻¹ o₁`, then this frame is
`γ⁻¹ o₁` for some `γ` whose finite part lies in `stdLevel E n`, the group of integral points. 

### `smul_eq_of_frameChar_eq`

 The characters `ψ_u` separate frames away from `T` and its conjugates: two frames with the same
values `frameChar T` agree once their components at these places are removed, that is, after
multiplying by `1 - idemAdele T.conjClosure`, where `idemAdele T.conjClosure` is `1` at these places
and `0` elsewhere. 

### `blockQuotMeasure`

 The invariant measure on `U(n₂)(𝔸) \ U(n)(𝔸)`, carried by `U(n)(𝔸)`. 

### `isClosedEmbedding_secondBlock`

 The embedding of the second block is a closed embedding of `U(n₂)(𝔸)` in `U(n)(𝔸)`. 

### `continuous_blockPeriod`

 The period `I(h) = ∫ Y(diag(h₁, h₂) h) dh₂` of a continuous function `Y` on `[U(n)]` is
continuous in `h`. 

### `blockPeriod_eq_of_movedFrame_eq`

 For a continuous function `Y` on `[U(n)]`, the period `I(h) = ∫ Y(diag(h₁, h₂) h) dh₂` is left
invariant under the second block, so it depends only on the frame `h⁻¹ o₁`. 

### `mem_map_Gamma_secondBlock`

 The rational points of the second block are the rational points of `U(n)` that fix the
frame `o₁`. 

### `movedFrame_inv_blockEmb_mul`

 The frame attached to `diag(h₁, 1)⁻¹ g` is `g⁻¹ o₁ h₁`. 

### `hasIntegrableTerms_hyperbolicSplitting_of_isRapid`

 The theta integral of a datum `f` for the split space `hyperbolicSpace E n₁` against a rapidly
decreasing function `Y` on `U(n)(𝔸)` converges absolutely term by term (`HasIntegrableTerms`),
because the sum of the norms of the terms grows at most like a power of the height. 

### `exists_theta_homSlice_eq_mul_frameChar`

 Let `f` be the Heisenberg translate of the vacuum along the vector of the isotropic subspace of
`A.homSource V` that has coordinates `α₀ ū` in the adapted basis, where `α₀ = scaleIdele E` and the
components of `u` at `T` and its conjugates are removed. The theta value of the mixed model of `f`
at the frame `α₀ x` is `c · ψ_u(x) · vac[α₀ x]`, with `c ≠ 0` independent of `x`. Here `ψ_u` is
`frameChar T · u` and `vac[α₀ ·]` is `frameWeight`. The complement of `A` is the zero space
`stdSpace E Empty`, and `θ` is the theta function of its `hom V`. 

### `DescentsVanish.integral_frameChar_eq_zero`

 Let `Y` be a continuous function on `[U(n)]` whose descents to the split space
`hyperbolicSpace E n₁` vanish for all data that are vacuum at `T`. Then `ψ_u(x) · vac[α₀ x] · Y(g)`,
with the frame `x = g⁻¹ o₁ h₁` and `o₁ = firstFrame E o`, is integrable over `U(n)(𝔸)` modulo the
rational points of `U(n₂)`, with integral zero. Here `ψ_u(x) = ψ(δ ∑ u_{ij} x_{ij})`
(`frameChar T`), where `δ` generates the inverse different and the terms at `T` and their conjugates
are dropped. Also `vac[α₀ x] = |e(α₀ x)|²` (`frameWeight`), with `e` the vacuum function and
`α₀ = scaleIdele E`. The character of the split space is that of the zero space, `1`, times
`upsilonU1` for each of the `n₁` hyperbolic planes. 

### `DescentsVanish.integral_frameChar_mul_blockPeriod_eq_zero`

 Integrating first over `[U(n₂)]`. Let `Y` be a continuous function on `[U(n)]` whose descents to
`hyperbolicSpace E n₁`, with character `upsilonU1 ^ n₁`, vanish for all data that are vacuum at `T`.
Set `h = diag(h₁, 1)⁻¹ g`, the frame `x = h⁻¹ o₁` with `o₁ = firstFrame E o`, and
`I(h) = ∫ Y(diag(h₁, h₂) h) dh₂` over `[U(n₂)]`. Then `ψ_u(x) · vac[α₀ x] · I(h)` is integrable over
`U(n₂)(𝔸) \ U(n)(𝔸)` with integral zero. Here `ψ_u(x) = ψ(δ ∑ u_{ij} x_{ij})` without the terms at
`T` and their conjugates, and `vac[α₀ x] = |e(α₀ x)|²`, with `e` the vacuum function and
`α₀ = scaleIdele E`. 

### `blockPeriod_eq_of_frameChar_eq`

 Let `Y` be a continuous function on `[U(n)]` that is right invariant under the integral points
supported on `T` and its conjugates. At points with finite part in `stdLevel E n`, the group of
integral points, the period `I(a)` depends only on the values `ψ_u(a⁻¹ o₁)` of the characters. 

### `exists_continuousMap_eq_conj_blockPeriod`

 Split the basis of the definite space of rank `n` by `o : n₁ ⊕ n₂ ≃ n`, and let `o₁` be the
frame of the first `n₁` basis vectors. Let `Y` be a continuous function on `U(n)(𝔸)`. It is left
invariant under the rational points. It is right invariant (`HasLevel`) under the integral points
(`stdLevel`) supported on the places of `T` and their conjugates (`supportedOn`). Fix `h₁` in
`U(n₁)(𝔸)` and let `I(h) = ∫ Y(diag(h₁, h₂) h) dh₂` over `[U(n₂)]` (`blockPeriod`). Then there is a
continuous `χ` on the product of circles indexed by the adelic `n × n₁` frames `u` with
`star I(h) = χ(u ↦ ψ_u(h⁻¹ o₁))` (`frameChar T`). This holds whenever the frame `x = h⁻¹ o₁`
(`movedFrame`) has `frameWeight x = |e(α₀ x)|² ≠ 0`, where `e` is the vacuum function and
`α₀ = scaleIdele E`. Here `ψ_u(x) = ψ(δ ∑ u_{ij} x_{ij})`, with `ψ` the standard additive character,
`δ = invDifferentIdele E`, and the components at the places of `T` and their conjugates set to
zero. 

### `integral_continuousMap_frameChar_eq_zero`

 Stone–Weierstrass: let `x` be a continuous family of frames. Let `ψ_u = frameChar T · u` be
`x ↦ ψ(δ ∑ u_{ij} x_{ij})`, where `ψ` is the standard additive character, `δ` is an idele generating
the inverse different, and the components at the places of `T` and their conjugates are set to zero.
If `ψ_u(x(g)) w(g)` is integrable with integral zero for all `u`, then the same holds with `ψ_u`
replaced by any continuous function `χ` of the values `u ↦ ψ_u(x(g))`. 

### `integral_blockEmb_eq_zero_of_descentsVanish`

 From descents to periods. Let `Y` be a continuous function on `[U(n)]` that is right invariant
(`HasLevel`) under the elements of `stdLevel E n` with component 1 at every place outside `T` and
its conjugate places, and split the basis as `n₁ ⊕ n₂`. Suppose the integrals over `[U(n)]` of `Y`
against the theta kernels of the hyperbolic space of rank `2 n₁`, twisted by `upsilonU1 ^ card n₁`
of the determinant, vanish for all data on `Hom` that are vacua at the places of `T` and their
conjugates. Then `∫ Y(diag(h₁, h₂)) dh₂ = 0` over `[U(n₂)]`, for all `h₁`. 
