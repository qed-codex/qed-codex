---
{
  "module": "src/Lib/Adelic/AutomorphicForms/PAdicGauge.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/AutomorphicForms/PAdicGauge.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/AutomorphicForms/PAdicGauge.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The p-adic gauge of algebraic forms, class sums, and integral forms of a level

Fix a prime `p` and a map `ιₚ : ℂ →+* ℂ_[p]`, written ι in prose and given by the instance
`[ι : PadicPlace p]`. The gauge `New.weylGauge κ e g ξ` is the largest `p`-adic absolute value of a
coordinate of `g⁻¹ ι(ξ)`, for a finite adelic unitary point `g` acting in weight `(κ, e)`. It
measures the `p`-integrality of the values of algebraic forms (`New.AlgForm`). The file proves
invariance properties of the gauge, bounds the forms `New.deltaForm` on `New.stdSpace E n` that are
supported on one double coset, bounds class sums over `Γ \ G / K`, and studies the sizes of
algebraic forms whose level is cut out at finitely many split places.

## Main definitions and results

* `New.exists_mul_mem_integralAbove`: a rational point moves `g` to a point integral above `p`.
* `New.LevelPlaces.LevelForm`: forms of weight (κ, e) on which the level `New.levelOf` of H acts
  through χ, a finite-dimensional inner product space under the class sum of the Gram pairing.
* `New.gramForm_mem_embValRing`: the Gram pairing of two vectors of gauge at most one, for
  `ι ∘ conj` and for `ι`, is integral; `New.LevelPlaces.LevelForm.norm_nsmul_inner_le_one`: so is
  the inner product of two such forms, after multiplication by a common multiple of the orders of
  the stabilisers.
* `New.LevelPlaces.LevelForm.valueCoord`, `New.LevelPlaces.LevelForm.valueMetric`: coordinates of a
  form in which the inner product has a rational matrix, if the classes have no nontrivial
  automorphisms.
* `New.Rows.weylGauge_classSum_le_one`: `p`-integrality (gauge `New.weylGauge` at most one) passes
  to the class sum after multiplication by a common multiple of the orders of the stabilisers.

Notions from other files:
* `New.weylGauge`: at the infinite place τ, g⁻¹ acts through its component at the prime induced by
  the embedding x ↦ ι(Φ_τ(x̄)) of E into ℂ_p.
* `New.stdSpace`: the definite space `I_n`, the sum of `n` norms with its standard lattice.
* `New.integralAbove`: the subgroup of finite adelic unitary points whose components at all primes
  above p are integral invertible matrices.
* `New.classSum`: the class sum of f, that is, the sum over the double cosets c in Γ\G/K of
  f(g_c)/#(Γ ∩ g_c K g_c⁻¹), with g_c a chosen representative; `New.classAut` is Γ ∩ gKg⁻¹.
* `New.stdLevel`: K₀ = G_f ∩ GL_n(Ô), the stabiliser of the standard lattice in the finite adelic
  unitary group G_f = `New.Gf`; `New.maxCompactAt n w` is its part supported at w and w̄.

## Relation to the literature

Known; see `Lib.Adelic.AutomorphicForms.SmoothAlgebraicForms` and `Lib.Adelic.Hecke.ClassSums` for
sources.



## Invariance of the gauge, integral forms, weak approximation above p

* `New.GaugeLe`, `New.integralFormsAt`: bounds for forms, and the module of integral forms over the
  valuation ring `New.embValRing` of `ι`.


 ### Weak approximation above `p` and properties of the gauge 

### `adeleExtension_mem_intGL`

 The extension to the finite adeles of an embedding `σ : E →+* ℂ_[p]` maps a unitary point that
is integral above `p` to an integral matrix with integral inverse. 

### `exists_mul_mem_integralAbove`

 Weak approximation above `p`: for finite adelic points `g`, `d` there is a rational point `γ` of
the definite space `V` (by default the standard one), embedded by `V.embFin`, such that `γ g` and
`d (γ g) d⁻¹` are integral at all primes above `p`. 

### `weylGauge_embFin`

 The gauge of `γ ξ` at `γ g` is the gauge of `ξ` at `g`, for a rational point `γ`. 

### `weylGauge_mul_of_mem_integralAbove`

 The gauge of a vector is unchanged when the point is multiplied on the right by an element
that is integral at the primes above `p`. 

### `weylGauge_smul`

 The gauge is homogeneous for the absolute value of scalars under `ι`. 

### `weylGauge_le_one_iff`

 At a point `k` that is integral above `p`, a vector has gauge at most one if and only if all
its coordinates have absolute value at most one under `ι`. 

### `weylGauge_sum_le`

 The gauge is ultrametric: if every `f a` has gauge at most `C ≥ 0`, so does their sum. 

 ### Integral forms 

### `GaugeLe`

 The algebraic form `φ` (with `φ.val (γ g)` equal to `γ` acting on `φ.val g` for rational `γ`) is
bounded by `c` at `d`: for every `g`, the gauge of `φ g` at `g * d` is at most `c`. 

### `embValRing`

 The valuation ring O_ι ⊂ ℂ of complex numbers whose image under ι : ℂ → ℂ_p has absolute
value at most 1. 

### `integralFormsAt`

 The O_ι-module of forms φ in S that are integral at d: the value φ(g) has gauge at most 1 at
gd for every g. 

### `stdLevel_le_localLevel`

 The stabiliser of the standard lattice is integral at every set `S` of finite places. 

### `weylGauge_le_one_of_integralAbove`

 If the values of an algebraic form `φ` at the points integral above `p` have `ι`-integral
coordinates, then `φ g` has gauge at most `1` at `g` for every `g`. 


## Classes at a level and the gauge of delta forms

* `New.StdClasses`: the set of classes `Γ \ G_f / K` at a level `K`, where `G_f = New.Gf E n` is the
  finite adelic group and `Γ` is the image of its rational points.
* `New.Rows.weylGauge_deltaForm_le`: the values of the delta form made from `v` at `x` have gauge at
  most the gauge of `v` at `x`.
* `New.Rows.weylNormSq_deltaForm_le`: after any automorphism `σ` of `ℂ`, the values of the delta
  form have squared norm at most `#Aut(x)²` times that of `σ ∘ v`.


### `StdClasses`

 The set of classes of the standard space I_n for a subgroup K: double cosets of the finite
adelic unitary group by its rational points on the left and K on the right. 

### `exists_reps_integralAbove`

 The classes at level `K` have a system of representatives `r` whose members are all integral
at the primes above `p`. 

### `Rows.weylGauge_deltaForm_le`

 For a level K (an open subgroup of the stabiliser of the standard lattice) and χ with values of
finite order, the delta form attached to χ, x, v (the form supported on the double coset of x that
is made from the vector v) has, at every point g, gauge at ι at most the gauge of v at x. 

### `Rows.weylNormSq_deltaForm_le`

 Let `χ` be a character of the subgroup `K` with values of finite order, trivial near `1`, where
`K` has finite type for the rational points (so there are finitely many double cosets of the
rational points and `K`), and `σ` a field automorphism of `ℂ`. The value at any `g` of the delta
form at `x` made from `v`, after applying `σ` to its coordinates, has squared norm
(`New.weylNormSq`) at most `#Aut(x)²` times that of `σ ∘ v`, where `Aut(x)` is the stabiliser
`New.classAut` of the coset `x K` among the rational points. 


## Algebraic forms of a level: class sum metrics and integral forms

Algebraic forms on the standard definite space `New.stdSpace` whose level is cut out at finitely
many split places, and their sizes under the automorphisms of ℂ and the embeddings ℂ → ℂ_l.

* `New.LevelPlaces`: two finite families of split places; `New.fockLetters`, `New.letterPoly`:
  substitution of sums of variables into the polynomial of a vector of weight κ.
* `New.LevelPlaces.LevelForm.innerAt`, `New.LevelPlaces.LevelForm.norm_map_inner_le`: the pairing
  after an automorphism σ of ℂ, and Cauchy–Schwarz for σ of the inner product.
* `New.LevelPlaces.LevelForm.integralForms`, `New.LevelPlaces.LevelForm.norm_nsmul_inner_le_one`:
  forms integral at j : ℂ → ℂ_l, and integrality of their inner products.

A form takes values in coordinate vectors indexed by `New.WeylIndex`, paired by the integer matrix
`New.weylGram`.


 ### Places and letters 

### `LevelPlaces`

 Two finite families of finite places of E, called the chosen places and the places of the
twist, all distinct, none of them conjugate to itself or to another. 

### `LevelPlaces.ChosenIndex`

 The index set of the chosen places. 

### `LevelPlaces.TwistIndex`

 The index set of the places of the twist. 

### `LevelPlaces.fintypeChosen`

 There are finitely many chosen places. 

### `LevelPlaces.fintypeTwist`

 There are finitely many places of the twist. 

### `LevelPlaces.chosenPlace`

 The chosen places. 

### `LevelPlaces.twistPlace`

 The places of the twist. 

### `LevelPlaces.apart`

 No place of either family equals another place or the conjugate of one. 

### `maxCompactAt_le_levelOf`

 If none of the places `u i` is `w` or `w̄`, then every element of K₀ = `New.stdLevel` supported
at `w` and `w̄` lies in `levelOf u H`, the subgroup of elements of K₀ whose reductions at the `u i`
form an element of `H`. 

### `fockLetters`

 The algebra map sending the variable (τ, i, h) to the sum of the variables (τ, i, a) over
the indices a with sign s(a) = c and ord(a) = h. 

### `letterPoly`

 The linear map sending ξ of weight κ to its polynomial `New.toPoly` ξ, with each variable
(τ, i, h) replaced by ∑ X(τ, i, a) over s(a) = c, ord(a) = h. 

 ### Forms of a level and the class sum metric 

### `stdClassSum`

 The class sum on the standard definite space: for a subgroup K and a function f on the finite
points, the sum of f(g_c) / #Aut(g_c) over the double cosets c of the rational points and K. 

### `norm_map_stdClassSum_gramForm_le`

 The Cauchy–Schwarz inequality for class sums of any level `K`. Let `σ` be an automorphism of
`ℂ` and `σ' = conj ∘ σ ∘ conj`. The image under `σ` of the class sum of the Gram pairings of `φ g`
and `φ' g` has absolute value at most the norm of `φ` at `σ'` times the norm of `φ'` at `σ`; the
norm at `σ` is the square root of the class sum of the squared norms of the images under `σ`. 

### `isConjApart_chosenPlace`

 The chosen places are pairwise distinct, and none is the conjugate of itself or of another. 

### `placeAt`

 The family of all places of `P`: the chosen places and the places of the twist, indexed by the
disjoint union of the two index sets. 

### `places`

 The set of the chosen places and the places of the twist of `P`. 

### `LevelForm`

 The space of algebraic forms of weight (κ, e) on the standard definite space on which the level
cut out by H at the places of S acts through the character χ. 

### `LevelForm.algFormRep_eq_self_of_mem`

 A form is fixed by the elements of `New.stdLevel E n`, the stabiliser of the standard lattice,
that reduce to `1` at all places of `S`. 

### `LevelForm.mem_sphericalAt`

 A form is spherical (fixed by every element of `New.maxCompactAt n w`) at every place `w` such
that neither `w` nor `w̄` is a place of `S`. 

### `_root_.New.Rows.evalForm`

 Evaluation at g, as a complex-linear map on the forms of the level. 

### `LevelForm.toSmoothForm`

 An algebraic form of level H on the standard definite space, viewed as a smooth form, that is, a
form with open stabiliser under right translation. 

### `LevelForm.innerAt`

 For an automorphism σ of ℂ, the pairing sending (φ, φ') to σ⁻¹ of the class sum of
conj(σ φ(g))ᵀ G (σ φ'(g)), with G the integral Gram matrix of weight κ. 

### `LevelForm.apply_mul_eq_smul`

 An element `k` of the level acts on a form, by right translation, through the character `χ`. 

### `LevelForm.innerAt_eq_stdClassSum`

 For a CM field `E`, level places `S`, a subgroup `H` of the product of the groups `GL n` over
the residue fields at the places of `S`, a character `χ` and weight `(κ, e)`, let `φ φ'` be level
forms and `σ` an automorphism of `ℂ`. The pairing `innerAt σ φ φ'` equals `σ⁻¹` of the class sum at
the level `levelOf S.placeAt H`, which consists of the elements of `K₀` whose reductions at the
places of `S` lie in `H`. That class sum is the sum over double cosets `c` of the rational points
and this level in `Gf E n` of `gramForm (σ ∘ φ g_c) (σ ∘ φ' g_c) / #Aut(g_c)`. 

### `LevelForm.conj_innerAt`

 The pairing `innerAt σ` is Hermitian for the conjugation `σ⁻¹ ∘ conj ∘ σ`. 

### `LevelForm.eq_zero_of_innerAt_self`

 The pairing `innerAt σ` is definite: a form whose pairing with itself is zero is zero. 

### `LevelForm.inner_eq_stdClassSum`

 The inner product of two forms is the class sum, at the level cut out by `H`, of the Gram
pairings of their values. 

### `isOfFinOrder_level_char`

 The character `χ` of the finite group `H`, read on the level, has values of finite order. 

### `map_inner_self_eq`

 Let φ, ψ be forms of the level cut out by H, σ ∈ Aut ℂ, p a permutation of the infinite places
carrying the diagrams κ of φ to those of ψ, and write p also for the induced bijection of the
coordinate indices. If for all g, i we have σ(φ(g)_i) = c·a(g)·ψ(g)_{p i},
conj σ(conj φ(g)_i) = c'·a'(g)·ψ(g)_{p i} and a(g)·conj a'(g) = 1, then
σ⟨φ, φ⟩ = conj(c')·c·⟨ψ, ψ⟩. 

 ### Archimedean and l-adic sizes of inner products 

### `normSqAt`

 For σ ∈ Aut ℂ, the number ‖φ‖²_σ: the class sum of the squared Gram norms of the vectors
σ(φ(g)). 

### `norm_map_inner_le`

 Cauchy–Schwarz for conjugates: for forms φ, φ' of one level and σ ∈ Aut ℂ, we have |σ⟨φ',
φ⟩| ≤ ‖φ‖_σ·‖φ'‖_{σ'}, where σ' = conj ∘ σ ∘ conj and ‖φ‖²_σ = `φ.normSqAt σ` is the class sum of
the squared Gram norms of the vectors σ(φ(g)). This is `New.norm_map_stdClassSum_gramForm_le` for
the values of the two forms. 

### `_root_.New.weylGramOver_mul_weylRep`

 Let `ρ` be the representation `New.weylRep κ e` and `G` the Gram matrix of weight `κ`. Then
`G ρ(a) = ρ(aᵀ)ᵀ G`: the matrices of `a` and of its transpose are adjoint for `G`. 

### `_root_.New.map_inv_weightEmbedding_comp_conj`

 For a unitary point `g` and `j : ℂ → ℂ_l`, the component of `g⁻¹` at the embedding of `E`
induced by `j ∘ conj` at the infinite place `τ` is the transpose of the component of `g` at the one
induced by `j`. 

### `_root_.New.gramForm_mem_embValRing`

 Let `j : ℂ → ℂ_l`. If `u` has gauge at most 1 at `g` for `j ∘ conj`, and `v` has gauge at most 1
at `g` for `j`, then the Gram pairing of `u` and `v` lies in the valuation ring `embValRing` of `j`.


### `integralForms`

 The forms integral at j : ℂ → ℂ_l: the module, over the valuation ring `New.embValRing` of j, of
the forms φ whose value φ(g) has gauge `New.weylGauge` at most 1 for every g. 

### `norm_nsmul_inner_le_one`

 Let `j` be an `l`-adic place of ℂ, a ring map `j.ιₚ : ℂ → ℂ_l`. Let A be divisible by the orders
of all stabilisers `classAut` Γ ∩ gKg⁻¹ of the rational points U_n(E) at the level
K = `levelOf S.placeAt H`. If the level form φ is integral at j ∘ conj and φ' is integral at j
(their values have gauge `weylGauge` at most 1), then |j(A·⟨φ, φ'⟩)| ≤ 1. 

 ### Coordinates of a form 

### `ValueIndex`

 The index set of the coordinates of a form: pairs of a class and an index of the standard basis
of the Weyl module. 

### `valueCoord`

 The coordinates of the values of a form at fixed representatives of the classes. 

### `valueMetric`

 The block diagonal matrix with one copy of the Gram matrix of the Weyl module for each class. 

### `map_valueMetric`

 Over `ℂ`, `valueMetric` is the Kronecker product of the identity and the Gram matrix. 

### `stdClassSum_gramForm_eq`

 If the classes have no nontrivial automorphisms, then the class sum of the Gram pairings of the
values conjugated by σ is the pairing of the conjugated coordinates for `valueMetric`. 

### `inner_eq_valueCoord`

 If the classes have no nontrivial automorphisms, then the inner product of forms has the block
Gram matrix `valueMetric` in the coordinates `valueCoord` (the values at representatives of the
classes). 

### `normSqAt_eq_re_valueCoord`

 If the classes have no nontrivial automorphisms, then ‖φ‖²_σ is the squared norm of the
conjugated coordinates for `valueMetric`. 


## Integrality and size of class sums

Arithmetic of class sums `New.classSum Γ K f = ∑ f g / #Aut g` over `Γ \ G / K`, for functions with
values in a weight module `New.WeylIndex V κ → ℂ`.


### `weylGauge_add_le_max`

 The gauge satisfies the ultrametric inequality. 

### `weylGauge_classSum_le_one`

 If every `c • f x` has gauge at most one at `g` and `A` is divisible by the orders of all
stabilisers `classAut Γ K x`, then `A * c` times the class sum of `f` has gauge at most one at
`g`. 

### `sqrt_weylNormSq_classSum_le`

 If the conjugate by `σ` of every `f x` has norm at most `B`, that of the class sum of `f` has
norm at most `B` times the number of double cosets. 
