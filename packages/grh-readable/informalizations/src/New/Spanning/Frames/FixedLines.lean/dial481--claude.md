---
{
  "module": "src/New/Spanning/Frames/FixedLines.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/FixedLines.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/FixedLines.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Groups that fix given vectors at chosen places have a small mass integral

Let `S` be an admissible filling with base `b = S.b`, and `T` a finite set of finite places of `E`
stable under conjugation. The product `LocProd T` of the completions at `T` is read as one ring,
with integers `R` (`New.Floors.IntegralPlace`), and `F` is a filling datum on it, of modulus
`g = F.levelUnit`. An `F.IntermediateGroup` is a group `Z` with `K(g) ≤ Z ≤ K`, for the integral
unitary group `K` and its congruence subgroup `K(g)` (both `New.unitaryLevel`). `F.groupMeasure` is
a Haar measure on the unitary group, and `F.massIntegral Z` is the mass integral, the number ∫ |∫_Z
χ_g(y x y⁻¹) dy|² dx, where χ_g is `New.Floors.IntegralPlace.extendedBesselChar g`.

* `New.Filling.volume_integers_diff_intUnits_le`: at the chosen places and their conjugates
  (`New.Filling.chosenPlacesAndConj`), few integers are not units.
* `New.Filling.IsFillingData.exists_intermediateGroup_one_place`: for one place `w`, some group `Z`
  contains the elements that fix the given vectors, and `F.massIntegral Z / F.groupMeasure Z` is
  smaller than `F.massIntegral K / F.groupMeasure K` by at least the factor `b ^ (6 * 𝔰.k)` (for no
  place, the factor is `1`). Here `𝔰.k` is the rank of the block `X₀` of the shape `𝔰`. The proof
  takes the stabiliser of the vector at `w`, which has large index in `K`.
* `New.Filling.IsFillingData.exists_intermediateGroup_places`: for several places, take the product;
  the factors multiply. The places of `T` are cut into the fibres `New.Filling.placeFiber` of a map
  `blk`; `New.Filling.evalFiber` and `New.Filling.toFibers` restrict elements of `LocProd T` and
  unitary matrices to the fibres.

Notions from other files:
* `New.Filling`: `S.levelPrime 0` and `S.levelPrime 1` are the level primes `p₀` and `p₁`,
  `S.chosenPlaces i` is the finite set of chosen places of norm `pᵢ`, and `S.ideleM` is the level
  `M = p₀ p₁` as a finite idele.
* `New.Filling.IsFillingData`: `F` is a large lattice datum on `LocProd T` whose modulus is the
  component of `M` at `T` and whose character is `S.charOnPlaces T`.
* `New.Filling.latticeStabilizer`: the integral elements of the finite adelic unitary group;
  `S.reduction` reduces them modulo the chosen places, `S.toPlaces T` takes components at `T`.
* `New.Filling.vectorFixer`: for a chosen place `w` and `d = (ε, v)`, the elements of `S.ResidueGL`
  (the product of the general linear groups over the residue fields) that fix the vector of the span
  of the frame with coordinates `v ≠ 0`, modulo `w` if `ε` is false and modulo its conjugate if `ε`
  is true; `S.fixer Sg d` is the intersection of these groups over `w ∈ Sg`.

## Relation to the literature

See `New.Spanning.MainTerm.EnergyEstimate` for related work.


 ### Few integers are not units 

### `chosenPlacesAndConj`

 The chosen places of the filling `S`, above both level primes, and their conjugates. 

### `b_pow_ten_le_q`

 Let `S` be a filling over `E` (the data of the filling theorem), whose chosen places
`S.chosenPlaces` lie above its two level primes. Suppose every place of `T` is a chosen place of `S`
or the conjugate of one. Then for each `w ∈ T` the residue field order `w.q` is at least
`S.b ^ 10`. 

### `card_le_b_of_subset_chosenPlacesAndConj`

 If every place of `T` is a chosen place of the filling `S` or the conjugate of one, then `T` has
at most `S.b` elements. 

### `volume_integers_diff_intUnits_le`

 Let `S` be an admissible filling with base `b = S.b`, let every place of `T` be a chosen place
of `S` or the conjugate of one, and let `P.integers` be the ring of integers of the product
`LocProd T` of the completions at `T`, with units `P.intUnits`. Then (a) `2 ≤ b ^ 9`, and (b) the
integers that are not units have volume at most `(b ^ 9)⁻¹`. 

 ### One place 

### `add_inv_pow_mul_mul_pow_le`

 If `2 ≤ B` and `B ^ (t + 1) * z ≤ k` in `ℝ≥0∞`, then `(z + B⁻¹ ^ (t + 1) * k) * B ^ t ≤ k`. 

### `range_toPlaces_latticeStabilizer`

 Let `S` be a filling of shape `𝔰` over `E` (the data of the filling theorem, with `𝔰.ϱ`
hyperbolic planes, a definite space X₀ and a vector z). Let `T` be a finite set of places stable
under conjugation, and `P.integers` the ring of integers of the product `LocProd T` of the
completions at `T`. The form `(S.latticeMiddle A).splitGram` over a ring `A` consists of `𝔰.ϱ`
hyperbolic planes and the Gram matrix `S.latticeMiddle A` of X₀ ⊕ Ez in the lattice basis. Taking
components at `T` (`S.toPlaces T`) maps the integral elements `S.latticeStabilizer` of the finite
adelic unitary group of `S` onto `unitaryLevel P.integers 1`. 

### `v_ideleM_lt_one`

 The level `M = S.ideleM`, the product of the two level primes as a finite idele, lies in the
maximal ideal at every chosen place `w`. 

### `reduceAt_eq_zero_of_inv_ideleM_smul`

 Let `w` be a chosen place and `r` an integral finite adele. If `M⁻¹ r` is integral at `w`, for
the level `M = S.ideleM`, then `r` vanishes modulo `w`. 

### `mem_of_inv_ideleM_mem_integralOff`

 If the inverse of the level `M = S.ideleM` is integral at all places outside `T₀`, then `T₀`
contains every chosen place. 

### `IsFillingData.reduction_eq_one`

 Let `F` be a filling datum at `T`: a large lattice datum on the product of the completions at
`T` whose modulus `g` is the component of the level `S.ideleM = p₀ p₁`. Let `w ∈ T` be a chosen
place. An integral element `k` of the adelic unitary group whose component at `T` lies in the
congruence subgroup `K(g) = F.congruenceSubgroup` has reduction `S.reduction k i w = 1` modulo
`w`. 

### `index_comap_vectorFixer`

 Let `S` be an admissible filling, `w` a chosen place above the level prime
`p = S.levelPrime i`, and `d` a nonzero vector modulo `w` or its conjugate. The integral elements
whose reduction fixes `d` (lies in `S.vectorFixer w d`) have index `p ^ r - 1` in the integral group
`S.latticeStabilizer`, where `r = 𝔰.r` is the size of the matrices. 

### `exists_exponent_le_k`

 Let `𝔰` be the shape of a filling, with the numbers `k = 𝔰.k`, `n = 𝔰.n` and the matrix size
`r = 𝔰.r`. Some `t` has `t + 1 + n + 2 · 10⁹ n⁴ ≤ k`, `6 k ≤ 9 t` and `t + 1 < r`. 

### `IsFillingData.massIntegral_mul_le_of_relIndex_eq`

 Let `S` be an admissible filling with base `b = S.b`, and `F` a filling datum at `T`, where
every place of `T` is a chosen place or the conjugate of one. Let `K = unitaryLevel P.integers 1 _`
be the integral unitary group over the completions at `T` and `K(g) = F.congruenceSubgroup` its
subgroup of elements congruent to `1` modulo `g`. Let `Z` with `K(g) ≤ Z ≤ K` have index
`p₀ ^ r - 1` in `K`, for the first level prime `p₀` and the size `r = 𝔰.r` of the matrices. Then
`ϰ(Z) vol(K) b ^ (6 k) ≤ ϰ(K) vol(Z)`. Here `vol = F.groupMeasure` is a Haar measure,
`ϰ(Z) = F.massIntegral Z` is ∫ |∫_Z χ_g(y x y⁻¹) dy|² dx for the function
χ_g = `extendedBesselChar g`, and `k = 𝔰.k` is the rank of the block `X₀` of the shape `𝔰`. 

### `IsFillingData.exists_intermediateGroup_one_place`

 Let `S` be an admissible filling and `F` a filling datum at `T`, of modulus `g`. Let `Sg` be a
set of chosen places above the first level prime, `d w` a nonzero vector modulo `w` or its
conjugate, and let the inverse of the level `S.ideleM` be integral off `T₀`. Let `o` be `none`, or a
place `w` of `Sg` such that `T` consists of the places of `T₀` equal to `w` or `w̄`. Then some group
`Z` with `K(g) ≤ Z ≤ K`, for the integral unitary group `K = unitaryLevel P.integers 1 _` and its
congruence subgroup `K(g) = F.congruenceSubgroup`, has two properties. (a) `Z` contains the
`T`-component of every integral element whose reduction fixes `d w` for all `w ∈ Sg`. (b) With the
mass integral `ϰ = F.massIntegral` and `vol = F.groupMeasure`, `ϰ(Z) vol(K) B ≤ ϰ(K) vol(Z)`, where
`B` is `S.b ^ (6 * 𝔰.k)` if `o` is a place, and `1` otherwise. 

 ### Restriction to the fibres of a map on places 

### `placeFiber`

 The places of `T` that the map `blk` sends to `i`. 

### `evalFiber`

 The projection from the product of the completions at `T` to the product of the completions at
the places of `T` that `blk` sends to `i`. 

### `evalFiber_apply`

 The projection to a fibre of `blk` keeps the component at each place `w` of the fibre. 

### `forall_placeFiber`

 A property holds at all places of `T` if and only if it holds on each fibre
`placeFiber T blk i` of the map `blk`. 

### `eq_iff_evalFiber_eq`

 Two elements of the product of the completions at `T` are equal if and only if their
projections to each fibre of `blk` are equal. 

### `mem_O_iff_evalFiber_mem`

 An element of the product of the completions at `T` is integral if and only if its projection
to each fibre of `blk` is integral. 

### `charOnPlaces_eq_prod_fibers`

 When `T` is cut into the fibres of a map `blk`, the additive character `S.charOnPlaces T` of the
product of the completions at `T`, which is the character of the finite adeles of `S` after
extension by zero, is the product of the characters of the fibres. 

### `toFibers`

 The map from the unitary group over the completions at `T` to the product of the unitary groups
over the fibres of `blk`, given by the projections `evalFiber T blk i` on matrix entries. 

### `toFibers_apply`

 For a unitary matrix `x` over the completions at `T`, the entries of its component
`S.toFibers T blk x i` at the fibre of `blk` over `i` are the projections of the entries of `x`. 

### `toFibers_toPlaces`

 For an adelic unitary matrix `x`, restricting its components at `T` to a fibre of `blk` gives
the components of `x` at that fibre. 

### `toFibers_surjective`

 Unitary matrices over the fibres of `blk` glue to a unitary matrix over `T`, that is, the map
`S.toFibers T blk` to the product of the unitary groups over the fibres is onto. 

### `mem_unitaryLevel_iff_toFibers`

 A unitary matrix over the completions at `T` is integral with integral inverse and congruent to
`1` modulo `u`, that is, lies in `unitaryLevel SemilocalField.O u`, if and only if its components
at all fibres of `blk` satisfy the same for the projections of `u`. 

### `unitaryLevel_eq_comap_toFibers`

 The group `unitaryLevel SemilocalField.O u` for the Gram matrix `splitGram` over the completions
at `T` is the preimage under `S.toFibers T blk` of the product, over all `i`, of the same groups
over the fibres of `blk`. For each `i`, the modulus there is `u` projected by
`evalFiber T blk i`. 

### `mem_besselU_iff_toFibers`

 A unitary matrix over the completions at `T` lies in `besselU`, the group of unitary matrices
that are unitriangular for the levels of the indices, if and only if this holds on each fibre of
`blk`. 

### `measurableEmbedding_toFibers`

 The map `S.toFibers T blk` from the unitary group over the completions at `T` to the product of
the unitary groups over the fibres of `blk` is a measurable embedding. 

### `extendedBesselChar_eq_prod_toFibers`

 Let `blk` send the places to indices in a finite type `ι`, and let the additive characters of
the integral places `P` at `T` and `P' i` at the fibres of `blk` be those of `S`. The function
`extendedBesselChar a` is the product of the same functions of the fibres. 

### `IsFillingData.levelUnit_eq_map_evalFiber`

 Let `F` be a filling datum at `T` and `F' i` a filling datum at each fibre of a map `blk` on
places. Then the modulus `(F' i).levelUnit` is the projection of the modulus `F.levelUnit` to the
fibre. 

### `IsFillingData.exists_massIntegral_pi_eq`

 Let `F` be a filling datum at `T` and `F' i` a filling datum at each fibre `placeFiber T blk i`
of a map `blk` from the places to a finite type `ι`. Then there is a constant `t` with the following
property. For all subgroups `Y i` of the unitary groups over the fibres, let `Z` be their product,
read in the group over `T` through `S.toFibers`. Then the volume `F.groupMeasure Z` is `t` times the
product of the volumes `(F' i).groupMeasure (Y i)`. The mass integral, `F.massIntegral Z` = ∫
|∫_Z χ_g(y x y⁻¹) dy|² dx, is `‖t.toReal‖ₑ ^ 2 * t` times the product of the mass integrals of the
`Y i`.

This factor is `t ^ 3` for finite `t`. 

### `IsFillingData.massIntegral_pi_mul_le`

 Let `F` be a filling datum at `T` and `F' i` a filling datum at each fibre of a map `blk` from
the places to a finite type, and let `ϰ` be the mass integral and `vol` the Haar volume. If on each
fibre `ϰ(Y i) vol(W i) c i ≤ ϰ(W i) vol(Y i)`, then the products of the groups, read in the group
over `T` through `S.toFibers`, satisfy `ϰ(∏ Y i) vol(∏ W i) (∏ c i) ≤ ϰ(∏ W i) vol(∏ Y i)`. 

 ### Several places 

### `exists_option_eq_some_iff`

 Let `Sg` be a set of chosen places of the filling `S` above the first level prime. A place `w`
lies in the pair `{s, star s}` for at most one `s` of `Sg`; the index `o` is this `s`, or `none` if
there is none. 

### `IsFillingData.exists_intermediateGroup_places`

 Let `S` be an admissible filling, `F` a filling datum at `T`, and let the inverse of the level
`S.ideleM` be integral off `T`. Let `Sg` be a set of chosen places above the first level prime
(index `0`) and let `d w = (ε, v)` prescribe, for each such place `w`, the frame vector with nonzero
coordinates `v` modulo `w` if `ε` is false and modulo its conjugate if `ε` is true; `S.fixer Sg d`
is the group that fixes these vectors for all `w` in `Sg`. Then some group `Z` between the
congruence subgroup `F.congruenceSubgroup` and the integral unitary group
`K = unitaryLevel P.integers 1 _` has two properties. (a) `Z` contains the `T`-component of every
integral element `k` whose reduction modulo the chosen places lies in `S.fixer Sg d`. (b) With
`ϰ = F.massIntegral` (the mass integral), `vol = F.groupMeasure` (a Haar measure) and `b = S.b`,
`ϰ(Z) vol(K) (b ^ (6 * 𝔰.k)) ^ #Sg ≤ ϰ(K) vol(Z)`. 
