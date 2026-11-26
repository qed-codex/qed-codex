---
{
  "module": "src/Lib/GaloisRep/LocalGlobal/IwahoriCompatibility.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/LocalGlobal/IwahoriCompatibility.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/LocalGlobal/IwahoriCompatibility.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Local-global compatibility at split places for Iwahori eigencharacters and parahoric types

Let `r` be an `ℓ`-adic Galois representation attached to an eigenform on a definite unitary group
over a CM field `E`, and let `w` be a split place. Level information on the form at `w` gives
polynomials that kill geometric Frobenius and inertia elements under `r`, in the sense of
`New.GaloisRep.PolyKillsAt`. At pro-`p` Iwahori level, with eigencharacter `New.torusChar ξ`, the
characters `ξ i` are tamely ramified and, when sorted, give the roots of such polynomials. For `w`
not above `ℓ`, when a parahoric subgroup acts by scalars there are analogous polynomials for the
Frobenius and inertia matrices. For the stabiliser in `GL_N(𝒪_w)` of a line modulo `w`, the Hecke
operator of `diag (ϖ, 1, …, 1)` acts like Frobenius on the image of `T - 1`, for the matrix `T` of
an inertia element, in the sense of an identity between traces. Here `p` is the residue
characteristic of `w`.

## Main definitions and results

* `New.GaloisRep.Attached.local_global_of_eigencharacter`: the main result, for `ξ i` sorted by size
  at a uniformiser.
* `New.Patching.IsParahoricCompatible`: commuting matrices `F`, `T` are killed by polynomials read
  off given scalars and an exponent that is not zero on a given vector.
* `New.Patching.isParahoricCompatible_galRep`: the Frobenius and inertia matrices have this property
  for a non-zero pro-`p` Iwahori fixed form on which a parahoric subgroup acts by scalars that tell
  its blocks apart.
* `New.Patching.hecke_eq_frob_on_parahoricEigenspace`: for the stabiliser in `GL_N(𝒪_w)` of a line
  modulo `w`, acting by a scalar character that is not of order dividing `N !` at the unit, the
  Hecke operator of `diag (ϖ, 1, …, 1)` acts like Frobenius on the image of `T - 1`, with `T` the
  inertia matrix, in the sense of an identity between traces.

Notions from other files:
* `New.GaloisRep.PolyKillsAt r A s P`: `P (r s) = 0` if `ℓ` is a unit at `A`; above `ℓ`, for every
  Weil pair `(s, k)`, `r` is potentially crystalline and `P` kills `New.Period.linearFrob`.
* `New.IsFrob A q σ`: `σ` stabilises `A` and acts as `x ↦ x ^ q` on its residue field.
* `New.Patching.localFormRep V κ hw`: the representation of `GL_N(E_w)`, with `N` the cardinality
  of `n`, on the forms of weight `κ` on `V` at the split place `w`.
* `New.IsIwahoriEigen ρ ξ x`: `x ≠ 0` is fixed by the pro-`p` Iwahori subgroup, and
  `U_t x = ξ t • x` for dominant diagonal `t`.
* `New.torusChar θ`: the character `t ↦ ∏ i, θ i (t i) * |t i| ^ (N - 1 - i)` of the diagonal torus
  of `GL_N`.

## Relation to the literature

Known; see `Lib.GaloisRep.LocalGlobal.LabelCompatibility` for sources.



## Compatibility for a sorted Iwahori eigencharacter

Let `f` be an eigenform on the standard definite unitary group over the CM field `E`, `r` an
`ℓ`-adic Galois representation attached to it (`New.GaloisRep.Attached`), `w` a split place and `A`
a place of `Ω` above `w`. Suppose that at `w` the form is an eigenvector at the pro-`p` Iwahori
level (`New.IsIwahoriEigen`) for the torus character `New.torusChar ξ`, that is
`t ↦ ∏ i, ξ i (t i) * |t i| ^ (N - 1 - i)` with `N` the cardinality of `n`.


### `IsIwahoriEigen.apply_eq_one_of_principal_unit`

 Let `f` be a pro-`p` Iwahori eigenvector at `w` with eigencharacter `torusChar ξ`. Then the
absolute value and the characters `ξ i` are trivial on the `y` congruent to `1` modulo `w`. 

### `IsIwahoriEigen.char_pow_q_sub_one_eq_one`

 Let `f` be a pro-`p` Iwahori eigenvector at `w` with eigencharacter `torusChar ξ`. Then the
absolute value and the characters `ξ i` kill the `(q - 1)`-th power of every local unit, where
`q = w.q` is the size of the residue field. 

### `GaloisRep.PolyKillsAt.of_mul_frob_pow`

 Let `s`, `φ` lie in the decomposition group of a place `A` above `w`, with `φ` a Frobenius. If
`∏ (X - a i)` kills `φ⁻¹`, with `a i ≠ 0`, and `∏ (X - α i * a i ^ m)` kills `s * φ⁻¹ ^ m` for all
`m > 0`, then `∏ (X - α i)` kills `s`. Here "kills" is `New.GaloisRep.PolyKillsAt` for `r`:
vanishing at the matrix away from `ℓ`, at the linear Frobenius above `ℓ`. 

### `IsIwahoriEigen.exists_hasHeckePolyAt`

 Let the eigenform `f` for the system `P` of Hecke polynomials be a pro-`p` Iwahori eigenvector
at `w` with eigencharacter `torusChar ξ`. If the `ξ i` are unramified and `‖ξ i ϖ‖` is antitone in
`i` for a uniformiser `ϖ`, then some eigenform for the same system `P` is spherical at `w` with
Hecke roots `ξ i ϖ` (`New.HasHeckePolyAt`). 

### `IsIwahoriEigen.antitone_norm`

 Let `f` be a pro-`p` Iwahori eigenvector at `w` with eigencharacter `torusChar ξ`. If
`‖ξ i (uniformizer w)‖` is antitone in `i`, so is `‖ξ i x‖` for `x` of order `k ≥ 0`. 

### `IsIwahoriEigen.finiteIndex_comap_zpowers`

 Let `f` be a pro-`p` Iwahori eigenvector at `w` with eigencharacter `torusChar ξ`. If `x` has
order `k > 0`, the `y` with `(|y|, ξ y)` a power of `(|x|, ξ x)` form a subgroup of finite index. 

### `IsIwahoriEigen.eq_of_localArtin_eq`

 Let `f` be a pro-`p` Iwahori eigenvector at `w` with eigencharacter `torusChar ξ`, and let `A`
be a place above `w`. If `y / x` is a unit and `x`, `y` have the same local Artin symbol at `A`,
then the absolute value and the `ξ i` agree at `x` and `y`. 

### `IsIwahoriEigen.order_eq_one_and_unramified`

 Let `ξ i` be characters of the completion at `w` and let `x` have order `k`. If `(|y|, ξ y)` is
a power of `(|x|, ξ x)` for every `y`, then `x` is a uniformiser and the `ξ i` are unramified. 

### `exists_char_trivial_of_prime_dvd_index`

 If a prime `p` divides the finite index of a subgroup `D` of a commutative group `G`, there is a
non-trivial character `χ` of `G` with values in `ℚ/ℤ` that is killed by `p` and trivial on `D`. 

### `index_comap_lt_of_char_ne_one`

 If a character `χ` of `G` is trivial on the subgroup `D` of finite index and on the image of
`N : G' →* G` but not at `x₀`, then the preimage of `D` under `N` has smaller index than `D`. 

### `GaloisRep.Attached.local_global_of_eigencharacter_of_unramified`

 The unramified case of `New.GaloisRep.Attached.local_global_of_eigencharacter`. Let `r` be
attached to the Hecke polynomials `P` of the eigenform `f` on the standard space over the CM field
`E`, where `f` is a pro-`p` Iwahori eigenvector at the split place `w` for `torusChar ξ`, each `ξ i`
is trivial on units, and `‖ξ i ϖ‖` is antitone in `i` for a uniformiser `ϖ`. If `A` lies above `w`
and `s⁻¹` is a Frobenius at `A`, then `r` is of finite type at `A` (trivial on inertia near `1` if
`ℓ` is a unit at `A`, and potentially crystalline), its Hodge–Tate jumps at `A` are
`jumps κ (card n)`, and `∏ i, (X - ιℓ (ξ i ϖ))` kills `r(s)` at `A` in the sense of
`New.GaloisRep.PolyKillsAt`. 

### `GaloisRep.Attached.local_global_of_eigencharacter_of_pos`

 The case `k > 0` of `New.GaloisRep.Attached.local_global_of_eigencharacter`, with the `ξ i`
sorted at `x`. Let `r` be attached to the eigenform `f`, a pro-`p` Iwahori eigenvector for
`torusChar ξ` at the split place `w` (`star w ≠ w`). Let `A` lie above `w`, let `s⁻¹` act as the
`q ^ k`-th power map on the residue field of `A`, and let `x`, of order `k`, have the class of `s`
as local Artin symbol. Then `r` is of finite type at `A`: it is trivial on inertia near `1` if `ℓ`
is a unit at `A`, and it is potentially crystalline along every embedding inducing `A`. It also has
the jumps of `κ`, and `∏ i, (X - ιℓ (ξ i x))` kills `s` (that is, kills `r s` if `ℓ` is a unit at
`A`). 

### `GaloisRep.Attached.local_global_of_eigencharacter`

 Local-global compatibility at a split place with a sorted pro-`p` Iwahori eigencharacter. Let
`r` be attached to the eigenform `f`, which at the split place `w` is a pro-`p` Iwahori eigenvector
for `New.torusChar ξ`, with `‖ξ i ϖ‖` antitone in `i` for the uniformiser `ϖ = New.uniformizer w`.
Let `A` lie above `w`, let `s⁻¹` act as the `q ^ k`-th power map on the residue field of `A`, and
let `x`, of order `k`, have the class of `s` as local Artin symbol. Then (a) `r` is of finite type
at `A` (`New.GaloisRep.IsFiniteTypeAt`: trivial on inertia near `1` away from `ℓ`, potentially
crystalline above `ℓ`), (b) it has the Hodge–Tate jumps of `κ`, and (c)
`∏ i, (X - ιℓ (ξ i x))` kills `s` (`New.GaloisRep.PolyKillsAt`). Parts (a) and (b) do not involve
`s`, `x`, `k`; they stand here because one induction proves all three. Here `q = w.q` is the size
of the residue field at `w` and `ιℓ` is the fixed isomorphism of `ℂ` with `ℚ̄_ℓ`. 


## Frobenius and inertia for parahoric types

At a finite place `w ≠ w̄` of `E` not above `ℓ`, the action of `GL_N(E_w)`, with `N` the cardinality
of `n`, on a form `y` of an isotypic space `x` (`New.Patching.localFormRep`) is compared with the
Galois representation `x.galRep` attached to `x`. A place `A` of the algebraic closure above `w` is
fixed. `New.proIwahori` is the pro-`p` Iwahori subgroup and `ιℓ : ℂ ≃+* ℚ̄_ℓ`.


### `IsParahoricCompatible`

 `IsParahoricCompatible ρ z ϖ d F T` says that the matrices `F`, `T` behave as those of a
geometric Frobenius that comes from `ϖ` and of an inertia element, as seen by the vector `z` of `ρ`:
they commute, `T` is killed by every polynomial that vanishes at all `ιℓ (d i)`, and there are
characters `θ i`, with an exponent functional that is not zero on `z`, such that
`∏ i, (X - ιℓ (θ i ϖ * d i ^ b))` kills `F * T ^ b` for every natural number `b`. 

### `IsParahoricCompatible.aeval_inertia_eq_zero`

 Every polynomial that vanishes at all `ιℓ (d i)` kills `T`. 

### `IsParahoricCompatible.commute`

 `F` and `T` commute. 

### `IsParahoricCompatible.exists_characters`

 There are characters `θ i` such that some exponent `l` for the torus character of `θ`
  (`New.IsExponent`) is not zero on `z`, and `∏ i, (X - ιℓ (θ i ϖ * d i ^ b))` kills `F * T ^ b`
  for all `b`. 

### `isParahoricCompatible_galRep`

 Let `A` lie above `w ∤ ℓ`. Let the local Artin map send the uniformiser `ϖ` to `s`, the inverse
of a Frobenius element, and the unit `u` to the inertia element `τ`. Let `y ≠ 0` in the isotypic
space `x` be fixed by the pro-`p` Iwahori subgroup at `w`, let the parahoric subgroup with blocks
`f` act on `y` by scalars `c`, and write `d i` for the scalar of the diagonal matrix with `u` in
slot `i` and `1` elsewhere. Assume that slots with the same `d` lie in one block. Then the matrices
`F` of `s` and `T` of `τ` commute, and `T` is killed by every polynomial that vanishes at all
`ιℓ (d i)`. Also, there are characters `θ i` and an exponent for `New.torusChar θ` (a linear
functional as in `New.IsExponent`) that is not zero on `y`, such that
`∏ i, (X - ιℓ (θ i ϖ * d i ^ b))` kills `F * T ^ b` for every natural number `b`
(`New.Patching.IsParahoricCompatible`). 

### `mul_sub_one_eq_smul_sub_one`

 Let `F` and `T` commute, let `T` be semisimple with eigenvalues among `d 0, 1, …, 1`, where
`d 0 ≠ 0` and `d 0 ^ N ! ≠ 1`, and let `∏ i, (X - α i * d i ^ b)` kill `F * T ^ b` for every `b`,
with all `α i ≠ 0`. Then `F * (T - 1) = α 0 • (T - 1)`: `F` is the scalar `α 0` on the image of
`T - 1`. 

### `hecke_eq_frob_on_parahoricEigenspace`

 Let `A` lie above `w ∤ ℓ`. Let the local Artin map send the uniformiser `ϖ` to `s`, the inverse
of a Frobenius element, and the unit `u` to the inertia element `τ`. Let `y` in the isotypic space
`x` be fixed by the pro-`p` Iwahori subgroup at `w`, and let the stabiliser in `GL_N(𝒪_w)` of the
first coordinate line modulo `w` act on `y` by `χ` of the top left entry
(`New.Patching.parahoricEigenspace`), where `χ u ≠ 0` and `χ u ^ (card n)! ≠ 1`. Let `U` be the
Hecke operator of `diag (ϖ, 1, …, 1)`, `F` the matrix of `s` and `T` that of `τ` minus `1`. Then
`tr (T M) • G(U) y = tr (G(F) T M) • y` through `ιℓ`, for every complex polynomial `G` and every
matrix `M`: `U` acts like `F` on the image of `T`. 
