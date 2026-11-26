---
{
  "module": "src/New/OneLift/FalseLifts/PeriodsOfFalseLifts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/FalseLifts/PeriodsOfFalseLifts.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/FalseLifts/PeriodsOfFalseLifts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The tower of descents and the periods of false lifts

This file applies the inductive step of `New.OneLift.FalseLifts.HyperbolicPlaneStep` to false lifts
`Ξ` on a definite space `I_n`. Such a `Ξ` is killed by the descent `O.normalizedDescent` to `W`, by
the hyperplane sums at the chosen places, and by one Hecke polynomial. The file builds the tower of
vanishing descents to `W ⊕ ℍ^N` and deduces that the periods of `Ξ` over the block `I_l` of
`I_n = I_N ⊕ I_l` vanish, written as class sums. Here `O` is a descent pair `(W, I_n)`
(`New.DescentPair`) of ranks `r < n`. It carries two finite families of finite places, the chosen
places `O.chosenPlace` and the twist places `O.twistPlace`, which together form the level
`O.places`, and a character `O.tamePart w` of each residue field; the results on the tower and on
periods assume `2 r + 2 N + 3 < n`.

## Main definitions and results

* `New.Rows.stdClassSum_gramForm_eq_zero`: Periods of false lifts vanish, as class sums.

## The steps of the argument

* The bottom of the tower: `New.Rows.lift_polyVector_blockDatum_eq_zero` passes from the harmonic
  polynomial to all polynomials, and `New.DescentPair.descentsVanish_of_hyperplaneSumsAnnihilate`
  passes from the block datum to all data.
* The tower `New.Rows.descentsVanish_hyperbolicSum`: all descents of the coefficients of `Ξ` to
  `W ⊕ ℍ^N` vanish, for data that are the vacuum off the places of the level.
* From descents to periods, for `I_n = I_N ⊕ I_l`:
  `New.Rows.integral_conj_pairTheta_mul_algFormCoeff_eq_zero` absorbs the kernel of `W` and applies
  `New.SiegelWeil.integral_blockEmb_eq_zero_of_descentsVanish`, which takes a Fourier coefficient
  and varies the datum.
* The theorem `New.Rows.stdClassSum_gramForm_eq_zero` writes the periods over the block `I_l` as
  class sums `New.stdClassSum`. `New.Rows.stdClassSum_gramForm_eq_zero_of_rank_one` is the case of
  false lifts from a line; that of false lifts on `V_j` is in
  `New.OneLift.ComparisonOperator.GluingMaps`.
* Two uses: `New.Rows.stdClassSum_period_eq_zero` for point forms, and
  `New.Rows.DividedSplitting.stdClassSum_inner_productForm_eq_zero` for the product forms
  `New.Rows.DividedSplitting.productForm` of the kernel vectors.

Notions from other files:
* `New.pairWeil`: the Weil representation of U(W) × U(V) on the data space 𝒮(Hom(W, V)), twisted by
  two characters of U(1); `New.Space.θ` is the theta functional on that space.
* `New.Space.projOn`: the projection whose fixed vectors are the data that are the vacuum at the
  places of a set `S` and their conjugates. For `S` the complement of the places of the level and
  their conjugates, these are the test vectors.
* `New.heckePolyOp`: the operator ∑ (−X)^i q^(i choose 2) T_{w,i}, q the order of the residue field
  at w; `New.sphericalAt π w` is the space of vectors spherical at w.
* `New.algFormCoeff`: the matrix coefficient `g ↦ L (ρ(g_∞⁻¹) φ(g_f))` of a form `φ` at a functional
  `L`, with `ρ` the representation `New.conjWeylRep` on the vectors `New.WeylIndex n κ → ℂ` and `L`
  often `New.gramForm ζ`, the invariant inner product with `ζ`.
* `New.SiegelWeil.descentsVanish_add_planes`: vanishing of descents passes from `W` to `W` plus
  hyperbolic planes for `Y` killed by a Hecke polynomial at a small point.

## Relation to the literature

Let V=V₁⊕V₂ with V₁ of small rank, and take a form on a definite U(V) that is killed by theta
descent, by the hyperplane sums at the chosen places (as good forms are), and by a Hecke polynomial
at one split place at the smallest root of lifts. Then it has zero theta periods over U(V₂), so the
forms built from these kernels are orthogonal to it. It is known that vanishing of lifts in a theta
tower kills theta periods on a subgroup. Related work: C. Wu, Poles of Eisenstein series and theta
lifts for unitary groups, arXiv 2104.11954, 2021; Ginzburg–Jiang–Soudry, Poles of L-functions and
theta liftings for orthogonal groups, 2009; Jiang–Wu, On (χ,b)-factors of cuspidal automorphic
representations of unitary groups I, 2016; Rallis, On the Howe duality conjecture, 1984.


### `lift_polyVector_blockDatum_eq_zero`

 Let `O` be a descent pair `(W, I_n)` that fits the parameter `l₀` on `W`, and let the descent
`O.normalizedDescent` to `W` kill the form `Ξ` on `I_n`. Then the descent to `W`, twisted by the
character `O.charW`, of the conjugate matrix coefficient (`algFormCoeff`) of `Ξ` at the highest
vector vanishes for every datum `v_P ⊗ O.blockDatum`, where `v_P` is the Fock vector of a polynomial
`P` and `O.blockDatum` is the finite datum of the pair. 

### `descentsVanish_hyperbolicSum`

 Let the archimedean parameter `l₀` on `W` correspond to the parameter `O.paramV` on `I_n`,
compatibly with the weights of `O` (`O.FitsParams`), and let the residue characters
`χ_v = O.tamePart v` be nontrivial at the twist places. Let the algebraic form `Ξ` on `U(I_n)` be
killed by
* each product over the chosen places `v` of the sums `∑ χ_v(det s)⁻¹ s` over the invertible
  `s = 1 + u λ_v`, for rows `λ_v` that are not all zero,
* the theta descent `O.normalizedDescent` to `W`,
* the Hecke polynomial at the number `O.liftHeckeRoot w`, for a split place `w` of norm `q` off the
  level.

If `2 card r + 2 card N + 3 < card n`, then the theta descents to `W ⊕ ℍ^N` of the conjugate matrix
coefficient of `Ξ` at any vector `ζ` vanish, for all data of the Weil representation that are the
vacuum at the finite places other than those of the level and their conjugates
(`DescentsVanish`). 

### `exists_projOn_eq_pairTheta_ne_zero`

 At every point `p` of `U(W)(𝔸) × U(V)(𝔸)` some datum `φ` in `𝒮(Hom(W, V))` has a nonzero theta
kernel `pairTheta W V a b φ p`, twisted by the characters `a` and `b`. This `φ` can be chosen fixed
by `projOn (W.hom V) T`, the mean over the Heisenberg operators of integral vectors at the places of
`T` and their conjugates. 

### `integral_conj_pairTheta_mul_algFormCoeff_eq_zero`

 Let the archimedean parameter `l₀` on `W` correspond to the parameter `O.paramV` on `I_n`
(`O.FitsParams`), and let the residue characters `O.tamePart` be nontrivial at the twist places. A
false lift is here an algebraic form `Ξ` on the definite group `U(I_n)` with three properties. It is
killed by the hyperplane sums at the chosen places. It is killed by the theta descent
`O.normalizedDescent` to `W`. It is killed by the Hecke polynomial at a split place `w` off the
level, taken at the number `O.liftHeckeRoot w` of modulus `q^(1 - n + r / 2)`, `q` the norm of `w`.
Let `ε` split `I_n = I_N ⊕ I_l` with `2 r + 2 N + 3 < n`. Then the integral over `h₂` in the adelic
quotient of `U(I_l)` of the conjugate theta kernel of the pair `O.W, I_l` times the matrix
coefficient `algFormCoeff 1 (gramForm ζ) Ξ` at `(h₁, h₂) γ` is zero. This holds for every vector
`ζ`, every character `b` of `U(1)` twisting the kernel, all `g` and `h₁`, every finite `γ` supported
on `O.places`, and all data `φ` that are the vacuum off these places and their conjugates. 

### `stdClassSum_gramForm_eq_zero`

 Let the archimedean parameter `l₀` on `W` correspond to the parameter `O.paramV` on `I_n`
(`O.FitsParams`), and let the residue characters `O.tamePart` be nontrivial at the twist places. Let
the algebraic form `Ξ` on `U(I_n)` be killed by the hyperplane sums at the chosen places. Let `Ξ`
also be killed by the theta descent `O.normalizedDescent` to `W`, and by the Hecke polynomial at the
number `O.liftHeckeRoot w` for a split place `w` off the level. Let `ε` split `I_n = I_N ⊕ I_l` with
`2 #r + 2 #N + 3 < #n`, and let `x` be supported on `O.places`. Let `ϑ` be a function on the finite
points of `U(I_l)` whose coordinates, moved by the real points, are multiples of conjugate theta
kernels of the pair `O.W, I_l` with data that are the vacuum off `O.places` and their conjugates.
Let the conjugate-linear map `C` carry its values to the space of values of `Ξ`, equivariantly for
the real points of `U(I_l)` acting by `conjWeylRep`, the representation of the given weight. Then
the invariant inner product `gramForm` of `C (ϑ h)` with `Ξ ((h₁, h) x)`, the block point being
`U.block ε (h₁, h)`, is left invariant under the rational points. Its class sum `stdClassSum` is
zero at every level `K` that fixes it. 

### `stdClassSum_gramForm_kernelVector_eq_zero`

 The case of `stdClassSum_gramForm_eq_zero` in which `ϑ h` is `kernelVector O b 𝔪 Ψ κ g h`, the
vector of the values at `(g, h)` of the conjugate theta kernels of the pair `O.W, I_l`, one for each
basis polynomial of weight `κ`, with the finite datum `Ψ` modulo the ideal `𝔪`, whose places lie in
the level `O.places`. Let the archimedean parameter `l₀` on `W = O.W` correspond to that on `I_n`
(`O.FitsParams`), and let the residue characters `O.tamePart` be nontrivial at the twist places. Let
the form `Ξ` on `U(I_n)` be killed by the hyperplane sums at the chosen places, by the theta descent
to `W`, and by the Hecke polynomial at the number `O.liftHeckeRoot w` for a split place `w` off the
level. Let `ε` split `I_n = I_N ⊕ I_l` with `2 #r + 2 #N + 3 < #n`, let `C` be conjugate-linear and
equivariant for the real points of the block `I_l` acting by `conjWeylRep`, and let `x` be supported
on `O.places`. If the level `K` fixes `Ψ` and its conjugate by `x` fixes `Ξ`, then the class sum
over `K` of the invariant inner product `gramForm` of `C (ϑ h)` with `Ξ ((h₁, h) x)` is zero. 

### `coeff_labelIdem_X_sub_one`

 In rank one the idempotent `labelIdem` that the polynomial `X - 1` labels in the group algebra
of `GL_1(k)` is the mean over the group: each coefficient is the inverse of the group order. 

### `hyperplaneSum_mul_labelIdem_X_sub_one`

 Let `k` be a finite field, `χ ≠ 1` a character of `kˣ` and `l ≠ 0` a row of length one. The
hyperplane sum `∑ χ(det s)⁻¹ s` over the invertible `s = 1 + u l`, an element of the group algebra
of `GL_1(k)`, annihilates the idempotent of the label `X - 1`, the mean over the group. 

### `hyperplaneSum_apply_eq_zero_of_rank_one`

 Let `O` be a descent pair `(W, I_n)` with `W` a line (index type `Unit`), and let the residue
characters `χ_w = O.tamePart w` be nontrivial at the chosen places `w`. The product of the groups
`GL_1(k_w)` acts on the forms on `U(I_n)` by `O.formAction`. Let `Ξ` lie in the image of the mean
over this product, which is the idempotent `tupleIdem` of the labels `X - 1`. Then `Ξ` is killed by
every tensor product (`piTensorElem`) of hyperplane sums `∑ χ_w(det s)⁻¹ s`, over the invertible
`s = 1 + u (v w)`, in which one row `v i` is not `0`. 

### `stdClassSum_gramForm_eq_zero_of_rank_one`

 Periods of false lifts from a line vanish. Let the archimedean parameter `l₀` on `W` correspond
to that on `I_n` (`O.FitsParams`), and let the residue characters `O.tamePart` be nontrivial at all
places of the level. Let the form `Ξ` on `U(I_n)` be a false lift (`O.falseLiftsAt`): it lies in the
image of the mean over the product of the groups `GL_1(k_v)` at the chosen places `v`, and it is
killed by the theta descent `O.normalizedDescent` to `W` and by the Hecke polynomial at the number
`O.liftHeckeRoot w` for a split place `w` off the level. Let `ε` split `I_n = I_N ⊕ I_l` with
`2 #N + 5 < #n`, and let `x` be supported on `O.places`. Let each coordinate of `ϑ`, moved by the
real points of `U(I_l)`, be a multiple of a conjugate theta kernel (`pairTheta`) of the pair
`O.W, I_l` whose datum is the vacuum off `O.places` and their conjugates. Let `C` be
conjugate-linear and equivariant for the real points of `U(I_l)`, which act by the representation
`conjWeylRep` of the given weight. Then the invariant inner product `gramForm` of `C (ϑ h)` with
`Ξ ((h₁, h) x)` is left invariant under the rational points, and its class sum is zero at every
level `K` that fixes it. 

### `algFormRep_conj_block_apply_eq_self`

 Conjugates of the second block fix forms. Let `ε` split `I_n = I_N ⊕ I_l`, with `U.block ε` the
block diagonal embedding; `reduceAt` is reduction to the residue field and `inclMatrix e` the matrix
of the columns `e` of `1`. Let `A` in the maximal level `stdLevel E n` have columns `O.incl` equal
to `Y` at the chosen places, and rows `e'`, which lie in the block `N` through `rowInBlock`, equal
to the rows `O.incl` of `1` at the twist places. If `x` is supported at the chosen places and
`x⁻¹ (1, k) x` lies in `stdLevel E n` and fixes `Y`, then right translation (`algFormRep`) by the
conjugate of `(1, k)` by `x * A` fixes every form `Ξ`. 

### `stdClassSum_period_eq_zero`

 Periods against point forms vanish. Let `O` be a descent pair `(W, I_n)`; its level `O.places`
consists of the chosen places and the twist places. Let the archimedean parameter `l₀` on `W`
correspond to that on `I_n` (`O.FitsParams`), and let the residue characters `O.tamePart` be
nontrivial at the twist places. Let the form `Ξ` on `U(I_n)` be killed by three things: the
hyperplane sums (character sums over the matrices `1 + u λ`) at the chosen places, the theta descent
`O.normalizedDescent` to `W`, and the Hecke polynomial `O.heckePolyOnForms` at the number
`O.liftHeckeRoot w` for a split place `w` off the level. Let `ε` split `I_n = I_N ⊕ I_l` with
`2 #r + 2 #N + 3 < #n`. Let `C`, from vectors of weight `κ` to vectors of weight `O.columnCount`, be
conjugate-linear and equivariant (`conjWeylRep`) for the real points of the second block. Let `x` be
supported at the chosen places. Let the level `K` fix the datum `Ψ` modulo the ideal `𝔪`, and after
conjugation by `x` fix the matrices `Y i`, each with independent columns. The places of `𝔪` lie in
`O.places` and the rows `e'` in the block `I_N`. Let `f h` be the inner product of `Ξ` with the
point form at `(h₁, h) x`. This form is supported on the class of `(h₁, h) x A` with value
`C (kernelVector O b 𝔪 Ψ κ g h)` there. Here `A = pointLift hY e'` is an integral point with columns
`Y` at the chosen places. The vector `kernelVector O b 𝔪 Ψ κ g h` lists the values at `(g, h)` of
the conjugate theta kernels of the pair `W, I_l` with datum `Ψ`, twisted by `b`, one for each basis
polynomial of weight `κ`. Then the class sum of `f` over `K` (the sum over the double cosets
weighted by `1 / #Aut`) is zero. 

### `DividedSplitting.algFormRep_conj_block_eq_self`

 Forms are fixed by the second block near the point of a divided lattice. A `DividedSplitting`
`V` is a splitting `V.ε` of `I_n = I_N ⊕ I_l` with the indices of `W` and those of a further index
type `ι` embedded in `N`; the embedding `z` is a parameter without conditions. A divided lattice `L`
is a lattice `γ 𝒪ⁿ`, with `γ = L.point` supported at the chosen places of `O`, that lies between
`ϖ 𝒪ⁿ` and `𝒪ⁿ` there, for the idele `ϖ = O.genIdele`. Every form `Ξ` in `O.FormV` on `U(I_n)` is
fixed by right translation (`algFormRep`) by `γ⁻¹ (1, k) γ`, with `(1, k) = U.block V.ε (1, k)`, if
the integral point `k` of the second block `I_l` is `1` modulo the square of the product of the
chosen places (`O.chosenModulusSq`). 

### `DividedSplitting.stdClassSum_inner_productForm_eq_zero`

 Slices of false lifts are orthogonal to theta kernels. Let `O` be a descent pair `(W, I_n)`, and
let `V` split `I_n = I_N ⊕ I_l` with the indices of `W` and those of a further index type `ι`
embedded in `N`. Let `L` be a divided lattice `γ 𝒪ⁿ`, with `γ = L.point` supported at the chosen
places. Let the archimedean parameter `l₀` on `W` correspond to that on `I_n` (`O.FitsParams`), and
let the residue characters `O.tamePart` be nontrivial at the twist places. Let the form `Ξ` on
`U(I_n)` be killed by the hyperplane sums at the chosen places, by the theta descent to `W` and by
the Hecke polynomial at the number `O.liftHeckeRoot w`, for a split place `w` off the level, and let
`2 #r + 2 #N + 3 < #n`. Let `ϖ` generate the square of the product of the chosen places. The product
form `V.productForm L (x, h) y η` is supported on the class of `(x, h) γ`, with value the Cartan
product of `y`, of weight `O.colsPlus`, and `η`, of weight `O.colsMinus`. Take for `η` the conjugate
of `kernelVector … g h`, the vector of the conjugate theta kernels at `(g, h)` of the pair `W, I_l`
with any datum `Ψ` modulo `ϖ`. Then the class sum over `h`, at the principal level `ϖ` of `U(I_l)`,
of the inner product of this form with `Ξ` is zero. 
