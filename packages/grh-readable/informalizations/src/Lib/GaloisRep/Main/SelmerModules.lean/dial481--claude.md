---
{
  "module": "src/Lib/GaloisRep/Main/SelmerModules.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Main/SelmerModules.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Main/SelmerModules.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Selmer modules, Tate twists, components of cocycles and places above a prime

`E` is a CM field and `Ω ⊇ E` is an algebraic closure of `ℚ`. The class `New.CMFieldWithRoot5040`
bundles these hypotheses on `E` with a primitive root of unity of order `5040`. Linear conditions on
functions `Gal(Ω/E) → n → B` are sets of relations, and `New.obeying R B` is the module of functions
that obey all of `R`. Over `ℚ` we define modules of cocycles for the inverses of characters
`Υ = cyc ^ e * ψ`, into which Selmer groups over cyclotomic fields decompose, and we prove basic
facts on places of `Ω` above a rational prime for use with Gauss sums.

## Main definitions and results

* `New.IsFromU1`: Galois characters that come from idele class characters through `x ↦ x / x̄`.
* `New.selmerModule`: locally constant cocycles, unramified outside `S`, that obey the relations
  `L`.
* `New.Selmer.tateTwist`, `New.Selmer.shaOdd`: the Tate twist `Λ(-e)` and a module of cocycles that
  for `e ≠ 0` describes the odd part of `Ш¹`.
* `New.cyclotomicPowDirichlet l e ψ`: the character of `Gal(Ω/ℚ)` with values in `Oˣ` that is the
  `e`-th power of the `l`-adic cyclotomic character times the Dirichlet character `ψ` modulo `N`.
  The latter is read through the action on `N`-th roots of unity.
* `New.OddPart.component l e ψ ν`: the component for `Υ = cyc ^ e * ψ`, with values in `O / l ^ ν`.

Notions from other files:
* `New.cyclotomicChar`, `New.cyclotomicCharIn Λ`: the `ℓ`-adic cyclotomic character `cyc`, with
  values in `ℤ_[ℓ]ˣ` and in `Λˣ`.
* `New.cycloGalGroup`: The subgroup of Gal(ℚ̄/ℚ) fixing all N-th roots of unity: the absolute Galois
  group of ℚ(ζ_N).
* `New.IsPlaceOver`: The valuation subring A of Ω lies over the prime w of E: an integer of E is in
  the maximal ideal of A exactly when it lies in w.
* `Set.conjClosure`: The set S ∪ S̄ of the finite places in S and their complex conjugates.

## Relation to the literature

Known; see `Lib.Cyclotomic.OddSha`, `Lib.ClassField.Global.CMSplittingCharacters`,
`Lib.Cyclotomic.Kolyvagin.ReciprocityComponentBounds`,
`Lib.ClassField.GaloisCohomology.KummerCyclicClasses` and `Lib.ClassField.Places.LocalFields` for
sources.



## Selmer modules, Tate twists and the odd part of Ш

* `New.cmConj`, `New.conjGal`: a chosen complex conjugation `c` and the map `g ↦ c g c`.


### `CMFieldWithRoot5040`

 `E` is a CM number field with an embedding into the algebraic closure `Ω` of `ℚ`, and it
contains a primitive root of unity of order `7! = 5040` (`New.HasPrimitiveRoot5040`). 

 ### Valuation, places and complex conjugation 

### `ellVal`

 The valuation −log_ℓ|x| in [0, ∞], normalised by v(ℓ) = 1; it is ∞ at 0, and 0 for |x| ≥ 1. 

### `cmConj`

 A chosen complex conjugation `c` in Gal(Ω/ℚ). 

### `isComplexConj_cmConj`

 Here `Ω` is the fixed algebraic closure of ℚ into which `E` is embedded, and `cmConj` is the
chosen element of Gal(Ω/ℚ). The lemma says `cmConj` is a complex conjugation: for some embedding
`j : Ω → ℂ`, `j (cmConj x)` is the complex conjugate of `j x` for all `x`. 

### `placesDividing`

 For a natural number N, the set of finite places of E whose prime ideal contains N. 

### `instance : Fintype (placesDividing E ℓ)`

 Only finitely many places of `E` divide the prime `ℓ`. 

### `cmConj_cmConj`

 The chosen complex conjugation `cmConj` of `Ω` is an involution. 

### `cmConj_algebraMap`

 On the CM field `E ⊆ Ω`, the chosen complex conjugation `cmConj` of `Ω` restricts to the complex
conjugation `star` of `E`. 

### `conjGal`

 The endomorphism `g ↦ c g c` of `Gal(Ω/E)`, where `c` is the chosen complex conjugation
`New.cmConj`. 

 ### Characters that come from the norm-one torus 

### `IsFromU1`

 The Galois character `χ` comes from the norm-one torus: `χ(Art x) = η(x / x̄)` for an idele
class character `η` of modulus `I` that is trivial on the local components at `S ∪ S̄`. Here `S`
and `I` are sets of finite places of `E`, `S ∪ S̄` is `Set.conjClosure S`, `x̄` is `star x` and
`Art` is the Artin map `New.artinMap`. 

### `IsFromU1.isLocallyConstant`

 `χ` is locally constant. 

### `IsFromU1.exists_ideleChar`

 `χ(Art x) = η(x / x̄)` for a character `η` of the finite ideles that is trivial on `Eˣ` and on
  the ideles that are units off `S ∪ S̄` and `≡ 1` at the places of `I` off `S ∪ S̄`. 

 ### Twists and Selmer modules 

### `twistRep`

 Given a ring map e:O→O', a character ψ:G→O' and a matrix representation ρ over O, the
representation g ↦ ψ(g)·e(ρ(g)) over O'. 

### `locConst`

 The O-submodule of functions from a topological space G to an O-module B consisting of the
locally constant functions. 

### `selmerModule`

 The Selmer module: locally constant cocycles for ρ with values in B^n, unramified outside S
(zero on the inertia groups above the other places) and obeying the relations L. 

 ### Tate twists and the odd part of Ш 

### `cyclotomicInv`

 The inverse of the ℓ-adic cyclotomic character of Gal(Ω/E), with values in the ℤ_ℓ-algebra
Λ. 

### `tateTwist`

 The rank-one representation `Λ(-e)`: the `e`-th power of the inverse cyclotomic character
`cyclotomicInv`, written as `1 × 1` matrices (indexed by `Unit`). 

### `tateTwist_apply`

 The single entry of the matrix `tateTwist ℓ E Λ e g` is `cyclotomicInv ℓ E Λ g ^ e`. 

### `shaLocalSet`

 The elements of `Gal(Ω/E)` on which the local condition above `ℓ` is imposed. For `e = 0` they
form the union of the inertia groups at the places `A` of `Ω` above `ℓ`. For `e ≠ 0` they are the
elements of the decomposition groups at these places with trivial cyclotomic character. 

### `shaOdd`

 The module that for `e ≠ 0` describes the odd part of `Ш¹(E, Λ/ℓ^ν(-e))`: the functions `z` on
`Gal(Ω/E)` (with values vectors of length one) such that `z` vanishes on `shaLocalSet ℓ E e`, `z`
is odd under `conjGal` if `e ≠ 0`, and `z` is a continuous cocycle for `Λ(-e)` unramified outside
`ℓ`. For `e = 0` these are the continuous homomorphisms that are unramified everywhere. 

### `mem_shaOdd`

 `z` lies in `shaOdd ℓ E Λ e ν` exactly when `z` vanishes on `shaLocalSet ℓ E e`, `z` is odd
under `conjGal` if `e ≠ 0`, and `z` lies in the Selmer module of `Λ(-e)` unramified outside the
places above `ℓ`, with no further relations. Here `shaLocalSet` holds the local elements above `ℓ`,
`conjGal g = c g c` for complex conjugation `c`, and `QuotSpan a` is the quotient by `a`. 


## Locally constant cocycles and the components for `Υ = cyc ^ e * ψ`

* `New.OddPart.inertiaOff N l T`: inertia over `ℚ(μ_N)` at the places above neither `l` nor a prime
  of `T`.


### `_root_.New.cyclotomicPowDirichlet`

 The character Υ = cyc^e·ψ of Gal(ℚ̄/ℚ) with values in O^×, for a prime `l`, a `ℤ_l`-algebra `O`
and a Dirichlet character `ψ` modulo `N` with values in `O`: cyc is the l-adic cyclotomic
character, and ψ is read through the action on N-th roots of unity. 

### `vanishingCocycles`

 The O-module of locally constant maps x : Gal(Ω/ℚ) → B with x(gh) = x(g) + χ(g)x(h) (cocycles
for the character χ) that vanish on the set s. 

### `inertiaOff`

 The elements of Gal(Ω/ℚ(μ_N)) lying in the inertia group of some place above neither l nor
any prime of T. 

### `component`

 The component attached to the character `Υ = cyc ^ e * ψ` (`New.cyclotomicPowDirichlet l e ψ`).
It consists of the locally constant cocycles for `Υ⁻¹` on the absolute Galois group of `ℚ`, with
values in `O / l ^ ν`. They vanish at `New.cmConj` and at the elements of `New.cycloGalGroup N` that
lie in an inertia group at a place prime to `l` or in `New.Selmer.shaLocalSet l ℚ 1`. 


## Places of ℚ̄ above a rational prime

Places are valuation subrings `B`, and `B.valuation q < 1` says that `B` lies above `q`.


### `galUnitsRep`

 The action of `Gal(Ω/ℚ)` on `Ω^×`, written additively. 

### `principalUnits`

 The principal units of the valuation subring B of ℚ̄ (elements congruent to 1 modulo its
maximal ideal), as a subgroup of ℚ̄^× written additively. 

### `exists_isPlaceOver_prime`

 Let `B` be a place of `Ω` above the prime `q`, that is, `q` is not a unit at `B`. Then `B` lies
over a finite place `v` of `ℚ` (`IsPlaceOver B v`) of norm `v.q = q`, and `q`, written
`DiscreteUnits.ofNeZero q _` in the additive group `Ωˣ`, has order one at `B`, for the order
`ordRat ℚ B` normalised on `ℚ`. 

### `decompGroup_le_cycloGalGroup`

 Let `B` be a place of `Ω` above the prime `q` (`q` is not a unit at `B`), and let
`q ≡ 1` mod `m`. Then the decomposition group of `B` in `Gal(Ω/ℚ)` fixes the `m`-th roots of unity:
it lies in `cycloGalGroup m`, the kernel of the cyclotomic character modulo `m`. 
