---
{
  "module": "src/Lib/LocalGL/Shintani/CosetDescent.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/LocalGL/Shintani/CosetDescent.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/LocalGL/Shintani/CosetDescent.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Descent of class functions along a coset and lifts from GL_n(k') ⋊ Gal(k'/k)

This file applies descent along a coset to `GL_n(k') ⋊ Gal(k'/k)` for an extension `k'/k` of finite
fields. Here functions on similarity classes of matrices (`New.Hall k`) are multiplied by parabolic
induction. It defines lifts of such functions from `k` to `k'` and proves that they are stable under
differences and products. It then shows that the eigenvalue sums `New.Hall.brauerLift k θ` have
virtual lifts.

## Main definitions and results

* `New.DescendsTo Φ X`: a function Φ on GL_n(k') ⋊ Gal(k'/k) (`New.GalSemidirect`) descends to X,
  that is, Φ(s) = X(s^{ord σ}) on the coset of each σ whose fixed field is the field of X.
* `New.Lift Z F F'`: in each rank, some `Z`-combination of characters of `GL_n(k') ⋊ Gal(k'/k)`
  descends to `F` over `k` and to `F'` over `k'`.
* `New.Lift.sub`, `New.Lift.mul`, `New.Lift.mulMoebius`,
  `New.Lift.rankPart_mulMoebius_mul_constOne`: lifts are stable under differences, under the
  product, and under pointwise multiplication by the inverse μ (`moebius`; `F.mulMoebius` is F·μ) of
  the constant function 1.
* `New.exists_torus_induced_descendsTo`: the character induced from (k' ⊗ L)ˣ ⋊ Gal(k'/k), for
  [L:k] = m, descends to C_θ·μ over k, where C_θ = `New.Hall.greenCuspidal` k θ.
* `New.exists_lift_brauerLift`: the eigenvalue sum `β_θ = New.Hall.brauerLift k θ` has a virtual
  lift. It is obtained from `New.exists_torus_induced_descendsTo` by recursion on the rank and
  `β_θ = −C_θ ∗ 𝟙`.

Notions from other files:
* `New.Hall.constOne`: The complex-valued function on classes of endomorphisms that takes the value
  1 on every class, in every dimension.
* `New.Hall.rankPart`: The function on similarity classes equal to F on classes of dimension n and
  zero on the others.
* `New.Hall.rankInner`: For complex functions F, H on similarity classes, the average over GL_n(k)
  of the conjugate of F times H.
* `New.IsRootChoice` (`Lib.LocalGL.Shintani.CosetRootChoice`): a conjugation-equivariant choice of
  `(ord σ)`-th roots over `σ`.
* `New.induceClassFn` (`Lib.LocalGL.Shintani.CosetRootChoice`): induction of class functions
  along `ρ` over `Γ`.

## Relation to the literature

Known; see `Lib.LocalGL.Shintani.LiftingGreenCharacters` and `Lib.LocalGL.Green.CuspidalFunctions`
for sources.



## Descent from GL_n(k') ⋊ Gal(k'/k) and lifts under products

`F.evalGL` is the restriction of a function `F` in `New.Hall k` to one `GL_n(k)`, and
`New.virtualChars Z G` is the `Z`-span of the characters of `G`. For levels `b : n → ι`,
`parabolic b` is the subgroup of block upper triangular matrices and `blockHom b i` takes the
diagonal block of level `i`.


### `galActionGL`

 The action of Gal(k'/k) on GL_n(k') by group automorphisms, applying the field automorphism
to each matrix entry. 

### `GalSemidirect`

 The semidirect product GL_n(k') ⋊ Gal(k'/k), the Galois group acting on matrix entries. 

### `HasFixedField`

 The fixed field of σ ∈ Gal(k'/k) is k₀: the image of k₀ in k' is exactly the set of elements
fixed by σ. 

### `DescendsTo`

 For each σ ∈ Gal(k'/k) with fixed field k₀ and each s over σ in GL_n(k')⋊Gal(k'/k) whose
power s^{ord σ} is γ ∈ GL_n(k₀), Φ(s) = X(γ). 

### `HasCommonLift`

 Some Z-combination Φ of characters of GL_n(k') ⋊ Gal(k'/k) descends, in the sense of
`New.DescendsTo`, both to F over k and to F' over k'. 

### `Lift`

 F lifts to F' over Z: for every m, one Z-combination Φ of characters of GL_m(k')⋊Gal(k'/k)
satisfies `New.DescendsTo` for both F (over k) and F' (over k'). 

### `reindexGL_comp_galActionGL`

 Renumbering the rows and columns along `e` commutes with the action of `τ` on the entries. 

### `descendsTo_comp_reindexGL`

 Renumbering the rows and columns along `e` keeps the relation `DescendsTo` with `X`. 

### `Lift.hasCommonLift`

 If (F, F') is a lift with coefficients in Z, then for every finite index set n some
Z-combination of characters of GL_n(k')⋊Gal(k'/k) descends (`New.DescendsTo`) to F over k and to F'
over k'. 

### `isClassFunction_evalGL`

 The restriction `F.evalGL` of a function on similarity classes to `GL n k` is a class
function. 

### `DescendsTo.of_evalGL_eq`

 If `Φ` descends to `X` (`New.DescendsTo`) and `Y` takes the same values as `X` on
`GL n k₀`, then `Φ` descends to `Y`. 

### `evalGL_moebius_add_one_sub_constOne_pow_mul`

 On `GL_m(k₀)`, the function `moebius + (1 - constOne) ^ (m + 1) * -moebius` agrees with
`moebius`: its second term vanishes on classes of dimension at most `m`. 

### `moebius_add_one_sub_constOne_pow_succ_mul`

 One step `J ↦ J - (constOne * J - 1)` of the iteration that approaches `moebius` takes
`moebius + (1 - constOne) ^ N * -moebius` to the same expression with exponent `N + 1`. 

 ### First properties and examples of lifts 

### `exists_isRootChoice_GL`

 Let σ have fixed field k₀. Then the matrices γ in GL_n(k₀) have (a) a natural choice of
(ord σ)-th roots r(γ) over σ in GL_n(k') ⋊ Gal(k'/k) (`New.IsRootChoice`) such that (b) the matrix
part of r(γ) lies in every k'-subalgebra of matrices that contains the image of γ. 

### `DescendsTo.iff_comp_inl_eq_evalGL`

 Φ descends to a class function F' over k' itself exactly when F' is the restriction of Φ to
GL_n(k'). 

### `Lift.exists_lift_of_descendsTo`

 If in every rank some Z-combination of characters descends to F, then F lifts to some class
function G over k'. 

### `hasCommonLift_of_gal_trivial`

 Suppose Gal(k'/k) is trivial, F' on GL_n(k') is a Z-combination of characters, and F' agrees
with F on GL_n(k). Then some Z-combination of characters of GL_n(k') ⋊ Gal(k'/k) descends
(`New.DescendsTo`) to both F and F'. 

### `Lift.rankPart_of_hasCommonLift`

 If one Z-combination Φ of characters of GL_m(k')⋊Gal(k'/k) descends (`New.DescendsTo`) to F over
k and to F' over k', then the dimension m parts of F and F' form a lift over Z in all ranks. 

### `Lift.lift_constOne`

 The constant function 1 lifts to itself, through the trivial character. 

### `Lift.one`

 The unit of the product, the dimension 0 part of the constant function, lifts to itself. 

### `Lift.evalGL_mem_virtualChars`

 If `F` lifts to `G` with coefficients in `Z` (`New.Lift`, here with both functions over
`k`, so along the trivial extension `k/k`), then the restriction of `F` to `GL_n(k)` is a
`Z`-combination of characters of `GL_n(k)`. 

### `Lift.sub`

 If F lifts to F' and G lifts to G' with coefficients in a commutative ring R (`New.Lift`), then
F - G lifts to F' - G'. 

### `DescendsTo.induceClassFn_parabolic`

 Let `b` split the indices `n` into ordered blocks. Let `P` be the subgroup of
`GL_n(k') ⋊ Gal(k'/k)` whose matrix part is block upper triangular for `b`, and let `β i` send an
element of `P` to its `i`-th diagonal block together with its Galois part. If each `Ψ i` is a
`Z`-combination of characters of its block's group that descends to `Y i` (its value at `s` over `σ`
with fixed field `k₀` is `Y i` at `s ^ orderOf σ`), then the function induced along `P`
(`induceClassFn`; it conjugates only by matrices, since `rightHom` is the Galois part) from the
product of the `Ψ i ∘ β i` descends to the induction product of the `Y i`, each `Y i` taken in the
dimension of its block. 

### `sum_evalGL_prod_rankPart`

 The value of the product `F * G` at `γ` in `GL_m(k)`, sorted by the dimension `a` of the stable
subspace: it is the sum over `a ≤ m` of the value at `γ` of the product of the part of `F` of
dimension `#{j < a} = a` and the part of `G` of dimension `#{j ≥ a} = m - a`. 

### `Lift.mul`

 `F` lifts to `F'` over `Z` (`New.Lift`) when, for every `m`, one `Z`-combination of characters
of `GL_m(k') ⋊ Gal(k'/k)` descends (`New.DescendsTo`) both to `F` over `k` and to `F'` over `k'`.
Lifting is multiplicative: if `F` lifts to `F'` and `G` lifts to `G'` over `Z`, then the
parabolic-induction product `F * G` lifts to `F' * G'`. 

 ### The inverse of the constant function, and characters of degree one 

### `Lift.mulMoebius`

 If F lifts to F' with coefficients in a commutative ring R, then F·μ lifts to F'·μ. Here μ is
the inverse of the constant function 1 for the parabolic-induction product. 

### `Lift.rankPart_mulMoebius_mul_constOne`

 If F lifts to F', then (−1)^m times the dimension m part of `F.mulMoebius * constOne` lifts to
the same expression for F'. Here `F.mulMoebius` is the pointwise product F·μ, with μ the inverse of
`constOne`. 

### `exists_norm_char_semidirect`

 Let S be a finite monoid, α an action of Gal(k'/k) on its unit group Sˣ, and ν : S → ℂ a monoid
homomorphism. Then there is a function ϑ on Sˣ ⋊ Gal(k'/k) such that (a) ϑ is a character, (b)
ϑ(s) = ∏_τ ν(α(τ) s₁), with s₁ the component of s in Sˣ, and (c) for σ with fixed field k,
ϑ(s) = ν(γ) whenever s lies over σ and s^{ord σ} = γ. 


## Green's theorem with Galois action for Brauer functions

Let `k'/k` be an extension of finite fields and `θ` a multiplicative character of an algebraically
closed field `K` over `k'`.


### `simClassOf_leftMulMatrix`

 For a basis `b` of a finite `k`-algebra `A` and an element `t` of `A`, the matrix of left
multiplication by `t` in the basis `b` and left multiplication by `t` on `A` have the same
similarity class. 

### `basis_repr_congr_one_apply`

 Let `b` be a basis of `L` over `k`, and `σ ∈ Gal(k'/k)`. Applying `σ` to the factor `k'` of
`k' ⊗[k] L` applies `σ` to the coordinates in the basis of `k' ⊗[k] L` over `k'` induced by `b`. 

### `mem_range_unitsMap_includeRight_iff`

 Let `σ ∈ Gal(k'/k)` have fixed field `k` and act on `k' ⊗[k] L` through the factor `k'`. A unit
of `k' ⊗[k] L` is `1 ⊗ y` for a unit `y` of `L` exactly when `σ` fixes it. 

### `descendsTo_induceClassFn_greenCuspidal_mulMoebius`

 Let `L` be an extension of `k` of degree `m` with basis `b`. Let `β` be the action of
`Gal(k'/k)` on `(k' ⊗[k] L)ˣ` through the factor `k'`, and let `ρ` map `(k' ⊗[k] L)ˣ ⋊ Gal(k'/k)` to
`GL_m(k') ⋊ Gal(k'/k)` by sending a unit to its multiplication matrix in the basis induced by `b`;
by `h_comp` this map turns `β` into the entrywise action `galActionGL`. Suppose `ϑ` is a character
of `(k' ⊗[k] L)ˣ ⋊ Gal(k'/k)` with `ϑ s = θ (φ u)` whenever `s` lies over some `σ` with fixed field
`k` and `s ^ orderOf σ = u`. Then the induction of `ϑ` along `ρ` descends over `k` to
`(New.Hall.greenCuspidal k θ).mulMoebius`, that is, to `((β_θ·μ) ∗ 𝟙)·μ`, where `μ` is the inverse
of `𝟙` for the induction product: its value at each such `s` equals that class function at
`s ^ orderOf σ ∈ GL_m(k)`. 

### `descendsTo_induceClassFn_of_rankInner_eq`

 Descent over `k'` in `exists_torus_induced_descendsTo`. Let `B` be a `k'`-basis of `k' ⊗[k] L`,
let `β` be the action of `Gal(k'/k)` on `(k' ⊗[k] L)ˣ` through the factor `k'`, and let
`ρ : (k' ⊗[k] L)ˣ ⋊ Gal(k'/k) → GL_m(k') ⋊ Gal(k'/k)` send a unit to its matrix in `B`. If `ϑ` is a
character with `ϑ(s) = ∏_τ θ(φ(τ s₁))`, where `s₁` is the unit part of `s`, then the class function
induced from `ϑ` along `ρ` over `Gal(k'/k)` satisfies `DescendsTo` (equals `X` on `GL_m(k')`) for
every `X : Hall k'` whose rank-`m` inner product with every `Y` is the mean over units `t` of
`conj θ(φ(∏_τ τ t))` times `Y` at the class of multiplication by `t`. 

### `exists_torus_induced_descendsTo`

 Let `k ⊆ k'` be finite fields, `K` a field over `k'` with a multiplicative character `θ`, `L` an
extension of `k` of degree `m`, and `φ : k' ⊗[k] L → K` a `k'`-algebra map. (a) There is a character
`Φ` of `GL_m(k') ⋊ Gal(k'/k)` that (b) descends over `k` to `C_θ·μ`, and (c) descends over `k'` to
every `X : Hall k'` whose rank-`m` inner product with every `Y` is the mean over `t ∈ (k' ⊗[k] L)ˣ`
of `conj θ(φ(∏_τ τ t))` times `Y` at the class of multiplication by `t`. Here
`C_θ = greenCuspidal k θ = (β_θ·μ) ∗ 1`, `μ` is the inverse of the constant function 1 for parabolic
induction, `τ ∈ Gal(k'/k)` acts on the factor `k'`, and `DescendsTo Φ X` means `Φ(s) = X(s^{ord σ})`
whenever `s` lies over a `σ` whose fixed field is the field of `X`. 

### `exists_lift_brauerLift`

 For a multiplicative character `θ` of `K`, let `β_θ = New.Hall.brauerLift k θ` send a matrix
over `k` to the sum of `θ` over the roots of its characteristic polynomial, with multiplicity. Then
some class function `B : Hall k'` lifts `β_θ` over `ℤ` (`New.Lift`). That is, for each `m` one
ℤ-combination of characters of `GL_m(k') ⋊ Gal(k'/k)` descends to both. 
