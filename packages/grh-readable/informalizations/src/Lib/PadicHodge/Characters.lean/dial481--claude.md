---
{
  "module": "src/Lib/PadicHodge/Characters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Characters.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Characters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# p-adic avatars of Hecke characters and local conditions for twists and characters

The file constructs the `p`-adic avatar of an algebraic Hecke character of a totally complex field
`K`. This is a continuous character of the absolute Galois group `Γ`, defined after fixing
`ι : ℂ ≃ ℚ̄_p`. The file then studies local conditions on a Galois representation `r` at a place `A`
of `Ω`: finite type, good, Hodge–Tate jumps, and polynomials killing an element.

## Main definitions and results

* `New.AlgHeckeChar.avatar`: the continuous character of `Γ` obtained from an algebraic Hecke
  character `(θ, n)` by correcting `ι ∘ θ` at the places above `p`. It is multiplicative in
  `(θ, n)`.
* `New.GaloisRep.localConditions_twist`: how the local conditions `New.GaloisRep.IsFiniteTypeAt`
  (finite type), `New.GaloisRep.IsGoodAt` (unramified, or crystalline above `ℓ`),
  `New.GaloisRep.JumpsRelAt` (Hodge–Tate jumps) and `New.GaloisRep.PolyKillsAt` (a polynomial kills
  an element) behave when a representation is multiplied by a character. It collects the four
  lemmas `IsFiniteTypeAt.twist`, `IsGoodAt.twist`, `JumpsRelAt.twist` and `PolyKillsAt.twist`.
* `New.Period.isPotentiallyCrystalline_of_unramified_char`: take a continuous `p`-adic character `ν`
  of an open subgroup of `G_p`, trivial on inertia near `1`. An algebra on which `ν` acts by scalars
  is potentially crystalline (`IsPotentiallyCrystalline.of_unramified_char`) with the jumps of the
  trivial action (`jump_eq_jump_one_of_unramified_char`). Weil elements act on its Weil–Deligne
  representation through `ν` (`isKilledBy_X_sub_C_of_unramified_char`).
* `New.GaloisRep.localConditions_char_of_finite_image_inertia`: the conditions for a character with
  finite image on inertia, collected from `IsFiniteTypeAt.scalar_of_finite_image_inertia`,
  `hasJumpsAt_zero_of_finite_image_inertia` and `polyKillsAt_X_sub_C_of_finite_image_inertia`.
* `New.GaloisRep.AvatarCompatAt`: local-global compatibility for the ℓ-adic avatar
  `New.AlgHeckeChar.avatar` of an algebraic Hecke character θ of a totally complex field E;
  `New.GaloisRep.AvatarCompatAt.isSphericalAbove_of_unramified` is its consequence where θ is
  unramified.
* `New.GaloisRep.avatarCompatAt_of_type_eq_zero`: it holds at a place w of E if the infinity type
  vanishes at the embeddings over w.

Notions from other files:
* `New.AlgHeckeChar`: The type of algebraic Hecke characters of K: pairs (θ, n) of a character of
  the finite ideles and its infinity type, as in `New.algHeckeChars`.
* `New.Period.IsPotentiallyCrystalline`: the elements of `Bmax ⊗ T` fixed by all `g` near `1`
  (`New.Period.Dpcris`) span `Bmax ⊗ T` over `Bmax`.
* `New.GaloisRep.HasJumpsAt`: For each local datum at `A` with embedding `e`, each `g` in
  `Gal(ℚ̄_ℓ/ℚ_ℓ)` and the embedding `γ` of `ℚ̄_ℓ` in `ℂ_ℓ` given by `g`, the Hodge–Tate jumps of
  `r` at `γ`, with multiplicity, are `J` at the embedding `ι_ℓ⁻¹ ∘ g⁻¹ ∘ e` of `E` in `ℂ`.
* `New.Period.IsKilledBy`: `T` is potentially crystalline and the polynomial `P` kills
  `New.Period.linearFrob ρ s k`, the `Bmax`-linear extension of `φ ^ k s ⊗ ρ s` from `Dpcris`.
* `New.IsFrob`: `σ` stabilises the valuation subring `A` and `σ • x ≡ x ^ q` modulo the maximal
  ideal for all `x ∈ A`.

## Relation to the literature

Known result: Characters with finite image on inertia are potentially crystalline of weight 0. Only
the potentially unramified case of the theorem on locally algebraic characters is covered, together
with the jumps and the action of Weil elements. The period is a solution of Lang's equation for GL_1
in A_inf with coefficients, and no Lubin–Tate theory is used. Source: B. Conrad, Lifting global
representations with local properties (preprint 2011), Appendix B; J.-P. Serre, Abelian l-adic
representations (1968), III, Appendix.

See also `Lib.ClassField.Avatar.LocalGlobalCompatibility` and
`Lib.PadicHodge.Crystalline.Regularity`.



## p-adic avatars of algebraic Hecke characters

Let `K` be a totally complex number field with absolute Galois group `Γ`, and fix `ι : ℂ ≃ ℚ̄_p`. An
algebraic Hecke character (`New.AlgHeckeChar`) is a pair `(θ, n)`: a character of the finite ideles
with open kernel (`θ.character` in the code) and integers `n σ` (`θ.infinityType σ`), with
`θ x = ∏ σ, σ x ^ (-n σ)` on `Kˣ`. Correcting `ι ∘ θ` at the places above `p` gives a character that
is trivial on `Kˣ`, so it comes from `Γ` by `New.exists_comp_artinMap`.


### `exists_avatar`

 There is a homomorphism `av` from algebraic Hecke characters `(θ, n)` to characters of `Γ` with
values in `ℚ̄_pˣ` such that (a) `av θ` is continuous and (b) if `g` maps to the Artin symbol of the
finite idele `x`, then `av θ g = ι (θ x) * ∏ σ, (ι σ x) ^ n σ`. Here `Γ = Gal(Ω/K)` with `Ω` an
algebraic closure of `K`, and `ι` is the fixed isomorphism `ιℓ : ℂ ≃ ℚ̄_p`, `θ x` is
`θ.character x`, `n σ` is `θ.infinityType σ`, and `ι σ x` (written with `adeleExtension`) is the
image of the component of `x` at the prime induced by `ι ∘ σ`.

A case of Weil's construction of Galois characters attached to algebraic Hecke characters, for `K`
totally complex. 

### `avatar`

 The p-adic avatar: a chosen homomorphism sending the algebraic Hecke character (θ, n) to the
continuous character μ of Γ with μ(Art x) = ι(θ(x)) ∏_σ (ισ)(x)^{n_σ}. Here ι is `ιℓ` and (ισ)(x) is
the image under ισ of the component of x at the prime induced by ισ. Its defining properties are
`continuous_avatar` and `avatar_apply_of_artinMap_eq`. 

### `continuous_avatar`

 Let `θ` be an algebraic Hecke character of the totally complex number field `K`, with infinity
type `n`. Its `p`-adic avatar `avatar θ` is the Galois character `μ` with
`μ(Art x) = ι(θ(x)) ∏_σ (ισ)(x)^{n_σ}`, where `ι` is the chosen isomorphism `ℂ ≅ ℚ̄_p`. This lemma
states that `avatar θ` is continuous. 

### `avatar_apply_of_artinMap_eq`

 The defining formula of the avatar of `(θ, n)`. If the class of `g` is the Artin symbol of the
finite idele `x`, then `avatar θ g = ι (θ x) * ∏ σ, (ι σ x) ^ n σ`. Here `ι` is `ιℓ : ℂ ≃ ℚ̄_p`,
`θ x` and `n σ` are `θ.character x` and `θ.infinityType σ`, and `ι σ x`, written with
`adeleExtension`, is the image under `ι ∘ σ` of the component of `x` at the prime induced by
`ι ∘ σ`. 

### `avatar_localArtin`

 Let `A` lie over the place `v`, and suppose that `v ∤ p`, or that the exponent
`n σ = θ.infinityType σ` is zero for every `σ` such that `ι ∘ σ` induces `v`. If `g` lies in the
decomposition group of `A` and its class is the local Artin symbol of `x` at `v`, then the avatar of
`(θ, n)` takes at `g` the value `ι (θ x)`, where `x` is viewed as the idele `locIdele v x` supported
at `v`. 


## Local conditions at a place and closure properties of killing polynomials

The local conditions on a representation `r` of `Gal(Ω/E)` at a place `A` of `Ω` used here are:
* `New.GaloisRep.IsFiniteTypeAt`: trivial on inertia near `1` away from `ℓ`, potentially
  crystalline above `ℓ`;
* `New.GaloisRep.IsGoodAt`: unramified away from `ℓ`, crystalline above `ℓ`;
* `New.GaloisRep.PolyKillsAt`: a polynomial kills `r s` away from `ℓ` and, above `ℓ`, kills
  `linearFrob` of each Weil pair `(s, k)`, its action on the Weil–Deligne representation.


### `IsFiniteTypeAt.aeval_eq_zero_of_roots`

 Let `A` be a place not above `ℓ`, let `r` be of finite type at `A` (trivial on inertia near
`1`), and let `s` be an inertia element killed by `P`, that is, `P (r s) = 0`. Then `Q (r s) = 0`
for every polynomial `Q` that vanishes at all roots of `P`. 

### `PolyKillsAt.isKilledBy_of_roots`

 Above `ℓ`, inertia acts on the Weil–Deligne representation through a finite group. So if `P`
kills an inertial element `s` there, then so does every `Q` that vanishes at the roots of `P`: `r`
restricted to the decomposition group is potentially crystalline and `Q` kills `linearFrob` of
`(s, 0)`. 

### `PolyKillsAt.of_dvd`

 If `P` kills `s` for `r` at `A`, so does every multiple of `P`. 

### `isGoodAt_iff`

 At a place `A`, `r` is good (unramified away from `ℓ`, crystalline above `ℓ`) exactly when it is
of finite type (trivial on inertia near `1` away from `ℓ`, potentially crystalline above `ℓ`) and
`X - 1` kills every element of inertia.

A case of the Weil–Deligne criterion for unramified, resp. crystalline, representations (Fontaine;
Brinon–Conrad). Here finite type replaces vanishing monodromy, and `X - 1` killing each inertial
element replaces trivial inertia action. 

 ## Local conditions of the twist of a representation by a character 

### `twistPairing`

 The pairing `(u, x) ↦ u 0 • x` of a vector with one entry and a vector indexed by `m`. 

### `twistPairing_decompRep`

 The twist `r' = μ • r` is the tensor product of `μ` and `r`: the pairing `twistPairing` is
equivariant for the decomposition group at `A`. Here `decompRep r A` is `r` restricted to that
group, acting by matrices on vectors `m → ℚ̄_ℓ`. 

### `isAdmissible_twist`

 Admissibility along a filter `F` passes from `r` and the character `μ`, both restricted to the
decomposition group at `A`, to the twist `r' = μ • r`. Admissible means crystalline for `F = ⊤` and
potentially crystalline for `F = nearOne`, the pull-back along `toGp` (given by `OverGp`) of the
neighbourhoods of `1` in `Gal(ℚ̄_ℓ/ℚ_ℓ)`. 

### `twist_apply_eq_one`

 Where `r` and the character `μ` are trivial, so is the twist `r' = μ • r`. 

### `IsFiniteTypeAt.twist`

 If `r` and the character `μ`, read as a representation by `1 × 1` matrices, are of finite type
at `A` (trivial on inertia near `1` away from `ℓ`, potentially crystalline above `ℓ`), so is the
twist `r' = μ • r`. 

### `IsGoodAt.twist`

 If `r` and the character `μ` are unramified at `A` (crystalline above `ℓ`), so is the twist
`r' = μ • r`. 

### `eval₂_comp_C_mul_X`

 Evaluating `Q (c X)` at an element `β` that commutes with the coefficients, mapped by `f`, is
evaluating `Q` at `f c * β`. 

### `PolyKillsAt.twist`

 If `Q (c X)` kills `s` for `r` and `X - c` kills `s` for the character `μ`, then `Q` kills `s`
for the twist `r' = μ • r`. Here `P` kills `s` if `P (r s) = 0` away from `ℓ` and, above `ℓ`, if it
kills `linearFrob` of `s` on the potentially crystalline restriction of `r`. 

### `jump_twist`

 Let `A` be a place of Ω whose decomposition group maps with open image to Gal(Q̄_ℓ/Q_ℓ)
(`OverGp`), let `γ` be a ℤ_ℓ-algebra embedding of Q̄_ℓ into ℂ_ℓ, and let `r' = μ • r` pointwise. If
`u` is a Hodge–Tate jump of multiplicity one at `γ` of the character `μ` restricted to the
decomposition group of `A`, then for every integer `w` the multiplicity of the jump `w + u` of `r'`
at `γ` equals that of the jump `w` of `r`, both restricted to that decomposition group. 

### `JumpsRelAt.twist`

 Let the character `μ` have the single jump `u τ` at each `τ`. If a relation `R` holds between
the multiplicities in `J τ` and those of the jumps of `r` (`JumpsRelAt`), then it holds between
those in `J τ` shifted by `u τ` and those of the jumps of the twist `r' = μ • r`. 

### `localConditions_twist`

 Let `r' = μ • r` be the twist of `r` by a character `μ`, read as a representation by `1 × 1`
matrices. At the place `A`: (a), (b) if `r` and `μ` are of finite type (trivial on inertia near 1 if
ℓ is a unit at A, else potentially crystalline), or unramified (crystalline above `ℓ`), so is `r'`;
(c) if the jumps of `r` stand in the relation `R` to a family `J` of multisets (for each integer v,
`R` holds between the multiplicity of v in `J` and its multiplicity as a jump), and `μ` has the
single jump `u τ` at each `τ`, then the jumps of `r'` stand in the relation `R` to `J` shifted by
`u`; (d) if `Q (c X)` kills `s` for `r` and `X - c` kills `s` for `μ`, then `Q` kills `s` for `r'`.
The clauses are `IsFiniteTypeAt.twist`, `IsGoodAt.twist`, `JumpsRelAt.twist` and
`PolyKillsAt.twist`.

The compatibility of Weil–Deligne representations and Hodge–Tate weights with tensor products, in
the case of twists by a character. 


## Potential crystallinity of p-adic characters unramified near 1

Let `Γ` be a topological group and `toGp`, from the instance `𝒥 : OverGp Γ p`, the given
homomorphism from `Γ` to `G_p`. If `toGp` is an open embedding, a continuous `p`-adic character `ν`
of `Γ` that is trivial on inertia near `1` is potentially crystalline. The monoid
`New.Period.FrobGal = ℕ × G_p` acts on `New.Period.Ainf`, the pair `(k, s)` as `φ ^ k s`.
`New.Period.IsWeilPair s k` says that `s` acts on the residue field as `x ↦ x ^ (1 / p ^ k)`.

* `New.Period.exists_unramified_period`: a case of Lang's theorem, a unit `y` of `A_inf ⊗ T`, for a
  finite free `ℤ_p`-algebra `T` and `a ∈ T`, with `φ ^ k s y = y` and `s y = a ^ k y` for every Weil
  pair `(s, k)`, when `1 - a` is nilpotent modulo `p`.


### `noncomputable instance : MulSemiringAction FrobGal (Ainf ⊗[ℤ_[p]] T)`

 The monoid `FrobGal = ℕ × G_p` acts on `A_inf ⊗ T` by its action on `A_inf`. 

### `rTensor_frobenius_sub_id_apply`

 The operator `φ - 1` of `A_inf`, tensored with `T`, is `φ - 1` on `A_inf ⊗ T`. 

### `exists_frobenius_smul_sub_eq`

 The map `φ - 1` is onto on `A_inf ⊗ T`, with `φ` the Frobenius of `A_inf`. 

### `exists_one_tmul_eq_of_frobenius_smul_eq`

 For a flat `ℤ_p`-algebra `T`, an element of `A_inf ⊗ T` fixed by the Frobenius lies in `T`. 

### `map_toWittResidue_smul_of_isWeilPair`

 For a Weil pair `(s, k)`, the action of `φ ^ k s` on `A_inf ⊗ T` disappears after reducing the
Witt coordinates of `A_inf` to the residue field by `toWittResidue`. 

### `exists_isUnit_mul_frobenius_smul_eq`

 If `1 - a` is nilpotent modulo `p`, then `A_inf ⊗ T` has a unit `y` with `(1 ⊗ a) φ y = y`. 

### `exists_unramified_period`

 A case of Lang's theorem for `GL₁`. Let `T` be a finite free `ℤ_p`-algebra and `a ∈ T` with
`1 - a` nilpotent modulo `p`. Then `A_inf ⊗ T` has a unit `y` whose line `T y` is kept by `φ` and
`G_p`, with `φ ^ k s • y = y` and `s • y = a ^ k y` for every Weil pair `(s, k)`, that is, whenever
`s` acts on the residue field as `x ↦ x ^ (1 / p ^ k)`.

A rank-one form of the fact that unramified representations have a basis of invariants over
`W(F̄_p)[1/p]` (see Caruso), for a value `a` unipotent modulo `p` and with the period taken in
`A_inf ⊗ T`. 

### `exists_root_near_one`

 If `‖1 - b‖ < 1` and `f ≠ 0`, then `b ∈ ℚ̄_p` has an `f`-th root `a` with `‖1 - a‖ < 1`. 

### `exists_openSubgroup_trivial_on_inertia_and_norm_sub_lt_one`

 If `toGp` is an open embedding, a continuous character `ν` that is trivial on inertia near `1`
is, on the preimage of some open subgroup of `G_p`, trivial on inertia (the `g` for which
`(toGp g, 0)` is a Weil pair) and at distance less than `1` from `1`. 

### `exists_isFrob_and_dense`

 Let `toGp` be an open embedding and `U` an open subgroup of `G_p`. The preimage of `U` contains
an arithmetic Frobenius `φ` for some `p ^ f` with `f ≠ 0`, and the `φ ^ k * i` with `i` in inertia
are dense in it: a closed set that contains them contains the whole preimage. 

### `exists_period_of_character`

 Let `Γ` be a topological group with a map `toGp : Γ → Gp p` that is an open embedding, and let
`ν : Γ →* (PadicAlgCl p)ˣ` be a continuous character with `ν g = 1` for all `g` near `1` in `Γ` such
that `toGp g` lies in inertia (`IsWeilPair (toGp g) 0`). Then there are a `CoeffRing` `O`, meaning
the ring of integers of a finite Galois extension of ℚ_p in ℚ̄_p, and a unit `y` of
`Ainf ⊗[ℤ_[p]] O` such that: (a) `y` is fixed by φ^k s for every Weil pair `(s, k)`, that is,
whenever `s⁻¹` acts on the residue field of ℚ̄_p as Frobenius for `p ^ k`; and (b) for `g` in
`nearOne Γ`, the pull-back along `toGp` of the neighbourhoods of `1` in `G_p`, we have
`toGp g • y = (1 ⊗ o) * y` for some `o` in `O` equal to `ν g⁻¹`. 

### `span_range_one_tmul_mul_eq_top`

 For a unit `z` of `Bmax ⊗ T`, the elements `(1 ⊗ x) * z` span `Bmax ⊗ T` over `Bmax`. 

### `jump_eq_jump_one_of_period`

 Let `ρ` act on the `ℚ̄_p`-algebra `T` by the scalars `ν g`, and let `y` be a unit of
`A_inf ⊗ O` that `toGp g` multiplies by `ν g⁻¹` for `g` near `1`. Then `ρ` has the jumps of the
trivial representation on `T`. 

### `toBmaxTensor`

 The map `A_inf ⊗ O → Bmax ⊗ T` induced by `A_inf → Bmax` and `O ⊆ ℚ̄_p → T`. 

### `tensorAction_one_tmul_mul_toBmaxTensor`

 Let `ρ` act on `T` by the scalars `ν g`. Then `m ⊗ ρ g` sends `(1 ⊗ x) * z` to `ν h` times
`(1 ⊗ ρ (h⁻¹ * g) x) * (m • z)`, where `z` and `m • z` are mapped to `Bmax ⊗ T`. 

### `one_tmul_mul_toBmaxTensor_mem_dpcris`

 Let `ρ` act on `T` by the scalars `ν g`, and let `toGp g` multiply `y ∈ A_inf ⊗ O` by `ν g⁻¹`
for `g` near `1`. Then the elements `(1 ⊗ x) * y` of `Bmax ⊗ T` are fixed by all `g` near `1`. 

### `IsPotentiallyCrystalline.of_unramified_char`

 Let `𝒥.toGp` be an open embedding and `ν` a continuous character of `Γ`, trivial on inertia near
`1`. If `ρ` acts on a commutative `ℚ̄_p`-algebra `T` by the scalars `ν g`, then `ρ` is potentially
crystalline. 

### `jump_eq_jump_one_of_unramified_char`

 Let `𝒥.toGp` be an open embedding and `ν` a continuous character of `Γ`, trivial on inertia near
`1`. If `ρ` acts on a commutative `ℚ̄_p`-algebra `T` by the scalars `ν g`, then `ρ` has the jumps
(Hodge–Tate weights with multiplicity) of the trivial representation on `T`. 

### `isKilledBy_X_sub_C_of_unramified_char`

 Let `𝒥.toGp` be an open embedding and `ν` a continuous character of `Γ`, trivial on inertia near
`1`, and let `ρ` act on a commutative `ℚ̄_p`-algebra `T` by the scalars `ν g`. For a Weil pair
`(toGp s, k)`, the polynomial `X - ν s` kills `ρ` at `s` and `k`: `ρ` is potentially crystalline and
`linearFrob ρ s k` is multiplication by `ν s` on `Bmax ⊗ T`. 

### `isPotentiallyCrystalline_of_unramified_char`

 Let `𝒥.toGp` be an open embedding and `ν` a continuous character of `Γ`, trivial on inertia near
`1`, and let `ρ` act on a commutative `ℚ̄_p`-algebra `T` by the scalars `ν g`. Then `ρ` is
potentially crystalline, has the jumps of the trivial action, and for every Weil pair `(toGp s, k)`
the polynomial `X - ν s` kills `linearFrob ρ s k`.

A case of the fact that potentially unramified characters are potentially crystalline of weight 0
(Caruso). 


## Local conditions for characters and for avatars with vanishing type

The local conditions `New.GaloisRep.IsFiniteTypeAt`, `New.GaloisRep.IsGoodAt`,
`New.GaloisRep.HasJumpsAt` and `New.GaloisRep.PolyKillsAt` for characters, at a valuation subring A
of Ω over a place w of E.


### `eventually_eq_one_of_finite_image_inertia`

 A continuous character with finite image on the inertia group of A is trivial on the elements
of inertia near 1. 

### `isOpenEmbedding_toGp`

 The map of a chart L at A from the decomposition group to Gal(ℚ̄_ℓ/ℚ_ℓ) is an open embedding. 

### `eventually_eq_one_of_isWeilPair_zero`

 The form of `eventually_eq_one_of_finite_image_inertia` along a chart L at A: the character is
trivial at the s near 1 in the decomposition group for which (`L.toGp s`, 0) is a Weil pair. 

### `IsFiniteTypeAt.scalar_of_finite_image_inertia`

 If a continuous ℓ-adic character μ has finite image on the inertia group of A, then the
representation by the scalar matrices μ(s) is of finite type at A: trivial on inertia near 1 off ℓ,
potentially crystalline above ℓ. 

### `polyKillsAt_X_sub_C_of_finite_image_inertia`

 If a continuous ℓ-adic character μ has finite image on the inertia group of A, then X − μ(s)
kills s for the representation r by the scalar matrices μ(s): it annihilates r(s) off ℓ, and above
ℓ the linearised Frobenius on periods at every Weil pair given by s. 

### `JumpsRelAt.congr`

 The condition `JumpsRelAt r A R J` (the relation `R` holds between the multiplicities in `J` and
those of the Hodge–Tate jumps of `r` at A) at a place A over w depends only on the values of J at
the embeddings τ that induce w. 

### `hasJumpsAt_zero_of_finite_image_inertia`

 If a continuous ℓ-adic character μ has finite image on the inertia group of A, then the
representation of rank one that it defines has the single Hodge–Tate jump 0 along every chart
at A. 

### `localConditions_char_of_finite_image_inertia`

 Let μ be a continuous ℓ-adic character with finite image on the inertia group of A, and r the
representation of rank one that it defines. Then (a) r is of finite type at A (trivial on inertia
near 1 off ℓ, potentially crystalline above ℓ), (b) its only Hodge–Tate jump is 0 along every chart
at A, and (c) X − μ(s) kills every s in the sense of `PolyKillsAt`: it annihilates r(s) off ℓ, and
above ℓ the linearised Frobenius on periods at every Weil pair given by s. 

 ### Avatars of algebraic Hecke characters 

### `AvatarCompatAt`

 Local-global compatibility at w for the avatar r of θ, whose infinity type is n. At every A over
w: (a) r is of finite type at A; (b) its jump at τ is −n(τ) for the τ that come from charts at A;
(c) for m = 0 or 1 and every s whose inverse is a Frobenius for the power q^m, q the norm of w,
there is x in E_w^× of order m with local Artin symbol the class of s, and X − ι(θ(x)) kills s. 

### `_root_.New.AlgHeckeChar.avatar_frob`

 If w ∤ ℓ and θ is unramified at w, the ℓ-adic avatar of θ at a geometric Frobenius at A over
w equals ι of the value of θ at the local idele of the chosen uniformiser at w. 

### `_root_.New.AlgHeckeChar.eventually_avatar_frob`

 For most geometric Frobenius elements s at places w (the filter `New.mostFrobenii`), the avatar
of θ at s is ι of the value of θ at the chosen uniformiser at w. 

### `avatarCompatAt_of_type_eq_zero`

 Local-global compatibility `New.GaloisRep.AvatarCompatAt` holds at w for the ℓ-adic avatar r of
an algebraic Hecke character θ of a totally complex E whose exponent n_σ vanishes for every σ with
ισ inducing w (`inducedPrime σ = w`). That is, at every A over w: r is of finite type; its jump at τ
is −n(τ); and for m = 0, 1, each s whose inverse is a Frobenius for q^m (q the norm of w) is killed
by X − ι(θ(x)) for some x in E_w^× of order m with local Artin symbol the class of s.

A case of the description of Hodge–Tate weights and Weil–Deligne representations of avatars of
algebraic Hecke characters: E is totally complex, and w is a place where the exponents at all
embeddings inducing w vanish. 

### `AvatarCompatAt.isSphericalAbove_of_unramified`

 Suppose local-global compatibility `AvatarCompatAt` holds at w for θ, with infinity type n, and
θ is unramified at w. Then at every place A of Ω over w, the avatar r of θ (a) is good (unramified
if ℓ is a unit at A, crystalline above ℓ). (b) Its Hodge–Tate jump multiplicities at the embeddings
τ coming from charts at A equal those of the single weight −n(τ), which is the role of the relation
`Eq` against the sets {−n(τ)}. (c) X − ι(θ(ϖ_w)) kills every geometric Frobenius at A, ϖ_w being the
chosen uniformiser (`heckeCoeff`). 
