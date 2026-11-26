---
{
  "module": "src/Lib/GaloisRep/Main/AllRanks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Main/AllRanks.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Main/AllRanks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Isotypic spaces of eigenforms and attached Galois representations in every positive rank

This file treats algebraic modular forms on a definite unitary group and their attached Galois
representations. The statement `New.GaloisRep.SphericalCompat` asserts the existence of an attached
Galois representation and local–global compatibility at a place where the form is spherical.

## Overview of this theory

Let `ℓ` be a prime and `ι : ℂ ≃ ℚ̄_ℓ` a fixed isomorphism. Let `E` be a CM field with `New.WeilData`
(auxiliary adelic data). Let `f` be an eigenform of weight `κ`, with Hecke polynomials `P w` at
finite places `w`, on the unitary group of the standard definite hermitian space of rank `n ≥ 1`. A
continuous `r : Gal(Ω/E) → GL_n(ℚ̄_ℓ)` with non-degenerate trace form is `New.GaloisRep.Attached` to
`P` if, for each `ε > 0`, `det (X - r s)` is coefficientwise within `ε` of `ι(P w)` for most
Frobenii `s` at places `w` (`New.mostFrobenii`).

* `New.GaloisRep.sphericalCompat_std`: such an `r` exists. If `f` has maximal level at `w`, every
  such `r` is unramified or crystalline above `w`, with the Hodge–Tate jumps of `κ`; for split `w`
  the Hecke polynomial kills geometric Frobenius. `New.GaloisRep.Attached.trace_eq`: `P` determines
  `tr r`.
* `New.GaloisRep.Attached.local_global_of_eigencharacter`: let `w` be split (`w̄ ≠ w`) and `A` a
  place above it. Let `f` be a pro-`p` Iwahori eigenvector (`p` below `w`) with character
  `ξ = (ξᵢ)`, where `‖ξᵢ(ϖ)‖` is non-increasing for the uniformiser `ϖ`. Then `r` is of finite type
  at `A` (`New.GaloisRep.IsFiniteTypeAt`) and has the jumps of `κ`. Also `∏ (X - ι ξᵢ(x))` kills, in
  the sense of `New.GaloisRep.PolyKillsAt`, each `s` in the decomposition group with `s⁻¹` the
  `q^k`-th power on the residue field (`q` the residue cardinality, `k ≥ 0`). Here `x ∈ E_wˣ` has
  order `k` and local Artin symbol the class of `s`.
* `New.GaloisRep.Attached.isLabelledAt`: the first two conclusions also hold if `f` has a
  `New.HasProductLabel` at `w`. Then a polynomial built from the values of the label's tame
  characters kills each element of inertia, in the same sense.

These replace base change to `GL_n` (Labesse), Galois representations with local–global
compatibility (Shin, Chenevier–Harris, Barnet-Lamb–Gee–Geraghty–Taylor) and the local Langlands
correspondence. Local polynomials kill but need not be characteristic. No Weil–Deligne
representation is built.

Plan. `Lib.Shimura`: models of signature `(1, n - 1)`, the congruence relation and, for odd `n`,
eigenvalues of forms with a cuspidal type in cohomology. `Lib.Cohomology`: base change, fixed point
formula. `Lib.PadicComparison`: cohomology above `ℓ` is crystalline; Hodge classes give jumps.
`Main.SeedRepresentation` cuts it to rank `n` by `KillingPolynomials`. `Main.OddRank`: all forms by
`ℓ`-adic limits (`WeightCongruence`, `Pseudocharacter`, `Lib.PadicHodge.Limit`), then fields with
Weil data by `Main.QuadraticStep` and `BaseChange`. `Main.ThetaLift`, `Main.AllRanks`: two lifts to
rank `2n + 1`, then cancel characters. `LocalGlobal`: tame base change down to the spherical case.

## Main definitions and results

* `New.GaloisRep.sphericalCompat_std`: `New.GaloisRep.SphericalCompat` holds in every positive rank
  n. The proof lifts the eigenform to the odd rank 2n + 1 along two different characters and cancels
  the n + 1 extra characters from each of the two representations.
* `New.Patching.eigenformsAt`: forms spherical at `w` with given eigenvalues (no condition if `w` is
  not split).
* `New.Patching.Isotypic`: the isotypic spaces, each the `liminf` of the `New.Patching.eigenformsAt`
  over the places. They are kept by operators supported at one place
  (`New.Patching.Isotypic.map_mem`).
* `New.Patching.Isotypic.iSupIndep_val`: the isotypic spaces are independent.
* `New.Patching.Isotypic.galRep`, `New.Patching.Isotypic.attached_galRep`: a chosen Galois
  representation of an isotypic space, attached to its Hecke polynomials when the space is nonzero
  (`New.Patching.Isotypic.exists_attached`, `New.Patching.Isotypic.attached_galRep_of_exists`).

Notions from other files:
* `New.WeilData`: Weil data on a stably unramified E: ȷ in E with ȷ = −ȷ̄, Im τȷ > 0 for every τ in
  the CM type and (1 − ȷ⁻¹)/2 integral; a finite idele α for which the completed integers Ô are
  self-dual under (z, u) ↦ ψ_f(ȷαᾱzu); and a splitting character υ equal to −1 at uniformisers of
  the places w with w = w̄.
* `New.AutChar.HasWeight μ e ψ`: the character μ of U(1)(𝔸) has weight e and tame part ψ, that is
  μ(u) = ∏_v u_v^{e(v)} · ∏_w ψ_w(u mod w) when u has integral finite part. From it,
  `HasWeight.toAlgebraic k j` is the algebraic Hecke character μ(x/x̄) υ(x)^{−k} |x|^{j−k/2}, and
  `New.heckeCoeff χ ∅ w` is the value of a Hecke character χ at the chosen uniformiser of w.
* `New.IsTraceNondeg r`: the trace form on the span of the image of r is non-degenerate.
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with xᴴJx
  equal to the diagonal matrix of its signs at the infinite places and 1 at the finite places.

## Relation to the literature

Known; see `Lib.GaloisRep.Main.OddRank`, `Lib.ClassField.Global.CMSplittingCharacters` and
`Lib.Adelic.AutomorphicForms.SmoothAlgebraicForms` for sources.



## Attached Galois representations in every positive rank

The local clauses are `New.GaloisRep.IsGoodAt` (unramified or crystalline),
`New.GaloisRep.HasJumpsAt` (Hodge–Tate jumps) and `New.GaloisRep.PolyKillsAt` (a polynomial kills a
Weil element: `P(r s) = 0` if ℓ is a unit at `A`, else `P` kills the Weil pairs of `s` along each
local datum at `A`). `New.mostFrobenii` is the filter of most Frobenii of degree one; a
`FrobeniusDatum` `y` gives a place `y.place` and a Frobenius element `y.frob` at it, and
`mostFrobeniiAt E g` also lets `y.frob` tend to `g`.


### `New.AlgHeckeChar.heckeChar`

 The character of the finite ideles of an algebraic Hecke character `ω = (θ, n)`: its first
component `θ`. 

### `New.AutChar.exists_pair_heckeCoeff_ne`

 Let `E` be a CM field with Weil data, including a splitting character `υ`, and let `e` assign an
integer to each infinite place. Then there are two characters `μ 0`, `μ 1` of `U(1)(𝔸)` (norm-one
adeles, trivial on `E`) with trivial tame part and weights `c 0`, `c 1` such that: (a) `c i ≤ e` at
every infinite place; and (b) for all integers `k`, `j`, `j'` and every split finite place `w`, the
algebraic Hecke characters `toAlgebraic k j` from `μ 0` and `toAlgebraic k j'` from `μ 1` take
different values at the uniformiser of `w`. Here `toAlgebraic k j` from `μ` is
`x ↦ μ(x/x̄) υ(x)^{−k} |x|^{j−k/2}`. 

### `New.GaloisRep.isGoodAt_hasJumpsAt_of_trace_eq_sub`

 Let `r` be continuous with non-degenerate trace form, and let its trace be that of `ρ` minus the
traces of the one-dimensional representations `χ l`. Let `ρ` and every `χ l` be continuous and
unramified or crystalline at `A`, with jumps `J + ∑ l, j l` for `ρ` and `j l` for `χ l`. Then `r` is
unramified or crystalline at `A` and has the jumps `J`. Moreover, every polynomial `P` that kills
`s` at `A` for `ρ` and for every `χ l` kills it for `r` (`PolyKillsAt`: `P(r s) = 0` if ℓ is a unit
at `A`, and otherwise `P` kills the Weil pairs of `s` along each local datum at `A`). 

### `New.GaloisRep.PolyKillsAt.add`

 If `P` and `Q` kill `s` for `r` at `A`, so does `P + Q`. 

### `New.GaloisRep.PolyKillsAt.of_mul_of_isCoprime`

 If `P * a` and `P * b` kill `s` for `r` at `A`, and `a` and `b` are coprime, then `P` kills
`s`. 

### `New.GaloisRep.Attached.tendsto_trace_sub`

 Let `ρ`, of rank `card n + card T`, be attached to the polynomials `P w * ∏ l, (X - c l w)`.
Suppose that at most Frobenii `P w` is monic of degree `card n` (`hP_monic`) and `ιℓ (c l w)` is the
value of the continuous character `ψ l` at the Frobenius element (`hψ_val`). Along Frobenii
tending to `g`, minus the coefficient of degree `card n - 1` of `P w` (the sum of its roots) tends
to `tr ρ g - ∑ l, ψ l g`. 

### `New.GaloisRep.Attached.of_trace_sub`

 Let `ρ` be attached to `P * R`, where at most Frobenii `ιℓ (R w)` is `∏ l, (X - ψ l s)`, with
`s` the Frobenius element and `ψ l` continuous characters. A representation `r` with
non-degenerate trace form and trace `tr ρ - ∑ l, ψ l` is attached to `P`. 

### `New.GaloisRep.Attached.exists_attached_of_mul_prod`

 Let `ρ 0`, `ρ 1` be attached to the polynomials `P w * ∏ l, (X - c i l w)`. Suppose that at most
Frobenii `P w` is monic of degree `card n` (`hP_monic`) and `ιℓ (c i l w)` is the value of the
continuous character `ψ i l` at the Frobenius element (`hψ_val`), and that no `ψ 0 l` equals a
`ψ 1 l'`. Then some representation of rank `card n` is attached to `P`, and every representation
`r` attached to `P` has trace `tr ρ i - ∑ l, ψ i l` for both `i`. 

### `New.GaloisRep.Attached.twistByChar_of_scaleRoots_eq`

 Let `σ` be attached to `Q` and let `ν` be a continuous character. Suppose that at most Frobenii
`ν` takes the value `ιℓ (z w)`, `Q w` is monic of degree `card m`, and `Q w` with its roots
multiplied by `z w` is `P w`. Then the twist of `σ` by `ν` is attached to `P`. 

### `New.GaloisRep.exists_attached_mul_prod_X_sub_C`

 Let `μ` be a character of `U(1)(𝔸)` with trivial tame part and weight `c ≤ κ.2`, and let `f` be
an eigenform of weight `κ` on the standard definite space of rank `card n`, with Hecke polynomials
`P`. Let `t > card n` with `card n + t` odd, and let `R v` be the product of the `X - z`, where `z`
runs over the values at the uniformiser of `v` of the `t` characters
`toAlgebraic (card n + t) (t - l)` made from `μ`. Some `ρ` of rank `card n + t` is attached to
`P * R`; and if `f` is spherical at `w`, then at every place `A` of `Ω` over `w`, `ρ` is unramified
or crystalline, has the jumps of `κ` in rank `card n` together with those of the `t` characters,
and for split `w`, where `f` has Hecke polynomial `Pw`, `ιℓ (Pw * R w)` kills every geometric
Frobenius element. 

### `New.GaloisRep.sphericalCompat_std`

 Let `E` be a CM field with Weil data (a primitive 5040th root of unity, an element ȷ, an idele α
and a splitting character υ), and let `n` be nonempty. Then `SphericalCompat E n (card n) w` holds:
for every eigenform `f` of weight `κ` on the standard definite unitary space of rank `card n`, with
Hecke polynomials `P`, some representation is attached to `P`. If `f` is spherical at `w` (fixed by
`K_w`), every representation attached to `P` satisfies `IsCompatibleAt` at each place of `Ω` over
`w`: it is unramified or crystalline there, has the jumps of `κ` in rank `card n`, and, if `w` is
split, `ιℓ` of the Hecke polynomial kills every geometric Frobenius.

A weak analogue of the Galois representations attached to conjugate self-dual cohomological cuspidal
representations of GL_n (Shin, Chenevier–Harris, Barnet-Lamb–Gee–Geraghty–Taylor): forms on definite
U(n), given Weil data, with local compatibility only at spherical places. 


## Isotypic spaces of eigenforms and their Galois representations

Decomposition of algebraic modular forms on a definite unitary group by their Hecke eigenvalues at
almost all places. `V.forms κ` is the space of forms of weight `κ`, `V.formTranslation κ` the action
of the finite adelic group on it by right translation, and `New.heckeSplit` the Hecke operator
`T_{w,j}` at a split place `w`.


### `EllAdicIntegers`

 The valuation ring of `ℚ̄_ℓ`, as a new type. 

### `instance : Algebra EllAdicIntegers ℂ`

 `EllAdicIntegers` maps to `ℂ` by the inverse of the fixed isomorphism `ιℓ : ℂ ≃ ℚ̄_ℓ`. 

### `iota_ell_algebraMap`

 The isomorphism `ιℓ` takes the image in `ℂ` of an element of `EllAdicIntegers` to its image in
`ℚ̄_ℓ`. 

### `endPreserving`

 The `New.Patching.EllAdicIntegers`-algebra of complex-linear endomorphisms of W that map the
submodule M into itself. 

 ### Local eigenspaces and isotypic spaces 

### `localGroupAlgebra`

 The `New.Patching.EllAdicIntegers`-algebra of operators on forms generated by the right
translations by elements of G_f supported at w and w̄. 

### `eigenformsAt`

 The forms that, if `w` is split, are fixed by `maxCompactAt n w` and have `T_{w,j} f = t j • f`
for all `j`; all forms if `w` is not split. 

### `Isotypic`

 Isotypic spaces. For a system `t` of eigenvalues at all places, take the space (possibly zero)
of forms that lie in `eigenformsAt V κ w (t w)` for all but finitely many `w`; `Isotypic V κ` is
the type of all these spaces. For `x : Isotypic V κ`, `x.val` is the space and
`x.heckeEigenvalues` a system that defines it. 

### `Isotypic.exists_heckeEigenvalues`

 An isotypic space `x` is cut out by some system `t` of Hecke eigenvalues: a form lies in `x`
exactly when it lies in `eigenformsAt V κ w (t w)` at all but finitely many places `w`. 

### `Isotypic.heckeEigenvalues`

 A chosen system of Hecke eigenvalues, one sequence for each finite place, whose isotypic
space is x (`Isotypic.exists_heckeEigenvalues`). 

### `Isotypic.heckePolyAt`

 The Hecke polynomial `heckePoly w.q (card n)` of the chosen eigenvalues of the isotypic space x
at w. 

### `Isotypic.galRep`

 A chosen representation `Gal(Ω/E) → GL_n(ℚ̄_ℓ)` attached to the Hecke polynomials of the
isotypic space x; arbitrary if none exists. 

### `commute_of_mem_localGroupAlgebra`

 The translation by an element `y` of `G_f` that is trivial at `w` commutes with every operator
`a` in the algebra generated by the translations supported at `w` and `w̄`. 

### `heckeFun_mem_localGroupAlgebra`

 Let `w` be split and let `θ` map a group `G` to `GL_n` of the local field at `w`. For a
subgroup `K` and a set `s` of `G`, the Hecke operator of the indicator of `s`, for the translations
through `θ` and `ofSplitPlace hw`, lies in the algebra `localGroupAlgebra w`. 

### `hasHeckePolyAt_of_mem_eigenformsAt`

 A form in `eigenformsAt V κ w t`, for a split place `w`, has the Hecke polynomial
`heckePoly w.q (card n) t` at `w`. 

### `Isotypic.mem_iff_eventually`

 A form lies in the isotypic space `x` exactly when, at all but finitely many places `w`, it lies
in `eigenformsAt V κ w` for the chosen eigenvalues `x.heckeEigenvalues w`. 

### `Isotypic.map_mem`

 An operator `a` in `localGroupAlgebra v`, the algebra generated by the translations supported at
one place `v` and its conjugate, maps the isotypic space `x` into itself. 

### `Isotypic.isEigenform`

 A nonzero form `f` in the isotypic space `x` is an eigenform for the Hecke polynomials
`x.heckePolyAt`. The hypothesis `HasPrimitiveRoot5040 E` (`E` contains a primitive 5040th root of
unity) makes every place of prime norm split. 

### `exists_isotypic_of_isSphericalOff`

 A nonzero form of maximal level off `S` that has Hecke polynomial `P w` at every split `w` with
`w, w̄ ∉ S` lies in some isotypic space. 

 ### Independence and the attached Galois representation 

### `Isotypic.iSupIndep_val`

 Let `s` be a set of isotypic subspaces of `V.forms κ`, where an isotypic subspace is one given
by a system of Hecke eigenvalues at all finite places: it consists of the forms that are eigenforms
with those eigenvalues at all but finitely many places. Then these subspaces are independent, so
their sum is direct. 

### `Isotypic.attached_galRep_of_exists`

 If some representation is attached to the Hecke polynomials of the isotypic space `x`, then
the chosen `x.galRep` is attached to them. 

### `Isotypic.exists_attached`

 If the isotypic space `x` on the standard definite space `V` holds a form `f ≠ 0`, then some
Galois representation is attached to the Hecke polynomials of `x`. Here `Ω` is the algebraic
closure of `ℚ`, an `E`-algebra, and a representation is a homomorphism `Gal(Ω/E) → GL_n(ℚ̄_ℓ)`. 

### `Isotypic.attached_galRep`

 If the isotypic space `x` on the standard definite space `V` holds a form `f ≠ 0`, then
`x.galRep` is attached to its Hecke polynomials. 
