---
{
  "module": "src/Lib/PadicHodge/Crystalline/Regularity.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Crystalline/Regularity.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Crystalline/Regularity.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Regularity of B_max, closure of admissibility, and crystalline descent from inertia

This file proves the regularity of the period ring `B = New.Period.Bmax` and shows that
representations admissible along a filter have bases of fixed elements. It proves closure
properties of crystalline and potentially crystalline representations under subobjects, quotients
of tensor products and twisted duals. It also shows that a potentially crystalline representation
is crystalline when the linear Frobenius operators are trivial on inertia.

## Main definitions and results

* `New.Period.fontaine_regularity`, `New.Period.IsAdmissible.exists_basis`: regularity of `B`; bases
  of fixed elements.
* `New.Period.IsAdmissible.of_jointly_injective`, `New.Period.IsKilledBy.of_jointly_injective`:
  subobjects of finite sums.
* `New.Period.linearFrob_apply`, `New.Period.linearFrob_mul`,
  `New.Period.linearFrob_twist_cyclotomicGp`,
  `New.Period.IsPotentiallyCrystalline.eventually_linearFrob_eq_one`: the operators are
  multiplicative and change by a power of `p` under Tate twists. They are trivial on inertia near
  `1` if `T` is finite free.
* `New.Period.IsAdmissible.of_bilinear`, `New.Period.linearFrob_baseChangePairing`: quotients of
  tensor products.
* `New.Period.IsAdmissible.of_pairing`: twisted duals.
* `New.Period.IsPotentiallyCrystalline.isCrystalline_of_inertia_fixes`: descent from inertia.

Notions from other files:
* `New.Period.BPlus`, `New.Period.Bmax`: B⁺ = A_max[1/p] and B = B⁺[1/μ], μ = [ε] − 1.
* `New.Period.nearOne`: The filter 'near 1' on Γ: the pull-back along j: Γ → G_p of the filter of
  neighbourhoods of the identity.
* `New.Period.IsWeilPair`: (s, m) is a Weil pair if s acts on the residue field of the integers of
  Q̄_p as x ↦ x^(1/p^m); m = 0 means that s is in inertia.

## Relation to the literature

Known result: Potentially crystalline representations, Hodge–Tate weights and Weil–Deligne
Frobenius. Here the representations are abstract modules over any p-adic coefficient ring, with
Colmez's B_max as period ring and "crystalline" defined by the invariants spanning. Polynomials
killing one linear Frobenius replace the Weil–Deligne representation. Source: J.-M. Fontaine,
Représentations p-adiques semi-stables (Exp. III §1, §5) and Représentations l-adiques
potentiellement semi-stables (Exp. VIII 2.3), Astérisque 223 (1994); O. Brinon, B. Conrad, CMI
Summer School notes on p-adic Hodge theory (2009), 2.3.1, 5.2.1, 6.3, 9.1–9.3.

See also `Lib.PadicHodge.PeriodRings.DeRhamPeriods` and `Lib.PadicHodge.Kisin.PeriodMatrixFrame`.



## Closure properties of admissible representations

Closure properties of admissible representations for the period ring `B = New.Period.Bmax`. The
group `Γ` comes with a map `toGp` to `G_p` with open image (`New.Period.OverGp`).
`New.Period.fixedPeriods ρ B F` is the set of elements of `B ⊗ T` fixed by `g` along the filter `F`.
`New.Period.IsAdmissible` says that these elements span: this is crystalline for `F = ⊤` and
potentially crystalline (`New.Period.IsPotentiallyCrystalline`) for `F = nearOne Γ`. For a Weil pair
`(s, m)` (`New.Period.IsWeilPair`), `New.Period.linearFrob` is the operator `β` that extends
`φ ^ m s` linearly. `New.Period.IsKilledBy` says that `T` is potentially crystalline and `P(β) = 0`.


### `eventually_tensorAction_eq`

 Let `x i` (`i : ι`) be elements of `Bmax ⊗ T` fixed along the filter `F` for the representation
`ρ` of `Γ` on `T`, and let `a : ι →₀ Bmax`. Then along `F` the group acts on `∑ a i • x i` through
the coefficients: `g` sends it to `∑ (toGp g • a i) • x i`. 

### `map_eq_zero_of_roots`

 Let K be algebraically closed of characteristic 0 and φ: K[X] → A a ring homomorphism with
φ(X)^n = 1 for some n > 0. If φ(Q) = 0, then φ(P) = 0 for every P vanishing at all roots of
Q. 

### `IsWeilPair.inv`

 If `(toGp s, 0)` is a Weil pair, that is, `toGp s` lies in inertia, then so is
`(toGp s⁻¹, 0)`. 

### `exists_leftInverse_baseChange`

 Let `f i : T' → S i` (`i : κ`, `κ` finite) be `ℤ_[p]`-linear maps that are jointly injective:
only `0` is sent to `0` by all of them. Then the family of base changes `Bmax ⊗ T' → Bmax ⊗ S i`
has a `Bmax`-linear left inverse. 

 ### Regularity, bases of fixed elements, subobjects

In this section `hF : nearOne Γ ≤ F`: every property that holds along `F` holds for all `g` with
`toGp g` near `1`. 

### `fontaine_regularity`

 Part of Fontaine's regularity of `B = Bmax` (fixed fractions lie in `B`). Let
`nearOne Γ ≤ F`, let `w : ι →₀ Bmax` and `b ≠ 0` in `Bmax`. If the fraction `w / b` is fixed
along `F`, in the sense that `b • g w = (g b) • w` for `F`-almost all `g` (acting through
`toGp`), then `w = b • a` for some `a` fixed by `F`-almost all `g`. 

### `le_of_fixed_mem_of_saturated`

 Let `hF : nearOne Γ ≤ F`. Let `W` be a submodule of the free `Bmax`-module `ι →₀ Bmax` that is
saturated (`b • w ∈ W` with `b ≠ 0` implies `w ∈ W`) and stable along `F` (`toGp g • v ∈ W`
for `F`-almost all `g`, for each `v ∈ W`). If every element of `W` fixed along `F` lies in
`W'`, then `W ≤ W'`. 

### `IsAdmissible.exists_basis`

 Let `nearOne Γ ≤ F` (`nearOne Γ`: the filter of `g` with `toGp g` near `1`). If `ρ` is
admissible along `F`, that is, the elements of `Bmax ⊗ T` fixed by `F`-almost all `g` span it over
`Bmax`, then `Bmax ⊗ T` has a `Bmax`-basis of such fixed elements.

A form, over `Bmax` and for invariants along `F`, of the statement in Fontaine's admissibility
formalism that the period module of an admissible representation has a basis of invariant
elements. 

### `IsAdmissible.of_retraction`

 Let `F` be a filter on `Γ` with `nearOne Γ ≤ F`, where `nearOne Γ` is the pull-back along `toGp`
of the neighbourhoods of `1` in Gal(Q̄_p/Q_p). Let finitely many representations `τ i` on `S i` be
admissible along `F` (`hA`): the elements of `Bmax ⊗ S i` fixed by `toGp g ⊗ τ i g` for `F`-almost
all `g` span `Bmax ⊗ S i` over `Bmax`. Let `Bmax`-linear maps `Φ i : Bmax ⊗ T' → Bmax ⊗ S i`
commute, for `F`-almost all `g`, with the diagonal actions `b ⊗ x ↦ (toGp g • b) ⊗ ρ' g x` and
`b ⊗ y ↦ (toGp g • b) ⊗ τ i g y`; if `LinearMap.pi Φ` also has a `Bmax`-linear left inverse `Ψ`,
then `ρ'` is admissible along `F` in the same sense. 

### `IsAdmissible.of_jointly_injective`

 Let `Γ` come with a homomorphism `j : Γ → Gp p` of open image (`OverGp`), and let every set in
the filter `F` contain the preimage under `j` of a neighbourhood of `1` (`hF : nearOne Γ ≤ F`). A
representation `ρ` on `T` is admissible along `F` when the elements of `Bmax ⊗ T` fixed by
`j(g) ⊗ ρ(g)` for `F`-almost all `g` span `Bmax ⊗ T` over `Bmax`. If each `τ i` is admissible along
`F` (`hA`) and finitely many `ℤ_[p]`-linear maps `f i : T' → S i` are jointly injective (`hi`) and
equivariant for `F`-almost all `g` (`hf`), then `ρ'` is admissible along `F`.

A form of Fontaine's stability of admissible representations under finite direct sums and
subrepresentations. 

### `tensorAction_gp_eq_tensorAction_frobGal`

 The action of `g` in `G_p` on `Bmax ⊗ T` is the action of the pair `(1, g)` of `FrobGal`. 

 ### The operators attached to Weil pairs

Here `hs : IsWeilPair (toGp s) m` says that `(toGp s, m)` is a Weil pair: `toGp s` acts on the
residue field of the integers of `Q̄_p` as `x ↦ x ^ (1 / p ^ m)`. 

### `IsWeilPair.smul_eq_of_fixed_nearOne`

 Let `(toGp s, m)` be a Weil pair. If `b` in `Bmax` is fixed by `toGp g` for all `g` near `1`,
then `φ ^ m` composed with `toGp s`, the action of the pair `(ofAdd m, toGp s)` of `FrobGal`,
fixes `b`. 

### `linearFrob_apply`

 Let `ρ` be potentially crystalline (`h`) and let `(toGp s, m)` be a Weil pair (`hs`), meaning
`toGp s` acts on the residue field of the valuation ring of Q̄_p as `x ↦ x ^ (1 / p ^ m)`. On
`Dpcris ρ`, the set of elements of `Bmax ⊗ T` fixed by `toGp g ⊗ ρ g` for all `g` near `1`, the map
`linearFrob ρ s m` acts as `φ ^ m s ⊗ ρ s`. Here the pair `(ofAdd m, toGp s)` of `FrobGal` acts on
`Bmax` as `φ ^ m ∘ toGp s`, `φ` being Frobenius, and `ρ s` acts on `T`. 

### `linearFrob_zero_apply`

 Let `ρ` be potentially crystalline and `toGp s` in inertia (`(toGp s, 0)` a Weil pair). On
`Dpcris ρ`, the elements fixed by all `g` near `1`, the map `linearFrob ρ s 0` is the action of
`s`. 

### `linearFrob_mul`

 Multiplicativity of the linear Frobenius: for `ρ` potentially crystalline (`h`) and Weil pairs
`(toGp s, m)` (`hs`) and `(toGp t, k)` (`ht`), one has `β_{st, m+k} = β_{s,m} β_{t,k}`, where
`β_{s,m}` is `linearFrob ρ s m`. 

### `linearFrob_pow`

 For `ρ` potentially crystalline (`h`) and `(toGp s, m)` a Weil pair (`hs`),
`β_{s^n, n m} = β_{s,m}^n` for every natural number `n`, where `β_{s,m}` is `linearFrob ρ s m`. 

### `baseChange_linearFrob`

 Let `ρ`, `ρ'` be potentially crystalline (`h`, `h'`) and let `(toGp s, m)` be a Weil pair
(`hs`), meaning `toGp s` acts on the residue field of Q̄_p's valuation ring as
`x ↦ x ^ (1 / p ^ m)`. Here `linearFrob ρ s m` is the `Bmax`-linear endomorphism of `Bmax ⊗ T` that
equals `φ ^ m s ⊗ ρ s` on `Dpcris ρ` (the elements of `Bmax ⊗ T` fixed by `toGp g ⊗ ρ g` for all `g`
near `1`; potentially crystalline means that they span over `Bmax`), where `φ` is Frobenius. The
claim: if a `ℤ_[p]`-linear map `f : T → T'` satisfies `f ∘ ρ g = ρ' g ∘ f` for all `g` near `1` and
for `g = s` (`hf`), then its base change to `Bmax` intertwines `linearFrob ρ s m` and
`linearFrob ρ' s m`. 

### `commute_coeffEnd_linearFrob`

 For `ρ` potentially crystalline (`h`) and `(toGp s, m)` a Weil pair (`hs`), the action of `a` in
`R` on `Bmax ⊗ T` (`coeffEnd`) commutes with `linearFrob ρ s m`. 

### `linearFrob_twist_cyclotomicGp`

 Let `ρ` be potentially crystalline (`h`), `(toGp s, m)` a Weil pair (`hs`), and let `σ` be the
twist of `ρ` by the power `-d` of the cyclotomic character `χ = cyclotomicGp ∘ toGp` (`hσ`). Then
the operator `β_{s,m} = linearFrob σ s m` of `σ` equals `p ^ (m d)` times that of `ρ`. 

### `IsKilledBy.of_jointly_injective`

 Let `(toGp s, m)` be a Weil pair (`hs`), and let `F` be a filter with `nearOne Γ ⊔ pure s ≤ F`.
Let finitely many `ℤ_[p]`-linear maps `f i : T' → S i` be jointly injective (`hi`), semilinear along
`φ : R' → R` (`hφ`), and equivariant along `F` (`hf`). If the image `P` of `Q` under `φ` kills
`(s, m)` on every `S i` (`IsKilledBy`: the representation is potentially crystalline and
`P(β_{s,m}) = 0`), then `Q` kills `(s, m)` on `T'`.

A form of the exactness of Fontaine's Weil–Deligne functor, for subobjects. 

### `IsCrystalline.linearFrob_eq_one`

 Let `ρ` be crystalline and let `toGp s` lie in inertia, that is, `(toGp s, 0)` is a Weil pair,
so `toGp s` acts trivially on the residue field of Q̄_p's valuation ring. Then `linearFrob ρ s 0` is
the identity. This is the `Bmax`-linear endomorphism of `Bmax ⊗ T` that agrees with `toGp s ⊗ ρ s`
on `Dpcris ρ`.

This is one direction of Fontaine's criterion that a potentially crystalline representation is
crystalline exactly when inertia acts trivially on its Weil–Deligne representation. 

### `IsPotentiallyCrystalline.eventually_linearFrob_eq_one`

 Let `T` be finite and free over `R` and `ρ` potentially crystalline. Then for all `g` with
`toGp g` close enough to `1` (along `nearOne Γ`) and in inertia (`IsWeilPair (toGp g) 0`),
`β_{g,0} = linearFrob ρ g 0` is the identity of `Bmax ⊗ T`. This operator is the `Bmax`-linear
endomorphism of `Bmax ⊗ T` that agrees on `Dpcris ρ` with `toGp g ⊗ ρ g`.

This is a form of the finiteness of the inertia action on Fontaine's Weil–Deligne representation. 

### `baseChangePairing_mem_fixedPeriods`

 For `B` equivariant (`hB_equiv`), the base change of `B` to `Bmax` sends a pair of elements
fixed along `F` to an element fixed along `F`, for the actions `toGp g ⊗ σ g`, `toGp g ⊗ ρ g`,
`toGp g ⊗ ρ' g` on `Bmax ⊗ T''`, `Bmax ⊗ T`, `Bmax ⊗ T'`. 

### `IsAdmissible.of_bilinear`

 Let `B : T'' → T → T'` be a `ℤ_[p]`-bilinear map, equivariant for `σ`, `ρ`, `ρ'` (`hB_equiv`),
whose values span `T'` over `ℤ_[p]` (`h_surj`). If `σ` and `ρ` are admissible along `F` (the
elements of `Bmax ⊗ T''` and `Bmax ⊗ T` fixed along `F` span them over `Bmax`), then so is `ρ'`.

A form of the stability of admissible representations under tensor products and quotients in
Fontaine's formalism. 

### `linearFrob_baseChangePairing`

 Let toGp have open image, let (toGp s, m) be a Weil pair, and let B: T'' × T → T' be an
equivariant ℤ_p-bilinear map of potentially crystalline representations. Its base change satisfies
B(β_{s,m}x, β_{s,m}y) = β_{s,m}B(x, y), where β_{s,m} is `linearFrob σ s m`, `linearFrob ρ s m`,
`linearFrob ρ' s m` on Bmax ⊗ T'', Bmax ⊗ T, Bmax ⊗ T' respectively.

Proves the form of the compatibility of the Weil–Deligne functor with tensor products that is used
here, for bilinear maps only. 

### `IsAdmissible.of_pairing`

 Let `toGp` have open image and `nearOne Γ ≤ F`. Let `T` be finite free over `R` and admissible
along `F`, meaning the elements of `Bmax ⊗ T` fixed by `toGp g ⊗ ρ g` for `F`-almost all `g` span
`Bmax ⊗ T` over `Bmax`. Let the pairing `b` identify `T''` equivariantly with `Hom_R(T, R(c))`,
where `R(c)` is `R` with `Γ` acting through the power `χ ^ c` of the cyclotomic character. Then
`T''` is admissible along `F`. Moreover, for `s` in inertia (`(toGp s, 0)` a Weil pair), a
polynomial that kills `s` on `T` (its value at `linearFrob ρ s 0` vanishes on `Bmax ⊗ T`) kills
`s⁻¹` on `T''`.

Proves the form of Fontaine's stability of admissible representations under twisted duals that is
used here, and, for inertia only, of the compatibility of Weil–Deligne representations with duals
and Tate twists. 


## Crystalline descent from inertia

`New.Period.IsPotentiallyCrystalline.isCrystalline_of_inertia_fixes`: if `ρ` is potentially
crystalline (`New.Period.IsPotentiallyCrystalline`) and `New.Period.linearFrob ρ s 0 = 1` for every
`s` with `toGp s` in inertia, then `ρ` is crystalline (`New.Period.IsCrystalline`).


### `New.Period.IsPotentiallyCrystalline.isCrystalline_of_inertia_fixes`

 Descent: let `ρ` be a potentially crystalline representation of `Γ`, where `toGp : Γ → Gp p` has
open image. Suppose that for every `s` with `toGp s` in inertia (`IsWeilPair (toGp s) 0`),
`linearFrob ρ s 0` is the identity; this map is the `Bmax`-linear endomorphism of `Bmax ⊗ T` that
agrees with `toGp s ⊗ ρ s` on `Dpcris ρ`. Then `ρ` is crystalline, i.e. the elements of `Bmax ⊗ T`
fixed by all of `Γ` span it over `Bmax`. The field fixed by inertia and by a small open subgroup is
unramified, so its integers are Witt vectors, which lie in `Bmax`.

A variant of the criterion that a potentially crystalline representation is crystalline when inertia
fixes its D_pcris. 
