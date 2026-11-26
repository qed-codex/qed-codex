---
{
  "module": "src/New/Congruences/GaloisRepresentations/AttachedRepresentations.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/GaloisRepresentations/AttachedRepresentations.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/GaloisRepresentations/AttachedRepresentations.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Lift settings and conjugate self-duality of attached Galois representations

This file shows that good tuples of labels form lift settings with the descent pairs of the data.
It also shows that, for a main pair, the constant label `X - 1` forms a lift setting for the lift
from `U(1)`. It bounds the `ℓ`-adic valuation of `p_i ^ d - 1` and gives basic facts on lattices
in a representation. It proves that representations attached to Hecke eigenforms are conjugate
self-dual. It also shows that representations of a type arise from labelled eigenforms and are
preserved by twisting with avatars.

## Main definitions and results

* `New.Selmer.isConjSelfDual_of_attached`: a Galois representation `r` of rank `n` attached to a
  Hecke eigenform (`New.GaloisRep.Attached`) satisfies `New.Selmer.IsConjSelfDual`. In particular,
  tr r(g^c) = χ(g)^(n-1) tr r(g⁻¹) with χ = `New.Selmer.cyclotomicInv`. The Hecke operators at w and
  w̄ are dual (`New.heckeSplit_dual`), which gives the relation for most Frobenii. It passes to
  every g along the filter `New.mostFrobeniiAt`.
* `New.Selmer.isRepOfType_of_hasProductLabel`: the representation attached to a labelled eigenform
  is a representation of a type.

Notions from other files:
* `New.Data.descentPair`: The j-th descent pair (`New.DescentPair`) for ϑ: W = W_j of rank r,
  V = I_{r+t}, the character μ_j⁰ϑ of weight −w_j, and the places `New.Data.levelPlaces`.
* `New.Data.CriticalPair.IsMainPair`: A pair `p = (p.character, z)` with `p.character` of weight
  `-c` is a main pair for `j` if the index type `RankOneIndex z` has `2 z` elements and `2 ≤ z`
  (`HasLiftRank`), `m < z ≤ r`, `1 ≤ j ≤ m`, the tame part of `p.character` is `D.chiMLocal ^ j`
  (`D.chiMLocal` the tame character of the data), and `w_j + r - t ≤ c ≤ w_j` at every infinite
  place, with `w_j = D.liftWeight j`.
* `New.Selmer.IsConjSelfDual`: `R` is continuous, has non-degenerate trace form, and is conjugate
  self-dual up to twist on traces, tr R(g^c) = χ(g)^(t-1) tr R(g⁻¹), with `g^c = c g c`
  (`New.conjGal`) and χ = `New.Selmer.cyclotomicInv`.
* `New.Selmer.IsLiftSetting`: the descent pair `O` with the labels `c` is a lift setting for the
  twist `ϑ`.
* `New.Selmer.IsRepOfType`: `R` is a conjugate self-dual representation of level `S`, and inertia
  at the chosen places acts through the roots of the labels `c`.

## Relation to the literature

For sources see `Lib.GaloisRep.Main.OddRank`, `Lib.PadicHodge.Crystalline.Regularity` and
`New.Congruences.GaloisRepresentations.RowsFromEigensystems`.



## Lift settings for the descent pairs and for the lift from U(1)

* `New.Selmer.isLiftSetting_descentPair`: the good tuples of labels form a lift setting with the
  descent pair of index `j`.
* `New.Selmer.isLiftSetting_mainPair`, `New.Selmer.trivialLift_mem_range_typeProjection`: for a main
  pair, the constant label `X - 1` forms a lift setting for the lift from `U(1)`. The form
  `trivialLift`, a multiple of the theta lift of the constant function `1`, lies in the range of the
  corresponding idempotent.


### `not_isRoot_one_scaleRoots_inv`

 If a unit `y` is not a root of `q`, then `1` is not a root of `q` with its roots multiplied by
`y⁻¹`. 

### `isLiftSetting_descentPair`

 Let `j` be a lift index, `1 ≤ j ≤ D.m`, and `ϑ` a twist. Let `c` be a good family of polynomials
over the residue fields at the chosen places: each is a label of degree `D.r` (monic, squarefree,
nonzero at `0`) that vanishes at no `q₂`-th root of unity of its field, `q₂ = P.q₂ D.towerExp`, and
over each of `p₀`, `p₁` one of them is primitive. The `j`-th descent pair with the labels `c` is a
lift setting for `ϑ`. 

### `isLiftSetting_mainPair`

 Let `p = (ν, z)` be a main pair for `j` (`New.Data.CriticalPair.IsMainPair`): `D.m < z ≤ D.r`,
`1 ≤ j ≤ D.m`, the character `ν` of `U(1)` has tame part `D.chiMLocal ^ j`, and its weight `-c`
satisfies `w_j + D.r - D.t ≤ c ≤ w_j` with `w_j = D.liftWeight j`. Let `ϑ` be a twist. The descent
pair of `p.lValueData hp.hasLiftRank ϑ`, the data for the lift of `ν ϑ` from `U(1)` to `U(2 z)`, has
a space `W` of rank one. With every label equal to `X - 1` it is a lift setting for `ϑ`
(`New.Selmer.IsLiftSetting`). 

### `trivialLift_mem_range_typeProjection`

 Let `p = (ν, z)` be a main pair for `j`: `D.m < z ≤ D.r`, `1 ≤ j ≤ D.m`, the character `ν` of
`U(1)` has tame part `D.chiMLocal ^ j`, and its weight `-c` satisfies `w_j + D.r - D.t ≤ c ≤ w_j`
with `w_j = D.liftWeight j`. Let `ϑ` be a twist and `Y = p.lValueData hp.hasLiftRank ϑ` the data for
the lift of `ν ϑ` from `U(1)` to `U(2 z)`. Then the form `Y.trivialLift`, a multiple of the theta
lift of the constant function `1`, lies in the range of the idempotent `typeProjection` of the
descent pair of `Y` with every label equal to `X - 1`. 


## Divisors of the chosen group order, places above p₀ and p₁, and lattices

* `New.Selmer.levelPrime_pow_sub_one_dvd_chosenGroupOrder`,
  `New.Selmer.ellVal_levelPrime_pow_sub_one_le`: with `p_i = D.levelPrime i`, the number
  `p_i ^ d - 1` divides `New.Data.chosenGroupOrder` for `1 ≤ d ≤ r t`, which bounds its `ℓ`-adic
  valuation.
* `New.Selmer.IsLatticeIn.exists_algHom` and its companions: a lattice `u` in `R` has the same
  determinants and traces as `R`, is trivial where `R` is, and is continuous if `R` is.


 ### The primes `p₀`, `p₁` and the places above them 

### `levelPrime_pow_sub_one_dvd_chosenGroupOrder`

 For `1 ≤ d ≤ D.r * D.t` and each of the two primes `p_i = D.levelPrime i`, the number
`p_i ^ d - 1` divides `D.chosenGroupOrder`. That number is the product, over the chosen places above
`p₀` and `p₁`, of the orders of `GL (D.r * D.t)` over the residue fields. 

### `ellVal_levelPrime_pow_sub_one_le`

 For each of the two primes `p_i = D.levelPrime i` and each `d` with `1 ≤ d ≤ D.r * D.t`, the
`ℓ`-adic valuation of `p_i ^ d - 1` is at most that of `D.chosenGroupOrder`. 

### `card_le_of_subset_placesAboveM`

 Every finite set `T` of finite places of `E = D.E` inside `placesAboveM D` (the places above the
primes `p₀`, `p₁` of `D`) has at most `4 * D.f` elements, where `D.f` is the number of infinite
places of `E`. 

### `exists_chosen_notMem_placesDividing`

 Let `p₀ = D.levelPrime 0` and `p₁ = D.levelPrime 1` be the two primes of the data `D`, and `ℓ`
a prime. Some finite place `w` of `D.E` is chosen (`New.Data.IsChosen`: it divides the integer
`D.piM`), lies above `p₀` or `p₁` (`placesAboveM D`) but not above `ℓ`, and has a residue field of
order `w.q` equal to `p₀` or `p₁`. 

 ### Lattices in a representation 

### `IsLatticeIn.exists_algHom`

 If u is a lattice in R over O (`New.Selmer.IsLatticeIn`: R is conjugate to the image of u over
ℚ̄_ℓ), some injective O-algebra map F from matrices over O to matrices over ℚ̄_ℓ sends u(g) to R(g)
and preserves determinants and traces. 

### `IsLatticeIn.continuous`

 A lattice in a continuous representation is continuous. 

### `IsLatticeIn.eq_one`

 A lattice in `R` is trivial wherever `R` is trivial. 

### `IsLatticeIn.trace_eq`

 If `u` is a lattice in `R` (`IsLatticeIn R u`), then for every `g` in `AbsGal D` the trace of
`u g`, read in `ℚ̄_ℓ`, equals the trace of `R g`. 

 ## Conjugate self-duality of attached representations 

### `New.Selmer.coeff_zero_mul_coeff_star`

 Let a nonzero `f` in rank `k + 1` be spherical at the split place `w` with Hecke polynomial
`Q w` and at `star w` with Hecke polynomial `Q (star w)` (`New.HasHeckePolyAt`). Then the constant
coefficient of `Q w` times the `k`-th coefficient of `Q (star w)` is `q ^ k` times the linear
coefficient of `Q w`, where `q` is the order of the residue field at `w`. 

### `New.Selmer.isConjSelfDual_of_attached`

 Let f be an eigenform in rank n for the system Q of Hecke polynomials (`New.IsEigenform`), and
let r be an ℓ-adic Galois representation attached to Q. Then r satisfies
`New.Selmer.IsConjSelfDual`: it is continuous, has non-degenerate trace form, and is conjugate
self-dual on traces, tr r(cgc) = cyc(g)^{1−n} tr r(g⁻¹) for all g, with c complex conjugation and
cyc the cyclotomic character. 


## Representations of a type under conjugate places, twists, and labelled eigenforms

How the property `New.Selmer.IsRepOfType` of an `ℓ`-adic Galois representation `R` arises and how it
is preserved.

* `New.Selmer.IsRepOfType.twist_avatar`: `IsRepOfType` is preserved, with shifted twist, jumps and
  labels, by twisting with the avatar of an algebraic Hecke character whose tame part is `1` off the
  chosen places.


### `isTraceNondeg_transpose_inv`

 If the trace form on the image of `R` is non-degenerate, so is that on the image of its dual
`R'`, `g ↦ (R g⁻¹)ᵀ`. 

### `count_jumps_comp_star`

 Composing a complex embedding `σ` with complex conjugation replaces each jump `u` of a weight
`κ` in rank `k` (`New.jumps`) by `k - 1 - u`. 

### `isFiniteTypeAt_and_hasJumpsAt_of_conjPlace`

 Let `R` be conjugate dual with twist `1 - k` and of finite type at the conjugate `conjPlace A`
of the place `A`. Then (a) `R` is of finite type at `A`; (b) if `R` has the jumps of a weight `κ` in
rank `k` at the conjugate place, it has them at `A`; (c) a polynomial that kills an inertial `s` at
the conjugate place kills `conjGal s⁻¹` at `A`.

A case of the compatibility of Weil–Deligne representations and Hodge–Tate weights with duals and
conjugation (Fontaine). 

### `prod_aroots_dvd_prod_aroots_scaleRoots_comp`

 Let `φ : K →* L` be multiplicative and `u` a unit of `F`. The product of `X - φ x` over the
roots `x` of `p` in `K` divides `Q (φ u * X)`, where `Q` is the same product for the polynomial
whose roots are those of `p` times `u`. 

### `IsRepOfType.twist_avatar`

 Let the descent pair `O` with some polynomials `d` form a lift setting for `ϑ`, so that the
places `O.chosenPlace i` are chosen. Let `R` be a representation of a type: conjugate self-dual of
twist `1 - k`, with jumps `J` and level `S`, inertia at `O.chosenPlace i` acting through the roots
of a polynomial `c i` over the residue field. Let `a` be a character of `U(1)` of weight `e` whose
tame part `ψ` is `1` at every place that is not chosen (`D.IsChosen`). Twist `R` by the `ℓ`-adic
avatar of the algebraic Hecke character `ha.toAlgebraic k' j`,
`y ↦ a(y / ȳ) υ(y)^{-k'} |y|^{j - k'/2}` with `υ` the fixed splitting character. The result is a
representation of a type of level `S` and twist `1 - b`, where `(b - 1) + (2 * j - k') = k - 1` with
truncated subtractions `b - 1`, `k - 1`. Its jumps are shifted by minus the infinity type, and the
roots of `c i` are scaled by the unit of the residue field that names the character
`ψ (O.chosenPlace i)` (`New.charName`). 

### `isRepOfType_of_hasProductLabel`

 Let the descent pair `O` with some polynomials `d` form a lift setting for `ϑ`, so that the
places `O.chosenPlace i` are chosen. Let `f` be an eigenform of weight `κ` on the definite unitary
group of rank `card m`, and `R` attached to its Hecke polynomials `H`. Suppose that `f` is spherical
at every place that is off `S`, above `ℓ` or above `p₀ p₁`, except the chosen places of `O` and
their conjugates. Suppose also that the type of `f` at `O.chosenPlace i` is induced from the one
with label `c i`, a polynomial of degree `card r`, and trivial characters on blocks of sizes `t l`.
Then `R` is a representation of a type: conjugate self-dual of twist `1 - card m` and level `S`,
with the jumps of `κ`, inertia at `O.chosenPlace i` acting through the roots of
`c i * (X - 1) ^ (card m - card r)`. 
