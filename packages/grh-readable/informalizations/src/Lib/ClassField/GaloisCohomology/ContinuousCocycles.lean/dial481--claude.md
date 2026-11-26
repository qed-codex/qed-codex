---
{
  "module": "src/Lib/ClassField/GaloisCohomology/ContinuousCocycles.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/GaloisCohomology/ContinuousCocycles.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/GaloisCohomology/ContinuousCocycles.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Continuous cohomology of discrete modules: cocycles, H², cyclic classes, local Artin map

This file builds the part of continuous group cohomology used in this library, using explicit
cochains. It works with a representation `ρ` of a topological group `G` on a discrete `R`-module
`M`, and with discrete modules `New.DiscreteModule R Γ`. It also defines the cyclic class of a
character into `ℚ/ℤ` and an invariant, and the basic objects of local class field theory, where `Γ`
is a Galois group of `Ω` over `K`. It then treats restriction and short exact sequences of discrete
modules, and counts continuous 1-cocycles along exact sequences.

## Main definitions and results

* `New.Z2`, `New.B2`, `New.H2`: continuous 2-cocycles, coboundaries and their quotient.
* `New.QZ`, `New.QZ.carry`, `New.QZChar`: the discrete group `ℚ/ℤ`, the carry of two representatives
  in `[0, 1)`, and continuous characters into `ℚ/ℤ`.
* `New.cyclicClass`: the class of `(g, h) ↦ carry (χ g) (χ h) • w`, additive in `χ` and in `w`.
* `New.IsClassOfInvariant`, `New.Cohomology.classOfInvariant`: the map from `ℚ/ℤ` to `H²(Γ, Ωˣ)`
  normalised on unramified cyclic classes.
* `New.IsLocalArtin`, `New.localArtin`, `New.placeOver`: the local Artin map, defined by duality
  with the cyclic classes `New.cyclicClass`, its version on the completion of a number field at a
  prime, and a chosen place over that prime.
* `New.DiscreteModule R Γ`: a discrete `R`-module with a continuous `R`-linear action of `Γ`.

Notions from other files:
* `New.DiscreteUnits Ω`: the group `Ωˣ` written additively, with the discrete topology;
  `New.unitsRep` is the action of `Γ` on it.
* `New.IsFrob A q σ`: `σ` stabilises `A` and `σ • x ≡ x ^ q` modulo the maximal ideal of `A`;
  `New.inertiaGroup Γ A` is the case `q = 1`.
* `New.IsPlaceOver A v`: the valuation subring `A` of `Ω` lies over the prime `v` of the number
  field `K`: an integer of `K` lies in the maximal ideal of `A` exactly when it lies in `v`.

## Relation to the literature

Known; see `Lib.ClassField.GaloisCohomology.KummerCyclicClasses`, `Lib.ClassField.Local.ArtinMap`,
`Lib.ClassField.Places.LocalFields` and `Lib.ClassField.LocalDuality.CrystallineDuality` for
sources.



## Continuous cocycles, H² and compatible pairs

Cochains are functions `G → M` and `G × G → M` (inhomogeneous cochains).

* `New.actionRep`, `New.charRep`: the representation given by a homomorphism into a monoid acting on
  `M`, and the one in which a character `G → Rˣ` acts by scalars.


### `instance (priority`

 On a discrete module, scalar multiplication by each constant of `R` is continuous. 

### `Z1`

 The continuous 1-cocycles of `ρ`: the `R`-submodule of continuous `f : G → M` with
`f (g * h) = f g + ρ g (f h)`. 

### `coboundaryMap`

 The coboundary map in degree 0: the `R`-linear map from `M` to functions `G → M` sending `m`
to `g ↦ ρ g m - m`. 

### `Z2`

 The continuous 2-cocycles of `ρ`: continuous `f : G × G → M` with
`f (g * h, k) = f (g, h * k) - f (g, h) + ρ g (f (h, k))`. 

### `B2`

 The 2-coboundaries of `ρ`: the functions `(g, h) ↦ ρ g (c h) - c (g * h) + c g` on `G × G`, for
continuous `c : G → M`. 

### `H2`

 Continuous cohomology `H²(G, M)`: the continuous 2-cocycles of `ρ` modulo the coboundaries of
continuous 1-cochains `G → M`. 

 ### Maps induced by a compatible pair 

### `pairMapZ1`

 For a continuous homomorphism `φ : H →ₜ* G` and an `R`-linear `u : M → N` with
`u (ρ (φ g) m) = ρ' g (u m)` (the hypothesis `h`, proved by `bound` when it is not
given), the additive map `f ↦ u ∘ f ∘ φ` from continuous 1-cocycles of `ρ` to those of `ρ'`. 

### `pairMapH2`

 The linear map `H²(G, M) → H²(H, N)` induced by a continuous homomorphism `φ : H →ₜ* G` and an
`R`-linear `u : M → N` with `u (ρ (φ g) m) = ρ' g (u m)` (the hypothesis `h`, proved by
`bound` when it is not given): the class of `f` goes to the class of
`(g, g') ↦ u (f (φ g, φ g'))`. 

 ### Representations given by a homomorphism 

### `actionRep`

 The `R`-linear representation of a monoid `G` on `M` obtained from a homomorphism `χ : G →* S`
into a monoid `S` acting `R`-linearly on `M`: `g` acts as `χ g`. 

### `charRep`

 For an `R`-module `M` and a character `χ : G →* Rˣ`, the representation of `G` on `M` in which
`g` acts as the scalar `χ g`. 


## Characters into ℚ/ℤ and the cyclic class of (χ, w)

Symbols in the second cohomology: for a character `χ` and an invariant `w`, the class of the cocycle
`(g, h) ↦ carry (χ g) (χ h) • w`. This class is defined directly by this cocycle; it is the cup
product of `w` with the image `δχ` of `χ` under the connecting map of `0 → ℤ → ℚ → ℚ/ℤ → 0`. This
identification is not proved here, and nothing in this file uses it.

* `New.QZ`: the discrete group `ℚ/ℤ`; `New.QZ.fracRep`: the representative in `[0, 1)`.
* `New.QZ.carry`: the integer `fracRep a + fracRep b - fracRep (a + b)` (`New.QZ.cast_carry`), which
  is 0 or 1 since both representatives lie in `[0, 1)`.


### `QZ`

 The group ℚ/ℤ; it is given the discrete topology. 

### `instance : TopologicalSpace QZ`

 `ℚ/ℤ` carries the discrete topology. 

### `QZ.mk`

 The quotient homomorphism ℚ → ℚ/ℤ. 

### `QZ.fracRep`

 For a class `a` in `ℚ/ℤ`, its unique rational representative in the interval `[0, 1)`. 

### `QZ.carry`

 For `a`, `b` in `ℚ/ℤ`, the integer part `⌊fracRep a + fracRep b⌋` of the sum of their
representatives in `[0, 1)`; it is `0` or `1`, as both representatives lie in `[0, 1)`. 

### `QZ.fracRep_mk`

 The representative in `[0, 1)` of the class of a rational `r` is its fractional part. 

### `QZ.cast_carry`

 The carry measures how far the representative in `[0, 1)` is from being additive:
`carry a b = fracRep a + fracRep b - fracRep (a + b)` in `ℚ`. 

### `QZ.carry_add_add_carry`

 The carry is a 2-cocycle of `ℚ/ℤ` with values in `ℤ`:
`carry (a + b) c + carry a b = carry a (b + c) + carry b c`. 

### `QZChar`

 Continuous characters `G → ℚ/ℤ`: the continuous 1-cocycles for the trivial action. 

### `QZChar.apply_mul`

 A continuous character `χ : G → ℚ/ℤ` turns products into sums. 

### `carry_smul_mem_Z2`

 For a continuous character `χ : G → ℚ/ℤ` and an invariant `w` of `ρ`, the function
`(g, h) ↦ carry (χ g) (χ h) • w` on `G × G` is a continuous 2-cocycle of `ρ`. 

### `cyclicClass`

 The class in `H²(G, M)` of the cocycle `(g, h) ↦ carry (χ g) (χ h) • w`, additive in the
continuous character `χ : G → ℚ/ℤ` and in the invariant `w` of `ρ`. 


## Definitions for local class field theory

`A` is a valuation subring of `Ω`. `A.valuation` is multiplicative and below `1` on the maximal
ideal.

Several objects are chosen by `epsilon` from their characteristic property. `New.DiscreteUnits Ω` is
`Ωˣ` written additively, with the action `New.unitsRep`.


### `IsUniformiser`

 `π` is a uniformiser of `K` for `A`: an element `x` of `K` lies in the maximal ideal of `A`
exactly when its valuation is at most that of `π`. Here `valuationVia K A x` is the valuation of
`A` at the image of `x` in `Ω`. 

### `fixedFieldOf`

 For a subgroup `H` of `Γ`, the intermediate field of `Ω / K` of the elements fixed by `H`. 

### `cyclotomicCharMod`

 The cyclotomic character modulo `N`: the homomorphism `Γ →* (ZMod N)ˣ` giving the action of `Γ`
on the `N`-th roots of unity in `Ω`. 

 ### Characters as homomorphisms 

### `QZChar.toHom`

 A continuous character `χ : Γ → ℚ/ℤ` as a group homomorphism to `ℚ/ℤ` written
multiplicatively. 

### `QZChar.ker`

 The kernel of a continuous character `χ : Γ → ℚ/ℤ`, as a subgroup of `Γ`. 

### `QZChar.toHom_apply`

 `QZChar.toHom χ` sends `g` to `χ g`, written multiplicatively. 

### `QZChar.mem_ker_iff`

 An element `g` lies in the kernel of the character `χ` exactly when `χ g = 0`. 

### `QZChar.isClosed_ker`

 The kernel of a continuous character `χ : Γ → ℚ/ℤ` is closed in `Γ`. 

### `QZChar.abelianLift`

 The homomorphism induced by the continuous character `χ` on the topological abelianisation of
`Γ`, with values in `ℚ/ℤ` written multiplicatively. 

### `DiscreteUnits.ofBase`

 The homomorphism from `Kˣ` to the `Γ`-invariants of `Ωˣ` (both written additively) induced by
the map `K → Ω`. 

 ### The order, the class of an invariant and the local Artin map 

### `residueCard`

 The number of elements of the residue field of the valuation ring `A ∩ K` of `K` (zero if it is
infinite). 

### `ordRat`

 The order normalised on `K`: a chosen additive `f : Ωˣ → ℚ` with `n * f x = a` exactly when
`x ^ n` and `π ^ a` have equal valuation, for every uniformiser `π` of `K` (`New.IsUniformiser`: an
`x : K` lies in the maximal ideal of `A` exactly when its valuation is at most that of `π`);
valuations are those of `A`, taken in `Ω`. It is unspecified if no such map exists; see
`New.valuation_pow_eq_iff_mul_ordRat_eq_of_exists`. 

### `valuation_pow_eq_iff_mul_ordRat_eq_of_exists`

 The defining property of `New.ordRat` (`x ^ n` and `π ^ a` have equal valuation in `A` exactly
when `n * ordRat K A x = a`, for each uniformiser `π`) holds as soon as some additive map has it. 

### `IsClassOfInvariant`

 The property that a map `b : ℚ/ℤ → H²(Γ, Ωˣ)` sends `r` to the class of invariant `r`. First,
`b` is injective. Second, let the continuous character `χ : Γ → ℚ/ℤ` vanish on the inertia group
of `A`, let `φ` be a Frobenius element for `q = residueCard K A`, the number of elements of the
residue field, and let the invariant `w` of `Ωˣ` have normalised order `ordRat K A w = n`; then
`cyclicClass unitsRep χ w = n • b (χ φ)`. 

### `Cohomology.classOfInvariant`

 A chosen additive map `ℚ/ℤ → H²(Γ, Ωˣ)` with the property `New.IsClassOfInvariant`; when such a
map exists, it sends `r` to the class of invariant `r`. See
`New.Cohomology.isClassOfInvariant_classOfInvariant_of_exists`, and for local fields
`New.IsLocalGalois.isClassOfInvariant_classOfInvariant`. 

### `Cohomology.isClassOfInvariant_classOfInvariant_of_exists`

 `New.Cohomology.classOfInvariant` has the property `New.IsClassOfInvariant` as soon as some map
has it. 

### `IsLocalArtin`

 The property that the homomorphism `f` from `Lˣ` to the topological abelianisation of `Γ`
satisfies `classOfInvariant (χ (f x)) = -cyclicClass unitsRep χ x` for every continuous character
`χ : Γ → ℚ/ℤ` and every `x` in `Lˣ`, where `x` is viewed as an invariant of `Ωˣ`, and `χ (f x)` is
the value at `f x` of `QZChar.abelianLift χ`, the map induced by `χ` on the topological
abelianisation. 

 ### The local Artin map at a prime of a number field 

### `localArtin`

 The local Artin map at `v`: a chosen homomorphism from the units of the completion
`v.adicCompletion K` of `K` at `v` to the abelianised decomposition group of `A`, whose
restriction to `Kˣ` satisfies `New.IsLocalArtin` over the fixed field of the decomposition group;
unspecified if there is none (see `New.isLocalArtin_localArtin_comp_of_exists` and
`New.IsPlaceOver.isLocalArtin_localArtin`). 

### `isLocalArtin_localArtin_comp_of_exists`

 The restriction of `New.localArtin Γ A v` to `Kˣ` has its defining property as soon as the
restriction of some homomorphism has it. 

### `placeOver`

 For a finite prime `v` of the number field `K`, a chosen valuation subring of `New.Ω` (the
algebraic closure of `ℚ`) lying over `v`. It does lie over `v`
(`New.FinPlace.isPlaceOver_placeOver`). 

### `isPlaceOver_placeOver_of_exists`

 `New.placeOver v` lies over `v`, provided some valuation subring of `New.Ω` does. 


## Discrete modules: restriction, short exact sequences, functions on a finite quotient

* `New.DiscreteModule.restrictAlong`, `New.DiscreteModule.restrictTo`: restriction along a
  continuous homomorphism, and to a subgroup.
* `New.DiscreteModule.submodule`, `New.DiscreteModule.quotient`: a stable submodule, and the
  quotient by it.
* `New.DiscreteModule.funModule`: the functions from the finite quotient `Γ ⧸ U` to `A`, with `g`
  sending `f` to `x ↦ g (f (g⁻¹ • x))`. The maps `New.DiscreteModule.const` go into it and
  `New.DiscreteModule.sum` out of it.


### `New.DiscreteModule`

 A discrete Γ-module over R: an R-module with the discrete topology and a continuous R-linear
action of the topological group Γ. 

### `New.DiscreteModule.V`

 The underlying type. 

### `New.DiscreteModule.addCommGroup`

 `V` is an abelian group. 

### `New.DiscreteModule.moduleR`

 `V` is an `R`-module. 

### `New.DiscreteModule.topologicalSpace`

 The topology on `V`. 

### `New.DiscreteModule.discrete`

 The topology on `V` is discrete. 

### `New.DiscreteModule.ρ`

 The `R`-linear action of `Γ` on `V`. 

### `New.DiscreteModule.continuous`

 The action map `Γ × V → V` is continuous. 

### `New.subgroupIncl`

 The inclusion of a subgroup U in G, as a continuous homomorphism. 

### `instance : CoeSort (DiscreteModule R Γ) Type`

 A discrete module is read as its underlying type `V`. 

 ### Morphisms, cohomology and restriction 

### `Hom`

 For discrete Γ-modules M and A over R, the R-linear maps M → A commuting with the action of
Γ. 

### `coboundary`

 The linear map from a discrete Γ-module A to its continuous 1-cocycles sending m to
g ↦ gm − m. 

### `H0`

 The R-submodule of elements of a discrete Γ-module A fixed by all of Γ. 

### `H2`

 The continuous cohomology H²(Γ,A) of a discrete Γ-module A. 

### `restrictAlong`

 For a continuous homomorphism φ: G → Γ, the discrete Γ-module A viewed as a discrete
G-module through φ. 

### `restrictTo`

 For a subgroup U of Γ, the discrete Γ-module A viewed as a discrete U-module. 

### `resH2`

 For a subgroup U of Γ, the restriction map H²(Γ,A) → H²(U,A). 

### `Hom.mapH2`

 The linear map H²(Γ,M) → H²(Γ,N) induced by composing cocycles with a Γ-equivariant linear
map M → N. 

 ### Short exact sequences 

### `IsShortExact`

 The equivariant maps `ι : M → N` and `π : N → P` form a short exact sequence. That is, `ι` is
injective, `π` is surjective, and the kernel of `π` is the image of `ι`. 

### `IsShortExact.restrictAlong`

 A short exact sequence of discrete `Γ`-modules stays short exact after restriction along a
continuous homomorphism `φ : G → Γ`. 

### `submodule`

 A Γ-stable R-submodule W of a discrete Γ-module A, as a discrete Γ-module with the
restricted action. 

### `quotient`

 For a Γ-stable R-submodule W of a discrete Γ-module A, the quotient A ⧸ W as a discrete
Γ-module, with the action induced on cosets. 

### `isShortExact_submodule`

 For a `Γ`-stable submodule `W` of `A`, the inclusion and the quotient map form a short exact
sequence `0 → W → A → A ⧸ W → 0` of discrete `Γ`-modules. 

 ### Functions on a finite quotient `Γ ⧸ U` 

### `funModule`

 The discrete Γ-module of functions f: Γ/U → A, for a subgroup U of finite index with Γ/U
discrete, with action (gf)(x) = g·f(g⁻¹x). 

### `const`

 The Γ-equivariant linear map from A to A-valued functions on Γ/U sending m to the constant
function with value m. 

### `sum`

 The Γ-equivariant linear map from A-valued functions on the finite set Γ/U to A sending f to the
sum of its values. 


## Counting continuous 1-cocycles along exact sequences

* `New.DiscreteModule.Hom.mapZ1`: the map on continuous 1-cocycles given by an equivariant map.
* `New.DiscreteModule.card_eq_mul_of_exact`: for an exact sequence of groups `0 → A → B → C`, a
  subgroup `W` of `B` has as many elements as its preimage in `A` times its image in `C`.
* `New.DiscreteModule.Hom.card_eq_card_comap_mul_card_map`: the same count for a group `W` of
  continuous 1-cocycles of `N`, along `0 → Z¹(M) → Z¹(N) → Z¹(P)` for `0 → M → N → P` exact.

Cardinalities are `Nat.card`, which is `0` on infinite types.


### `Hom.mapZ1`

 For a morphism ι: M → N of Γ-modules, the map on continuous 1-cocycles Z¹(M) → Z¹(N) given
by composing with ι. 

### `card_eq_mul_of_exact`

 Let `f : A → B` be injective and `g : B → C` have kernel the image of `f`. Then for every
additive subgroup `W` of `B`, the cardinality of `W` is that of its preimage under `f` times that of
its image under `g`. 

### `IsShortExact.card_eq_card_mul_card`

 In a short exact sequence `0 → M → N → P → 0` of discrete `Γ`-modules, given by `ι : M → N` and
`π : N → P`, the number of elements of `N` is that of `M` times that of `P`. 

### `mem_Z1_of_injective_of_comp_mem_Z1`

 For an injective equivariant map `ι : M → N`, a function `f : Γ → M` is a continuous 1-cocycle
as soon as `ι ∘ f` is one. 

### `Hom.card_eq_card_comap_mul_card_map`

 Let `ι : M → N` be injective and `π : N → P` have kernel the image of `ι`. Then for every
additive subgroup `W` of the continuous 1-cocycles of `N`, the cardinality of `W` is that of its
preimage in the cocycles of `M` times that of its image in the cocycles of `P`. 
