---
{
  "module": "src/Lib/Shimura/Eigenspace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/Eigenspace.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/Eigenspace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Eigenquotients for Hecke eigensystems and the Galois representations they cut out

Let `ρ i` be finitely many finite-dimensional `ℚ_ℓ`-representations of `Γ`, with operators `T i s`
and scalars `θ s` in `ℚ̄_ℓ`. The eigenquotient is the largest quotient of `ℚ̄_ℓ ⊗ ⨁ V i` on which
each `T i s` acts by `θ s`. It is given in a basis by `r : Γ → GL_N(ℚ̄_ℓ)` and maps `F i`. If the
`ρ i` are crystalline, then it is crystalline, and a relation between `T` and Frobenius gives a
polynomial that kills Frobenius on it. Suppose moreover that the `T i s` commute with each other and
with `Γ`, and that `γ : ℚ̄_ℓ → ℂ_ℓ` agrees with `a ∈ Gal(ℚ̄_ℓ/ℚ_ℓ)`. If `u` is not a Hodge–Tate jump
of `r` at `γ`, then some polynomial in `T` that is `1` at the conjugate eigenvalues `a ∘ θ` kills
the vectors of weight `u`. These results are applied to the `ℓ`-adic cohomology of a
`New.Variety.Model` to obtain a Galois representation from a system `θ` of Hecke eigenvalues.

## Overview of this theory

Let `E` be a CM field strictly containing `K₀ = ℚ(√-d)`, with `d ≡ 3` mod 4. Let `v₀` be the base
infinite place of a CM type `Φ` of `E`, and let `𝔑` be a nonzero neat level in `𝓞_E`. A finite place
`w` of `E` over a place `u` of `K₀` is *safe* if `u` is split and prime to `d`, and `𝔑` is prime to
`w` and `ū`. The unitary similitude group, of rank `n ≥ 1`, has signature `(1, n - 1)` at `v₀` and
is definite at the other infinite places.

* `New.Variety.exists_model`: an integral model `Z` of Kuga–Sato type for this group, with level
  covers and the congruence relation at safe places. It lives over a localisation `R ⊆ E` of `𝓞_E`
  whose maximal ideals lie over primes good for the PEL data. The inputs are PEL data
  (`New.Variety.exists_pel`) and a family of abelian schemes over such `R`
  (`New.Variety.ThetaNull.nonempty_universalFamily`), for which no universal property is proved. If
  `E` contains a primitive root of unity of order `7! = 5040`, the PEL data exist for a suitable CM
  type and for every nonzero `𝔑` divisible by an integer `N ≠ 0`, which can be taken prime to any
  given finite set of places.
* `New.Variety.exists_isCoefficientSystem`: let `n` be odd, `κ` a weight, and `Φ` a CM type in which
  `Φ v₀` differs on `K₀` from every other `Φ v`. Take a Hecke eigenform of neat level on the
  definite side, with coefficients in an extension of the weight `κ` to `GL_n(E)` that the theorem
  supplies. At one split place it is of cuspidal type. At another split place it is spherical, and
  there the level is pro-`p` Iwahori, `p` being the residue characteristic of that place. Then its
  Hecke eigenvalues `θ` at safe places occur, in the sense of `New.Variety.OccursInWeight`, in
  weight `z + μ` for each jump `z` of `κ` at `Φ v₀`. The jumps are integers given by `New.jumps`.
  Here `μ ∈ ℕ` does not depend on the form or the level.
* `New.Variety.Model.exists_galois_rep`: let `ℓ` be a prime, `ιℓ : ℂ ≃ ℚ̄_ℓ`, and `θ` a system of
  Hecke eigenvalues at safe places. Let `R` be a localisation of `𝓞_E` at elements prime to the safe
  places. Take a model `Z` over `R` and weights `h ≥ 0` in which `θ` occurs. Then there is a
  continuous `ρ : Gal(Ē/E) → GL_m(ℚ̄_ℓ)` of undetermined dimension `m`; the proof cuts it out of the
  cohomology of `Z`. At safe places `ρ` is unramified or crystalline, and the Hecke polynomial of
  `ιℓ ∘ θ` kills geometric Frobenius. If the place over `ℓ` induced by `ιℓ` and the given embedding
  of `E` into `ℂ` is safe, the jumps (Hodge–Tate weights) of `ρ` at that embedding include the given
  weights. Other embeddings and multiplicities are not controlled.

This theory proves the cases that are used of PEL integral models (Kottwitz) and of the geometric
step in the Galois representations of cuspidal forms on `GL_n` (Shin). A direct comparison of two
finite counts replaces the description of automorphic forms on unitary groups via `GL_n` (Labesse).
No moduli functor is represented, nothing is transferred to `GL_n`, and no dimension is computed
here.

1. `ComplexTheta`, `AbelianScheme`, `ThetaGroup`, `Uniformisation`: theta functions and the complex
   uniformisation.
2. `GoodReduction`, `ThetaNormality`, `ArcExtension`: good reduction along a valuation ring of `ℂ`.
3. `ThetaModuli`, `Deformation`: the closure of the theta-null points of the PEL abelian varieties
   carries a family of abelian schemes and is smooth.
4. `HeckeTower` (the list of properties of a model), `CongruenceRelation`, `IntegralModel`: level
   covers, the congruence relation and the model.
5. `TraceFormula`, `Transfer`: the comparison with the definite unitary group. Last, `Eigenspace`:
   the Galois representation.

## Main definitions and results

* `New.Variety.IsEigenQuotient`, `New.Variety.exists_isEigenQuotient`: the definition; existence and
  continuity.
* `New.Variety.IsEigenQuotient.isCrystalline`: `r` is crystalline if the `ρ i` are.
* `New.Variety.IsEigenQuotient.isKilledBy`: a relation between `T` and Frobenius gives a polynomial
  that kills Frobenius on `r`.
* `New.Variety.IsEigenQuotient.exists_sum_baseChange_eq_zero_of_jump_eq_zero`: let the `ρ i` be
  crystalline and the `T i s` commute with each other and with `Γ`. If `u` is not a Hodge–Tate jump
  of `r` at an embedding `γ` given by `a ∈ Gal(ℚ̄_ℓ/ℚ_ℓ)`, some polynomial in `T` that is `1` at
  `a ∘ θ` kills the vectors of weight `u`.

Notions from other files:
* `New.Period.IsCrystalline`: T is crystalline: the elements of B⊗T fixed by all of Γ span B⊗T over
  B.
* `New.HasHodgeTateWeight`: The element y of C_p⊗T (over Z_p) has Hodge–Tate weight u:
  (j(g)⊗ρ(g))y = χ(j(g))^(−u)·y for all g in Γ, with χ the cyclotomic character.
* `New.Period.jump`: The multiplicity of the Hodge–Tate jump u at γ: the dimension over Q̄_p (zero
  if infinite) of the space `New.Period.hodgeTateMaps` of forms of weight u: γ-semilinear f :
  T → C_p with f(gx) = χ(g)^(−u)·g f(x) for g near 1.
* `New.Period.IsKilledBy`: The polynomial P over R kills (s, m): T is potentially crystalline and
  P(β_{s,m}) = 0 on B⊗T, the coefficients acting through T.
* `New.Period.linearFrob`: β_{s,m}: a chosen B-linear endomorphism of B⊗T agreeing with φ^m
  j(s) ⊗ ρ(s) on D_pcris(T), if one exists (arbitrary otherwise).

## Relation to the literature

Known result: Galois representation cut out of cohomology by a Hecke eigensystem, and the
Eichler-Shimura relation. Here the representation is a quotient of total cohomology rather than an
isotypic part. No dimension or semisimplicity is stated, only good reduction, annihilation by the
Hecke polynomial and the occurrence of given Hodge-Tate weights. Source: Deligne, Formes modulaires
et représentations l-adiques, Sém. Bourbaki 355 (1969), Thm 4.9; Harris and Taylor, The geometry and
cohomology of some simple Shimura varieties (2001), ch. VII; Wedhorn, Congruence relations on some
Shimura varieties, J. reine angew. Math. 524 (2000).



## The largest quotient on which Hecke operators act by an eigensystem

In `New.Variety.IsEigenQuotient.isCrystalline`, `New.Variety.IsEigenQuotient.isKilledBy` and
`New.Variety.IsEigenQuotient.exists_sum_baseChange_eq_zero_of_jump_eq_zero`, the instance
`[OverGp Γ ℓ]` gives a map `toGp : Γ → Gal(ℚ̄_ℓ/ℚ_ℓ)` with open image. B denotes the period ring
`New.Period.Bmax`. In the notions glossed in the head, `T` is the module (`V i` or `ℚ̄_ℓ ^ N`), `j`
is `toGp`, and `(s, m)` is `(g, f)`.


### `IsEigenQuotient`

 `r` is the largest quotient on which `T` acts by `θ`: the `ℚ_ℓ`-linear maps
`F i : V i → ℚ̄_ℓ ^ N` intertwine `ρ i` with `matrixRep r` (the matrices `r g` acting on
`ℚ̄_ℓ ^ N`), have values that span, turn `T i s` into the scalar `θ s`, and are universal among the
families of maps to `ℚ̄_ℓ`-vector spaces that do so. 

### `IsEigenQuotient.map_equivariant`

 The `F i` are equivariant. 

### `IsEigenQuotient.span_range_eq_top`

 The values of the `F i` span `ℚ̄_ℓ ^ N`. 

### `IsEigenQuotient.map_T_eq_smul`

 `F i` turns `T i s` into the scalar `θ s`. 

### `IsEigenQuotient.exists_factor`

 Every family `f` of maps to a `ℚ̄_ℓ`-vector space that turns each `T i s` into `θ s` factors
  through `F`. 

### `exists_isEigenQuotient`

 If the operators `T i s` commute with `Γ`, the largest quotient on which they act by `θ`
exists, and it is continuous if the `ρ i` are. Continuity of `ρ i` is assumed in the form in
which it is used: `g ↦ f (ρ i g x)` is continuous for every `x` and every `ℚ_ℓ`-linear
`f : V i → ℚ̄_ℓ ^ N`, so no topology on `V i` is needed. 

### `IsEigenQuotient.isCrystalline`

 Let `r` with the maps `F i` be the largest quotient on which `T` acts by `θ` (hypothesis `h`).
If every `ρ i` is crystalline (hypothesis `hρ`), then so is the representation `g ↦ r g` on
`ℚ̄_ℓ ^ N`. 

### `IsEigenQuotient.isKilledBy`

 Let `r` with the maps `F i` be the largest quotient on which `T` acts by `θ` (hypothesis `h`),
and let the `ρ i` be crystalline (hypothesis `hρ`). Let `toGp` (from the instance `[OverGp Γ ℓ]`)
have open image. Let `toGp g` act on the residue field as `x ↦ x ^ (1 / ℓ ^ f)`. If
`∑ k ∈ s, m k • T (t k) ∘ β(g ^ d k)` vanishes on each `B ⊗ V i`, with `β` the linearised Frobenius
`linearFrob`, then the polynomial `∑ k ∈ s, m k θ (t k) X ^ d k` kills `β(g)` for `r`. 

### `IsEigenQuotient.exists_sum_baseChange_eq_zero_of_jump_eq_zero`

 Let `r` with the maps `F i` be the largest quotient on which `T` acts by `θ` (`h`), the `ρ i`
crystalline (`hρ`), `toGp` (from `[OverGp Γ ℓ]`) of open image, and the `T i s` commuting with each
other and with `Γ`. Let `γ : ℚ̄_ℓ → ℂ_ℓ` agree with `a ∈ Gal(ℚ̄_ℓ/ℚ_ℓ)`. If `u` is not a Hodge–Tate
jump of `r` at `γ`, some combination `c` of words in `σ` has (a) `c(a ∘ θ) = 1` and
(b) `c(T)` killing the vectors of Hodge–Tate weight `u` in each `ℂ_ℓ ⊗ V i`. 


## The Galois representation attached to a Hecke eigensystem of a model

The result `New.Variety.Model.exists_galois_rep` builds a Galois representation from a system `θ` of
Hecke eigenvalues. In the proof, this representation is the largest quotient
(`New.Variety.IsEigenQuotient`) of the `ℓ`-adic cohomology of the base of a `New.Variety.Model` on
which the Hecke operators act by `θ`. The Hecke polynomial comes from the congruence relation of the
model. The jumps come from the Lefschetz formula and the Hodge–Tate map.


### `New.Variety.algebraMap_mem_of_isLocalization`

 If `R` is the localization of `𝓞 E` at a set `M` of denominators prime to `w`, then `R` is
integral at every place `A` of `Ω` above `w`. 

### `New.Variety.Model.isNullHecke_mul_of_kills_weight`

 Let `X` be a Kuga–Sato tower over `R` with base `Z`, at a neat level (`hN`), with `R` mapping
into `A` (`hR`). Let `T n` act on `V^n(Z)`, `n ≤ 2 * X.dimension`. Assume (`hT_word`) that for each
word `L` and each `b` spanned by `GUPlus`, at all large levels the coset sum of leg pull-backs over
`b * τ_L` equals the coset sum over `b` of pull-backs composed with `T_L`. Let `ε` identify `ℂ` with
the algebraic closure of `ℚ_[ℓ]` compatibly with `A`. If the combination of words `c(T)` kills all
vectors of Hodge–Tate weight `h` (`hc_kill`), then for every `b` in the Hecke algebra the product
`b * c(τ)` is `h`-null (`New.Variety.IsNullHecke`: its Lefschetz sums in weight `h` vanish). Here
`c(τ) = ∑ L, ε⁻¹ (c L) • τ_L` is the same combination of the Hecke elements. 

### `New.Variety.Model.jumpsRelAt_of_isEigenQuotient`

 Let `T` be Hecke operators on the cohomology groups `V^n(Z)` of the model `X` that
act through the legs of the levels `l w` (`hT`) and commute with the Galois action (`hT_gal`). Let
`A` be a place of `Ω` at which `R` is integral (`hR`) and the cohomology is crystalline
(`h_crys`), and let `(r, F)` be the largest quotient on which `T` acts by `ιℓ ∘ θ`, as a
representation of the decomposition group of `A` (`New.Variety.IsEigenQuotient`). If every member
of `J` is a weight `h ≥ 0` in which `θ` occurs, then every member of `J` is a Hodge–Tate jump of
`r` at `A` for the embedding `algebraMap E ℂ`. 

### `New.Variety.Model.aeval_heckePoly_eq_zero_of_isEigenQuotient`

 Eichler–Shimura away from `ℓ`. Let the Hecke operators `T` on the cohomology groups `V^n(Z)` of
the model `X` act through the legs of the levels `l w` (`hT_pull`), whose pull-backs along the leg
`X.leg i ⟦1⟧` are injective (`h_inj`), and let `(r, F)` be the largest quotient on which `T` acts by
`ιℓ ∘ θ`. Let `A` lie above the safe place `w`, with `R` integral at `A` and `ℓ` a unit at `A`. Then
the Hecke polynomial of `θ` at `w` kills `r s` for every geometric Frobenius `s` at `A`. 

### `New.Variety.Model.isKilledBy_heckePoly_of_isEigenQuotient`

 Eichler–Shimura at `ℓ`. Let `T` act on `V^n(Z) = H^n(X.base)` as follows: over `Bmax`, `T(w, j)`
followed by pull-back along `X.leg (l w) ⟦1⟧` equals the sum of pull-backs along the legs at
`invHeckeIsogeny w c`, over subspaces `c` of dimension `j` (`hT_pull_cris`). Pull-backs along
`X.leg i ⟦1⟧` are injective (`h_inj`). Let `(r, F)` be the largest quotient on which `T` acts by
`ιℓ ∘ θ` for the decomposition group of `A` over the safe place `w`, with `R` integral at `A` and
crystalline cohomology. Then for `s` a geometric Frobenius at `A` and `(s, k)` a Weil pair, the
Hecke polynomial of `ιℓ ∘ θ` at `w` kills `decompRep r A` at `(s, k)`. 

### `New.Variety.Model.exists_galois_rep`

 The Galois representation cut out of the cohomology of the model `X` by the system `θ` of Hecke
eigenvalues. Let `R` be the localization of `𝓞 E` at `M`, prime to every safe place, and `J` a set
of weights `h ≥ 0` in which `θ` occurs (`New.Variety.OccursInWeight`: no combination `c` of Hecke
words with `c(θ) = 1` makes every `b * c(τ)` `h`-null). Some continuous `ℓ`-adic representation `ρ`
then satisfies `IsSphericalAbove` at each safe place `w`: `ρ` is unramified or crystalline above
`w`, has each `h ∈ J` as a jump at `algebraMap E ℂ`, and the Hecke polynomial of `θ` at `w` kills
geometric Frobenius. 
