---
{
  "module": "src/Lib/PadicComparison/Crystalline/ComparisonMap.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicComparison/Crystalline/ComparisonMap.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicComparison/Crystalline/ComparisonMap.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Crystalline comparison: bijectivity on étale charts and spanning of period cohomology

Write A_inf = `New.Period.Ainf`, A_max = `New.Period.Amax`, B_max = `New.Period.Bmax`, and 𝔡(B) =
`New.Variety.pdIdeal` B for the ideal of the x with n! ∣ x^n for all n. Here ξ = `New.Period.xi`
generates the kernel of θ : A_inf → O_C. Fix an action of A_inf on A_max satisfying
`New.Variety.CrysPeriodAlgebra`. For a functor P on O_C-algebras, the crystalline comparison
compares two cohomologies. The first is that of D ↦ P(D/𝔡(D)) on p-torsion-free p-complete
A_max-algebras D, with coefficients B_max ⊗ D. The second is that of P on p-adic tests. Finally, let
S be a complete discrete valuation ring with uniformiser p, let O_C be an algebra over a ring R with
a map R → S/𝔡(S), let A_max be an S-algebra, and assume a given natural map from D ↦ D/𝔡(D) (as
R-algebras via O_C → A_max/𝔡(A_max)) to D ↦ D/𝔡(D) (via R → S/𝔡(S)) on p-torsion-free p-complete
A_max-algebras is an isomorphism; let V be a subfunctor of a functor X on R-algebras with
`New.Variety.IsCharting` V (V covers X and is built from charts étale over tori). Then the classes
pulled back from D ↦ V(D/𝔡) on p-torsion-free p-complete S-algebras span the period cohomology of V
over B_max when it is finite.

## Main definitions and results

* `New.Variety.CrysPeriodAlgebra`: the properties of an A_inf-algebra structure on A_max that the
  comparison needs.
* `New.Variety.exists_crysPeriodAlgebra`: for each y in O_C with p ∣ y^N, there is an algebra
  structure as in `New.Variety.CrysPeriodAlgebra` that is equivariant for Frobenius and Galois and
  whose map O_C → A_max/𝔡(A_max) kills y.
* `New.Variety.HasCrysComparison`: the comparison along `New.Variety.crysThickening` and
  `New.Variety.testToPdReduction` is bijective in every degree.
* `New.Variety.hasCrysComparison_of_witt`, `New.Variety.hasCrysComparison_of_etale`:
  `New.Variety.HasCrysComparison` holds for P = Hom_{A_inf}(T, −), with scalars restricted from O_C
  to A_inf, when the A_inf-algebra T maps to W(b), for a perfect π-torsion-free O^♭-algebra b, by a
  map bijective on p-adic completions. It also holds for P = Hom(B, −) with B étale over O_C[G],
  where G is a ℚ≥0-module.
* `New.Variety.hasCrysComparison_chart`: the comparison holds for Hom_R(B, −) on O_C-algebras when B
  is étale over R[X_1, …, X_d], each X_i going to a unit t_i. Adjoining all roots of the t_i reduces
  it to `New.Variety.hasCrysComparison_of_etale`.
* `New.Variety.span_range_crysComparison_pull_eq_top`: for S a complete discrete valuation ring with
  uniformiser p, the classes pulled back from the cohomology of D ↦ V(D/𝔡) span the period
  cohomology of V over B_max when it is finite.

Notions from other files:
* `New.OC`: The ring of integers O_C of the field C_p of p-adic complex numbers.
* `New.Period.OFlat`: The ring O^♭, the inverse limit of O_C/p along x ↦ x^p;
  π = p♭ = `New.Variety.pFlat` is ξ mod p, the zeroth Witt coefficient of ξ.
* `New.Variety.PadicTest`: A p-adic test: a non-empty family of cells (`New.Variety.IsCell`) with a
  ring map from O_C to their product S (`ProdRing`); S^♭ is the tilt of S and θ : W(S^♭) → S is
  Fontaine's map.
* `New.Period.Amax`: Colmez's period ring A_max, the p-adic completion of A_inf[X]/(pX − ξ).
* `New.Variety.compatibleRoots`: The functor of characters ℚ≥0 → A on O_C-algebras A, with the twist
  by s ↦ (ε^s)^♯ as an endomorphism (a functor on O_C-algebras × Bℕ, `New.Variety.TimesBNat`).
* `New.Variety.IsLine`: A map Y → U from a functor with an endomorphism is a line if the cohomology
  of U maps bijectively to that of Y on the product with Bℕ.

## Relation to the literature

Known result: Crystalline comparison for p-adic étale cohomology with good reduction. Only
crystallinity is proved here. It is for cohomology on p-adic test rings, which is not identified
with étale cohomology. There is no filtration and no identification with crystalline cohomology.
Invariants come from p-complete torsion-free rings modulo elements with divided powers, and they are
compared on toric towers one coordinate at a time. Source: Bhatt, Morrow, Scholze, Integral p-adic
Hodge theory, 2018, Publ. IHÉS 128, Thm 1.1(i) (first proved in Faltings, Crystalline cohomology and
p-adic Galois representations, 1989); for the site, Bhatt, Prismatic F-gauges, 2022, Rem. 2.5.12;
for the line lemma, Andreatta–Brinon, Acyclicité géométrique de B_cris relatif, 2013, Comment. Math.
Helv. 88.



## Frobenius-twisted actions of A_inf on A_max and their existence

The crystalline comparison uses A_max = `New.Period.Amax` as an algebra over A_inf =
`New.Period.Ainf` through a structure as in `New.Variety.CrysPeriodAlgebra`;
`New.Variety.exists_crysPeriodAlgebra` builds one from the usual map composed with a power of
Frobenius.

* `New.Variety.integersToPdQuotient`: the ring map O_C → A_max/𝔡(A_max) induced by such an algebra
  structure.


### `instance : Module.Flat Amax Bmax`

 B_max is flat over A_max. 

### `crysPeriodCoeff`

 The coefficient functor on p-torsion-free p-complete A_max-algebras sending D to B_max
⊗_{A_max} D. 

### `CrysPeriodAlgebra`

 Conditions on an A_inf-algebra structure on A_max: A_max is p-torsion-free and p-complete, p
divides the image of ξ, the image of τ becomes a unit in B_max (`New.Variety.IsPeriodRingPair`), p³
divides the image of μ, and the image of μ becomes a unit in B_max. Here μ = [ε] − 1
(`New.Period.mu`) and τ = [ε^{1/p}] − 1 (`New.Period.tau`), so that ξτ = μ. 

### `CrysPeriodAlgebra.p_cube_dvd_mu`

 The image of μ in A_max is divisible by p³. 

### `CrysPeriodAlgebra.isUnit_mu`

 The image of μ in B_max is a unit. 

### `integersToPdQuotient`

 The ring map O_C → A_max/𝔡(A_max) obtained by factoring A_inf → A_max/𝔡(A_max) through
Fontaine's surjection θ: A_inf → O_C. 

### `integersToPdQuotient_untilt`

 For t in O^♭, the map `New.Variety.integersToPdQuotient` sends the untilt t^♯ of t to the class
of the image of the Teichmüller lift [t] under the algebra structure h. 

### `exists_crysPeriodAlgebra`

 For every N and every y in O_C with p dividing y^N, there is an A_inf-algebra structure on
A_max, satisfying `New.Variety.CrysPeriodAlgebra`, such that (a) ℤ_p acts on A_max through A_inf as
it does directly, (b) the structure map commutes with the action of the monoid
`New.Period.FrobGal` generated by Frobenius and G_p, and (c) the map O_C → A_max/𝔡(A_max) of
`New.Variety.integersToPdQuotient` kills y. 


## The comparison map and its bijectivity for étale algebras over O_C[G]

* `New.Variety.crysThickening`: a test S goes to D_S, the p-adic completion of A_max ⊗ W(S^♭).
* `New.Variety.testToPdReduction`: the O_C-algebra map S → D_S/𝔡(D_S) with θ(x) ↦ 1 ⊗ x.


### `crysThickening`

 The functor sending a p-adic test S to the p-adic completion of A_max ⊗_{A_inf} W(S^♭), a
p-torsion-free p-complete A_max-algebra. 

### `toPdReduction`

 The quotient map E → E/𝔡(E), natural in the p-torsion-free p-complete A_max-algebra E, as a map
of A_inf-algebras; A_inf acts on E through the algebra structure h and on E/𝔡(E) through θ and
`New.Variety.integersToPdQuotient`. 

### `testToPdReduction`

 For a p-adic test with ring S, the O_C-algebra map S → D/𝔡(D), where D is the p-adic completion
of A_max ⊗ W(S^♭): the inverse of the isomorphism O_C ⊗ W(S^♭) ≅ S
(`New.Variety.PadicTest.thetaIso`) followed by the map O_C ⊗ W(S^♭) → D/𝔡(D) induced by W(S^♭) → D
and `New.Variety.toPdReduction`. It sends θ(x) to the class of 1 ⊗ x
(`New.Variety.testToPdReduction_theta`). 

### `testToPdReduction_theta`

 For a p-adic test `c` with ring S and x in W(S^♭), `New.Variety.testToPdReduction` sends θ(x), θ
Fontaine's map, to the class of 1 ⊗ x in D/𝔡(D), D the p-adic completion of A_max ⊗ W(S^♭) over
A_inf. Here `.of _ _` is the map `AdicCompletion.of` into D and `Quot.mk _` the class modulo
𝔡(D). 

### `HasCrysComparison`

 For a functor P from O_C-algebras to types, `HasCrysComparison P` says that restriction along
`New.Variety.crysThickening` and `New.Variety.testToPdReduction` is bijective in every degree. It
goes from the cohomology of D ↦ P(D/𝔡(D)) on p-torsion-free p-complete A_max-algebras D, with
coefficients B_max ⊗ D, to that of S ↦ P(S) on p-adic tests, with coefficients B_max ⊗ D_S,
D_S = `crysThickening` S. 

### `bijective_comp_toPdReduction_app`

 Let E be a p-torsion-free p-complete A_max-algebra, 𝔡(E) the ideal `New.Variety.pdIdeal`, and b
a perfect O^♭-algebra, with A_inf acting on A_max through the standing structure
`h : CrysPeriodAlgebra`. Then every A_inf-algebra map from the Witt vectors W(b) to E/𝔡(E) lifts
uniquely to an A_inf-algebra map W(b) → E. Here A_inf acts on E/𝔡(E) through θ and
`integersToPdQuotient`, and the lift means that composing with the quotient map
`New.Variety.toPdReduction` : E → E/𝔡(E) is a bijection. 

### `hasCrysComparison_of_witt`

 Let b be a perfect π-torsion-free O^♭-algebra (π = ξ mod p, `New.Variety.pFlat`), and let
k : T → W(b) be an A_inf-algebra map that induces a bijection of p-adic completions. Then the
crystalline comparison `New.Variety.HasCrysComparison` is bijective for S ↦ Hom_{A_inf}(T, S) on
O_C-algebras, with scalars restricted to A_inf. 

### `exists_isCompletionBijective_witt_tensor`

 Let G be a commutative monoid that is a module over ℚ≥0, T an étale algebra over the monoid
algebra A_inf[G] (and an A_inf-algebra through it), and b = O^♭[G] ⊗_{A_inf[G]} T, assumed perfect.
Then there is an A_inf-algebra map k : T → W(b) that induces a bijection of p-adic completions. 

### `hasCrysComparison_of_etale`

 Let G be a commutative (additive) monoid that is a module over ℚ≥0, and B an O_C-algebra étale
over the monoid algebra O_C[G] compatibly with O_C, with A_max carrying the standing structure
`CrysPeriodAlgebra`. Then for P = Hom(B, −), restriction along `crysThickening` and
`testToPdReduction` is bijective in every degree (`New.Variety.HasCrysComparison`). The map goes
from the cohomology of D ↦ Hom(B, D/𝔡(D)) on p-torsion-free p-complete A_max-algebras D, with
coefficients B_max ⊗ D and 𝔡 the ideal `New.Variety.pdIdeal`, to the cohomology of S ↦ Hom(B, S) on
p-adic tests. 


## Root systems of a unit form a line on p-torsion-free p-complete A_max-algebras

Here 𝔡(D) is the ideal `New.Variety.pdIdeal` of the x with n! ∣ x^n for all n, and a unit is taken
in D/𝔡(D).


### `CrysPeriodAlgebra.p_mul_teichmuller_sub_one_dvd`

 Let a ∈ ℚ≥0 have denominator greater than 1, so that a is not an integer. Then
p · ([ε^a] − 1) divides μ = [ε] − 1 in A_max, where [ε^a] is the Teichmüller lift of ε^a
(`New.Variety.epsPowNNRat`) mapped from A_inf to A_max by the algebra structure that
`CrysPeriodAlgebra` fixes. 

### `_root_.NNRat.equivIcoProdNat`

 The split of c ∈ ℚ≥0 into its fractional part c − ⌊c⌋, in [0, 1), and its integral part ⌊c⌋. 

### `lineGen`

 For t in a p-torsion-free p-complete A_max-algebra A, the element t − v of A[ℚ≥0], where
`single a 1` stands for v^a. 

### `lineEnvelope`

 The divided power envelope of A[ℚ≥0] along t − v (`lineGen`). 

### `lineEnvelope.incl`

 The map from A to the envelope `lineEnvelope t`. 

### `lineEnvelope.var`

 The character a ↦ v^a of ℚ≥0 in the envelope `lineEnvelope t`. 

### `pdQuotientMk_lineEnvelope_var_ofAdd_one`

 In the envelope `lineEnvelope t`, the variable v and t agree modulo 𝔡, because t − v has
divided powers there. 

### `lineEnvelope.point`

 The point of the root systems of t modulo 𝔡 at the envelope `lineEnvelope t`: the variable v
modulo 𝔡, and the map from A. 

### `bijective_pointMap_lineEnvelope_point`

 The envelope `lineEnvelope t` with its point `lineEnvelope.point t` represents the root systems
of t modulo 𝔡: for every p-torsion-free p-complete A_max-algebra B, a map f : A → B with a
character of ℚ≥0 in B/𝔡(B) whose value at 1 is f(t) modulo 𝔡 comes from exactly one map from the
envelope to B. 

### `koszulExact_lineEnvelope`

 Let t ∈ A be a unit modulo 𝔡(A), E = `lineEnvelope t` with the map i from A and the variable
v, and γ an endomorphism of E that fixes A (`hγ_fix`) and multiplies v^a by [ε^a] for every
a ∈ ℚ≥0 (`hγ_v`). Then B_max ⊗ − (`crysPeriodCoeff`) turns i and γ into a Koszul-exact pair. 

### `compatibleRootsAreLines_crysTest`

 Let A be a p-torsion-free p-complete A_max-algebra (with the standing structure
`CrysPeriodAlgebra`) and y a unit of A/𝔡(A), where 𝔡 is the ideal `New.Variety.pdIdeal` and
`pdReduction` sends D to D/𝔡(D), an O_C-algebra through `integersToPdQuotient`. On such algebras D,
let Y(D) be the pairs of a map f : A → D and a character s : ℚ≥0 → D/𝔡(D) with s(1) = f(y), with the
twist multiplying s by the image of a ↦ (ε^a)^♯. Then forgetting s induces a bijection, in every
degree, from the cohomology of Hom(A, −) to that of Y on the product with Bℕ (the homotopy quotient
by the twist), with coefficients D ↦ B_max ⊗_{A_max} D (`crysPeriodCoeff`). 


## The comparison on a chart étale over a torus

A root system of t is a character of ℚ≥0 with value t at 1.


### `IsClosedClass.of_prod_nat`

 Let P be a closed class of functors from C × Bℕ to abelian groups (`IsClosedClass`: P holds
for zero objects, and along a short exact sequence whose first term is in P, the middle term is in
P exactly when the last one is). If P holds for the free abelian group functor of Y × ℕ (Y
restricted to C, times ℕ with its shift), then it holds for that of Y: the short exact sequence
`TimesBNat.shortExact_induced` resolves ℤ[Y] by two copies of ℤ[Y × ℕ]. 

### `Comparison.IsBijective.isBijectiveOn_of_compatibleRoots`

 Let c be a comparison from F on C to F' on C' (a functor φ : C' ⥤ C with a map of coefficients),
ψ and ψ' functors to O_C-algebras with η : ψ' ⟶ φ ⋙ ψ, and U a functor on O_C-algebras. Let t₁, …,
t_n be unit-valued functions on U (`h_unit`), x a point of U(T), and r_i root systems of the t_i(x),
that is, characters of ℚ≥0 with r_i(1) = t_i(x) (`h_root`). Suppose that T, with x and the r_i,
represents the points y of U together with root systems s_i of the t_i(y) (`h_rep`). Suppose root
systems form lines (`CompatibleRootsAreLines`) for ψ with F and for ψ' with F': for each unit of
ψ(A), projecting its root systems to Hom(A, −) is bijective on cohomology. Then bijectivity of c on
the functor represented by T (`hT`) implies bijectivity on U. Here c is bijective on P when the maps
Hⁿ(ψ ⋙ P, F) → Hⁿ(ψ' ⋙ P, F') induced along η are bijective for all n. 

### `compatibleRootsAreLines_padicTest`

 Assume the conditions `CrysPeriodAlgebra` on A_max. On p-adic tests (`PadicTest.algFunctor`
sends a test to its O_C-algebra), the root systems of every unit form a line
(`CompatibleRootsAreLines`) for the coefficients of the crystalline comparison, B_max ⊗ D read on
the thickening `crysThickening` of the test. That is, for every test A and unit y of its
O_C-algebra, the projection from the root systems of y to Hom(A, −) is bijective on cohomology with
these coefficients. 

### `hasCrysComparison_chart`

 Crystalline comparison on a chart. Assume `New.Variety.CrysPeriodAlgebra`, let O_C be an
R-algebra, and let t_1, …, t_d be units of the R-algebra B such that the map R[X_1, …, X_d] → B,
X_i ↦ t_i (`polyEval t`), is étale. Then the functor of R-algebra maps from B to O_C-algebras
satisfies `New.Variety.HasCrysComparison`: restriction from p-complete p-torsion-free A_max-algebras
to p-adic tests is bijective on cohomology. 


## Spanning of period cohomology by crystalline classes

Here S is a ring with a map r : R → S/𝔡(S), O_C is an R-algebra, A_max an S-algebra, and V a
subfunctor of a functor X on R-algebras.

* `New.Variety.crysComparison`, `New.Variety.toCrysPoints`: the comparison from p-torsion-free
  p-complete S-algebras to p-adic tests, and the map from V on p-adic tests to D ↦ V(D/𝔡).


### `HasFlatBaseChange.pdReduction_reprBy`

 Flat base change for the maps from an S/𝔡(S)-algebra to reductions modulo divided powers. Here
𝔡 is the ideal `New.Variety.pdIdeal` of the x with n! ∣ x^n for all n, and G is a commutative
S/𝔡(S)-algebra. The free abelian group on the functor B ↦ Hom(G, B/𝔡(B)), on p-torsion-free
p-complete S-algebras B, has flat base change (`New.Variety.HasFlatBaseChange`): its cohomology
commutes with tensoring by flat modules. 

### `hasFlatBaseChange_freeAb_pdReduction_of_isCharting`

 Flat base change for the points of V modulo divided powers. Suppose that V satisfies
`New.Variety.IsCharting` (V covers X and is built from charts étale over tori). Then the free
abelian group on D ↦ V(D/𝔡(D)), on p-torsion-free p-complete S-algebras D, has flat base change
(`New.Variety.HasFlatBaseChange`). Here D/𝔡(D) is an R-algebra through r : R → S/𝔡(S). 

### `counitCoeff`

 For an adjunction L ⊣ U, a functor φ into the source of U and a functor Θ to A-algebras, the
map of A-modules Θ(L(U(φ c))) → Θ(φ c) induced by the counit, natural in c. 

### `coeffCompBijective_counitCoeff`

 Let L ⊣ U. If restriction along φ, via v : Y'' ⟶ Y ∘ U ∘ φ, is bijective on the cohomology of Y
∘ U with coefficients G ∘ Θ, then the comparison along U ∘ φ given by the counit is bijective on the
cohomology of Y with coefficients G ∘ Θ ∘ L. 

### `crysComparison`

 The comparison (a functor from p-adic tests with a map of coefficient functors) along the
functor sending a p-adic test c to D = completed A_max ⊗ W(c^♭), viewed over S, from coefficients D
to B_max ⊗ D by x ↦ 1 ⊗ x. 

### `toCrysPoints`

 The natural map V(c) → V(D/𝔡(D)) on p-adic tests c induced by `New.Variety.testToPdReduction`
followed by i, which passes from the R-structure through O_C to the one through r, D the completion
of A_max ⊗ W(c^♭) viewed over S. 

### `crysBaseChange`

 Completed base change along S → A_max: the functor sending a p-torsion-free p-complete
S-algebra D to the p-adic completion of A_max ⊗_S D. As A_max is flat over S, this completion is
again p-torsion-free. 

### `toCrysBaseChange`

 The map from A_max ⊗_S D to its p-adic completion (`crysBaseChange` of D), natural in the
p-torsion-free p-complete S-algebra D. 

### `crysBaseChangeAdj`

 Completed base change along S → A_max (`crysBaseChange`) is left adjoint to restriction of
scalars, between p-torsion-free p-complete S-algebras and A_max-algebras. 

### `bijective_pullₗ_toCrysBaseChange`

 Completing the coefficients is bijective on cohomology, under a finiteness condition. Let S be a
p-torsion-free p-complete discrete valuation ring with uniformiser p, over which A_max is a flat
algebra. Let N be a functor to abelian groups on p-torsion-free p-complete S-algebras D that has
flat base change (`New.Variety.HasFlatBaseChange`). Let L D be the p-adic completion of A_max ⊗_S D
(`crysBaseChange`). Suppose that B_max ⊗ H^m(N, L D) is a finite B_max-module in every degree m.
Then the map H^n(N, A_max ⊗_S D) → H^n(N, L D) induced by the completion is bijective. 

### `span_range_crysComparison_pull_eq_top`

 Let S be a p-torsion-free p-complete discrete valuation ring with uniformiser p, and 𝔡(D) the
ideal of x with n! ∣ xⁿ for all n. On p-torsion-free p-complete A_max-algebras D, let `i` be an
isomorphism of R-algebras from D/𝔡(D), reduced along O_C → A_max/𝔡(A_max), to D viewed over S and
reduced along `r`. Let `V` be a subfunctor of the functor `X` on R-algebras with `IsCharting V`.
Suppose that for every degree, the cohomology of V on p-adic tests c (products of cells with a map
from O_C) is a finite B_max-module, with coefficients B_max ⊗ D, where D is the completed
A_max ⊗ W(c^♭). Then in each degree n it is spanned over B_max by the classes pulled back along
`New.Variety.crysComparison` from H^n of D ↦ V(D/𝔡(D)). 
