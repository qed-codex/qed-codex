---
{
  "module": "src/Lib/GaloisRep/WeightCongruence.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/WeightCongruence.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/WeightCongruence.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# ℓ-adic models of algebraic forms and congruences that change the weight

A prime `l` and an isomorphism `ιℓ` from `ℂ` to the algebraic closure of `ℚ_[l]` are fixed. Twisting
an algebraic modular form by its weight, evaluated at the components of `g` above `l`, gives its
`l`-adic model. An ultrametric Stone–Weierstrass theorem is proved. It shows that combinations of
matrix coefficients of free weights are uniformly dense among continuous `l`-adic functions that
factor through general linear groups over one finite extension of `ℚ_[l]`.

## Main definitions and results

* `New.padicComponents`: the continuous homomorphism sending `g` to its components at the places
  above `l` induced by the embeddings `New.weightEmbedding`, one for each infinite place.
* `New.padicModel`: the `ιℓ`-semilinear map `f ↦ (g ↦ M ρ_κ'(z g)⁻¹ ιℓ(f g))`, where `ρ` is
  `New.weylRep` and `z` is `New.padicComponents`.
* `New.stoneWeierstrass_ultrametric`: a function that agrees with an element of `N` on each fibre of
  the family of all multipliers lies in the closure of `N`.
* `New.mem_uniformClosure_weylRep_coeff`: a continuous function that factors through
  `z : X → ∏ GL_N(k)`, whose entries lie in one finite extension of `ℚ_[l]`, is a uniform limit
  (`New.uniformClosure`) of combinations of matrix coefficients of free weights.
* `New.GaloisRep.exists_padicModel_hecke_contraction`: a Hecke operator at a split place, acting on
  `l`-adic functions without increasing the sup norm. It acts on the model of an eigenform by a
  fixed multiple of a coefficient of the Hecke polynomial.
* `New.padicModel_mem_uniformClosure`: the model of a form `f` is a uniform limit from the span of
  models of forms of level `K` and character `θ` whose weights are free (`New.HasNoSmallRelations`)
  at a chosen set `T` of places, if the elements of `K` trivial over `T` fix `f` and have `θ = 1`.

Notions from other files:
* `New.Space.forms`: Algebraic modular forms of weight κ on a definite space V: functions f on G_f
  with open right stabiliser and f(γg) = ρ_κ(γ)f(g) for rational γ, ρ_κ = `New.Space.weightRep`.
* `New.Weight`: for `κ : Weight E` and an infinite place `v` of `E`, `κ.1 v h` is the number of
  columns of height `h` of a Young diagram, and `κ.2 v` is an integer exponent of the determinant.
* `New.weylRep`: The monoid homomorphism from ∏_τ GL(n_τ,R) to square matrices sending g to ∏_τ
  det(g_τ)^{e_τ} times the Schur matrix of g, for integers e_τ; its rows and columns are indexed by
  `WeylIndex`/`WeylIndexFamily`, the coordinates of vectors of weight κ.
* `New.HasHeckePolyAt`: At the split place w, f is fixed by K_w, each Hecke operator T_{w,j} acts on
  f by a scalar t_j, and P = Σ(−1)^j q_w^{j(j−1)/2} t_j X^{n−j}.
* `New.ofSplitPlace`: For a split place w, the homomorphism GL_n(E_w) → G_f sending g to the unitary
  element with component g at w and 1 off w, w̄.

## Relation to the literature

Known result: Non-archimedean Stone–Weierstrass theorem for modules (localisation form). The result
concerns scalar-valued functions on a compact space over an ultrametric normed field. A continuous
function that agrees with some member of a subspace on each level set of the subspace's multipliers
lies in the closure of that subspace. Source: Dieudonné 1944; Kaplansky, The Weierstrass theorem in
fields with valuations (1950); module form as in Prolla, Approximation of Vector Valued Functions
(1977) and Topics in Functional Analysis over Valued Division Rings (1982).

Known result: Density of algebraic vectors, congruences to supercuspidal types, and limits of
eigensystems. For definite unitary groups, a form is an l-adic uniform limit of forms with very
different weight gaps at some embeddings and a prescribed character on the level, such as a wild
type. No completed cohomology or congruences modulo powers of l are used. Source: M. Emerton, V.
Paškūnas, On the density of supercuspidal points of fixed regular weight, J. Éc. polytech. Math. 7
(2020); J. Fintzen, S. W. Shin, Congruences of algebraic automorphic forms and supercuspidal
representations, Camb. J. Math. 9 (2021); Kaplansky, Proc. AMS 1 (1950).



## The ℓ-adic model of an algebraic form

* `New.comp_weightRep_eq_weylRep_mulVec`: on a rational point the weight acts, after `ιℓ`, through
  `New.padicComponents`.


### `padicComponents`

 The homomorphism sending g to the family, over infinite places v, of its component at the place
induced by x ↦ ιΦ_v(x̄) (`New.weightEmbedding`; Φ_v is the embedding of the CM type at v, x̄ the
complex conjugate of x), read in GL_n(Q̄_l). 

### `padicModel`

 The ι-semilinear map sending f to the l-adic function g ↦ M ρ_{κ'}(z(g))⁻¹ ι(f(g)), with
z = `New.padicComponents`, viewed as a function of g and a coordinate. 

### `comp_weightRep_eq_weylRep_mulVec`

 For a rational point `γ`, applying `ιℓ` turns the action of `γ` on vectors of weight `κ` into
multiplication by the matrix `weylRep` at `padicComponents` of the finite adelic image of `γ`. 

### `exists_padic_field_of_form_values`

 The values `ιℓ (f g i)` of an algebraic form `f` of weight `κ` all lie in one finite extension
`L` of `ℚ_[l]` inside its algebraic closure. 


## Density of matrix coefficients of weights

A Stone–Weierstrass theorem over an ultrametric field `k`, applied to matrix coefficients of general
linear groups. For a submodule `N` of `C(X, k)`, `N / N` is the set of its multipliers.


### `New.stoneWeierstrass_ultrametric`

 An ultrametric Stone–Weierstrass theorem. Suppose that for each point `a` some `d ∈ N` equals
`φ` at all points where every multiplier `u ∈ N / N` takes the same value as at `a`. Then `φ` lies
in the closure of `N`. 

### `New.natCast_le_rank_of_isAlgClosed`

 An algebraically closed extension of `ℚ_[l]` has infinite degree over every finite extension. 

### `New.hasNoSmallRelations_of_lacunary`

 Natural numbers `y 0, …, y (n - 1)` in which each `y j` is below `y i / (n + 1) ^ 2` for all
`i < j` give free integers `-y i` (`New.HasNoSmallRelations`: a short sum of them, with its number
of terms, determines how often each occurs). 

### `New.hasNoSmallRelations_of_rapid_decrease`

 Column multiplicities `κ h` that equal `(N + 1) ^ (4 * (N - h))` for `h ≥ 2` and are at least
that for `h = 1` give a weight whose shifted entries `-∑_{j < h < N} (κ h + 1)`, `j < N`, are free
(`New.HasNoSmallRelations`). 

### `New.mem_uniformClosure_weylRep_coeff`

 Let `k` be an algebraically closed ultrametric normed field over `ℚ_[l]`, `X` compact, and `z` a
continuous family, over a finite set `Φ`, of invertible `N × N` matrices with entries in one finite
extension `L` of `ℚ_[l]`. A continuous `φ` factoring through `z` is a uniform limit of sums of
matrix coefficients `γ ↦ β ⬝ᵥ weylRep κ e (z γ) *ᵥ ξ` (any `e`) of weights `(κ, e)` satisfying a
freeness condition at every `τ`. The condition is that the integers
`e_j = -∑_{j < h < N} (κ τ h + 1)`, `j < N`, have no small relations (`New.HasNoSmallRelations`): if
`α`, `β` are vectors of natural numbers with `∑ α j = ∑ β j ≤ (N + 1) ^ 2` and
`∑ α j e_j = ∑ β j e_j`, then `α = β` (these `e_j`, `α`, `β` are not the `e`, `β` of the matrix
coefficients). 

 ## Approximation by forms with weights free at chosen places 

### `InducesPlacePair`

 The statement that the finite place `u` of E induced by the l-adic embedding x ↦ ιΦ_v(x̄)
attached to the infinite place `v` (`New.weightEmbedding`) is w or its conjugate w̄. 

### `inducesPlacePair_mk`

 An embedding of `E` that induces the place `w` lies over an infinite place inducing `w` or its
conjugate. 

### `padicComponents_ofSplitPlace`

 An element supported at `w` and its conjugate has component `1` over `τ`, unless `w` lies above
`l` and `τ` induces `w` or its conjugate. 

### `InducesPlacePair.atPlace_eq_one`

 If `v` induces `w` or its conjugate and the component of `g` over `v` is `1`, then `g` is `1`
at `w`. 

### `GaloisRep.exists_padicModel_hecke_contraction`

 For a place `w` distinct from its conjugate and an index `j` there are a scalar `a ≠ 0`, with
(a) `a = -1` when `w` does not contain `l`, and a linear operator `T` on `l`-adic functions such
that: (b) `T` does not increase sup norms; (c) `T F = (a * ιℓ (P.coeff j)) • F` for the model
`F = padicModel κ κ' M f` if `f` has Hecke polynomial `P` at `w` and `M` intertwines weights `κ'`
and `κ` (`κ.1`: column heights) on the elements supported at `w` and its conjugate. 

### `map_mem_uniformClosure_of_bound`

 A linear map that is bounded for the uniform norms and sends `S` into the span of `D` sends
uniform limits from the span of `S` to uniform limits from the span of `D`. 

### `exists_weylRep_eq_submatrix_kronecker`

 Splitting the places into `T` and its complement writes `weylRep` as a Kronecker product, up to
a reindexing `σ` of rows and columns; `p` is the pair of the restrictions of the weight `μ` to `T`
and to its complement, and the exponents `η` are split in the same way. 

### `continuous_character_smul_form`

 For a character `θ` of `K` that is `1` near `1`, a form `f` of weight `κ` and `c` in
`Gf E (Fin N)`, the function `k ↦ (ιℓ (θ k), ιℓ (θ k⁻¹) • ιℓ ∘ f (c * k))` on `K` is continuous.
It is locally constant, since `f` has an open right stabiliser and `θ` is `1` near `1`. 

### `padicComponents_apply_mem_iSup_adjoin`

 The entries of the component over `τ ∈ T` of `padicComponents x` lie in the compositum, over the
places of `T`, of the fields generated over `ℚ_[l]` by the images of `E` under `weightEmbedding`. 

### `padicModel_mem_uniformClosure`

 Let `K` be an open subgroup of `New.stdLevel`, `θ` a character of `K` trivial near `1`, `T` a
set of infinite places and `f` a form of weight `κ` fixed by every `d ∈ K` whose components
(`New.padicComponents`) over `T` are `1`, with `θ d = 1` for these `d`. Suppose the span of `D`
contains `padicModel κ ν M φ` for all weights `ν` equal to `κ` off `T` and free on `T`
(`New.HasNoSmallRelations`), forms `φ` of type `θ`, and matrices `M` intertwining `ν` and `κ` on
the families that are `1` over `T`. Then the `l`-adic model of `f` is a uniform limit from the span
of `D`. 
