---
{
  "module": "src/Lib/GaloisRep/Main/SeedRepresentation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Main/SeedRepresentation.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Main/SeedRepresentation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Seed representations: odd rank, a cuspidal type and free jumps

The Galois representation of a form `f` of odd rank on the definite unitary group, under two extra
local hypotheses: a cuspidal type at a split place and free jumps.

* `New.GaloisRep.exists_rep_of_cuspidal_type`: under these hypotheses, there is a continuous
  representation with the characteristic polynomials of Frobenius given by the Hecke polynomials of
  `f`, spherical at a further split place outside the ramification.

The proof transfers `f` to a form on the definite frames on which the centre acts by a character
(`New.GaloisRep.exists_central_eigenform`), realizes its Hecke eigenvalues in the cohomology of a
PEL model for each complex embedding of `E`, and joins the representations so obtained into one of
rank `a` (`New.GaloisRep.exists_galRep_charpoly_eq_of_forall_embedding`).

Notions from other files:
* `New.jumps κ N σ`: the multiset {j − 1 − λ_j} if σ is in the CM type, else {λ_j + N − j},
  1 ≤ j ≤ N, with λ the highest weight of κ at the place v of σ: λ_j = `κ.2 v` + Σ_{j ≤ h < N}
  `κ.1 v h`.
* `New.Variety.definiteForms 𝔑 ξ`: the functions `φ` on `GL n (𝔸f E)` with `φ (y x) = ξ y (φ x)` for
  rational `y`, zero off the definite frames, and right invariant under the level `levelGU n 𝔑`.
* `New.Variety.IsSafe 𝔑 w`: the place of `QuadField d` below `w` satisfies `IsSplitPrimeToDisc`, and
  `𝔑` lies neither in `w` nor in any place above the conjugate of that place.
* `New.GaloisRep.IsSphericalAbove r R J w P`: at every place above `w`, `r` is unramified or
  crystalline, its jumps are related to the multisets `J` by `R` (`OccursIn`: each member of `J` is
  among its jumps; `Eq`: they are exactly its jumps), and `P` kills its geometric Frobenius
  elements.
* `New.HasNoSmallRelations e`: two families of natural numbers with the same sum, at most
  `(n + 1) ^ 2`, and the same sum weighted by the `e i`, are equal.

## Relation to the literature

Known; see `Lib.GaloisRep.Main.OddRank` for sources.


### `New.GaloisRep.invTransposeGL_ofSplitPlace_eq_conjAtSplit`

 `conjAtSplit w g` is the inverse transpose of the unitary element `ofSplitPlace w g`. 

### `New.GaloisRep.exists_forall_mk_eq_mk_mul_conjAtSplit`

 Moving a coset representative at a split place. Let the cosets modulo the level `levelGU n 𝔑`
of `toFinGL y₀ * invTransposeGL u₀` and of `x` agree, and let `𝔑 ∉ star w` for the split place `w`.
Then for some `c` at `w` and all `y : GL n E` and `g` at `w`, the cosets of
`toFinGL (y * y₀) * invTransposeGL (u₀ * ofSplitPlace w (c * g))` and of
`toFinGL y * (x * conjAtSplit w g)` agree. 

### `New.GaloisRep.exists_frame_extension`

 Extension of a function `f` on `Gf E n`, on which rational unitary matrices act through `ξ`
(`h_rat`) and which is invariant at level `𝔑` (`h_level`), to a function `φ` on `GL n (𝔸f E)`. `φ`
agrees with `f` on `Gf E n` embedded by `invTransposeGL`, is right invariant under `levelGU n 𝔑`,
and vanishes off the definite frames (`IsSignedFrame x 1`: frames of totally positive definite
rational forms). At each split place `w` with `𝔑 ∉ star w` and each `x`,
`φ (y * x * conjAtSplit w g)` is `ξ y` of one linear map `L` applied to the translate of `f` by
`ofSplitPlace w g`. 

### `New.GaloisRep.exists_central_eigenform`

 Let `f ≠ 0` on `Gf E n` take values in a finite-dimensional `W`, let rational unitary matrices
act on `f` through `ξ`, let `f` be invariant at the neat level `𝔑`, and let some split place `w₀`
have `𝔑 ∉ star w₀`. Then some nonzero `ψ` in `definiteForms 𝔑 ξ` exists. This means `ψ` is left
`ξ`-equivariant under `GL n E`, zero off the definite frames, and right `levelGU n 𝔑`-invariant. It
has a central character `ω` (the finite ideles of `QuadField d` act through `centralScalar` by `ω`),
and at each split `w` with `𝔑 ∉ star w`, its translates are the images of those of `f` under one
linear map `L`. 

### `New.GaloisRep.isSplitPrimeToDisc_below_of_prime_norm`

 A place `w` of `E` whose residue field has prime order and which does not contain `d` lies above
a place of `QuadField d` with `IsSplitPrimeToDisc`: that place contains `betaK d - b` for an integer
`b`, and this element is coprime to its conjugate. 

### `New.GaloisRep.card_eq_and_eventually_charpoly_eq_of_hasNoSmallRelations`

 Rank and characteristic polynomials from a Hodge–Tate frame: if the image of `r` spans the
diagonal matrices, `P w`, monic of degree `a`, kills `r` along `mostFrobenii E`, and `r` is
good at the place of `ε` with the free jumps `e i` of `κ` among its jumps, then `r` has rank `a` and
characteristic polynomials `P w` along `mostFrobenii E`: near `1` the cocharacter of the frame lies
in the Zariski closure of the image of `r`, and `card_eq_and_charpoly_eq` applies. 

### `New.GaloisRep.exists_galRep_charpoly_eq_of_forall_embedding`

 One representation from one for each embedding. Let `P w` be monic of degree `a` along the
filter `mostFrobenii E` (each nonempty open set of the Galois group has a nonempty open part whose
Frobenii have the property at almost all places).
Let the `a` jumps of `κ` at `ε` be free integers `e i` (`HasNoSmallRelations`), with
the place of `ε` in `F`. Suppose that for each embedding `τ₀` some continuous `ρ`, eventually along
those places and `F`, satisfies `IsSphericalAbove` with `OccursIn`: it is good above `w`, the jumps
of `κ` at `τ₀` occur in `ρ`, and `P w` kills its geometric Frobenii. Then one continuous `r` of rank
`a` has characteristic polynomial `P w` along `mostFrobenii E` and, eventually along `F`, exactly
the jumps of `κ`. 

### `New.GaloisRep.disjoint_iInf_primeCompl_iff`

 The submonoid of the integers of `E` that lie in no place `u` with `G u` is disjoint from the
place `w` exactly when `G w` holds. 

### `New.GaloisRep.centralChar_mem_algHeckeChars_and_charUnramifiedAt`

 Let `ψ ≠ 0` lie in `definiteForms 𝔑 ξ`, with `𝔑 ≠ 0`, and let the ideles `x` of `QuadField d`
act on `ψ` through the central scalars by `ω x` (`hψ_cen`). Let the scalar matrix of `x̄`, for `x`
in `(QuadField d)ˣ`, act in `ξ` by `∏ s, s x ^ (-A s)` (`hξ_centre`). Then `(ω, A)` is an algebraic
Hecke character of `QuadField d` (a member of `algHeckeChars`), and its base change to `E` is
unramified at every place `w` with `IsSafe 𝔑 w`. 

### `New.GaloisRep.levelPlaces`

 The place `w₁` together with the places `u` of `S` or conjugate to a place of `S` such that
the conjugate of the place of `QuadField d` below `u` is neither the place below `w₀` nor the
place below `w'`. The seed construction takes a level that lies exactly in these places and in the
places that contain an integer `N`. 

### `New.GaloisRep.mem_or_star_mem_insert_filter_of_isSplitPrimeToDisc`

 Each place in `insert w₁ S` or its conjugate lies in `levelPlaces d S w₀ w₁ w'`, written out:
`w₁` together with the places `u` of `S` or conjugate to a place of `S` such that the conjugate
of the place below `u` is neither the place below `w₀` nor the place below `w'`. The reason: the
places below `w₀` and `w'` are split and not conjugate to each other, since the place below `w₀`
contains `ℓ` (as `v`, the place of `ε`, does), hence so does its conjugate, and then `hw'`
applies. 

### `New.GaloisRep.exists_apply_mul_eq_of_mem_unitary`

 Rational unitary matrices act on a form through its coefficient system. Let `f` be a form of
weight `κ` on the unitary group, and let `ξ y` be the action of `ȳ` in weight `κ` for unitary `y`
(`hξ`). Then every rational unitary `y` acts on `f` by left translation by
`embFin (entryConj y)`, whose inverse transpose is `toFinGL y`. 

### `New.GaloisRep.comp_algebraMap_eq_of_isSafe`

 An embedding `s` of `E` that induces a safe place `w` (`IsSafe 𝔑 w`) restricts on `QuadField d`
to the embedding given by `ε`, if `𝔑 ∈ w₀` and `v`, the place of `ε`, lies over the same place of
`QuadField d` as `w₀`. Otherwise `s` restricts to its conjugate, and `w₀` would lie above the
conjugate of the place below `w`, which a safe place forbids. 

### `New.GaloisRep.exists_padicRep_of_pel`

 Galois representations from the cohomology of a PEL model: for PEL data `D` with neat level,
`D.β = betaK d`, good at the safe places, a safe place `v`, and a multiset `J` of nonnegative
integers each occurring in weight `ν + 1` for `θ`, some continuous representation satisfies
`IsSphericalAbove` at every safe place `w`: the members of `J` occur among its jumps at the
embedding `algebraMap E ℂ`, with no condition at the other embeddings, and the Hecke polynomial of
`ιℓ ∘ θ w` kills its geometric Frobenius elements. The model lives over the localisation at the
integers that lie in no safe place. 

### `New.GaloisRep.isSafe_and_mem_of_mem_iff`

 The level `𝔑` is prime to the places the local conditions ask for: if `𝔑` lies exactly in the
places containing `N` and those of `levelPlaces d S w₀ w₁ w'`, `N` is prime to `w₀` and `w'`, and
`w₁` is split and far from `w'`, `S` and `N`, `w₀ ∈ S`, `w₀` and `w'` lie over places with
`IsSplitPrimeToDisc`, `v` and `star v` lie outside `S` with `v` over the place below `w₀`, and `w'`
lies over that place too if `ℓ ∈ w'`, then `v`, and `w'` if `w'` and `star w'` lie outside `S`, are
safe, `𝔑 ∉ star w₀`, and `𝔑` lies in `w₁` but not in `star w₁`. 

### `New.GaloisRep.isSafe_of_notMem_image_below`

 A place `u` of `E` is safe for `𝔑` (`IsSafe`) if the place below it satisfies
`IsSplitPrimeToDisc`, neither that place nor its conjugate lies below `w₁` or below a place of `S`,
and it is prime to `N`; here `𝔑` lies exactly in the places that contain `N` and in those of
`levelPlaces d S w₀ w₁ w'`. 

### `New.GaloisRep.mem_and_notMem_of_isSafe`

 A place `w` that is safe for `𝔑` (`IsSafe`) lies outside `S`, and so does its conjugate, and
`𝔑` lies in `w₀`. Here `𝔑` lies exactly in the places that contain `N` and in those of
`levelPlaces d S w₀ w₁ w'`, each place of `insert w₁ S` or its conjugate lies in that set
(`h_cover`), `w₀ ∈ S`, and `𝔑` is prime to the conjugate of `w₀`. 

### `New.GaloisRep.exists_levelGU_le_rightStabilizer`

 A principal level inside the stabiliser of `f`: if `f` has an open stabiliser and is fixed by
the integral points trivial at `S ∋ w₀`, and each place of `insert w₁ S` or its conjugate lies in
`levelPlaces d S w₀ w₁ w'`, then some multiple `𝔑` of `N` lies exactly in the places containing `N`
and those of that set, and each `u` whose inverse transpose lies in `levelGU (Fin a) 𝔑` fixes `f`,
is `≡ 1` modulo `w₀` and lies in `proIwahori` at `w₁`. 

### `New.GaloisRep.asAlgebraHom_heckeSum_eq_smul`

 At a safe place `w`, the Hecke element `heckeSum` of index `j` acts on `ψ` by the eigenvalue
`t w j` of `f` (`ht_eig`) times `ω` of the inverse of `uniformizerNorm w ^ j`: the linear maps `L`,
with `L w hw f = ψ`, carry the local Hecke operator over from `f` (`hL`), and the central scalar
acts through `ω` (`hψ_cen`). 

### `New.GaloisRep.exists_padicRep_of_cuspidal_type_at_embedding`

 The representation for one embedding. Under the hypotheses of
`New.GaloisRep.exists_rep_of_cuspidal_type` other than the free jumps, for each complex embedding
`τ₀` of `E` some continuous representation satisfies `IsSphericalAbove` at the places of the
Frobenius data along `mostFrobenii E`, at `v`, and at `w'` if `w'` and its conjugate are outside
`S`: the jumps of `κ` at `τ₀` occur among its jumps, with no condition at the other embeddings, and
`ιℓ (P w)` kills its Frobenius elements. 

### `New.GaloisRep.exists_rep_of_cuspidal_type`

 A weak form of a case of the theorem on Galois representations attached to cohomological
cuspidal forms, in odd rank `a`. Let `f` be a form of weight `κ` on the definite unitary group,
spherical off `S` with Hecke polynomials `P` (`hP`), that transforms at a split place `w₀ ∈ S` by a
cuspidal type `χ` of the matrices `≡ 1` modulo `w₀` (`localCongruence (Fin a) w₀ 0`). Let `v`, the
place of `ε`, lie with its conjugate outside `S` and over the place of `QuadField d` below `w₀`, and
let `κ` have `a` free jumps `e i` at `ε` (`HasNoSmallRelations`). Then some continuous `r` of rank
`a` has characteristic polynomials `ιℓ (P w)` along the filter `mostFrobenii E` and satisfies
`IsSphericalAbove` with exactly the jumps of `κ` at a given place `w'` as in `hw'`, if `w'` and its
conjugate lie outside `S`. 
