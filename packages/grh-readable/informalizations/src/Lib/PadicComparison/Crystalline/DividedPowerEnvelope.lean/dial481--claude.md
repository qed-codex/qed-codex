---
{
  "module": "src/Lib/PadicComparison/Crystalline/DividedPowerEnvelope.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicComparison/Crystalline/DividedPowerEnvelope.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicComparison/Crystalline/DividedPowerEnvelope.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Divided power envelopes, lifts modulo divided powers, and one divided power variable

For a prime `p` (fixed by the class `New.ThePrime p`) and a `p`-torsion-free, `p`-adically
complete ring `S` (`New.Variety.IsCompleteTorsionFree`), `New.Variety.pdIdeal S` is the ideal of the
`x` with `n ! ∣ x ^ n` for all `n`. The file proves lifting results along `S → S ⧸ pdIdeal S`. It
then constructs the divided power envelope of a subset `J` of `T` and proves its universal property.
Finally it treats one divided power variable `z = t - v`.

## Main definitions and results

* `New.Variety.IsCompleteTorsionFree.monoidHom_lift_bijective`,
  `New.Variety.IsCompleteTorsionFree.existsUnique_witt_lift`: multiplicative maps from a perfect
  monoid, and ring maps from a perfect ring via its Witt vectors, lift uniquely from `S ⧸ pdIdeal S`
  to `S`.
* `New.Variety.IsCompletionBijective.comp_bijective`: maps to a `p`-complete ring extend uniquely
  along a map that is bijective modulo every power of `p` (`New.Variety.IsCompletionBijective`).
* `New.Variety.preEnvelope`, `New.Variety.Envelope`: adjoin the `x ^ n / n !`, `x ∈ J`, inside
  `T ⊗ ℚ`, then complete; `New.Variety.Envelope.existsUnique_lift` is the universal property.
* `New.Variety.exists_preEnvelope_basis`: if `T` has the `B`-basis `u a * v ^ n`, the uncompleted
  envelope of `z = t - v` has the basis `u a * z ^ n / n !`.
* `New.Variety.koszulExact_pd_line`: take an endomorphism `γ` that scales the unit `v` by `1 + q`
  with `p ^ 3 ∣ q`. It must also scale each `u a` with `a ≠ 0` by `1 + η` with `p * η ∣ q`, and
  `u 0 = 1`. Then the sequence `0 → B → E → E → 0` given by `γ - 1` is exact after a base change
  that inverts `q`. The proof uses a shift `S` of the basis such that `(γ - 1) S` is `q * v` times
  `1 - p W` for an endomorphism `W`.

Notions from other files:
* `New.Variety.CrysTest`: the category of `p`-torsion-free, `p`-adically complete `S`-algebras
  (`New.Variety.IsCompleteTorsionFree`); an object `E` is read as its underlying ring.
* `New.Variety.KoszulExact`: for a map `i` and an endomorphism `g`, the map `i` is injective, every
  fixed point of `g` lies in the image of `i`, and `z ↦ g z - z` is onto.

## Relation to the literature

Known; see `Lib.PadicComparison.Crystalline.ComparisonMap` for sources.


 ## Lifts modulo divided powers and the divided power envelope 

 ### Lifting modulo the divided power ideal 

### `frobModPd`

 For p not a unit in S, the ring homomorphism S/𝔡(S) → S/p induced by x ↦ x^p, where 𝔡(S) is
the ideal of elements with divided powers. 

### `IsCompleteTorsionFree.p_mem_pdIdeal`

 In a `p`-torsion-free, `p`-complete ring `S`, `p` has divided powers: `n !` divides `p ^ n`. 

### `IsCompleteTorsionFree.isLocalHom_pdQuotientMk`

 If `S` is `p`-torsion-free and `p`-complete, the quotient map `S → S ⧸ pdIdeal S` is a local
homomorphism: an element whose class is a unit is a unit. 

### `IsCompleteTorsionFree.monoidHom_lift_bijective`

 Let `S` be `p`-torsion-free and `p`-complete, and `M` a commutative monoid on which `x ↦ x ^ p`
is bijective. Composition with the quotient map `S → S ⧸ pdIdeal S` is a bijection from `M →* S`
to `M →* S ⧸ pdIdeal S`. 

### `IsCompleteTorsionFree.existsUnique_witt_lift`

 Let `S` be `p`-torsion-free and `p`-complete, and `b` a perfect ring with `p = 0`. Each ring
map `f : b → S ⧸ pdIdeal S` has a unique lift `g : W(b) → S`: the class of `g x` modulo
`pdIdeal S` is `f` of the zeroth Witt coefficient of `x`, for every Witt vector `x`. 

### `IsCompletionBijective.comp_bijective`

 If a map κ: C → W of S-algebras is bijective modulo every power of p and the S-algebra X is
p-adically complete, then composition with κ is a bijection Hom(W, X) → Hom(C, X). 

### `instance : CoeSort (CrysTest S) Type`

 A test object is read as its underlying type. 

### `instance : HasUniqueDiv E`

 A `p`-torsion-free `p`-complete algebra has no additive torsion: `n` divides `p ^ n` there. 

### `CrysTest.p_eq_zero_mod_pdIdeal`

 In a `p`-torsion-free `p`-complete algebra `E`, `p` vanishes modulo `pdIdeal E`. 

 ### The divided power envelope 

### `preEnvelope`

 For a subset J of T, the T-subalgebra of T ⊗_ℤ ℚ generated by the divided powers x^n/n! with
x in J and n ≥ 0. 

### `Envelope`

 The divided power envelope of T along J: the p-adic completion of `New.Variety.preEnvelope`, as
a p-torsion-free p-complete S-algebra. 

### `Envelope.existsUnique_lift`

 Universal property of the envelope: an S-algebra map h from T to a p-torsion-free p-complete
S-algebra B that sends J into the elements with divided powers factors uniquely through the
canonical map from T to the envelope of J. 

### `Envelope.algebraMap_mem_pdIdeal`

 For a subset J of the S-algebra T and x in J, the image of x in the envelope E of T along J
lies in the ideal 𝔡(E) = `New.Variety.pdIdeal` E: n! divides its n-th power for every n. 

 ## A basis of the envelope of one element and exactness of γ − 1 

### `exists_preEnvelope_basis`

 Let B be a p-torsion-free, p-adically complete A-algebra (`New.Variety.CrysTest`), T a
B-algebra with a B-basis b indexed by I × ℕ with b(a, n) = u a * v ^ n, and z = t − v with t in B.
Then the subalgebra `New.Variety.preEnvelope {z}` of T ⊗ ℚ, generated over T by the z ^ n / n!,
contains elements y n with z ^ n = n! * y n, and the u a * y n form a B-basis c of it. 

### `exists_map_dividedPow_succ`

 Taylor's formula for divided powers in a `p`-torsion-free, `p`-complete algebra `E`: if
`y n = x ^ n / n !` and `γ x = x + p ^ 3 * z`, then
`γ (y (n + 1)) ≡ y (n + 1) + p ^ 3 * z * y n` modulo `p ^ 4 * z`. 

### `IsCompleteTorsionFree.bijective_one_sub_smul`

 If the B-algebra E is p-torsion-free and p-adically complete, then 1 − p • W is bijective for
every B-linear endomorphism W of E. 

### `koszulExact_of_bijective_sub`

 Let `m : N → M` be a split injection (`κ ∘ m = id`) whose image `γ` fixes pointwise. Suppose
that `γ S - S` is bijective for an endomorphism `S` and that `m ∘ κ' - V = S ∘ G` for a bijection
`V`, an endomorphism `G` and a map `κ' : M → N`. Then `m` and `γ` are Koszul-exact
(`New.Variety.KoszulExact`): `m` is injective, every fixed point of `γ` lies in the image of `m`,
and `γ - 1` is onto. 

### `koszulExact_baseChange_of_sub_comp_eq_smul`

 Let `B → E` be `p`-torsion-free, `p`-complete `A`-algebras, `K` an `A`-algebra in which `q` is a
unit, `v` a unit of `E`, `t ∈ B`, and `γ` a `B`-algebra endomorphism of `E` fixing the image of the
inclusion `m : B → E`. Let `κ : E → B` be a `B`-linear left inverse of `m`, and let `S`, `G`, `W` be
`B`-linear endomorphisms of `E` with `γ ∘ S - S = q v (1 - p W)` and `m ∘ (q t κ) - q v = S ∘ G`,
where `v` acts by multiplication. Then after base change to `K` the map `m ⊗ K` is injective, every
fixed point of `γ ⊗ K` lies in its image, and `z ↦ (γ ⊗ K)(z) - z` is onto
(`New.Variety.KoszulExact`); `ULift` only moves the modules to universe `1`. 

### `koszulExact_pd_line`

 Let `B → E` be `p`-torsion-free, `p`-complete `A`-algebras, where `E` has the topological
`B`-basis `u a * y n` (via `j`), `y n = (t - v) ^ n / n !`, `v` a unit, `u 0 = 1`. Let `p ^ 3 ∣ q`
with `q` a unit in `K`, and let `γ` scale `v` by `q + 1` and each `u a` (`a ≠ 0`) by `η + 1` with
`p η ∣ q`. Then `K ⊗ B → K ⊗ E` and `γ` are Koszul-exact: injective, fixed points in the image,
`γ - 1` onto. `ULift` only moves the modules to universe `1`. 
