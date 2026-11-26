---
{
  "module": "src/Lib/ClassField/Places/LocalFields.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Places/LocalFields.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Places/LocalFields.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Local fields: Frobenius, uniformisers, normalised valuation, extensions, unramified characters

A local field is a field `k` whose absolute Galois group `Γ` acts on an algebraic closure `Ω` and
stabilises a valuation subring `A` of `Ω` (`New.IsLocalGalois`). The trace `O = A ∩ k`
(`New.valRingBelow k A`) must be a discrete valuation ring whose residue field has finite order `q`
(`New.residueCard k A`); completeness is not assumed. `A.valuation` is multiplicative (at most 1 on
`A`). For a uniformiser `π` of `k`, the additive valuation `New.ordRat k A : Ωˣ → ℚ` is normalised
so that `π` has order `1`; it is defined on `DiscreteUnits Ω`, which is `Ωˣ` written additively
(`x.toMul` is the unit). `valuationVia k A c` is `A.valuation` of the image of `c : k` in `Ω`.

## Main definitions and results

* `New.IsLocalGalois.frobenius_spec`: for a henselian local field `k`, `Γ` contains an arithmetic
  Frobenius `φ`. The products of a power `φ ^ n` (`n ≥ 0`) with an element of inertia are dense in
  `Γ`, and `A` is integral over `A ∩ k`. The three parts are `New.IsLocalGalois.exists_isFrob`,
  `New.IsLocalGalois.denseRange_frob_pow_mul_inertia` and
  `New.IsLocalGalois.isIntegral_valRingBelow`.
* `New.IsLocalGalois.of_finite`: a finite extension `k'` of `k` is local, and its ramification index
  `e` and residue degree `f` satisfy `e * f = [k' : k]`. Moreover `e = 1` if the group of `k'`
  contains inertia.
* `New.existsUnique_unramified_char`: for a local field `k` and `r ∈ ℚ/ℤ` there is exactly one
  continuous character of its absolute Galois group that is trivial on inertia and sends a given
  Frobenius to `r`. It comes from the action on roots of unity of order dividing `q ^ m - 1`, `m`
  the order of `r`.

Notions from other files:
* `New.IsFrob`: `σ` stabilises the valuation subring `A` and `σ • x ≡ x ^ q` modulo the maximal
  ideal for all `x ∈ A`.
* `New.IsUniformiser`: `π` is a uniformiser of `K` for `A`: an element of `K` lies in the maximal
  ideal of `A` exactly when its valuation is at most that of `π`.
* `New.residueCard k A`: the order of the residue field of A ∩ k (zero if infinite).
* `New.ordRat k A`: the order on Ωˣ normalised on k, chosen so that `n * ordRat k A x = a` exactly
  when `x ^ n` and `π ^ a` have the same valuation, for uniformisers `π` of `k`.
* `New.QZ`: the group ℚ/ℤ; it is given the discrete topology.

## Relation to the literature

Known result: Hilbert ramification theory for infinite Galois extensions, here for local fields.
Places are valuation rings of an algebraic closure acted on by an abstract profinite group, and
local fields are only henselian with finite residue field. Source: J. Neukirch, Algebraic Number
Theory, 1999, I §9, II §§7–9, VI §1; J.-P. Serre, Local Fields, 1979, I §7, IV §2; Stacks Project,
tag 09EE.


 ## Existence of Frobenius; Frobenius and inertia are topological generators 

### `New.isInvariantSubring_valRingBelow_of_forall_mem_decompGroup`

 If every element of `Γ` maps the valuation subring `A` of `Ω` to itself, then `A`, as the
subring `New.valRingBelow Ω A` of `Ω`, is stable under `Γ`. 

### `New.isFrob_iff_forall_smul_residue_eq_pow`

 Let every element of `Γ` map the valuation subring `A` of `Ω` to itself, so that `Γ` acts on
`A` (as the subring `New.valRingBelow Ω A`) and on its residue field. Then `g` is a Frobenius
element for `q` at `A` (`New.IsFrob`) exactly when it acts on the residue field as `y ↦ y ^ q`. 

### `New.IsLocalGalois.frobenius_spec`

 Let `Γ` be the absolute Galois group of a henselian local field `K`, `A` the valuation ring of
the algebraic closure `Ω`, and `q` the order of the residue field of `A ∩ K`.
(a) There is an arithmetic Frobenius: `φ ∈ Γ` with `φ • x ≡ x ^ q` modulo the maximal ideal.
(b) For every such `φ`, the products `φ ^ n * i` (`n ≥ 0`, `i` in inertia) are dense in `Γ`.
(c) Every element of `A` (here `New.valRingBelow Ω A`) is integral over `A ∩ K`
(`New.valRingBelow K A`). 

### `New.IsLocalGalois.denseRange_frob_pow_mul_inertia`

 For an arithmetic Frobenius `φ`, the products `φ ^ n * i` (`n : ℕ`, `i` in the inertia group
of `A`) are dense in `Γ`. 

### `New.IsLocalGalois.isIntegral_valRingBelow`

 Every element of `A` (as `New.valRingBelow Ω A`) is integral over `New.valRingBelow K A`. 


## Uniformisers and the normalised additive valuation

The idea: the product of the conjugates of x ∈ Ω lies in k and has the valuation of a power of x
(`New.Cohomology.exists_val_eq_pow_index`), so the order of x is a rational number.


### `IsUniformiser.valuationVia_lt_one`

 A uniformiser `π` of `k` lies in the maximal ideal of `A`: its valuation is below `1`. 

### `isUniformiser_iff_irreducible`

 If A ∩ k is a discrete valuation ring, then π ∈ k is a uniformiser for A if and only if π
lies in A ∩ k and is irreducible there. 

### `Cohomology.exists_val_eq_pow_index`

 If all of Γ = Gal(Ω / k) maps the valuation subring A to itself, then for x ∈ Ω the power
x ^ m, with m the number of conjugates of x (the index of its stabiliser), has the valuation of an
element of k. 

### `IsUniformiser.card_quotient_span_eq_pow`

 If π is a uniformiser of k for A and x in the valuation ring 𝒪 of k has the valuation of
π^a, then #(𝒪/x) = q^a, with q the order of the residue field. 

### `IsUniformiser.exists_valuationVia_eq_zpow`

 A non-zero element of the local field k has the valuation of an integral power of the
uniformiser π. 

### `IsUniformiser.exists_addMonoidHom_valuation_pow_eq_iff`

 Let `Γ` be the Galois group of `Ω / k`, where `Ω` is algebraically closed of characteristic 0,
`Γ` stabilises the valuation subring `A`, and `A ∩ k` is a discrete valuation ring with finite
residue field (`IsLocalGalois`). If `k` has a uniformiser `π`, then there is an additive map `f`
from `Ωˣ` (written additively as `DiscreteUnits Ω`) to `ℚ` with the following property, which
defines `New.ordRat`: for every uniformiser `p` of `k`, every `x`, every `n : ℕ` and every `a : ℤ`,
the `A`-valuation of `x` raised to the power `n` equals `valuationVia k A p ^ a` exactly when
`n * f x = a`. 

### `IsUniformiser.valuation_pow_eq_zpow_iff_mul_ordRat_eq`

 Let k be a henselian local field with uniformiser π. For x ∈ Ω^×, n ∈ ℕ and a ∈ ℤ, x^n and π^a
have equal A-valuation if and only if n·ord(x) = a, where ord is the order normalised on k. 

### `IsUniformiser.ordRat_eq_one`

 A uniformiser `π` of `k` has order `1` for the order `New.ordRat k A` normalised on `k`. 

 ## Finite extensions, ramification index and residue degree 

### `valuation_residueCard_lt_one`

 The order `q = residueCard k A` of the residue field of `O = A ∩ k` lies in the maximal ideal
of `A`: its valuation `A q` is less than `1`. 

### `IsRamificationData`

 For fields `k` and `k'` inside `Ω`, at the valuation subring `A`: the number `e` is the
ramification index and `f` the residue degree of `k'` over `k`, and their product is `n`. 

### `IsRamificationData.mul_eq`

 The product of `e` and `f` is `n`. 

### `IsRamificationData.residueCard_eq`

 The orders of the residue fields satisfy `q' = q ^ f`. 

### `IsRamificationData.ordRat_eq`

 The normalised additive valuations satisfy `ord' = e • ord`. 

### `IsLocalExtension`

 The field `k'` inside `Ω` is local with group `V ≤ Γ`, and its ramification index, residue
degree and valuation ring are those of an extension of `k` of degree `V.index`. 

### `IsLocalExtension.isLocalGalois`

 The field `k'` is local with group `V`. 

### `IsLocalExtension.exists_isRamificationData`

 There are `e` and `f` with `e * f = V.index`, and `e = 1` if `V` contains inertia. 

### `IsLocalExtension.card_quotient`

 For the valuation rings, `#(O' / n) = #(O / n) ^ V.index`; an infinite order is `0`. 

### `ordRat_eq_nsmul_ordRat_of_valuationVia_eq_zpow`

 Let `k` be local (the instance `G`) and `k'` local with group `V`, over `k` inside `Ω`, with
uniformisers `π` of `k` and `π'` of `k'`. If `π` has the valuation of `π' ^ e`, then the orders
normalised on `k'` and on `k` satisfy `ordRat k' A = e • ordRat k A`. 

### `index_le_of_isFrob_pow_mem`

 If an open subgroup `V` of `Γ` contains inertia and the power `σ ^ f` (`f ≠ 0`) of an
arithmetic Frobenius `σ`, then `V` has index at most `f`. 

### `IsLocalGalois.isLocalExtension`

 A finite extension of a local field is local. Here `Γ` is the Galois group of an algebraically
closed field `Ω` of characteristic 0 over `k`, stabilising the valuation subring `A`, with `A ∩ k` a
discrete valuation ring with finite residue field. Given an open subgroup `V` of `Γ` and a finite
extension `k'` of `k` inside `Ω` with Galois group `V`, the claim is that `k'` is local in the same
sense with group `V` and ring `A`, and that its ramification index, residue degree and valuation
ring are those of an extension of `k` of degree `V.index`. 

### `IsLocalGalois.of_finite`

 A finite extension of a local field is local: `New.IsLocalGalois.isLocalExtension`, with `k'` by
default the fixed field in `Ω` of the open subgroup `V` of `Γ`. 

### `IsLocalGalois.isLocalExtension_fixedFieldOf`

 The fixed field of an open subgroup `V` of `Γ` is local, a finite extension of `k`
(`New.IsLocalExtension`). 

### `IsLocalGalois.exists_ordRat_eq_intCast`

 Over a local field `k`, an element of `Ωˣ` fixed by the inertia group has integral order,
for the order normalised on `k`. 


## Unramified characters with a given value at Frobenius

* `New.exists_openNormalSubgroup_apply_eq`: a continuous map from `Γ × Y` (`Γ` a Galois group as in
  `New.IsProGalois`, `Y` compact) to a discrete space satisfies `f (u, y) = f (1, y)` on an open
  normal subgroup.


### `exists_openNormalSubgroup_apply_eq`

 For the Galois group `Γ` of `Ω` over `k` (`New.IsProGalois`), a compact space `Y`, a discrete
space `X` and a continuous `f : Γ × Y → X`, there is an open normal subgroup `U` of `Γ` with
`f (u, y) = f (1, y)` for all `u ∈ U` and all `y`. 

### `existsUnique_unramified_char`

 Let `Γ` be the absolute Galois group of a local field `k` and `φ` an arithmetic Frobenius
(`New.IsFrob` for `q = residueCard k A`). For every `r` in `QZ = ℚ/ℤ` there is exactly one
continuous character `χ : Γ → ℚ/ℤ` (an element of `New.QZChar Γ`, applied as `χ.val`) that is
trivial on inertia and has `χ φ = r`. 
