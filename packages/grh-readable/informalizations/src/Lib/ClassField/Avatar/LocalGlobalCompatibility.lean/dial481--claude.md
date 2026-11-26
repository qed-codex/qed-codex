---
{
  "module": "src/Lib/ClassField/Avatar/LocalGlobalCompatibility.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Avatar/LocalGlobalCompatibility.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Avatar/LocalGlobalCompatibility.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Local-global compatibility for the ℓ-adic avatar of an algebraic Hecke character

Local-global compatibility, including the places above `ℓ`, for the ℓ-adic avatar of an algebraic
Hecke character `θ` of a CM field `E` satisfying `New.HasPrimitiveRoot5040`.

* `New.GaloisRep.avatarCompatAt_of_hasPrimitiveRoot5040`: the statement
  `New.GaloisRep.AvatarCompatAt w θ` at every finite place `w`.

A base change reduces to a split place `w`, one with `star w ≠ w`. There
(`New.GaloisRep.avatarCompatAt_of_isSplit`) `θ = θ₁ (θ / θ₁)`, with `θ₁` the character of a rank one
eigenform (`New.GaloisRep.sphericalCompat_of_odd`, `New.GaloisRep.Attached.exists_det_eq_avatar`)
and `θ / θ₁` of type `0` at the embeddings inducing `w`
(`New.GaloisRep.avatarCompatAt_of_type_eq_zero`).

Notions from other files:
* `New.AlgHeckeChar`: pairs of a character of the finite ideles and its infinity type.
* `New.AlgHeckeChar.avatar`: the ℓ-adic character of `Gal(Ω/E)` attached to such a pair.
* `New.GaloisRep.AvatarCompatAt`: at each place of `Ω` over `w` the avatar has finite type
  (`IsFiniteTypeAt`), its jumps are minus the type of `θ`, and inertia and geometric Frobenius
  elements act through `θ` and local class field theory.
* `New.IsEigenform`, `New.HasHeckePolyAt`: `f ≠ 0` has Hecke polynomial `P u` at almost all places
  `u` of prime norm; `f` is spherical at a split place with the given Hecke polynomial.

## Relation to the literature

Known result: the existence of the ℓ-adic avatar of an algebraic Hecke character and its local
behaviour. The avatar is constructed over totally complex fields (in an imported file). For the CM
fields used here, the behaviour at places above ℓ is read from the rank-one case of the Galois
representations of `Lib.GaloisRep.Main.OddRank` rather than from Lubin–Tate theory. Source: J.-P.
Serre, Abelian ℓ-adic representations and elliptic curves, 1968, II–III (locally algebraic =
Hodge–Tate, Tate's theorem); B. Conrad, Lifting global representations with local properties,
App. B (crystalline case).


### `New.GaloisRep.avatar_baseChange`

 Let `E` be a totally complex number field and `L ⊇ E` a CM field, both inside the fixed
algebraic closure `Ω` of `ℚ`. For an algebraic Hecke character `θ` of `E`, the ℓ-adic avatar (the
character of the Galois group attached to it) of the base change `θ ∘ N_{L/E}` is the restriction
to `Gal(Ω/L)` of the avatar of `θ`. 

### `New.GaloisRep.exists_eigenform_rank_one`

 Let `E` be a CM field, with CM type `Φ` (`CMType E`: one embedding from each conjugate pair),
with a primitive root of unity of order `5040`, `w` a split finite place and `κ` a weight. Then
there is an eigenform `f` of weight `κ` on the definite unitary group of rank one
(`stdSpace E (Fin 1)`), with system `P` of Hecke polynomials, that is spherical at `w` with Hecke
polynomial `P w`. 

### `New.GaloisRep.avatarCompatAt_of_isSplit`

 Let `E` be a CM field containing a primitive root of unity of order `5040`, `θ` an algebraic
Hecke character of `E` with infinity type `n`, and `w` a finite place of `E` that is split
(`star w ≠ w`). Then the ℓ-adic avatar `r` of `θ`, taken through the chosen isomorphism
`ι : ℂ ≃ ℚ̄_ℓ`, satisfies `New.GaloisRep.AvatarCompatAt` at `w`. That is, at every `A` over `w`: (a)
`r` is of finite type at `A`; (b) its jump at each `τ` coming from a chart at `A` is `−n(τ)`; (c)
for `m = 0` or `1` and every `s` whose inverse is a Frobenius for `q^m`, with `q` the norm of `w`,
there is `x ∈ E_w^×` of order `m` whose local Artin symbol is the class of `s`, and `X − ι(θ(x))`
kills `s`. 

### `New.GaloisRep.avatarCompatAt_of_hasPrimitiveRoot5040`

 Let `E` be a CM field containing a primitive root of unity of order `5040`, and `θ` an algebraic
Hecke character of `E` with infinity type `n`. Then at every finite place `w` the ℓ-adic avatar `r`
of `θ`, taken through the chosen isomorphism `ι : ℂ ≃ ℚ̄_ℓ`, satisfies
`New.GaloisRep.AvatarCompatAt`. That is, at every `A` over `w`: (a) `r` is of finite type at `A`;
(b) its jump at each `τ` coming from a chart at `A` is `−n(τ)`; (c) for `m = 0` or `1` and every `s`
whose inverse is a Frobenius for `q^m`, with `q` the norm of `w`, there is `x ∈ E_w^×` of order `m`
whose local Artin symbol is the class of `s`, and `X − ι(θ(x))` kills `s`. 
