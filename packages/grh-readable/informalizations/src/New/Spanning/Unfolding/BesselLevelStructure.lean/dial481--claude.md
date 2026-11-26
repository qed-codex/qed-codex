---
{
  "module": "src/New/Spanning/Unfolding/BesselLevelStructure.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselLevelStructure.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselLevelStructure.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Bessel data: level subgroup, Eichler maps and strong approximation for the unipotent group

The file works with filling data `S : New.Filling E 𝔰` and the unitary group `S.G` of the form
`T.splitGram`, where `T` is the middle Gram matrix, at rational points, finite adeles and
archimedean points. The middle space is X₀ ⊕ E z, with X₀ spanned by the basis vectors indexed by
`κ`. Write 𝖴 for the Bessel unipotent group `New.Shape.Form.besselU`. Write H for
`New.Shape.Form.besselH`, the unitary group U(X₀), acting only on the basis vectors indexed by `κ`.
Write `New.Shape.Form.besselS` for the group they generate. Write σ = `New.simpleRootSum` for the
sum of the entries just above the diagonal on the frame. The level is `S.M = p₀ p₁` with
`pᵢ = S.levelPrime i`, and `S.chosenPlaces i` are the chosen places of norm `pᵢ`. K(M) is
`S.principalLevel`. For a class c, h_c = `S.classRep c` is its representative in H. For classes c,
d, `S.translateByClassReps c d γ` is h_c⁻¹ γ h_d, and `S.termsOver c s d` is the set of rational γ
with `S.translateByClassReps c d γ` integral of reduction s.

## Main definitions and results

* `New.Filling.besselFn_adelicToInf_mul_eq_prod_wave_smul`, `New.Filling.besselFn_ratToInf_mul`: how
  the Bessel function `New.Filling.besselFn` transforms under left translation by `𝖴`.
* `New.exists_mem_besselU_eq_eichlerMap`: for a hermitian invertible form, if x is a combination of
  the frame vectors of index below a and v is orthogonal to these vectors, then the Eichler map
  along x and v, with ς = τ h(v, v), lies in the unipotent group `New.Shape.Form.besselU`; the lemma
  also computes its `New.simpleRootSum`.
* `New.besselU_dense`, `New.Filling.exists_besselU_approx`: strong approximation for 𝖴.
* `New.Filling.mem_reducedImage_besselU_iff_exists_termsOver`,
  `New.Filling.prod_wave_eq_star_unipotentChar`: the rational points of 𝖴 that are integral for a
  class map onto the reduction of the integral points of 𝖴(𝔸_f), and on them the character at
  infinity is the conjugate of the finite character at an integral point with the same reduction.
* `New.Filling.exists_besselS_mem_termsOver`: each reduction `s` of an integral element of
  `New.Shape.Form.besselS` is reached from each class c by a rational element of
  `New.Shape.Form.besselS`.

Notions from other files:
* `New.Shape.Form.splitGram`: The Gram matrix of ϱ hyperbolic planes and a middle space with Gram
  matrix T: identity blocks pair the first and last ϱ indices, T is the middle block, all else is
  zero.
* `New.Filling.selfDualChar`: The additive character x ↦ ψ_f(−x/ϖ) of the finite adeles.
* `New.Filling.IsAdmissible`: The standing hypotheses on the data: among them, `sourceLevel` is the
  preimage of K(M), `reduction` is onto, and some size inequalities hold.
* `S.GFin`: The finite adelic points of the unitary group in the lattice basis.
* `New.Filling.unipotentChar`: The value of the additive character `S.selfDualChar` at M⁻¹ σ(u),
  where σ(u) = `New.simpleRootSum u` sums the entries of u at the simple roots.

## Relation to the literature

See `Lib.DiscreteSeries.Bruhat.FloorGroups` for sources.



## Bessel groups at rational, finite adelic and archimedean points

* `New.Filling.termsOver.mul`, `New.Filling.termsOver.inv`: the sets `New.Filling.termsOver` compose
  like a groupoid.
* `New.Filling.prod_wave_simpleRootSum_adelicToInf`, `New.Filling.prod_wave_simpleRootSum_ratToInf`:
  the character of `𝖴` at infinity in terms of the finite character.


 ### Change of ring and of basis in the Bessel groups 

### `map_splitGram_latticeMiddle`

 A ring homomorphism carries the Gram matrix in the lattice basis over `R` to the one over
`R'`: `S.latticeMiddle R` is the middle block of this matrix and `splitGram` the whole matrix. 

### `_root_.Membership.mem.map_mem_agreeWithOneOn`

 If `γ` agrees with the identity matrix at the entries `(i, j)` with `r i j`, then so does its
image under a ring homomorphism `f`; `agreeWithOneOn` is the group of such invertible matrices. 

### `instance : Floors.IsHermitianUnit (S.ratMiddle E)`

 The rational Gram matrix `S.ratMiddle E` of the middle space is hermitian and invertible. 

### `toLatticeBasis_mem_besselU`

 A finite adelic point lies in the unipotent group `besselU` in rational coordinates iff it does
in the lattice basis; `S.toLatticeBasis` is the change to the lattice basis. 

### `ratToFin_mem_besselU_iff`

 A rational point lies in the unipotent group `besselU` iff its finite adelic image in the
lattice basis does. 

### `inclHFin_mem_besselH`

 The inclusion `S.inclHFin` of the finite adelic points of the unitary group of `X₀` lands in
`besselH`, the isometries that fix the basis vectors outside `κ`. 

### `range_inclHFin`

 The image of `S.inclHFin`, the inclusion of the finite adelic points of the unitary group of
`X₀ = span κ` in the lattice basis, is the group `besselH` of isometries that fix the basis vectors
outside `κ`. 

### `ratToFin_toBesselH`

 The finite image of the rational `toBesselH` of `γ ∈ U(X₀)` is the inclusion `S.inclHFin` of the
finite adelic image of `γ`. 

### `classBasis`

 For a class `c`, let h be the image under `toBesselH` of the chosen element `c.out` of the
double coset `c`, in rational coordinates. This is the finite adelic matrix h · `S.latticeBasis`.
Its columns form a basis of hΛ₀, where Λ₀ is the lattice spanned by the columns of
`S.latticeBasis`. 

### `coe_translateByClassReps`

 The matrix of `S.translateByClassReps c c' γ` is `B_c⁻¹ γ B_c'`, with `B_c = classBasis c`. 

### `classRep_mem_besselS`

 The chosen representative `h_c = S.classRep c` of a class lies in `besselS`, as it lies in
`besselH`. 

### `_root_.Membership.mem.translateByClassReps_mem_besselU`

 If a rational `γ` lies in `besselU`, then so does `h_c⁻¹ γ h_c = S.translateByClassReps c c
γ`. 

### `termsOver.mul`

 The product of a term over `(c, s, c')` and a term over `(c', t, c'')` is a term over
`(c, s * t, c'')`. 

### `termsOver.inv`

 The inverse of a term over `(c, s, c')` is a term over `(c', s⁻¹, c)`. 

 ### The unipotent transformation law 

### `simpleRootSum_adelicToFin`

 Let `u` be an adelic point of the unitary group of the filling data `S`, and let
`σ = simpleRootSum` be the sum of the entries just above the diagonal on the frame e₁, …, e_ϱ, z.
The value of `σ` at `S.adelicToFin u`, the finite part of `u` written in the lattice basis, is the
finite part (the second component) of the adele `σ(u)`. 

### `simpleRootSum_ratToAdelic`

 The sum of the entries just above the diagonal on the frame commutes with the embedding of
`E` in the adeles. 

### `_root_.Membership.mem.ratToInf_mem_agreeWithOneOn`

 If a rational `γ` agrees with the identity matrix at the entries `(i, j)` with `r i j`, then so
does each component of its archimedean image `S.ratToInf γ`. 

### `simpleRootSum_adelicToInf`

 For adelic `x` and an infinite place `v`, `simpleRootSum (S.adelicToInf x v)` is the sum of the
entries just above the diagonal of the block on `(e_0, …, e_{ϱ-1}, z)` of the rescaled `v`-component
of `x`. It equals `-2πi` times the `v`-component of `-simpleRootSum x / (M ϖ)`. Here `M = S.M` is
the level and `ϖ = S.deltaE` generates the different of `E`. 

### `prod_wave_simpleRootSum_adelicToInf`

 Let `σ = New.simpleRootSum` be the sum of the entries just above the diagonal on the frame e₁,
…, e_ϱ, z, let `x` be an adelic point, and let `c_v = σ (S.adelicToInf x v)` be the value of `σ` at
the component of `x` at `v`, written in the basis rescaled by `S.basisScale v`. Let `ψ` be the
standard character of the adeles and `ψ_f` its finite part, `M = S.M` the level, the product of the
two primes `S.levelPrime i`, and `ϖ = S.deltaE` the generator of the different of `E`. The product
of the numbers `wave c_v = exp (c_v - c̄_v)` over the infinite places is `ψ(-σ(x) / (M ϖ))` divided
by `S.unipotentChar x_f = ψ_f(-σ(x_f) / (M ϖ))`, where `x_f = S.adelicToFin x` is the finite part of
`x`; that is, it is the archimedean factor of `ψ(-σ(x) / (M ϖ))`. 

### `prod_wave_simpleRootSum_ratToInf`

 For a rational point `γ`, take the product of `wave (simpleRootSum (S.ratToInf γ v))` over the
infinite places `v`; this is the character of `besselU` at infinity. It equals the complex conjugate
of the finite character `S.unipotentChar` at `S.ratToFin γ`, the finite adelic image of `γ`. 

### `besselFn_adelicToInf_mul_eq_prod_wave_smul`

 Let `x` be an adelic point in the unipotent group `besselU`. Left translation by
`S.adelicToInf x`, the rescaled infinite components of `x`, multiplies the Bessel function
`S.besselFn side` (full or cut) by a scalar. This scalar is the character of `besselU` at infinity:
the product of `wave (simpleRootSum (S.adelicToInf x v))` over the infinite places `v`. 

### `besselFn_ratToInf_mul`

 For rational `γ` in the unipotent group, left translation by the archimedean image of `γ`
multiplies the Bessel function `S.besselFn side` by the inverse of the finite character
`New.Filling.unipotentChar` of the finite image of `γ`. 


## Unimodularity of the lattice form and Eichler maps in 𝖴

Matrix computations for the form `T.splitGram` of `ϱ` hyperbolic planes and a middle space with Gram
matrix `T`, over a commutative ring with involution.

The basis is `e₁, …, e_ϱ`, a basis of the middle space ending in `z`, and `e*₁, …, e*_ϱ`. The frame
is `f = (e₁, …, e_ϱ, z)`, and `h(x, y)` is `xᴴ J y`.


### `finHeadWeight`

 The weight of a head `p 0, …, p (i - 1)` at the finite places: the product over `l < i` of the
`K`-th power of `√(genIndex D)`, where `D = p 0 * ⋯ * p l` and `genIndex D` is the inverse of the
factor by which multiplication by `D` scales Haar measure. It is `0` unless all these partial
products lie in the ring of integers `SemilocalField.O`. 

### `isUnimodular_latticeMiddleGram`

 Let `R` be a subring of `A` and let `N ∈ R` be fixed by the involution. Then
`latticeMiddleGram 𝔰 N`, the Gram matrix of the middle space `X₀ ⊕ A z` in the lattice basis, is
hermitian and lies in `GL(R)`. 

### `frameImage_one_mulVec`

 The combination of the frame vectors e₁, …, e_ϱ, z with coefficients `x` has `e`-coordinates
`init x`, `z`-coordinate the last coefficient, and all other coordinates zero. 

### `frameImage_mulVec`

 The combination of the columns of `γ` at the frame indices with coefficients `x` is the image
under `γ` of the same combination of the frame vectors. 

### `exists_star_vecMul_eq`

 For an invertible hermitian matrix `J`, every row vector is `vᴴ J` for some `v`. 

### `exists_mem_besselU_eq_eichlerMap`

 Let `J = T.splitGram` be hermitian and invertible, and `h(y, y') = yᴴ J y'`, conjugate-linear in
`y`. Let `f j = frameImage 1 *ᵥ j` be the combination of the frame vectors e₁, …, e_ϱ, z with
coefficients `j`, and put `x = r • f j`. Suppose `j b = 0` for `b ≥ a`, and that `v` is orthogonal
to the frame vectors of index below `a`. Let `τ = TraceOne.element` be the chosen element with
`τ + τ̄ = 1`, and `ς = τ h(v, v)`. Then the Eichler map `eichlerMap J x v ς : y ↦ y + h(v, y) x -
h(x, y) (v + ς x)` is an element `u` of the unipotent group `besselU`. Its `simpleRootSum`, the sum
of the entries just above the diagonal on the frame, is `r h(v, f j')`, where `j' = cons 0 (init j)`
is `j` shifted by one place. 


## The idele M, the self-dual character and the level subgroup K(M)

The global data `S` are translated into the terms of the abstract local theory over the pair
`Ô E ⊆ 𝔸f E` of integral and all finite adeles.


### `isUnimodular_latticeMiddle`

 The middle block `S.latticeMiddle F` of the form in the lattice basis, over a ring `F` with
involution, is hermitian and lies in `GL(R)` for every subring `R` of `F`. 

### `transpose_splitGram`

 The Gram matrix of the whole form in the lattice basis is symmetric. 

### `invAdjoint`

 The inverse adjoint s ↦ J⁻¹s⁻ᵀJ, an automorphism of the general linear group over F; J is the
Gram matrix in the lattice basis. 

### `idOrInvAdjoint`

 The automorphism s ↦ J⁻¹s⁻ᵀJ of the general linear group over F if b is true, else the
identity; J is the Gram matrix in the lattice basis. 

### `reduceAboveM`

 For a chosen place w, of norm p₀ or p₁, and a Boolean, the ring homomorphism from the integral
finite adeles to the residue field at w: reduction modulo w, preceded by conjugation if the Boolean
is true. 

### `exists_map_eq_of_mem_latticeStabilizer`

 Every element of `S.latticeStabilizer`, the group of integral finite adelic isometries, is the
image of a unitary matrix over the ring `Ô E` of integral finite adeles. 

### `intGL_map_reduceAboveM`

 Let `k` be an integral finite adelic isometry, `i : Fin 2`, `w` a place in `S.chosenPlaces i`
and `b` a Boolean. The image of `k` under `S.reduceAboveM (⟨i, w⟩, b)`, applied entrywise by
`intGL.map`, is `S.idOrInvAdjoint b` applied to the reduction `S.reduction k i w` of `k` at `w`. 

### `forall_selfDualChar_mul_eq_one_iff`

 The ring `Ô E` of integral finite adeles is self-dual for the character
`S.selfDualChar : x ↦ ψ_f(-x / ϖ)`, where `ψ_f` is the finite part of the standard additive
character and `ϖ` is the chosen generator of the different of `E`: the character is trivial on
`Ô E * a` iff `a` is integral. 

### `inv_ideleM_smul_mem_iff`

 For an integral finite adele `r` and the level `M`, seen as the idele `S.ideleM`, the adele
`M⁻¹ r` is integral iff `r` and its conjugate reduce to `0` at every chosen place; these reductions
are the maps `S.reduceAboveM x`. 

### `reduction_eq_one_iff`

 An integral finite adelic isometry `k` reduces to `1` at all chosen places iff `k` is congruent
to `1` modulo the level `M = S.ideleM`, that is, `M⁻¹ (k - 1)` has integral entries. 

### `principalLevel_eq_unitaryLevel`

 The image `S.principalLevel` of the kernel of the reduction at the chosen places equals
`unitaryLevel`: the isometries of the Gram matrix `(S.latticeMiddle (𝔸f E)).splitGram` that are
integral over `Ô E` and congruent to `1` modulo the level `M = S.ideleM`. 


## Strong approximation for 𝖴, rational terms of given reduction, and freeness

* `New.Filling.unipotentChar_eq_of_mem_principalLevel`,
  `New.Filling.exists_rat_approx_unipotentChar_eq`: approximation keeps the character
  `S.unipotentChar`.


### `noncomputable instance : TraceOne (𝔸f E)`

 The element `1 / 2` of the finite adeles has trace one. 

### `New.continuous_heisenbergElem_finAdele`

 The Heisenberg element `heisenbergElem a p` of floor `a` over the finite adeles is a continuous
function of its parameter `p`, a pair of a vector and a skew element. 

### `New.denseRange_skewPart_algebraMap`

 The skew elements `t - t̄` with `t ∈ E` are dense in the skew finite adeles. 

### `New.map_heisenbergElem_finAdele`

 Let `T` be an invertible hermitian middle block over `E`, and `T'` one over the finite adeles
`𝔸f E` whose Gram matrix `T'.splitGram` is the image of `T.splitGram` (`hT`). Take `a < 𝔰.ϱ`, the
index of a hyperbolic pair (e_a, e*_a). Let `v` be a vector on the basis indices `i` with
`floorOf i ≥ a + 1`. Let `β` be skew. Then `heisenbergElem a (v, β)` is the Eichler map with
e*_a ↦ e*_a + v + (β - h(v, v) / 2) e_a. The map from rational to finite adelic isometries sends the
element for `T` with parameter `(v, skewPart t)`, where `skewPart t = t - t̄`, to the element for
`T'` whose parameter is the image of `(v, t - t̄)` in `𝔸f E`. 

### `New.besselU_dense`

 Strong approximation for the unipotent group 𝖴 = `besselU` of the form made of ϱ hyperbolic
planes and a middle block. Let `T` be an invertible hermitian middle block over `E`, and `T'` one
over the finite adeles whose Gram matrix is the image of that of `T`. Then 𝖴(𝔸_f) lies in the
closure of the image of 𝖴(E). 

### `exists_besselU_approx`

 Strong approximation for the unipotent group 𝖴 = `besselU` of block upper unitriangular
isometries. `K(M) = S.principalLevel` is the group of integral points of `S.GFin` that are congruent
to `1` modulo `M`. For `x ∈ 𝖴(𝔸_f)` and any `y` in `S.GFin`, some rational `u ∈ 𝖴` has `y⁻¹ x⁻¹ u y`
in `K(M)`. 

### `unipotentChar_eq_of_mem_principalLevel`

 Let `u`, `v` lie in the unipotent group `besselU` inside the finite adelic unitary group
`S.GFin`. Let `g` be a finite adelic point of U(X₀), the unitary group `U 1` of the identity form on
`𝔰.κ`, and let `h = S.inclHFin g` be its image in `S.GFin`, an element of `New.Shape.Form.besselH`.
If `u⁻¹ h⁻¹ v h` lies in the principal congruence subgroup `S.principalLevel`, then the complex
character `S.unipotentChar` has the same value at `u` and `v`. 

### `mem_termsOver_reduction_iff`

 Let `k` be an integral finite adelic isometry, `γ` a rational one, and `c`, `d` classes with
representatives `h_c`, `h_d`. Then `h_c⁻¹ γ h_d = S.translateByClassReps c d γ` is integral with the
same reduction as `k` iff it lies in `k K(M)`, with `K(M) = S.principalLevel`. 

### `prod_wave_eq_star_unipotentChar`

 Let `γ` be a rational point of `𝖴 = besselU` with `h_c⁻¹ γ h_c` integral, where `h_c` represents
the class `c`, and let `k` be an integral point of `𝖴(𝔸_f)` with the same reduction at the chosen
places as `h_c⁻¹ γ h_c`. Let `σ = simpleRootSum` be the sum of the entries just above the diagonal
on the frame e₁, …, e_ϱ, z, and `γ_v = S.ratToInf γ v` the image of `γ` at the infinite place `v`,
in the rescaled basis. With `wave x = exp (x - x̄)`, the product of the numbers `wave (σ γ_v)` over
all `v` is the complex conjugate of `S.unipotentChar k = ψ_f(-σ(k) / (M ϖ))`. Here `ψ_f` is the
standard character of the finite adeles, `M = S.M` is the level and `ϖ` generates the different. 

### `eq_and_mem_classUnipotent_of_besselS`

 Let `c`, `d` be classes, that is, double cosets in U(X₀)(E⁺) \ U(X₀)(𝔸_f) / `S.sourceLevel`,
with chosen representatives `h_c = S.classRep c` and `h_d`. Let `S` satisfy the standing hypotheses
`S.IsAdmissible`; they include that `S.sourceLevel` is the preimage in U(X₀)(𝔸_f) of the principal
congruence subgroup `K(M) = S.principalLevel`. Let `γ` be a rational element of the Bessel subgroup
`besselS`. If `S.translateByClassReps c d γ = h_c⁻¹ γ h_d` lies in `K(M)`, then `c = d` and `γ` lies
in `S.classUnipotent c`, the group of rational unipotent `u` with `h_c⁻¹ u h_c ∈ K(M)`. 

### `exists_rat_approx_unipotentChar_eq`

 Let `S` be admissible (`S.IsAdmissible`), `c` a class in `S.Classes` with representative `h_c`,
and `u` in `𝖴(𝔸_f)`. There is a rational `u₀ ∈ 𝖴` such that
`S.translateByClassReps c c u₀ = h_c⁻¹ u₀ h_c` lies in `u K(M)`, with `K(M) = S.principalLevel`.
Moreover `S.unipotentChar`, the character u ↦ ψ_f(−σ(u)/(Mϖ)), takes the same value at
`S.ratToFin u₀` and at `u`. 

### `mem_reducedImage_besselU_iff_exists_termsOver`

 Let `S` be admissible. For each class `c` with representative `h_c`, the rational points `γ` of
`𝖴 = besselU` with `h_c⁻¹ γ h_c` integral map onto `S.reducedImage besselU`, the reduction of the
integral points of `𝖴(𝔸_f)`: an element `s` lies in this group if and only if it is the reduction of
some `h_c⁻¹ γ h_c`. 

### `exists_besselS_mem_termsOver`

 Let `S` satisfy the standing hypotheses `S.IsAdmissible`. They include that `S.sourceLevel` is
the preimage in U(X₀)(𝔸_f) of `S.principalLevel`, the kernel of reduction at the chosen places. Let
`s` in `S.ResidueGL`, the product of the general linear groups over the residue fields at these
places, be the reduction of an integral finite adelic element of the Bessel subgroup `besselS`. For
each class `c`, a double coset in U(X₀)(E⁺) \ U(X₀)(𝔸_f) / `S.sourceLevel`, there are a class `d`
and a rational `γ ∈ besselS` with `γ ∈ S.termsOver c s d`. 

### `eq_one_of_reduceAt_eq_one`

 Freeness in rank at most `𝔰.k`, the rank of the definite space X₀. Let `E` be a CM field that
contains a primitive 5040th root of unity, and let the filling data `S` over `E` satisfy the
standing hypotheses `S.IsAdmissible`. For `i = 0, 1`, `S.chosenPlaces i` is the chosen set of finite
places of `E` of norm the prime `S.levelPrime i`. Let `γ` be a rational point of the standard
unitary group in `n` variables, `|n| ≤ 𝔰.k`, and `g` a finite adelic point. If `g⁻¹ γ g` is integral
(lies in `stdLevel E n`) and reduces to `1` at every place of `S.chosenPlaces i`, then `γ = 1`. 
