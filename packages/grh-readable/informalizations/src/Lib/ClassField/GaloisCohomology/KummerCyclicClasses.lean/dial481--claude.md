---
{
  "module": "src/Lib/ClassField/GaloisCohomology/KummerCyclicClasses.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/GaloisCohomology/KummerCyclicClasses.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/GaloisCohomology/KummerCyclicClasses.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Cup products, Hilbert 90, Kummer cocycles and cyclic symbols in Galois cohomology

This file studies the Galois cohomology of `Ωˣ` for a group Γ acting on a field Ω. The group `Ωˣ` is
written additively (`New.DiscreteUnits`, with action `New.unitsRep`). In the last two sections Γ is
the profinite Galois group of Ω/K (`New.IsProGalois`). Take a continuous character χ : Γ → ℚ/ℤ with
kernel U and a Γ-invariant w in `Ωˣ`. The symbol (χ, w) = `New.cyclicClass ρ χ w` is the class in H²
of (g, h) ↦ carry(χ(g), χ(h))·w. The file first treats cup products of 1-cocycles, annihilators of
pairings, and a descent lemma for semilinear actions. Finally it shows that the classes vanishing on
U are the symbols (χ, w), and that (χ, w) = 0 exactly when w is a norm from U, that is, a field norm
from the field cut out by χ.

## Main definitions and results

* `New.cupProduct`, `New.cupProduct_flip`: the cup product of 1-cocycles, with values in `H²`, and
  its anticommutativity; `New.DiscreteModule.evalCup` is the case of the evaluation pairing.
* `New.Period.mem_span_fixed`: for a semilinear action, a vector fixed by a subgroup U of finite
  index is a linear combination of invariant vectors, provided every element outside U moves some
  U-fixed scalar. The invariant vectors are traces over the finitely many cosets, and Dedekind's
  independence of characters shows that their span contains the vector.
* `New.hilbert90_unitsRep`: Hilbert 90, every continuous 1-cocycle with values in `Ωˣ` is a
  coboundary.
* `New.exists_kummer_cocycle`: if `Γ` fixes the `n`-th roots of unity (`ζ ^ k` is
  `New.rootPowHom Ω n k` for a chosen primitive `n`-th root of unity `ζ`), an invariant `x = a ^ n`
  gives a homomorphism `f : Γ → ℤ/n` with `g a / a = ζ ^ f g`.
* `New.mk_eq_neg_cyclicClass_ofZModCocycle`: the cup product of `g ↦ g a / a` with `ξ : Γ → ℤ/n` is
  minus the cyclic class of `ξ / n` and `a ^ n`.
* `New.QZChar.cyclicClass_spec`: the classes in `H²(Γ, Ωˣ)` that die on `U` are the symbols `(χ, w)`
  of `New.cyclicClass` with `w` in `Kˣ` (embedded in `Ωˣ` by `New.DiscreteUnits.ofBase`), and
  `(χ, w) = 0` exactly when `w` is a norm from `U`. The two hard directions are
  `New.QZChar.exists_eq_cyclicClass_of_resH2_eq_zero` and
  `New.QZChar.exists_corestrictH0_eq_of_cyclicClass_eq_zero`.

Notions from other files:
* `New.DiscreteModule R Γ`: an `R`-module `V` with the discrete topology and a continuous `R`-linear
  action `ρ` of Γ; `New.Z1 ρ` and `New.Z2 ρ` are its continuous 1- and 2-cocycles.
* `New.unitsRep`: the ℤ-linear representation of Γ on Ω^× (written additively) coming from the
  action of Γ on the field Ω by ring automorphisms.
* `New.DiscreteModule.H2`: The continuous cohomology H²(Γ,A) of a discrete Γ-module A: 2-cocycles
  modulo the functions (g,h) ↦ g c(h) − c(gh) + c(g) with c continuous.
* `New.QZ` is ℚ/ℤ. `New.QZ.carry`: for a, b in ℚ/ℤ, the integer part (0 or 1) of the sum of their
  representatives in [0,1); `New.cyclicClass ρ χ w` is the class of the cocycle (g,h) ↦ carry(χ(g),
  χ(h))·w.
* `New.IsProGalois`: a profinite group acts on the Galois extension Ω/K as its Galois group, with
  open stabilisers.

## Relation to the literature

Known result: the parts of Galois cohomology in degrees ≤ 2 listed above, namely cup products,
Hilbert 90, Kummer cocycles and the symbols of cyclic extensions. Only explicit continuous cocycles
are used. Shapiro's lemma and corestriction (summation of functions on a coset space) come from
`Lib.ClassField.GaloisCohomology.ShapiroCorestriction`. Source: J.-P. Serre, Galois Cohomology
(1997); Neukirch–Schmidt–Wingberg, Cohomology of Number Fields (2nd ed. 2008), Ch. I, VI;
Atiyah–Wall in Cassels–Fröhlich (1967), IV §8.



## Elementary lemmas on the multiplicative group written additively

`New.DiscreteUnits Ω` is the group `Ωˣ` written additively, and `(x.toMul : Ω)` is the field element
underlying `x`.


### `ofNeZero`

 A non-zero element a of the field Ω, viewed as an element of the additively written
multiplicative group `New.DiscreteUnits` Ω. 

### `exists_nsmul`

 If Ω is algebraically closed and `n ≠ 0`, every `x` in `Ωˣ` (written additively) is `n • y`
for some `y`: the element `x` has an `n`-th root in `Ωˣ`. 


## Cup products, Hom modules and orders of annihilators

Orders are `Nat.card`, which is `0` for infinite groups.

* `New.DiscreteModule.cartierDual`: additive maps `M → Ωˣ` for finite `M`, with
  `g • f = g ∘ f ∘ g⁻¹`.


### `unitsModule`

 The multiplicative group Ω^×, written additively, as a discrete module with its continuous
action of Γ. 

### `instance [Finite A] : Finite (A →+ DiscreteUnits Ω)`

 Additive maps from a finite group `A` to `Ωˣ` (written additively) form a finite set. 

### `instance : DivisibleBy (DiscreteUnits Ω) ℤ`

 For Ω algebraically closed, `Ωˣ` written additively is divisible by every non-zero integer,
since every unit has `n`-th roots (`New.DiscreteUnits.exists_nsmul`). 

 ### Annihilators 

### `pairingAnnihilator`

 For a biadditive pairing b : A × B → C and a subgroup L of A, the subgroup of y in B with
b(x, y) = 0 for all x in L. 

### `index_ker_flip_dvd`

 Let `β : A × B → C` be biadditive and let `e` identify ℚ/ℤ (`New.QZ`) with `C`. The index in
`B` of the right kernel `{y | ∀ x, β x y = 0}` divides the index in `A` of the left kernel
`{x | ∀ y, β x y = 0}`. 

### `card_pairingAnnihilator_mul_card`

 Let `b : A × B → C` be biadditive and let `e` identify ℚ/ℤ (`New.QZ`) with `C`. For a subgroup
`L` of `A` with annihilator `L^⊥ = pairingAnnihilator b L` in `B`,
`#L^⊥ · #L = #B · #(L ∩ left kernel of b)`, where `#` is `Nat.card` (`0` for infinite groups). 

 ### Hom modules and cup products 

### `instance : TopologicalSpace (A →+ B)`

 Additive maps between two groups carry the discrete topology. 

### `DiscreteModule.cartierDual`

 For a finite discrete Γ-module `M`, the discrete Γ-module `Hom(M, Ω^×)` of additive maps to
`New.unitsModule`, on which `g` acts by `(g f)(m) = g f(g⁻¹ m)`. 

### `cupProduct`

 Let `M`, `N`, `W` be discrete Γ-modules and `b : M × N → W` a biadditive pairing that is
equivariant: `e` says `b (g x) (g y) = g (b x y)`. The cup product `Z¹(M) × Z¹(N) → H²(W)` sends
1-cocycles `x`, `y` to the class of the 2-cocycle `(g, h) ↦ b (x g) (g (y h))`. 

### `DiscreteModule.evalCup`

 For a finite discrete Γ-module `M`, the cup product `Z¹(Hom(M, Ω^×)) × Z¹(M) → H²(Ω^×)` of the
evaluation pairing `(f, m) ↦ f m` (`Hom(M, Ω^×)` is `New.DiscreteModule.cartierDual`). 

### `cupProduct_flip`

 Anticommutativity of the cup product. Let `Γ` be a group with a topology and let `W`, `M`, `N`
be discrete Γ-modules (`New.DiscreteModule`: a discrete module `V` with a continuous linear action
`ρ` of `Γ`). Let `b : M × N → W` be biadditive and equivariant, `b (g m) (g n) = g (b m n)`. Let
`x` and `y` be continuous 1-cocycles (`New.Z1`) with values in `M` and `N`. The cup product
`New.cupProduct W M N b h_equivariant x y` is the class in `H²(Γ, W)` of the 2-cocycle
`(g, h) ↦ b (x g) (g (y h))`. The flipped pairing `b.flip : (n, m) ↦ b m n` is equivariant too,
and the cup product of `y` and `x` for `b.flip` is minus the cup product of `x` and `y` for `b`. 

 ## Galois descent from a subgroup of finite index 

### `New.Period.mem_span_fixed`

 Galois descent. Let `G` act on the field `A`, let `τ` be semilinear along `j : Γ →* G`, and let
`U` have finite index in `G` and be the fixer of its own fixed scalars. A vector `y` fixed by every
`g` with `j g ∈ U` lies in the `A`-span of the vectors fixed by all of `Γ`. 


## Hilbert 90, Kummer cocycles and their cup products

`Ωˣ` is written additively (`New.DiscreteUnits`), so `n • a` is `a ^ n` and `g a - a` is `g a / a`;
`New.unitsModule Γ` is `Ωˣ` as a discrete `Γ`-module, with the action `New.unitsRep`. `New.Z1` of a
trivial module consists of the continuous homomorphisms.


### `isGalois_fixedFieldOf`

 The fixed field of a normal subgroup `U` of `Γ` is Galois over `K`. 

### `mk_eq_neg_cyclicClass_ofZModCocycle`

 The cup product of a Kummer cocycle with a character mod `n`. Let `w` in `Ωˣ` be `Γ`-invariant
with `a ^ n = w`, and let `ξ : Γ → ℤ/n` be a continuous homomorphism. If the 2-cocycle `z` is
`(g, h) ↦ (g a / a) ^ ξ(h)`, then its class is minus the symbol `(ξ / n, w)`. Here
`New.QZChar.ofZModCocycle n ξ` is the character `ξ / n : Γ → ℚ/ℤ`, and `New.cyclicClass ρ χ w` is
the class of `(g, h) ↦ carry(χ(g), χ(h)) • w`. 

### `hilbert90_unitsRep`

 Hilbert's Theorem 90. Let `Γ` act on `Ω` as the Galois group of `Ω / K` (`New.IsProGalois`).
Every continuous 1-cocycle `f` of `Γ` with values in `Ωˣ` is a coboundary: `f g = g m / m` for some
`m`, written additively as `unitsRep g m - m`. 

### `exists_kummer_cocycle`

 Kummer cocycle. Let `Ω` be algebraically closed of characteristic 0, and let `Γ`, the Galois
group of `Ω / K`, fix the `n`-th roots of unity (`h_cyc`: the cyclotomic character mod `n` is
trivial). For `x` in `Ωˣ` fixed by `Γ` there are an `n`-th root `a` of `x` and a continuous
homomorphism `f : Γ → ℤ/n` such that `g b / b = ζ ^ f(g)` for every `n`-th root `b` of `x`. Here
`ζ ^ k` is `New.rootPowHom Ω n k`, for a chosen primitive `n`-th root of unity `ζ`. 


## Symbols of cyclic extensions and norms

Let `χ : Γ → ℚ/ℤ` be a continuous character with kernel `U`. The proofs use Hilbert's Theorem 90
(`New.hilbert90_unitsRep`) for `U` and Shapiro's lemma.


### `IsProGalois.of_fixingSubgroup_eq`

 Let `U` be the closed subgroup of `Γ` of the elements that fix `L`, embedded in `Ω` by
`algebraMap L Ω`. Then `U` acts on `Ω` as the Galois group of `Ω / L` (`New.IsProGalois`). 

### `exists_carry_eq_one_sub_ite`

 Let `f` be an injective homomorphism from a finite group `Q` to `ℚ/ℤ` (written
multiplicatively). There is `γ` in `Q` such that the carry of `f q` and `f γ` is `0` for `q = 1` and
`1` for every other `q`: take for `γ` the element whose value has the largest representative in
`[0, 1)`. 

### `hilbert90_funModule`

 Hilbert 90 for functions on cosets: for an open subgroup `U` of `Γ`, every continuous
1-cocycle with values in the functions `Γ ⧸ U → Ωˣ` is a coboundary. By Shapiro's lemma this is
Hilbert 90 for `U`. 

### `QZChar.exists_eq_cyclicClass_of_resH2_eq_zero`

 The classes that vanish on the kernel of a character are symbols. Let `Γ` be the profinite
Galois group of the extension `Ω/K` (`IsProGalois`), and `H²(Γ, Ωˣ)` the continuous cohomology of
`Ωˣ`, written additively. Let `χ : Γ → ℚ/ℤ` be a continuous character with kernel `U`, an open
subgroup of `Γ`. If a class `x` in `H²(Γ, Ωˣ)` restricts to zero on `U`, then `x` is the symbol
`(χ, w)` (`New.cyclicClass`) of some `w` in `Kˣ`, where `w` is embedded in `Ωˣ` by
`New.DiscreteUnits.ofBase`. 

### `QZChar.exists_corestrictH0_eq_of_cyclicClass_eq_zero`

 A symbol that vanishes is a norm. Let `Γ` be the profinite Galois group of the extension `Ω/K`
(`IsProGalois`), acting on `Ωˣ` (written additively), and let `χ : Γ → ℚ/ℤ` be a continuous
character with kernel `U`, an open subgroup of `Γ`. Let `w` be a `Γ`-invariant element of `Ωˣ`. If
the symbol `(χ, w)` (`New.cyclicClass`) is zero in `H²(Γ, Ωˣ)`, then `w` is the norm
`New.DiscreteModule.corestrictH0 U y` of some `U`-invariant element `y` of `Ωˣ`, that is, the sum of
`g y` over the cosets `gU`. 

### `QZChar.cyclicClass_spec`

 Let `χ : Γ → ℚ/ℤ` be a continuous character and `U` its kernel, an open subgroup of `Γ`. A class
in `H²(Γ, Ωˣ)` dies on `U` exactly when it is a symbol `(χ, w)` with `w` in `Kˣ`; and for a
`Γ`-invariant `w` in `Ωˣ` the symbol `(χ, w)` is zero exactly when `w` is a norm
`New.DiscreteModule.corestrictH0 U y` of a `U`-invariant `y`. 

### `corestrictH0_ofBase_eq_norm`

 Let the open subgroup `U` of `Γ` act on `Ω` as the Galois group of `Ω / L`, with `L / K` finite
separable and `Ω` algebraically closed. Then the norm from `U` to `Γ`
(`New.DiscreteModule.corestrictH0`) of a unit `y` of `L` is its field norm to `K`. 

### `cyclicClass_eq_zero_iff_norm`

 If the kernel of the character `χ : Γ → ℚ/ℤ` is the Galois group of `Ω / L` (`J`), with `L / K`
finite separable and `Ω` algebraically closed, then the symbol `(χ, x)` (`New.cyclicClass`) of `x`
in `Kˣ` vanishes exactly when `x` is the norm of a unit of `L`. 
