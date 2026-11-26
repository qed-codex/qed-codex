---
{
  "module": "src/Lib/GaloisRep/Main/AttachedRepresentations.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Main/AttachedRepresentations.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Main/AttachedRepresentations.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Attached Galois representations: traces, characteristic polynomials and rank one

This file sets up the statement that eigenforms on a definite unitary group have attached Galois
representations. Here `ιℓ` identifies `ℂ` with an algebraic closure of `ℚ_ℓ`, and `P` is a system of
complex polynomials, one for each finite place. A continuous representation `ρ` with non-degenerate
trace form, with an open map `j` to the Galois group, is attached to `P` when, along most Frobenius
elements (the filter `New.mostFrobenii`), its characteristic polynomials approach `ιℓ (P w)`. The
file shows that the characteristic polynomials are then determined by `P`, so two attached
representations have the same traces. It also shows that the representation attached to an
eigenform on the definite unitary group of rank one is the avatar of an algebraic Hecke character.

## Main definitions and results

* `New.GaloisRep.Attached`: a representation `ρ` of a topological group `H`, together with a map `j`
  from `H` to the Galois group (by default the identity), is attached to `P`. This means that `ρ` is
  continuous, has a non-degenerate trace form (`New.IsTraceNondeg`), `j` is open, and along most
  Frobenius elements the characteristic polynomials of `ρ` approach `ιℓ (P w)`.
* `New.GaloisRep.SphericalCompat`: the statement that an attached representation exists, and that
  every attached representation satisfies `New.GaloisRep.IsCompatibleAt` (unramified or crystalline,
  Hodge–Tate jumps, Hecke polynomial) at a place `w` where the form is spherical.
* `New.GaloisRep.Attached.tendsto_charpoly_coeff`: `ιℓ (P w)` tends to `det (X - ρ x)` as the
  Frobenius element at `w` tends to `j x`.
* `New.GaloisRep.Attached.trace_eq`: two representations attached to `P` have the same traces.
* `New.IsRankOneCharacter`: the infinity type of an algebraic Hecke character `θ` and its values at
  split places are read off from a form on `U(1)` and its weight.
* `New.GaloisRep.Attached.exists_det_eq_avatar`: in rank one, an attached representation is the
  avatar of such a character `θ`.

Notions from other files:
* `New.Ω`: an algebraic closure of `ℚ`.
* `New.Gf E n`: the finite adelic points of the definite unitary group of the CM field `E`.
* `New.IsEigenform f P`: `f ≠ 0`, and at almost all `w` of prime norm, `w` is split and `f` is
  spherical with Hecke polynomial `P w` (`New.HasHeckePolyAt`).
* `New.mostFrobenii E`: a filter on triples `(w, A, s)` of a place `w` of prime norm, a place `A` of
  `Ω` over `w` and a geometric Frobenius element `s` at `A` (`New.FrobeniusDatum`). "Most" means:
  every non-empty open set of the Galois group has a non-empty open part `O` such that, for almost
  all `w`, the property holds for every triple with `s` in `O`.
* `New.mostFrobeniiAt E g`: the same filter, refined by the condition that `s` lies near `g`.

## Relation to the literature

Known; see `Lib.GaloisRep.Main.OddRank` for sources.


 ## Attached representations and the existence statement 

### `Attached`

 The representation `ρ` of `H`, read in the Galois group through a map `j`, is attached to the
system `P` of complex polynomials indexed by the finite places of `E`: `ρ` is continuous with
non-degenerate trace form, `j` is open, and for every `η > 0` the coefficients of
`det (X - ρ x) - ιℓ (P w)` have norm at most `η` for most Frobenius data `(w, A, s)` and all `x`
with `j x = s`. When `j` is omitted, `H` is the Galois group itself and `j` is the identity. 

### `Attached.continuous`

 The representation is continuous. 

### `Attached.isTraceNondeg`

 The trace form of the representation is non-degenerate. 

### `Attached.isOpenMap`

 The map to the Galois group is open. 

### `Attached.eventually_norm_coeff_le`

 Let `η > 0`. For most Frobenius data, with place `w` and Frobenius element `s`, and all `x`
  with `j x = s`, all coefficients of `det (X - ρ x) - ιℓ (P w)` have norm at most `η`. 

### `IsCompatibleAt`

 The local conditions on the Galois representation `r` at a place `A` of `Ω` over `w`, for a
function `f` of weight `κ` on the unitary group, with values in the space `WeylIndex n κ.1 → ℂ` of
the weight-`κ` representation, and the rank `N`: `r` is unramified or crystalline at `A`; it has the
Hodge–Tate jumps of `κ` in rank `N`; and if `w` is split and `f` has Hecke polynomial `Q` at `w`,
then `ιℓ Q` kills the action through `r` of every geometric Frobenius element `s` at `A`
(`PolyKillsAt`). 

### `SphericalCompat`

 Every eigenform `f` of any weight `κ` on the standard definite unitary group
(`f ∈ (stdSpace E n).forms κ`: the right stabiliser of `f` is open, and `f (γ g)` is the weight-`κ`
action of a global `γ` on `f g`), with system of Hecke polynomials `P`, has an attached Galois
representation; and if `f` is spherical at `w`, every representation attached to `P` satisfies the
local conditions `IsCompatibleAt` in rank `N` at every place of `Ω` over `w`. 

### `IsCompatibleAt.isGoodAt`

 Let `E` be a CM field, `f` a function of weight `κ` on the finite adelic unitary group, `r` an
`ℓ`-adic representation of `Gal(Ω/E)` and `A` a place of `Ω`. If `r` satisfies the local conditions
`IsCompatibleAt` for `f` at `A`, then `r` is good at `A` (`IsGoodAt`): it is trivial on the inertia
group of `A` if `ℓ` is a unit at `A`, and its restriction to the decomposition group of `A` is
crystalline along every embedding of `Ω` in the algebraic closure of `ℚ_ℓ` that induces `A`
(`PadicPlaceEmbedding`). The rank `N` and the finite place `w` of `E` play no role here. 

### `IsCompatibleAt.hasJumpsAt`

 Let `E` be a CM field with a chosen CM type, and let `r` be an `ℓ`-adic representation of
`Gal(Ω/E)` satisfying `IsCompatibleAt f N w r A`, the local conditions at the place `A` of `Ω` for a
function `f` of weight `κ` on the unitary group `Gf E n`, in rank `N`. Then `r` has Hodge–Tate jumps
`jumps κ N` at `A`: for each local datum at `A` with embedding `e` and each `g ∈ Gal(ℚ̄_ℓ/ℚ_ℓ)`, the
jumps of `r` at `g`, with multiplicity, are given by the embedding `σ = ιℓ⁻¹ ∘ g⁻¹ ∘ e` of `E` in
`ℂ`. They are {j − 1 − λ_j} if `σ` is in the CM type and {λ_j + N − j} otherwise (1 ≤ j ≤ N), where
λ is the highest weight of `κ` at the place of `σ`. 

### `IsCompatibleAt.polyKillsAt`

 Suppose `r` satisfies `IsCompatibleAt f N w r A`, the local conditions at the place `A` of `Ω`
for the function `f` of weight `κ` on the unitary group in rank `N`. Suppose also that `w` is split
(`star w ≠ w`), that `f` has Hecke polynomial `Q` at `w`, and that `s⁻¹` is an arithmetic Frobenius
at `A` for the norm `w.q` of `w`, so that `s` is a geometric Frobenius. Then `ιℓ Q`, the image of
`Q` under the fixed isomorphism `ιℓ : ℂ ≃ ℚ̄_ℓ`, kills `s` at `A` for `r` (`PolyKillsAt`):
`(ιℓ Q)(r s) = 0` if `ℓ` is a unit at `A`, and otherwise the corresponding condition on Weil pairs
holds. 

### `SphericalCompat.exists_attached`

 Assume `SphericalCompat E n N w`: every eigenform of any weight on the standard definite unitary
group has an attached Galois representation, and local conditions hold in rank `N` at places over
`w` where the form is spherical. Then an eigenform `f` of weight `κ` with Hecke polynomials `P` has
an attached `ℓ`-adic Galois representation. 

### `SphericalCompat.isCompatibleAt`

 Assume `SphericalCompat E n N w`, and let `f` be an algebraic modular form of weight `κ` on
`stdSpace E n` that is an eigenform with Hecke polynomials `P` and is spherical at `w` for the right
regular action. Then every `r : GalRep ℓ E n` attached to `P` satisfies `IsCompatibleAt f N w r A`
at every place `A` of `Ω` over `w`. These local conditions say that `r` is unramified or crystalline
at `A`, has the Hodge–Tate jumps of `κ` in rank `N`, and, if `w` is split, `ιℓ Q` kills every
geometric Frobenius at `A` for the Hecke polynomial `Q` of `f` at `w`. 

### `isRoot_of_isRoot_charpoly`

 If the polynomial `P` kills the square matrix `M`, then every root of the characteristic
polynomial of `M` is a root of `P`. 

 ## Characteristic polynomials and traces of attached representations 

### `norm_eq_one_of_continuous`

 A continuous character of a compact group with values in the algebraic closure of `ℚ_ℓ` has
values of absolute value `1`. 

### `norm_coeff_le_of_mul_monic`

 For polynomials `D`, `R` over the algebraic closure of `ℚ_ℓ` with `R` monic, if all coefficients
of `D * R` have absolute value at most `η`, then so do all coefficients of `D`. 

### `continuous_coeff_charpoly`

 The coefficients of the characteristic polynomial depend continuously on the matrix. 

### `GaloisRep.Attached.tendsto_charpoly_coeff`

 Here `E` is a number field embedded in `Ω` (`EmbeddedNumberField`). Let `ρ` be attached through
an open map `j` to the system of polynomials `P` (`GaloisRep.Attached`). As the Frobenius element at
`w` tends to `j x` (along most Frobenius data `(w, A, s)`, `New.mostFrobeniiAt`), the `i`-th
coefficient of `P w`, transported by `ιℓ`, tends to that of the characteristic polynomial of
`ρ x`. 

### `GaloisRep.Attached.trace_eq`

 If `ρ` on `H` and `σ` on `G`, of the same rank, are attached to the same system `P` through maps
`j`, `j'` to `Gal(Ω/E)`, then `ρ x` and `σ y` have the same trace whenever `j x = j' y`. 


## Rank one: the avatar of an algebraic Hecke character

The Galois representation attached to an eigenform on the definite unitary group of rank one is
computed from a character extending the scalars by which elements act on the form. This is used
to prove local-global compatibility for algebraic Hecke characters
(`New.GaloisRep.avatarCompatAt_of_hasPrimitiveRoot5040`).

`New.AlgHeckeChar E` consists of pairs of a character of the finite ideles with open kernel and an
infinity type that gives its values on principal ideles;
`New.AlgHeckeChar.avatar` is its `ℓ`-adic avatar. `New.ofSplitPlace hw g` is the element of the
finite adelic unitary group with component `g` at the split place `w`, and `New.rightRegular` is
right translation. `New.scalarFin (Fin 1) (New.divStar x)` is the element `x / star x` of `U(1)`.


### `New.exists_character_of_eigenvalues`

 The scalars by which elements of a commutative group act on a non-zero vector `f` extend to a
character of the whole group. 

### `New.continuous_scalarFin_divStar`

 The map `x ↦ x / star x` (`divStar`) from the finite ideles of `E` to the norm-one adeles, read
as scalar matrices in `U(1)` (`scalarFin`), is continuous. 

### `New.scalarFin_divStar_locIdele`

 At a split place `w`, the element `x / star x` of `U(1)` for the idele with component `x` at `w`
and `1` elsewhere is the scalar matrix `x` embedded at `w`. 

### `New.apply_mul_scalarFin_divStar_principalIdele`

 Let `f` be a form on `U(1)` whose weight is the power `κ` of the determinant. For `x` in `Eˣ`,
right translation by `x / star x` multiplies `f` by `∏ v, (star (Φ v x) / Φ v x) ^ κ v`, where
`Φ v` is the embedding of the CM type at the infinite place `v`. 

### `New.HasHeckePolyAt.rightRegular_ofSplitPlace_scalar`

 If a function `f` on `U(1)` is spherical with Hecke polynomial `Q` at the split place `w`
(`HasHeckePolyAt`), then right translation by a uniformiser `ϖ` of `E_w`, embedded at `w`
(`ofSplitPlace`), multiplies `f` by the scalar `-Q(0)`. 

### `New.IsRankOneCharacter`

 The algebraic Hecke character `θ` (character `θ.val.1` of the finite ideles, infinity type
`θ.val.2`) matches a function `f` on `U(1)` whose weight is the power `κ` of the determinant: its
infinity type is `± κ`, and at a split place `w` its value at `locIdele w x`, the idele with
component `x` at `w` and `1` elsewhere, is the scalar by which `x` acts on `f`, when there is
one. 

### `New.IsRankOneCharacter.type_eq`

 The exponent at `σ` is `± κ v` for the place `v` of `σ`, with `+` when `σ` is the embedding
  `Φ v` of the CM type. 

### `New.IsRankOneCharacter.apply_locIdele`

 If right translation by `x`, embedded at the split place `w`, multiplies `f` by `c`, then
  `θ_w(x) = c`. 

### `New.IsRankOneCharacter.apply_uniformizer`

 If `f` has the Hecke polynomial `Q` at the split place `w`, then `θ_w(x) = -Q(0)` for every
  uniformiser `x`. 

### `New.GaloisRep.Attached.exists_det_eq_avatar`

 Let `r` be attached to the Hecke polynomials `P` of an eigenform `f` on `U(1)` whose weight is
the power `κ` of the determinant (`Attached`: their characteristic polynomials approximate `ιℓ P`
at most Frobenius elements). Then `det r` is the `ℓ`-adic avatar (the associated Galois character)
of an algebraic Hecke character `θ` whose infinity type and values at split places are read off from
`κ` and `f` (`New.IsRankOneCharacter`). 
