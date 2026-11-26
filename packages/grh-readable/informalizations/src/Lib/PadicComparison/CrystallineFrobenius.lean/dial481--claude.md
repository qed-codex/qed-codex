---
{
  "module": "src/Lib/PadicComparison/CrystallineFrobenius.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicComparison/CrystallineFrobenius.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicComparison/CrystallineFrobenius.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Crystallinity of p-adic cohomology of charted proper schemes and Frobenius congruences

The `p`-adic cohomology `New.Variety.ellAdicCohom` of a proper scheme `Y` is crystalline when `Y` is
charted (`New.Variety.IsCharted`) over a noetherian ring `R` that maps into the valuation ring of a
`p`-adic place of `Ω`, and over `Ω`. A congruence relation Σ n_i [Frob^{a_i} u_i(x)] = 0 between
maps of proper schemes (`New.Variety.CongruenceRelation`) gives the same relation between the
operators on `New.Period.Bmax ⊗ Vⁿ(Y)`.

## Overview of this theory

Let `R` be a commutative ring and `Ω` a fixed algebraic closure of `ℚ` that is an `R`-algebra. Call
a scheme charted over a ring if it is built from charts étale over tori (`New.Variety.IsCharted`).
Let `Vⁿ(Y)` be `New.Variety.ellAdicCohom` for `ℓ = p`, that is, `ℚ_p ⊗ Hⁿ(Y_Ω, ℤ_p)`. A place above
`p` is given by a valuation ring `A` of `Ω` containing the image of `R`.

* `New.Variety.finite_and_primitive_comparison`: let `Y` be proper over `R` and charted over an
  algebraically closed field `Ω` mapping to `ℂ_p`. Let `M` be a module over the tilt `O♭` of
  `O_{ℂ_p}`, with `B ↦ B ⊗ M` acyclic along tilting at perfect `O♭`-algebras. Then the cohomology of
  `Y_Ω` commutes with flat extension of coefficients, and each `Hⁿ(Y_Ω, 𝔽_p)` is finite. If also `R`
  maps compatibly to `O_{ℂ_p}`, the cohomology of `Y_Ω` with coefficients (locally constant `O♭`)
  `⊗ M` maps bijectively to that of `S ↦ Y(S)`. Here `S` runs over the `p`-adic test rings
  (`New.Variety.PadicTest`), with coefficients `S♭ ⊗ M`.
* `New.Variety.exists_period_map`: let `R` map to `O_{ℂ_p}` compatibly with an embedding `Ω → ℚ̄_p`.
  Let `S` be a `p`-torsion-free, `p`-adically complete `A_inf`-algebra and `K` a flat `S`-algebra
  over `ℚ_p`, as in `IsPeriodRingPair`. There are `K`-linear maps from `K ⊗ Vⁿ(Y)` to `Hⁿ` of
  `T ↦ Y(T)` on test rings `T`, with coefficients built from `K` and `W(T♭)`. These maps are natural
  and Galois-compatible. They are bijective when `Y` is proper and charted over `Ω`.
* `New.Variety.ellAdicCohom.isCrystalline_and_linearFrob_rel`: let `R` be noetherian, `K` a field,
  and `Y` proper and charted over `R` and over `Ω`. Then the decomposition group of `A` over `K`
  acts crystallinely on `Vⁿ(Y)`. Let `W` be proper and charted over `Ω`, with maps `uᵢ : W ⟶ Y`.
  Suppose that `∑ mᵢ [Frob^{aᵢ}(uᵢ x)] = 0` at the field-valued points `x` of the special fibre of
  `W`. Suppose also that each `γᵢ` in the decomposition group acts on the residue field as
  `x ↦ x ^ (1/p^aᵢ)`. Then `∑ mᵢ uᵢ^* ∘ linearFrob(γᵢ, aᵢ) = 0` on `Bmax ⊗ Vⁿ(Y)`.
* `New.Variety.exists_hasHodgeTateWeight`: let `Y` be proper, smooth of relative dimension `d` and
  charted over `Ω`. Let `E` be a field between `R` and `Ω`, and let `E → k → ℚ̄_p` be compatible,
  with a section `ε` of `k → ℚ̄_p`. Fix `h`, a proper `W`, and a class `x` in degree-`q` Hodge
  cohomology of `Y` over `E`. Then there are `v` in `ℂ_p ⊗ V^(q+h)(Y)` and an `ε`-semilinear map `Θ`
  with two properties. First, `v` has Hodge–Tate weight `h` for the decomposition group over `E`.
  Second, `hodgeTateMap h (u^* x) = Θ(u^* v)` for every `u : W ⟶ Y`.

These replace the primitive, crystalline and Hodge–Tate comparison theorems (Faltings, Scholze,
Bhatt–Morrow–Scholze) as used in `Lib.Shimura.Eigenspace`. There is no integral form, no Hodge–Tate
decomposition, and no identification with étale or crystalline cohomology.

`Descent` defines the test rings and proves acyclicity for almost coefficients. `Duality` on powers
of `ℙ¹`, with `Lib.Cohomology.SmoothBaseChange`, extends the comparison from a point to `Y`.
`Primitive` deduces the first result and lifts it to periods by `Completion`; the map is in
`HodgeTate.PeriodMap`. `Crystalline` uses `ToricTower` (roots of one unit at a time) for the
crystalline statement, and `CrystallineFrobenius` treats Frobenius. `HodgeTate` builds the
Hodge–Tate map.

## Main definitions and results

* `New.Variety.exists_cancels_frobPow_locally`: if p divides a power of z and a fixed power of z
  divides the image of 𝔴, then near each maximal ideal of a test the relation holds modulo z.

Notions from other files:
* `New.Variety.Cancels`: the integers m_i add up to zero on every fibre of a family v_i, that is, Σ
  m_i [v_i] = 0 in the free abelian group on the v_i.
* `New.Variety.CongruenceRelation`: Σ m_i [F_i u_i(x)] = 0 (`New.Variety.Cancels`) for every point x
  of W in a field of characteristic p that kills 𝔴, where F_i is the a_i-th iterate of Frobenius.
* `New.Period.Bmax`: The period ring B = B^+[1/μ] (Colmez's B_max, not Fontaine's B_cris), over
  which crystalline representations are defined.
* `New.Period.linearFrob`: β_{s,m}: a chosen B-linear endomorphism of B⊗T agreeing with φ^m
  j(s) ⊗ ρ(s) on D_pcris(T), if one exists (arbitrary otherwise).

## Relation to the literature

Known result: Congruence relation for the crystalline Frobenius. In the literature, characteristic
polynomials are compared through cycle classes. Here a relation among Frobenius twists of maps,
given on points of the special fibre, is carried directly to a relation among operators on
crystalline invariants. Source: Scholl, Motives for modular forms, 1990, Invent. Math. 100, §4.2.3,
through Katz–Messing, Some consequences of the Riemann hypothesis for varieties over finite fields,
1974, Invent. Math. 23, Thm 2(2); for the ramified base, Berthelot–Ogus, F-isocrystals and de Rham
cohomology I, 1983, Invent. Math. 72.



## A Frobenius relation on p-adic tests modulo an element of O_C

A congruence relation Σ n_i [Frob^{a_i} u_i(x)] = 0 between maps u_i : W → Y of proper R-schemes,
known at points x in fields that kill an ideal 𝔴 (`New.Variety.CongruenceRelation`), is carried over
to points with values in p-adic tests (`New.Variety.PadicTest`), modulo an element z of O_C.


### `New.Variety.exists_factor_forall_dvd`

 Let `φ` map `T` to a valuation ring, and let `x` be neither zero nor a unit. If the product of
`n` ideals `𝔮 l` lies in `α` and `x ^ (n + 1)` divides `φ α`, then `x` divides `φ (𝔮 l)` for
some `l`. 

### `New.Variety.exists_primes_over_prod_le`

 In a noetherian ring `T`, every ideal `α` contains a product of finitely many primes, each
containing `α`. 

### `New.Variety.cancels_quotient_of_congruenceRelation`

 Let `Y` be proper over `Spec R`, and let `u i : W ⟶ Y` be maps over `Spec R` with integers `n i`
and exponents `a i`. Assume `CongruenceRelation n 𝔴 p a u`: at every field-valued point of `W` of
characteristic `p` killing `𝔴`, the points `u i` twisted by `Frob^(a i)` satisfy `∑ n i • [·] = 0`.
Then the same holds over `T ⧸ 𝔭`: for any point `t : Spec T ⟶ W.left` and prime `𝔭` of `T` that
contains the image of `𝔴` under `R → T` and has `p = 0` in `T ⧸ 𝔭`, the morphisms
`Spec (T ⧸ 𝔭) ⟶ Y.left` given by `u i ∘ t`, precomposed with the quotient `T → T ⧸ 𝔭` followed by
`frobPow` with exponent `a i` (the map `x ↦ x ^ p ^ a i`), satisfy `Cancels n`, that is,
`∑ n i • [·] = 0` in the free abelian group on such morphisms. 

### `New.Variety.cancels_frobPow_comp_of_spec_map_comp_eq`

 Let `Y` be proper and let the relation `CongruenceRelation` hold. Let `t : Spec T ⟶ W` be a
point and `𝔮` a prime of `T` that contains `p` and the image of `𝔴`. Let a point `x` of `W` in `S`
factor as `Spec β ≫ t`, and let `ρ : S → D`, with `p = 0` in `D`, kill `β 𝔮`. Then the relation
holds (`New.Variety.Cancels`) at the points `Frob^{a_i} ∘ ρ` of `u_i(x)`. 

### `New.Variety.exists_cancels_frobPow_locally`

 Let R be a noetherian ring with a map to O_C, W and Y proper over R, `u i : W ⟶ Y` maps with
integer weights `n i`, and p ∈ 𝔴. Suppose `∑ n i [u i(x) ∘ F^{a i}] = 0` as a formal sum of points
whenever x is a point of W over a field of characteristic p that kills 𝔴, with F the p-th power map
(`New.Variety.CongruenceRelation`). Then there is an M for which the following holds, for every z in
O_C such that (a) p divides a power of z and (b) z^{M+1} divides the image of every element of 𝔴.
For every point x of W in a p-adic test (a product of cells `c.Cell i`, which are valuation rings in
which p ≠ 0, with a map from O_C = `OC`, the valuation ring of ℂ_p) and every maximal ideal m of its
ring, there is b ∉ m with the following property. For every ring D in which p = 0 and every ring map
ρ to D that inverts b and kills the image of z, `∑ n i [u i ∘ x ∘ Spec(F^{a i} ∘ ρ)] = 0`
(`New.Variety.Cancels`). 


## Crystallinity and the Frobenius congruence relation

The period map of `New.Variety.exists_period_map` identifies `Bmax ⊗ Vⁿ(Y)` with cohomology on
`p`-adic tests. The classes that come from points over the period ring modulo its ideal
`New.Variety.pdIdeal` span it (`New.Variety.span_range_crysComparison_pull_eq_top`). On such classes
an operator is determined by how it moves those points. The trivial relation `[y] - [y] = 0` gives
Galois invariance.


### `exists_tensor_twist`

 Let `σ` on `S` and a natural family `s` of ring maps both lie over `τ : A →+* A`. Then `σ ⊗ s`
is a natural family of ring maps between the base changes to `S`. 

### `finite_of_forall_pow_eq`

 A domain in which `z ^ q = z` for every `z`, for some `q > 1`, is finite: every element is a
root of the nonzero polynomial `X ^ q - X`. 

### `exists_period_twist`

 Suppose the structure map `hP.algebraMap : Ainf → Amax` commutes with the action of
`(a, σ) ∈ FrobGal`. Then there is a natural transformation `τ` from the σ-twisted period sheaf to
the untwisted one. These are the functors from p-adic tests to commutative rings sending a test `c`
to the p-adic completion of `Amax ⊗ W(c^♭)`, with the tilt taken of `PadicTest.twist σ c` for the
twisted sheaf. `τ` sends the class of `b ⊗ w` to `((a, σ) • b) ⊗ W(Frob^a)(w)`, and modulo the
divided-power ideal (`pdQuotientMap`) it sends `testToPdReduction y` to
`(testToPdReduction y) ^ p ^ a` for every `y` in the ring `c.ProdRing` of the test. 

### `exists_dvd_pow_and_pow_dvd`

 Let `R` be noetherian with a ring map `σ` to `O_C`, and let the image of the ideal `𝔭` of `R`
lie in the maximal ideal. For every `M` there are `x` in `O_C` and `N` such that `p` divides
`x ^ N` and `x ^ (M + 1)` divides the image of every element of `𝔭`. 

### `pow_pow_eq_of_isWeilPair`

 Let `e` embed `Ω` in `ℚ̄_p` and carry `R` into the integers (`hR`), compatibly with the actions
of `Γ` through `toGp` (`hj`), and let `𝔭` be the ideal of the elements of `R` whose image has norm
`< 1` (`h𝔭`). If `s` fixes `R` and `(toGp s, f)` is a Weil pair, then `z ^ p ^ f = z` on `R ⧸ 𝔭`. 

### `teichReduction`

 Let `k` be a perfect domain of characteristic `p` and `πk : R →+* k`. The ring map
`R → W(k) ⧸ pdIdeal W(k)` that sends `z` to the class of the Teichmüller lift of `πk z`. 

### `periodCoeff`

 The coefficients `Bmax ⊗ A` of the period maps on `p`-adic tests, where `A` is the completion of
`Amax ⊗ W(c♭)` at the test `c`. 

### `crysClasses`

 Degree-`n` cohomology of the points of `V` in `B ⧸ pdIdeal B`, where `B` runs over the
`p`-torsion-free, `p`-adically complete `W(k)`-algebras and `R` acts through `teichReduction πk`,
with coefficients `B`. The periods `C z` of `map_J_tensorAction_eq_pull` and
`sum_linearFrob_apply_eq_zero` are indexed by its elements `z`. 

### `frobPowHom`

 Let `z ^ p ^ a = z` on `k`, and let `W(k) → A_max` agree with `integersToPdQuotient` on the
Teichmüller lifts of the image of `R` (`hr`). Then `x ↦ x ^ p ^ a` on `B ⧸ pdIdeal B`, for the
crystalline tests `B`, is a map of `R`-algebras from the structure through `integersToPdQuotient` to
the structure through `teichReduction πk`. 

### `bijective_frobPowHom_zero_app`

 For `a = 0` the map `frobPowHom` is `x ↦ x ^ p ^ 0 = x`, so it is bijective at every test. 

### `toRingHom_algebraMap_witt_eq`

 Let `algebraMap : W(k) → A_max` be the unique lift of `ℓ : k → A_max ⧸ pdIdeal A_max` (`h_lift`,
`h_lift_unique`), where `ℓ` comes from `integersToPdQuotient` on `R` (`hℓ`). If `z ^ p ^ a = z` on
`k`, then the pair `(a, toGp s)` fixes the image of `W(k)` in `A_max`. 

### `map_J_tensorAction_eq_pull`

 The main step of `ellAdicCohom.isCrystalline_and_linearFrob_rel`, for a period map `J` and a
subfunctor `V` of the points of `Y`. Let `C z` restrict on `V` to the pull-back of the crystalline
class `z` along the reduction of points (`hC`), and let every pair `(a, toGp s)` with
`z ^ p ^ a = z` on `k` fix `W(k)` in `A_max`. If `z ^ p ^ a = z` on `k`, then `(a, toGp s)` acting
on `Bmax`, with `s` acting on the cohomology, sends `C z` to a period that restricts to the
pull-back of `z` along the reduction of points followed by `Frob ^ a`. 

### `sum_linearFrob_apply_eq_zero`

 The congruence relation of `ellAdicCohom.isCrystalline_and_linearFrob_rel` on one period `C z`.
Let `periodCoeff` have Zariski descent (`h_zar`), let `V` be cohomologically dense (`hV_dense`), and
let the periods be fixed by `Γ` (`h_fixed`) and moved by the Weil pairs as in `h_action`. If the
relation of the points `Frob ^ a i (u i x)` holds near every closed point of a test once `p` and
`x₀` vanish (`h_rel_loc`), and `integersToPdQuotient` kills `x₀`, then
`∑ m i • (u i)^* ∘ linearFrob (γ i) (a i)` kills `C z`. 

### `ellAdicCohom.isCrystalline_and_linearFrob_rel`

 Let `R` be a noetherian ring and `K` a field. Let `Ω` be an algebraic closure of `ℚ` that is an
algebra over `R` and over `K`, compatibly with a map `R → K`. Let `A` be the valuation ring of a
`p`-adic place of `Ω` over `K` (`GaloisRep.PadicPlaceEmbedding`), with `R` mapping into `A`. Let
`Y`, `W` be proper over `R`, charted over `Ω`, and `Y` also charted over `R`. Suppose
`∑ m i [Frob ^ a i (u i x)] = 0` at the field-valued points `x` of `W` that kill the prime of `R` of
elements whose valuation in `A` is `< 1`. Let each `γ i` lie in the decomposition group of `A` in
the Galois group of `Ω` over `K` (`decompGroup`). Suppose its image in `G_p` forms an `IsWeilPair`
with `a i`. (a) The representation of this decomposition group on `Vⁿ(Y)` is crystalline. (b)
`∑ m i • (u i)^* ∘ β i = 0` on `Bmax ⊗ Vⁿ(Y)`, where `β i` is `linearFrob` of this representation
at `γ i` and `a i`. 
