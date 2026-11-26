---
{
  "module": "src/Lib/Weil/Periods/ConstantTerm.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/ConstantTerm.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/ConstantTerm.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Constant terms of Weil functions along maps of positive degree

This file studies the theta kernel on `Hom(V, V')` for gradings `Y` of `V` and `Y'` of `V'`
(`New.Grading`), with strings of lengths `s` and `s'`. It computes how the Weil action moves
Heisenberg operators and zero terms. It defines the constant term `New.Grading.constTerm` of
`f ∈ 𝒮 (Hom (V, V'))` along the maps of positive degree. It proves the transformation laws of this
constant term and the Fourier expansion of `f 0` in constant terms. It defines the unfolded
function `New.Grading.unfoldStep` and, for `s' = s - 1`, proves its continuity and invariance
properties.

## Main definitions and results

* `New.Seesaw.pairWeil_homHeisenbergOp`: the Weil action of a pair `(g, g₀)` moves the Heisenberg
  operator of `w` to that of `g₀ w g⁻¹`, in rational coordinates.
* `New.Grading.constTerm`: the constant term of `f ∈ 𝒮 (Hom (V, V'))` along the maps of positive
  degree; `New.Grading.constTerm_eq_theta_zeroTerm` and `New.Grading.exists_splitting_constTerm`
  write it as a theta value in a mixed model.
* `New.Grading.constTerm_mul_of_mem_ratBessel`, `New.Grading.constTerm_mul_of_mem_unipotent` (both
  cases together: `New.Grading.constTerm_mul`), `New.Grading.constTerm_congr_rat`,
  `New.Grading.constTerm_eq_homBicharacter_mul`: its transformation laws.
* `New.Grading.hasSum_constTerm_out`, `New.Grading.exists_tsum_enorm_constTerm_le` (both together:
  `New.Grading.hasSum_constTerm`): Fourier expansion of `f 0` in constant terms, with a bound.
* `New.Grading.unfoldStep`: the unfolded function `𝒲'`. The laws of the constant term and the
  following properties are proved for `s' = s - 1`. `New.Grading.continuous_unfoldStep`: it is
  continuous if `W` is equivariant. `New.Grading.unfoldStep_rat_mul`: it is left invariant under the
  rational points of the Bessel subgroup of `Y'`. `New.Grading.isEquivariant_unfoldStep`: if `W` is
  equivariant and `Y'.genericConst = Y.genericConst`, each `γ ↦ 𝒲'(γ h)` is again equivariant
  (`New.Grading.IsEquivariant`).

Notions from other files:
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with xᴴJx
  equal to diag(s) at the infinite places and 1 at the finite places.
* `New.𝒮`: The Banach space 𝒮(V) of integrable functions c on 𝔸^n with c(x) = ∫ c(y)β(y,x)e(x−y) dy,
  under the L¹ norm; β is the adelic bicharacter and e the vacuum function `New.vacuumFn`.
* `New.Grading.stringMap`, written `T`: the rational map `V → V'` that kills `X` and sends each
  string vector of `Y` to a multiple of the string vector of `Y'` with the same number (to `0` if
  there is none).
* `New.Grading.AgreesWithStringMap`: `w` agrees with `T` at the entries `(b, a)` where `a` has
  positive grade and `b` has grade below that of `a`.
* `New.Grading.ratBessel`: The rational points of U(V) that lie in the Bessel (Fourier–Jacobi)
  subgroup of the grading Y.

## Relation to the literature

See also `Lib.Weil.MixedModel.ZeroTerm`.



## The frame of Hom(V, V′) in rational coordinates

A space (`New.Space`) is a rational hermitian matrix with an adelic frame `x`. The space
`Hom(V, V')` (`New.Space.hom`) carries the frame built from the frames of `V` and `V'`.

* `New.Seesaw.x_inv_mulVec_matrixToVec`: the inverse frame of `Hom(V, V')`, applied to an adelic
  matrix `w` read as a vector, gives `New.Space.homAtPoint V V' w`, that is `x'⁻¹ w x`.


### `New.Seesaw.x_inv_mulVec_matrixToVec`

 The inverse frame of `Hom(V, V')` applied to an adelic matrix `w`, read as a vector, is
`New.Space.homAtPoint V V' w`, that is x'⁻¹wx. 


## Weil action on Heisenberg operators and the zero term

The basis of a hermitian space `U` carries integer weights `wt`. `D` is a splitting of `U`
(`New.Space.Splitting`: two dual isotropic frames `k`, `l` and a complement `V₀`) whose frame `k`
consists of the basis vectors of positive weight. `D.zeroTerm` is the zero term along `k`, the mean
over translations by the span of `k`.

`U.ratCoordMatrix g = x g x⁻¹` is `g` in rational coordinates, `x` the adelic frame of `U`.


### `ratCoordMatrix_onHom`

 In rational coordinates the element of the unitary group of Hom(U, V₀) given by a pair (g, g₀)
is the Kronecker product of g₀ and the transpose of g⁻¹. 

### `pairWeil_homHeisenbergOp`

 The Weil action normalises the Heisenberg operators: `ω(g, g₀) ϱ(w) = ϱ(g₀ w g⁻¹) ω(g, g₀)`,
with `g` and `g₀` in rational coordinates. 

### `det_eq_one_of_hasDegreeGe_one`

 If, in rational coordinates, `g - 1` raises the weights `wt` by at least one, then `g` has
determinant one. 

### `det_inclX`

 For a grading `Y` of `U`, the element `Y.inclX g` that is `g` on the summand indexed by `n₀`
and the identity on the strings has the determinant of `g`. 

### `kAdelic_mul_submatrix`

 Let the frame `k` of the splitting `D` be the basis vectors of positive weight. A matrix `B`
whose rows of non-positive weight vanish is a combination of this frame: in standard coordinates,
`x⁻¹ B` is `D.kAdelic = x⁻¹ k` times the rows of `B` of positive weight. 

### `kAdelic_mulVec`

 Let the frame `k` of `D` be the basis vectors of positive weight. A vector `y` supported in
positive weights is a combination of this frame: `x⁻¹ y` is `D.kAdelic` times the entries of `y` of
positive weight. 

### `actsOnFrame_submatrix_ratCoordMatrix`

 Let the frame `k` of `D` be the basis vectors of positive weight. If `g`, in rational
coordinates, maps their span to itself, then it acts on `k` by its block of positive weights. 

### `zeroTerm_omega_of_inclMatrix`

 Let `D` be a Witt splitting of `U` over `V₀` whose frame `k` is the basis vectors of positive
weight. Its zero term `D.zeroTerm : 𝒮(U) → 𝒮(V₀)` sends `f` to `y ↦` the mean of the theta function
of `f` at `ιy + kb` over `b` in `𝔸^p` modulo `E^p`. Let `C` agree with `g` (in rational coordinates)
in the columns of positive weight and with the identity at the entries `(i, l)` with
`wt i ≤ min 0 (wt l)`, and let `det C = u` with `u` of norm one; so `g` preserves the span of `k`
and has determinant `u` there. If `g` induces `g₀` on `V₀` modulo that span, then
`D.zeroTerm (ω(g) f) = υ(u)⁻¹ ω(g₀) (D.zeroTerm f)`, with `υ` the splitting character on `U(1)`. 


## Constant terms along maps of positive degree and the unfolded function

The graded spaces are `V = X ⊕ J_s`, `V' = X' ⊕ J_s'` (`New.Grading`). From the splitting of the
constant term on, `s' = s - 1`. An entry `(b, a)` of a map `V → V'` has degree `d b - gradeOf a`,
for weights `d` on `V'`; the transformation laws ask that the weights `d` be odd under
`Y'.stringReversal`, which sends each index to its dual index for the Gram matrix, of opposite
grade.


### `Space.mul_mem_ratMatrices`

 If `γ` and `δ` are rational points of U(V) and U(V′) and `w` is a rational map `V → V'`, then
`δ w γ`, in rational coordinates, is again a rational map. 

### `Space.ratParabolic`

 The rational points of the parabolic subgroup of U(V) of elements that, in rational
coordinates, do not lower the grading d of the basis. 

### `constTerm`

 The constant term of `f` at `w` along the maps of positive degree for the grades of `Y` and the
weights `d` on `V'`. It is the mean, over adelic vectors `v` modulo rational ones, of the value of
the Heisenberg translate of `f` by `w` at the map that keeps the entries of `v` of positive degree
and is zero elsewhere. 

### `constTermAtStringMap`

 The kernel of one unfolding step: the constant term at `T = Y.stringMap Y'`, for the weights
`Y'.gradeOf`, of the Weil translate of `f` by `(g, h)` twisted by the characters `α`. 

### `unfoldStep`

 The function `h ↦ ∫ W(r) * Y.constTermAtStringMap Y' α f r h dr` on U(V′)(𝔸) that one unfolding
step leaves; the integral is for `Y.besselMeasure`, the measure of the Bessel group of `Y` modulo
its rational points. 

### `instance : Countable (ratMatrices E ι' ι ⧸ Y.nonnegMaps d)`

 The classes of rational maps `V → V'` modulo maps of degree `≥ 0` are countable. 

### `gradedGram_apply_eq_zero`

 Row `i` of a graded Gram matrix vanishes outside the column of the dual index
`Y.stringReversal i`. 

### `hom_J_eq_zero_of_mapDegree_ne_neg`

 For weights `d` odd under the string reversal of `Y'`, the Gram matrix of `Hom (V, V')` pairs
only coordinates of opposite degrees. 

### `exists_splitting_k_eq_inclMatrix`

 For weights `d` odd under the string reversal of `Y'`, the space `Hom (V, V')` has a splitting
whose isotropic frame `D.k` consists of the coordinate vectors of positive degree. 

### `J_inv_mul_k_mul_eq_diagonal`

 Let the weights `d` be odd under the string reversal of `Y'`, and let the frame `k` of the
splitting `D` of `Hom (V, V')` consist of the coordinate vectors of positive degree. Then
`J⁻¹ k k† J` is the projection to the coordinates of negative degree. 

### `constTerm_eq_theta_zeroTerm`

 Let the frame `k` of the splitting `D` of `Hom (V, V')`, with complement `U`, consist of the
coordinate vectors `(b, a)` of positive degree `Y.mapDegree d`. The constant term of `f` at `w` is
the theta value on `U` of the zero term of `homHeisenbergOp w f`, the Heisenberg translate of `f` by
`w` on `Hom (V, V')`. Here the zero term takes the mean of the theta function along `k b`, for `b`
adelic modulo rational, and gives a function on `U`. 

### `exists_splitting_constTerm`

 Let the weights `d` on the basis of `V'` be odd under the string reversal of `Y'`. Then
`Hom (V, V')` has a splitting `D` with complement space `U` and isotropic frame indexed by the
coordinates `(b, a)` with `0 < Y.mapDegree d (b, a)`, such that: (a) `D.k` consists of the
coordinate vectors of those coordinates of positive degree; (b) `J⁻¹ k kᴴ J` is the diagonal
projection onto the coordinates of negative degree, where `J` is the Gram matrix of `Hom (V, V')`;
(c) for every `f` and adelic `w`, the constant term `Y.constTerm d f w` equals the theta value on
`U` of the zero term along `D` of the Heisenberg translate `homHeisenbergOp w f`. 

### `constTerm_congr_rat`

 For weights `d` odd under the string reversal of `Y'`, the constant term at a rational map
depends only on its class modulo maps of degree `≥ 0`. 

### `constTerm_out`

 For weights `d` odd under the string reversal of `Y'`, the constant term at the chosen
representative of the class of a rational map `w` is the constant term at `w`. 

### `agreesWithStringMap_congr_rat`

 If `d ≤ Y'.gradeOf ⊔ 0`, agreement with `T = Y.stringMap Y'` at the entries `(b, a)` with `a`
of positive grade and `b` of lower grade (`New.Grading.AgreesWithStringMap`) depends only on the
class modulo maps of degree `≥ 0` (`New.Grading.nonnegMaps`). 

### `constTerm_eq_homBicharacter_mul`

 For weights `d` odd under the string reversal of `Y'`: if `w - w'` has degree at least one,
the constant term at `w'` is `β(w, w')` times that at `w`, with `β` the Heisenberg bicharacter of
`Hom(V, V')` (`New.Space.homBicharacter`). 

 ### Fourier expansion 

### `exists_equiv_constTerm_eq_theta_slice`

 The degree of the entry `(b, a)` of a map is `d b` minus the grade of `a`. Let the weights `d`
be odd under the string reversal of `Y'`, which fixes `X'` and exchanges string vectors `i` and
`s − 2 − i`, and let the frame `k` of the splitting `D` of `Hom (V, V')`, with complement `U`,
consist of the coordinate vectors of positive degree. Then some bijection `e` from rational vectors
`a` indexed by the frame to rational maps modulo maps of degree `≥ 0` makes, for every `f` in 𝒮(Hom
(V, V')), the constant term `Y.constTerm d f` at a representative of `e a` equal the theta value on
`U` of the slice of `f` at `a`. 

### `hasSum_constTerm_out`

 For weights `d` odd under the string reversal of `Y'`, the value `f 0` is the sum of the
constant terms over the classes of rational maps modulo maps of degree `≥ 0`. 

### `exists_tsum_enorm_constTerm_le`

 For weights `d` odd under the string reversal of `Y'`, there is a constant `M` such that for
every `f` the norms of the constant terms, over the classes of rational maps modulo maps of degree
`≥ 0`, have sum at most `M * ‖f‖`. 

### `hasSum_constTerm`

 Let `d` be weights on the indices of `V'` that change sign under the string reversal of `Y'`.
Take rational matrices modulo `Y.nonnegMaps d`, the ones whose entry `(b, a)` vanishes whenever
`d b` is less than the grade of `a`. (a) The constant terms `Y.constTerm d f` along maps of positive
degree, taken at representatives of these classes, sum to `f 0`; (b) there is a constant `M` such
that for every `f` the sum of their norms is at most `M * ‖f‖`. This corollary joins
`hasSum_constTerm_out` and `exists_tsum_enorm_constTerm_le`. 

### `agreeingClasses`

 The set `𝒞` of classes whose chosen representative agrees with `T = Y.stringMap Y'`
(`New.Grading.AgreesWithStringMap`). For `d ≤ Y'.gradeOf ⊔ 0` any representative may be used
(`agreesWithStringMap_congr_rat`). 

### `tsum_constTerm_agreesWithStringMap`

 For weights `d ≤ Y'.gradeOf ⊔ 0` odd under the string reversal of `Y'`, take the classes of
rational maps modulo `Y.nonnegMaps d` (entry `(b, a)` zero when `d b < Y.gradeOf a`) that agree with
`T = Y.stringMap Y'`. The constant terms `Y.constTerm d f` at these classes add up to a Fourier
coefficient that does not depend on `d`: a mean over adelic maps `v : V' → V` modulo rational ones.
With `y` the map that keeps the entries `(a, b)` of `v` with `0 ⊔ Y'.gradeOf b < Y.gradeOf a`, the
function averaged is the value at `0` of the translate of `f` by the adjoint of `y`, divided by
`ψ (j tr (y T))`, where `ψ = stdAddChar E` and `j = WeilData.j`. 

### `constTerm_mul_of_zeroTerm_eq`

 Let the frame of the splitting `D` of `Hom (V, V')` consist of the coordinate vectors of
positive degree. If translation by `(γ, δ)` does not change the zero term at the origin, then in the
translate of `f` by `(γ g, δ h)` the constant term at `w` is that of the translate by `(g, h)` at
`δ⁻¹ w γ`, all written in rational coordinates. 

### `constTerm_mul_of_mem_ratBessel`

 Substitution law of the constant term for rational points. Let the weights `d` on `V'` be odd
under the string reversal of `Y'`, let `γ` be a rational point of the Bessel group of `Y` and `δ`
one of `V'.ratParabolic d`, that is, `δ` rational and, in rational coordinates, not lowering the
weights `d`. In the translate of `f` by `(γ g, δ h)` the constant term at `w` is that of the
translate by `(g, h)` at `δ⁻¹ w γ`, all written in rational coordinates. 

### `hasDegreeGe_ratCoordMatrix_onHom_sub_one`

 If `γ` is unipotent for the grading `Y` and `δ - 1` raises the weights `d` by at least one, then
the substitution `w ↦ δ w γ⁻¹` on `Hom (V, V')` is `1` plus a map that raises the degree by at least
one. 

### `constTerm_mul_of_mem_unipotent`

 Substitution law of the constant term for unipotent points. Let the weights `d` on `V'` be odd
under the string reversal of `Y'`, let `γ` be unipotent for the grading `Y`, and let `δ - 1` raise
the weights `d` by at least one. In the translate of `f` by `(γ g, δ h)` the constant term at `w`
is that of the translate by `(g, h)` at `δ⁻¹ w γ`, all written in rational coordinates. 

### `constTerm_mul`

 Substitution law of the constant term along weights `d` on `V'` that are odd under the string
reversal of `Y'`. Let `(γ, δ)` be of one of two kinds: rational (`γ` a rational point of the Bessel
group of `Y`, `δ` one of the parabolic subgroup of `d`) or unipotent (`γ` for the grading `Y`, `δ`
for the weights `d`). In the translate of `f` by `(γ g, δ h)` the constant term at `w` is that of
the translate by `(g, h)` at `δ⁻¹ w γ`, all written in rational coordinates. This corollary joins
`constTerm_mul_of_mem_ratBessel` and `constTerm_mul_of_mem_unipotent`. 

### `IsEquivariant.unipotent_mul_constTerm`

 Let `W` be equivariant, let `d` be weights odd under the string reversal of `Y'`, and let `u` be
an element of the Bessel group of `Y` that raises grades by at least `2` and is such that `w u - w`
has positive degree. Then `W (u r)` times the constant term `Y.constTerm d` at `w` of the twisted
Weil translate of `f` by `(u r, h)` equals `β(T u, T) / β(w u, w)` times `W r` times the same
constant term for `(r, h)`. Here `T = Y.stringMap Y'` and `β = V.homBicharacter V'`. 

 ### The unfolded function 

### `constTermAtStringMap_rat_mul`

 For `s' = s - 1` the constant term at the string map `T`, for the weights `Y'.gradeOf`, is left
invariant under the rational points of both Bessel subgroups. 

### `continuous_unfoldStep`

 Let `Y` grade `V` with a string of length `s`, and let `Y'` grade `V'` with a string of length
`s - 1`. Suppose `W` on the Bessel group of `Y` is equivariant: it is continuous, left invariant
under rational points, and transforms by the generic character `Y.unipotentChar` under elements
raising grades by at least `2`. Then `Y.unfoldStep Y' α f W` is continuous; this is the function
`h ↦ ∫ W r * Y.constTermAtStringMap Y' α f r h dr` on the unitary group of `V'`, integrated over the
Bessel group of `Y` modulo its rational points. 

### `unfoldStep_rat_mul`

 One unfolding step leaves the function `Y.unfoldStep Y' α f W` on U(V′)(𝔸), which is
`h ↦ ∫ W(r) * Y.constTermAtStringMap Y' α f r h dr` over the Bessel group of `Y` modulo its rational
points. This function is left invariant under the rational points of the Bessel group of `Y'`. 

### `isEquivariant_unfoldStep`

 Let `Y` grade `V` with a string of length `s`, and let `Y'` grade `V'` with a string of length
`s - 1`. Suppose `W` on the Bessel group of `Y` is equivariant, meaning continuous, left invariant
under rational points, and transforming by the generic character under elements raising grades by at
least `2`. Suppose also that the constants `Y'.genericConst` and `Y.genericConst` defining the
generic characters of the two gradings are equal. Then for each `h` in the unitary group of `V'`,
the function `γ ↦ Y.unfoldStep Y' α f W (γ * h)` on the Bessel group of `Y'` is equivariant for
`Y'`, where `Y.unfoldStep Y' α f W` is `h ↦ ∫ W r * Y.constTermAtStringMap Y' α f r h dr` over the
Bessel group of `Y` modulo its rational points. 
