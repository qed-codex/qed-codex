---
{
  "module": "src/Lib/ClassField/LocalDuality/CrystallineDuality.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/LocalDuality/CrystallineDuality.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/LocalDuality/CrystallineDuality.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Classes of Galois lattices, pairings and local duality for crystalline cocycles

The file studies classes of Galois lattices given by admissibility, allowed Hodge–Tate jumps and
polynomials that kill inertia. It shows how a class changes under twisted duals, tensor products and
jointly injective maps. It also defines pairings `Y × L → ℤ/p^m(1)` and the extensions of `O` by
`(Y ⊗ L)^∨(1)` that they give. At `ℓ`, it proves local duality statements for potentially
crystalline lattices: a perfect `ℤ_[ℓ]`-pairing of a lattice with its dual, the sizes of the
crystalline cocycles modulo `ℓ ^ m` and a divisibility of indices. Here Z_f denotes the crystalline
cocycles `New.Period.crysCocycles`.

## Main definitions and results

* `New.Lift.InClass`: the class of lattices given by admissibility, allowed jumps and polynomials
  that kill inertia.
* `New.Lift.Pairing`: an `O(1)`-valued form on `Y ⊗ L` whose coboundary is `p ^ m` times a
  crystalline cocycle.
* `New.Lift.cupOrthogonal`: the functions `Γ → L` whose cup products with crystalline cocycles of
  the lattices of a class are coboundaries.
* `New.Lift.dualDefect`: the length of the crystalline cocycles of `L` modulo those in
  `New.Lift.cupOrthogonal`.
* `New.Period.IsPotentiallyCrystalline.index_mul_index_dual`: the sizes of Z_f(L) and Z_f(L') modulo
  `ℓ ^ m`.
* `New.Period.IsPotentiallyCrystalline.relIndex_dvd_of_orthogonal`: a divisibility of indices from
  local Tate duality, which bounds the cocycles of `L / ℓ ^ m` orthogonal to a subgroup of Z_f(L').

Notions from other files, for a representation `ρ` of `Γ` on an `O`-module `T`:
* `New.Period.IsAdmissible ρ F`: the elements of `Bmax ⊗ T` fixed by `F`-almost all `g` span
  `Bmax ⊗ T` over `Bmax`; `New.Period.nearOne Γ` is the pull-back to `Γ` of the neighbourhoods of
  `1` in `G_p`.
* `New.Period.IsPotentiallyCrystalline ρ`: `ρ` is admissible along `New.Period.nearOne Γ`.
* `New.Period.IsKilledBy ρ s m Q`: `ρ` is potentially crystalline and `Q` evaluated at the linear
  Frobenius `New.Period.linearFrob ρ s m` is zero.
* `New.Period.IsWeilPair s 0`: `s` lies in the inertia group of `G_p`.
* `New.Period.jump ρ γ u`: the multiplicity of the Hodge–Tate jump `u : ℤ` of `ρ` at the
  `ℤ_[p]`-algebra map `γ : O → ℂ_[p]`. It is the dimension over Q̄_p (zero if infinite) of the space
  of `γ`-semilinear maps f : T → ℂ_p with f(gx) = χ(g)^(−u)·g f(x) for g near 1.
* `New.Period.HasJumps ρ γ J`: for every integer `u`, the multiplicity `jump ρ γ u` equals the
  number of times `u` occurs in the multiset `J`.

## Relation to the literature

Known result: Local Tate duality in degree 1 as an upper bound for orthogonal cocycle groups. Only
an inequality is proved. The bound is proved by Kummer theory and dévissage when `Γ` acts by
elements of `ℓ`-power order. For a general finite module `M`,
`New.DiscreteModule.local_duality_card_dvd` gives only a divisibility, by descent from an open
subgroup `U` of index prime to `#M`. It takes as a hypothesis a largest orthogonal pair of cocycle
groups over `U`, and this file supplies that pair for the reductions of crystalline cocycles
(`h_orth`, `h_max` in `card_pairingAnnihilator_mul_card_dvd`). Perfectness of the duality and the
Euler characteristic formula are outside the scope of this file, and no result in it uses them.
Source: J.-P. Serre, Galois Cohomology (1997), II §5.2 Thm 2 and §5.7; J. S. Milne, Arithmetic
Duality Theorems (2nd ed. 2006), I 2.3, 2.8.

See also `Lib.PadicHodge.Crystalline.Regularity` and `Lib.PadicHodge.ArtinSchreierSequence`.



## Classes of Galois lattices under duals and tensor products; pairings

The group `Γ` acts on periods through the map `toGp : Γ → G_p` given by `[OverGp Γ p]`. The results
on twisted duals, tensor products and jointly injective maps assume that `O` is a domain, finite
over `ℤ_[p]`.


### `GalLattice`

 A finite free O-module, with compatible Z_p-module structure, together with an O-linear
representation of the group Γ on it. 

### `GalLattice.Carrier`

 The underlying module `Λ`. 

### `GalLattice.addCommGroup`

 `Λ` is an abelian group. 

### `GalLattice.moduleO`

 `Λ` is an `O`-module. 

### `GalLattice.moduleZp`

 `Λ` is a `ℤ_p`-module. 

### `GalLattice.isScalarTower`

 The two module structures are compatible. 

### `GalLattice.free`

 `Λ` is free over `O`. 

### `GalLattice.module_finite`

 `Λ` is finitely generated over `O`. 

### `GalLattice.ρ`

 The `O`-linear action of `Γ` on `Λ`. 

### `instance : CoeSort (GalLattice O Γ) Type`

 A lattice is read as its underlying type. 

### `GalLattice.tateDual`

 The twisted dual L^∨(1) = Hom_O(L, O(1)) of a lattice L, with Γ acting on O(1) through the
cyclotomic character. 

### `InClass`

 The lattice `Y` lies in the class given by a filter `F` on `Γ`, a relation `K`, and finite sets
`U g` of integers for the `ℤ_[p]`-algebra maps `g : O → ℂ_[p]`. The periods of `Y` fixed by almost
all elements of `Γ` for the supremum of `F` and the filter 'near 1' span
(`New.Period.IsAdmissible`); every Hodge–Tate jump of `Y` at `g` lies in `U g`; and if `K s Q` holds
and `toGp s` is in inertia, the polynomial `Q` over `O` kills `s` on the periods of `Y`
(`New.Period.IsKilledBy`). For `K = ⊥` the last condition is empty. 

### `InClass.mem_of_jump_ne_zero`

 The jumps of a lattice in the class at the embedding `g` lie in `U g`. 

### `InClass.isKilledBy_of_isWeilPair`

 If `K s Q` holds and `toGp s` is in inertia, then `Q` kills `s` on a lattice in the class. 

### `InClass.isPotentiallyCrystalline`

 If the lattice `Y` lies in the class `InClass F K U`, then its representation `Y.ρ` is
potentially crystalline. Lying in the class means its periods are admissible, its Hodge–Tate jumps
lie in `U`, and it satisfies the killing condition `K`. 

### `GalLattice.tensor`

 The tensor product Y ⊗_O L of two lattices, with the diagonal action of Γ. 

### `Pairing`

 A pairing of Y and L modulo p^m, with m = `exponent`: an O-linear ψ = `integralForm` :
Y ⊗ L → O(1) with gψ − ψ = p^m c(g) for a crystalline cocycle c = `cocycle`, and a Z_p-linear
f = `toZp` : O → Z_p. 

### `Pairing.exponent`

 The exponent `m` of the modulus `p ^ m`. 

### `Pairing.integralForm`

 An `O`-linear form `ψ : Y ⊗ L → O(1)`, an element of `Z = (Y.tensor L).tateDual`. 

### `Pairing.toZp`

 A `ℤ_p`-linear map `f : O → ℤ_p`; the pairing is its composite with `ψ`, modulo `p ^ m`. 

### `Pairing.cocycle`

 A crystalline cocycle `c` of `Z`; it defines an extension `Z ⊕ O` of `O` by `Z`. 

### `Pairing.pow_smul_cocycle`

 The coboundary of `ψ` is `p ^ m` times the cocycle. 

### `Pairing.modPairing`

 The Z_p-bilinear pairing Y × L → Z_p/p^m sending (y, l) to f(ψ(y ⊗ l)) modulo p^m, for the
form ψ and the functional f: O → Z_p of P. 

### `Pairing.IsCupCoboundary`

 The cup product (g, h) ↦ b(a(g), g·c(h)) for b = `P.modPairing`, with Z/p^m(1) embedded in
Q̄_p^×, is the coboundary of a continuous cochain Γ → Q̄_p^×. 

### `cupOrthogonal`

 The annihilator `L^{⊥𝒬}` of a class `𝒬` of lattices: the `O`-module of functions `c : Γ → L`
(not assumed to be cocycles) such that for every lattice `Y` in `𝒬`, every `m`, every pairing
`P : Y × L → ℤ/p^m(1)` (`New.Lift.Pairing`) and every crystalline cocycle `a` of `Y`
(`New.Period.crysCocycles`), the cup product of `a` and `c` under `P` is a coboundary
(`New.Lift.Pairing.IsCupCoboundary`). 

### `dualDefect`

 The defect on the dual side: the length over `O`, not normalised, of the crystalline cocycles of
`L` modulo those in the annihilator `cupOrthogonal 𝒬 L` of the class `𝒬` under cup products. 

### `dualDefect_eq_zero_iff`

 The defect vanishes exactly when all crystalline cocycles of `L` are orthogonal to `𝒬`. 

### `HasCupExponent`

 The power `p ^ e` carries every crystalline cocycle of `L` into the annihilator
`cupOrthogonal 𝒬 L` of the class `𝒬` under cup products. 

### `HasCupExponent.mono`

 A larger power of `p` also carries the crystalline cocycles into `cupOrthogonal 𝒬 L`. 

### `Pairing.extensionForm`

 The O-valued pairing ((λ, o), t) ↦ (p^m λ + oψ)(t) of the extension of O by (Y ⊗ L)^∨(1)
along the cocycle c of P with Y ⊗ L. 

### `Pairing.extensionForm_equivariant`

 The pairing β = `P.extensionForm` of the extension of O by (Y ⊗ L)^∨(1) with Y ⊗ L is
equivariant into the Tate twist: β(gx, gt) = χ(g)·β(x, t) for g in Γ, where `g` acts on the
extension (`extensionRep`) by (λ, o) ↦ (gλ + o·c(g), o), with χ the cyclotomic character. 

### `Pairing.modPairing_rho`

 Let `Y`, `L` be lattices over the `ℤ_[p]`-algebra `O` with an action of the group `Γ`. The
pairing `Y × L → ℤ_p / p ^ m` of `P` is equivariant into the Tate twist: `⟨g y, g l⟩ = χ(g) ⟨y, l⟩`,
with `χ` the cyclotomic character. 

### `InClass.of_cyclotomic_pow`

 If every `g : Γ` acts on `L` by the scalar `χ g ^ c`, where `χ` is the cyclotomic character,
then `L` satisfies `InClass F ⊥ U` for every filter `F`, with `U` equal to `{-c}` at every embedding
`O → ℂ_[p]`. This means its periods are admissible, its only Hodge–Tate jump is `-c`, and the empty
relation `⊥` imposes no killing condition. 

### `jump_tateDual`

 Let `toGp` have open image and L be potentially crystalline. At each embedding γ, the
multiplicity of the jump u of the twisted dual L^∨(1) equals that of the jump −u − 1 of L. 

### `InClass.of_jointly_injective`

 A lattice `Y` with jointly injective equivariant `O`-linear maps to finitely many lattices of a
class lies in that class. 

### `InClass.dual`

 The twisted dual `Hom(Y, O(1))` of a lattice of a class lies in the class with the same filter
`F`. Its jumps at `g` are among the `-u - 1` with `u ∈ U g`, and `Q` kills `s` on it if `K s⁻¹ Q`
holds and `toGp s` is in inertia. 

### `InClass.tensor`

 Let `O` be a domain, finite over `ℤ_[p]`. Let `Y` lie in the class `InClass F K U` and `L` in
`InClass F K' U'`, with the same filter `F`. Such a class says that the periods fixed by almost all
elements of `Γ` (for `F` and 'near 1') span, that every Hodge–Tate jump at `g` lies in `U g`, and
that `K s Q` with `toGp s` in inertia forces `Q` to kill `s`. Then `Y ⊗ L` lies in the class with
filter `F`, allowed jumps `U g + U' g` at `g`, and the empty relation `⊥`, so no killing condition.

This is a form of the additivity of Hodge–Tate weights in tensor products: an inclusion of sets of
weights, without multiplicities. 

### `exists_isKilledBy_tateDual_tensor`

 Let `O` be a domain, finite over `ℤ_[p]`. Let `Y` lie in the class `InClass F K U` and `L` in
`InClass F K' U'`, with the same filter `F`. Such a class says that the periods fixed by almost all
of `Γ` (for `F` and 'near 1') span, that the Hodge–Tate jumps at `g` lie in `U g`, and that a
relation `K s Q` with `toGp s` in inertia forces `Q` to kill `s`. If `toGp s` is in inertia and `K`,
`K'` relate `s` to the images in `O[X]` of monic `q`, `r` over `ℤ_[p]`, then some monic `e` over
`ℤ_[p]` with degree at most `deg q * deg r` kills `(s⁻¹, 0)` on the twisted dual `(Y ⊗ L)^∨(1)`:
evaluated at the linear Frobenius of `s⁻¹`, it vanishes on `Bmax ⊗ (Y ⊗ L)^∨(1)`. 


## Perfect pairings and local duality for crystalline cocycles

`R` is the integer ring of a finite extension of `ℚ_ℓ`, and `Γ` maps by `𝒥.toGp` with open image to
the absolute Galois group of `ℚ_ℓ`. `L` and `L'` are potentially crystalline lattices. `b`
identifies `L'` equivariantly with the `ℤ_[ℓ]`-dual of `L`, twisted by the cyclotomic character `χ`.


### `Selmer.exists_perfect_pairing`

 There is a `ℤ_[ℓ]`-linear form `f` on `R` such that `(φ, x) ↦ f (φ x)` is a perfect pairing
over `ℤ_[ℓ]` between the `R`-dual of the lattice `L` and `L`. 

### `Period.IsPotentiallyCrystalline.index_mul_index_dual`

 The crystalline cocycles Z_f(L), Z_f(L') (`crysCocycles`) of two potentially crystalline
lattices in duality `b` have complementary sizes: the orders of Z_f(L) / ℓᵐ Z_f(L) and Z_f(L') / ℓᵐ
Z_f(L') multiply to `(ℓ ^ m) ^ (d (n + 2))`. Here `d` is the rank of `L` over `ℤ_[ℓ]`, and `n` is
the index of the image of `𝒥.toGp`.

The proof uses only the duality of Hodge–Tate jumps (`jump_eq_of_pairing`) and the rank formula
`crysCocycles.finrank_eq`. Classically the same count follows from Bloch–Kato duality for
crystalline classes and Tate's Euler characteristic formula, but neither is used here; only the
product of the orders is stated, not mutual annihilation. 

### `Period.exists_dual_reduction`

 The pairing `b` reduced modulo `ℓᵐ` gives a map from `L'` onto the dual `Hom(V, Q̄_ℓ^×)` of
`V = L / ℓᵐ L`, with kernel `ℓᵐ L'`. 

### `Period.exists_div_rootOfUnity`

 Division by `l ≠ 0`: some additive `E : ℤ_ℓ → Q̄_ℓ^×`, killed by a power of `ℓ`, takes at `l z`
the value of `zmodPowToUnits m` at the class of `z`. 

### `Period.cupModPow`

 The cup product `(g, h) ↦ b (g c(h)) (a g)` of maps `a : Γ → L` and `c : Γ → L'`, reduced
modulo `ℓᵐ` and embedded in `Q̄_ℓ^×` by `zmodPowToUnits m`. 

### `Period.IsCupOrthogonal`

 A map `s : Γ → V`, with `q : L → V` a reduction modulo `ℓᵐ`, is a continuous cocycle that is
orthogonal under the cup product to the group `H` of maps `Γ → L'`. 

### `Period.IsCupOrthogonal.mem_Z1`

 `s` is a continuous cocycle. 

### `Period.IsCupOrthogonal.exists_lift`

 The cup products of some lift of `s` with the elements of `H` are 2-coboundaries. 

### `Period.IsPotentiallyCrystalline.exists_twist_jump_pos`

 Let `L`, `L'` be potentially crystalline lattices over `R`, and let `b : L' ≃ Dual L` be a
pairing with `b (ρ' g x) (ρ g y) = χ g • b x y`. Let `q : L → V` be a `Γ`-equivariant map to a
finite discrete `Γ`-module, and let `U` be a subgroup whose `OverGp` structure is the restriction of
that of `Γ`. Then there are potentially crystalline `R`-linear actions `σ`, `σ'` of `Γ` on `L`, `L'`
such that `b` still satisfies the same twisted pairing identity and `q` is still equivariant for
`σ`. Moreover, every Hodge–Tate jump `k` of `σ'` restricted to `U`, read over `ℤ_[ℓ]` at the
standard embedding `ℤ_[ℓ] → ℂ_[ℓ]`, with nonzero multiplicity is positive. 

### `Period.IsPotentiallyCrystalline.cup_mem_B2_of_jump_pos`

 Suppose `𝒥.toGp` is an open embedding, `L` and `L'` are potentially crystalline, and `b`
identifies `L'` with the `ℤ_[ℓ]`-dual of `L` so that `b (g x) (g y) = χ g • b x y`. If every
Hodge–Tate jump `k` of `L'` with nonzero multiplicity (over `ℤ_[ℓ]`, at the inclusion into `ℂ_[ℓ]`)
is positive, then the cup product modulo `ℓᵐ` of a crystalline cocycle `c` of `L'` with a
crystalline cocycle `w` of `L` is a 2-coboundary. Here the cup product is the map
`(g, h) ↦ ζ^(b (c g) (g • w h))`, with the pairing reduced modulo `ℓ^m` and `ζ` the chosen primitive
`ℓ^m`-th root of unity (`zmodPowToUnits m`), and the coboundary is for `Γ` acting on the units of
Q̄_ℓ through `𝒥.toGp`. 

### `Period.IsPotentiallyCrystalline.card_range_reducedCocycle_mul`

 Suppose `𝒥.toGp` is an open embedding, `L` and `L'` are potentially crystalline, and `b`
identifies `L'` with the `ℤ_[ℓ]`-dual of `L` so that `b (g x) (g y) = χ g • b x y`. Let `q : L → V`
and `r : L' → V'` be `Γ`-equivariant additive maps into discrete modules, with kernels `ℓ^m L` and
`ℓ^m L'`. Then the number of cocycles `q ∘ c` (for `c` a crystalline cocycle of `L`) times the
number of cocycles `r ∘ c'` (for `c'` a crystalline cocycle of `L'`) equals `((ℓ^m)^n)^(2 + i)`,
where `n` is the `ℤ_[ℓ]`-rank of `L` and `i` is the index of the range of `𝒥.toGp`. 

### `Period.card_quotient_span_localFieldOf`

 In the local field cut out by `toGp`, of degree `n` over `ℚ_ℓ` (`n` is the index of the image of
`𝒥.toGp`), the integers modulo `ℓ` have `ℓⁿ` elements. 

### `Period.card_range_dvd_card_map_mul_index`

 For an additive map `f` and a subgroup `H` of its source, the size of the range of `f` divides
the size of the image of `H` times the index of `H`. 

### `instMulSemiringActionPadicAlgCl`

 `Γ` acts on `Q̄_ℓ` through `𝒥.toGp`. 

### `Period.dual_reduction_equivariant`

 The reduction `r` of the pairing `b` modulo `ℓᵐ` is an equivariant map from `L'` to the dual
`Hom(V, Q̄_ℓ^×)` of `V`. Here `Γ` acts on `Q̄_ℓ` through `𝒥.toGp`. 

### `Period.IsPotentiallyCrystalline.card_pairingAnnihilator_mul_card_dvd`

 Local duality for potentially crystalline Galois lattices `L`, `L'` (`hL`, `hL'`), with
`b : L' ≃ Hom(L, ℤ_ℓ)` satisfying `b (g x) (g y) = χ g • b x y`, and `𝒥.toGp` an open embedding
(`hj`). Let `V = L / ℓᵐ L` (via `q`), whose dual is `L' / ℓᵐ L'` through `r` (the reduction of `b`).
For a group `Y` of cocycles of `V.cartierDual = Hom(V, Q̄_ℓ^×)`, with annihilator `Y^⊥` under the
cup product, `#Y^⊥ · #Y` divides `#V ^ (2 + n)`, with `n` the index of the image of `𝒥.toGp` (the
degree of the local field). Here `Γ` acts on `Q̄_ℓ` through `𝒥.toGp`, and the `IsLocalGalois`
instance follows from `hj` (`isLocalGalois_of_isOpenEmbedding`). 

### `Period.IsPotentiallyCrystalline.relIndex_dvd_of_orthogonal`

 The inequality of local duality. Suppose `𝒥.toGp` is an open embedding of `Γ` into the Galois
group of `ℚ_ℓ`, `L` and `L'` are potentially crystalline lattices in perfect equivariant duality `b`
into `ℤ_ℓ(1)`, and `q` presents the finite module `V = L / ℓᵐ L` as a `Γ`-module. Let `A` be the
image under `q` of the crystalline cocycles `Z_f(L)` (`crysCocycles`), as maps `Γ → V`; if the
elements of `A` and of `S` are continuous cocycles orthogonal to `H` under the cup product built
from `b` modulo `ℓᵐ`, then `[S : S ∩ A]` divides `[Z_f(L') : H ∩ Z_f(L')]`.

One divisibility in Bloch–Kato duality for crystalline classes. 
