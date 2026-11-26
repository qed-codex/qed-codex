---
{
  "module": "src/Lib/Weil/Periods/BesselIntegral.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/BesselIntegral.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/BesselIntegral.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Integrals over the Bessel subgroup and the orbits surviving unipotent twists

A hermitian space `V` is graded by `Y`, which presents it as `X` plus a string of `s` vectors, and
`B` is its Bessel (Fourier–Jacobi) subgroup. For a second space `V'` graded by `Y'` with a string of
length `s - 1`, the file determines which terms of a Fourier expansion over rational maps
`w : V → V'` survive the unipotent twists. Each such `w` can be moved to a map of type
`New.Grading.AgreesWithStringMap`, and if that map also survives with degrees `Y'.gradeOf`, then
that map minus `Y.stringMap Y'` has degree `≥ 0`.

## Main definitions and results

* `New.Grading.isCocompact_ratBessel`: the adelic group `B` is compact modulo its rational points.
* `New.Grading.besselMeasure`: the measure that integrates over `B` modulo its rational points.
* `New.Grading.integral_besselMeasure_eq_of_mean`: such an integral is a fixed multiple of an
  integral over `U(X)` modulo its rational points, after averaging over the row of the unipotent
  part.
* `New.Grading.Survives`: no unipotent twist kills the term at `w`.
* `New.Grading.exists_agreesWithStringMap`: a rational `w` that is not killed can be moved by a
  rational unitary element of `V'` to a map of type `New.Grading.AgreesWithStringMap`;
  `New.Grading.agreesWithStringMap_mul_iff`: that element is unique up to `Y'.besselGroup`.
* `New.Grading.hasDegreeGe_of_survives`: a map of type `New.Grading.AgreesWithStringMap` is killed
  unless `w - Y.stringMap Y'` has degree `≥ 0`.

Notions from other files:
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with xᴴJx
  equal to the diagonal matrix of its signs at the infinite places and 1 at the finite places.
* `New.eichlerMap`: `eichlerMap J x u ς` is v ↦ v + h(u, v)x − h(x, v)(u + ςx), h the form of J.
* `New.Space.homBicharacter`: the phase `ψ ((j / 2) tr (y† x))` of two adelic maps `x`, `y`.

## Relation to the literature

Known; see `Lib.Weil.Periods.Unfolding` and `Lib.Adelic.Reduction.FiniteVolume` for sources.



## The Bessel subgroup, Eichler maps and integrals over [B]

`Y : New.Grading V N X s` presents the hermitian space `V` as `X` plus a string of `s` vectors, with
Gram matrix `gradedGram` built from a nonzero scalar `N : E`, graded by `New.Grading.gradeOf` (0 on
`X`, `s - 1 - 2 i` on the string). `New.Grading.unipotent` is the unipotent group that raises
grades, `New.Grading.inclX` embeds `U(X)`, and `New.Grading.besselGroup` is the Bessel
(Fourier–Jacobi) subgroup `B` that contains both. `Y.genericConst` is a nonzero scalar of `E`
carried by `Y`; with `c` for this scalar, the factors of `Y.shift` are `c`, `-N c` and `-N c²`.

`G E ε` is the adelic group containing the isometries of `V`; `U(X)` is `G E (1 : X → ℤˣ)`, the
group of the definite space `stdSpace E X`. `New.Space.ratCoordMatrix` is the matrix `x g x⁻¹` of
`g` in rational coordinates.

`Subgroup.quotMeasure` is the measure that integrates invariant functions over the quotient by a
subgroup (Haar measure times a cutoff). `New.IsContPeriodic` says that a function is continuous and
periodic under a subgroup of translations, and `New.quotMean` is its mean over the quotient.


### `exists_matrix_eq_ite_of_sub_one_lowers`

 A matrix over `E` can be defined by downward recursion on a level `w : ι → ℤ`. Let `n - 1`
strictly lower the level (its entry `(i, l)` vanishes unless `w i < w l`), and let `q : 𝔸 E → E`
be any map. Then some `Z` is the identity on and below the diagonal blocks of `w`, and each entry
of `Z` above them is `q` of the same entry of `(n - 1) * Z`. 

### `exists_unitriangular_mul_map_mem_matrix`

 A rational unitriangular matrix moves `n` to bounded entries. Let `q a` be a rational shift of
each adele `a` into `A` (`toAdele (q a) + a ∈ A`), and let `n - 1` strictly lower the level `w`.
Then some rational `r`, unitriangular for `w`, makes every entry of `n * r` equal to `0`, `1` or an
element of `A`. 

### `isCocompact_ratBessel`

 The rational points are cocompact in the adelic Bessel subgroup B of Y: there is a compact C ⊆ B
such that every g ∈ B has a rational γ ∈ B with γg ∈ C. 

### `exists_ratCoordMatrix_eq_eichlerMap`

 Let `J` be the Gram matrix of `V` mapped to the adeles, and `h(v, w) = vᴴ J w` its form. Let
`x` be supported in grades above `max 0 k` (hypothesis `hx`) and `y` in grade `-k` (hypothesis
`hy`). Then the Eichler map of `x`, `y` and `h(y, y) / 2` is the matrix, in rational coordinates,
of an element of the unipotent group `Y.unipotent`. 

### `besselMeasure`

 The measure on the Bessel (Fourier–Jacobi) subgroup B of Y that computes integrals over the
quotient of B by its rational points: Haar measure times a chosen cutoff. 

### `isFiniteMeasure_besselMeasure`

 The measure `New.Grading.besselMeasure` is finite, since the rational points are cocompact in
`B`. 

### `isMulRightInvariant_haar_besselGroup`

 The left Haar measure of the adelic Bessel group `B` is right invariant, that is, `B` is
unimodular, since its rational points have finite covolume. 

### `besselRow`

 The row of `n` over which the integral over the Bessel group is averaged: at `(j, x)` it is
`Y.genericConst` times the entry of `n - 1`, in rational coordinates, in the row of the grade-1
index `v j` and the column of the basis vector `x` of `X`. 

### `besselRow_mul_of_mem_unipotent`

 On the unipotent group the row adds: the row of `n * m` is the row of `n` plus that of `m`.
The cross term `(n - 1) (m - 1)` raises grades by at least `2`, while the row has entries from
grade `0` to grade `1`. 

### `besselRow_eq_of_ratCoordMatrix_eq_eichlerMap`

 The Eichler map of `x`, the indicator of the grade-1 indices, and of `y`, which on each basis
vector `x'` of `X` is `Y.genericConst⁻¹` times the sum of the conjugates `b̄ (j, x')` and vanishes
on the string, has row `b`, whatever its last argument `ς`. 

### `exists_continuous_unipotent_besselRow_mul`

 Eichler maps translate the row. There is a continuous family `u b` of elements of the unipotent
group, indexed by the row vectors `b`, such that the row of `n * u b` is `b` plus the row of `n`
for every unipotent `n`; `u b` is the Eichler map of
`New.Grading.besselRow_eq_of_ratCoordMatrix_eq_eichlerMap`. 

### `isMulRightInvariant_haar_comap_Gamma`

 Haar measure on the preimage `S` of the rational points of `U(X)` under a homomorphism `pr`
from the Bessel group is right invariant, when `S` is closed and `pr` keeps rational points
rational: the rational points of the Bessel group then lie in `S` and are cocompact in it. 

### `integral_add_sub_quotMean_eq_zero`

 A continuous function `F` on the adelic vectors that is periodic under the rational vectors
differs from its mean by a function of integral `0` modulo the rational vectors, also after a
translation by any `c`. 

### `integral_besselMeasure_eq_of_mean`

 Integration over `B = Y.besselGroup` modulo its rational points reduces to `U(X)`. Let `v`
embed `q` into the basis indices of grade `1` (there is at most one, so `q` has at most one
element), and let `row n` be the adelic vector with entry `Y.genericConst` times `(n - 1) (v j, x)`
at `(j, x)`, for `n` in rational coordinates and `x` a basis vector of `X`. There is one constant
`κ` such that `∫ φ = κ * ∫ M` for all `φ`, `f`, `M` with
(a) `φ : B → ℂ` continuous and left invariant under the rational points `Y.ratBessel` of `B`;
(b) `φ (n * a) = f a (row n)` for `n` unipotent and `a` in `U(X)`;
(c) each `f a` continuous and periodic under the rational vectors, with mean `M a` over the
adelic vectors modulo the rational ones;
(d) `M` continuous and left invariant under the rational points of `U(X)`. 


## Rational maps surviving unipotent twists

`New.Grading.gradeOf` is the weight of a basis vector and `New.Grading.stringReversal` the dual
index. `New.HasDegreeGe w' w d x` says that `x` raises weights by at least `d`.
`New.Space.formAdjoint` is the adjoint `†`. `New.Grading.stringMap` is the standard map `T` of
degree `-1`. `New.Grading.AgreesWithStringMap` is agreement with `T` in negative degree on the
vectors of positive weight.


### `Survives`

 The term at the rational map `w` survives the unipotent twists, for target weights `D`. Let `T`
be `Y.stringMap Y'`, and take any `u` in `Y.unipotent` such that `u - 1` has degree at least `2` and
`w (u - 1)` has degree at least `1` (weights `D` on the target), with `u` written in rational
coordinates. Then `New.Space.homBicharacter` takes the same value at `(T u, T)` and at
`(w u, w)`. 

### `formAdjoint_mul_self_mulVec_apply_eq_of_survives`

 Let `T` be `Y.stringMap Y'`, the rational map V → V' that kills `X` and the last string vector
and sends each other string vector to a multiple of the string vector of `V'` with the same number.
Suppose that `w` survives the unipotent twists for target weights `D` (`New.Grading.Survives`:
`homBicharacter` agrees at (T u, T) and (w u, w) for the relevant u in `Y.unipotent`). Then `T† T v`
and `w† w v` (with † the form adjoint) have the same coordinate `k`, provided that `v p = 0` unless
the weight of `p` is at least `1` and at least that of `k` plus `2` (`hv`); `(w v) p = 0` unless
`D p` is nonnegative and above the weight of `k` (`hwv`); and the entry of `w` in row `p` and the
column dual to `k` vanishes, or `v q = 0`, whenever `D p` plus the weight of `q` is at most `0`
(`hw_col`). 

### `exists_gradeOf_succ_isUnit_stringMap`

 Let `k` be an index of `Y'` whose weight is at least `0` if `k` is on the string and at least
`1` otherwise; as the weight off the string is `0`, `k` is on the string. Write `T` for
`Y.stringMap Y'`. There is an index `a` of `Y` with (a) weight one more than `k`; (b) `T k a` a
unit; (c) for every `w` of type `AgreesWithStringMap` and every row `m` that vanishes in weights
above that of `k`, the product of `m` with column `a` of `w` is `m k * T k a`. 

### `agreesWithStringMap_mul_iff`

 Let `w` be of type `New.Grading.AgreesWithStringMap` and let `γ` lie in `Y.besselGroup`. Then
`δ w γ` is again of type `AgreesWithStringMap` exactly when `δ` lies in `Y'.besselGroup`. Here `δ`
and `γ` are taken in rational coordinates. 

### `hasDegreeGe_of_survives`

 Let `T = Y.stringMap Y'` be the map that kills `X` and the last string vector of `V` and sends
each other string vector to a multiple of the same-numbered string vector of `V'`. Suppose `w`
agrees with `T` at every entry `(b, a)` where `a` has positive grade and `b` has grade below that
of `a`. Suppose also that `w` survives the unipotent twists with target weights `Y'.gradeOf`
(`New.Grading.Survives`): for every `u` in `Y.unipotent` with `u - 1` of degree at least `2` and
`w (u - 1)` of degree at least `1`, `New.Space.homBicharacter` takes the same value at `(T u, T)`
and at `(w u, w)`. Then `w - T` has degree at least `0`, i.e. its `(b, a)` entry vanishes whenever
the grade of `b` (`Y'.gradeOf`) is less than the grade of `a` (`Y.gradeOf`). 

### `hasLeftInv_submatrix_of_survives`

 Let the map `x` over `E` survive the unipotent twists (target weights `0`). Then `x` is
injective on the span of the basis vectors of positive weight: its restriction to them has a left
inverse. 

### `exists_agreesWithStringMap`

 Let `w` be a rational map `V → V'`, meaning an adelic matrix coming from a matrix over `E`, that
survives the unipotent twists with target weights `0` (`New.Grading.Survives`). That is, for every
`u` in `Y.unipotent` with `u - 1` of degree at least `2` and `w (u - 1)` of degree at least `1`,
`New.Space.homBicharacter` takes the same value at `(T u, T)` and at `(w u, w)`. Here
`T = Y.stringMap Y'` is the rational map that kills `X` and the last string vector of `V` and sends
each other string vector to a multiple of the same-numbered string vector of `V'`. Then some
rational unitary `δ` of `V'` makes `δ w` (in rational coordinates) agree with `T` at every entry
`(b, a)` where `a` has positive grade and `b` has grade below that of `a`
(`New.Grading.AgreesWithStringMap`). 
