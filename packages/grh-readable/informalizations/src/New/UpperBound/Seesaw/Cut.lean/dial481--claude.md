---
{
  "module": "src/New/UpperBound/Seesaw/Cut.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/Cut.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/Cut.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The outer variables: finitely many classes, with weights

Let `G_j = Gf D.E (D.Y j)` be the finite adelic unitary group of the hermitian space `Y_j` over the
CM field `D.E`. For each `j ≤ 2ϱ + 1` and each tame character `ϑ` we choose a finite set `Ω_j` of
classes of `G_j` modulo the level `levelY ϑ j`, with multiplicities that divide a power of
`q = ϑ.normQ`. The file defines the weighted sum of a function over `Ω_0 × ⋯ × Ω_{k-1}` and proves
that it is invariant under the levels `D.levelX j` and has coefficients integral away from `q`.

Notions from other files:
* A tame character `ϑ` is an automorphic character of `U(1)` of weight `0` with a finite set `ϑ.Q`
  of places as modulus, and `ϑ.normQ` is the product of the norms of these places.
* The chosen places are the prime divisors of `D.piM`; they lie above the primes `p₀` and `p₁` of
  the data `D`.
* `stdLevel D.E (D.Y j)` is the stabiliser in `G_j` of the standard lattice, and `levelY ϑ j` its
  subgroup of elements that reduce to `1` at the chosen places and at the places of `ϑ.Q`.
* `localLevel n S` is the group of points that are integral at every place in `S`.

## Relation to the literature

See `New.UpperBound.Seesaw.SeesawIdentity` for related work.


### `lt_m_of_le`

 Since the number `D.m` of lifts equals `2 ϱ + 2`, an index `j ≤ 2 ϱ + 1` satisfies `j < D.m`. 

 ### The cuts 

### `exists_conj_pow_mem_stdLevel`

 Let `x` be a finite adelic point of the unitary group of the space `Y_j` whose component
`x.atPlace w` is in `localIntGL = GL(O_w)` at every place `w` outside `ϑ.Q` and its conjugate. Then
there is an `n` such that, for all `u` in `levelY ϑ j`, the `q ^ n`-th power of `x u x⁻¹` lies in
the stabiliser `stdLevel` of the standard lattice. 

### `IsStageCut`

 A cut for the `j`-th outer variable: a finite set `T` of classes of `G_j = Gf D.E (D.Y j)`
modulo the level `levelY ϑ j`, used to write integrals over `R_j \ G_j` as finite sums. Here `R_j`
is the finite Bessel subgroup `(D.gradingY j hj).besselFin`. The multiplicity of a class is the
number of translates of `T` under `R_j / (R_j ∩ stdLevel)` that contain it, `stdLevel` the lattice
stabiliser. 

### `IsStageCut.mem_iff_smul_mem`

 The group `R_j ∩ stdLevel` permutes `T`. 

### `IsStageCut.integral`

 The points over `T` are integral at the places that do not divide `ϑ.normQ`. 

### `IsStageCut.multiplicity_dvd_pow`

 On `T` the multiplicity divides a power of `ϑ.normQ`. 

### `IsStageCut.ne_zero_of_hasBoundedOrbit`

 The multiplicity is nonzero at the points whose `R_j`-orbit meets the lattice bounds. 

### `exists_isStageCut`

 For every `j ≤ 2 D.ϱ + 1` there is a finite set `T` of classes of `Gf D.E (D.Y j)` modulo
`levelY ϑ j` with `IsStageCut ϑ j hj T`. Let `R_j` be the finite Bessel subgroup
`(D.gradingY j hj).besselFin`, and let `stdLevel` be the lattice stabiliser. The multiplicity of a
class is the number of translates of `T` under `R_j / (R_j ∩ stdLevel)` that contain it. Being a cut
means four things. First, `T` is stable under `R_j ∩ stdLevel`. Second, its points are integral at
the places prime to `q = ϑ.normQ`. Third, on `T` the multiplicity divides a power of `q`. Fourth,
the multiplicity is nonzero at each `x` such that some point of the orbit `R_j x` has a graded
lattice satisfying `HasLatticeBounds` for `twistIdele ϑ`, a generator of the ideal `ϑ.Q`
(`HasBoundedOrbit`). 

### `cutPoints`

 The classes `Ω_j` modulo `levelY ϑ j` over which the `j`-th outer variable is summed: the
classes of the elements of `D.chosenLevel` (integral points that reduce to `1` at the chosen places)
for `j = 0`, and a chosen cut (`IsStageCut`) for `j > 0`. 

### `isStageCut_cutPoints`

 For `k + 1 ≤ 2 ϱ + 1` the set `cutPoints ϑ (k + 1)` is a cut (`IsStageCut`). 

### `cutMultiplicity`

 The multiplicity of a class modulo `levelY ϑ j`: it is `1` for `j = 0`, and for `j > 0` the
number of translates of `cutPoints ϑ j` under `R_j / (R_j ∩ stdLevel)` that contain the class, with
`R_j` the finite Bessel subgroup and `stdLevel` the lattice stabiliser. 

### `mk_mem_cutPoints_zero`

 The set `cutPoints ϑ 0` consists of the classes modulo `levelY ϑ 0` of the elements of
`D.chosenLevel`, the integral points that reduce to `1` at every prime divisor of `D.piM`: the class
of a finite adelic point `x` of the unitary group of `Y_0` lies in it if and only if
`x ∈ D.chosenLevel`. 

### `mem_localLevel_of_mem_cutPoints`

 A point whose class lies in `cutPoints ϑ j` is integral at every place that does not divide
`ϑ.normQ`. 

### `exists_cutMultiplicity_dvd`

 If the class of a point `x` lies in `cutPoints ϑ j`, then its multiplicity
`cutMultiplicity ϑ j hj x` divides some power `ϑ.normQ ^ n` of `ϑ.normQ`. 

### `inclXFin_gradingY_mem_besselFin`

 The image in `U(Y_j)` of a finite point of `U(X_j)` lies in the finite Bessel subgroup. 

### `smul_mem_cutPoints_iff`

 Let `X_j` be the space that `D.gradingY j` embeds in the hermitian space `Y_j`, and let
`cutPoints ϑ j` be the finite set of classes of the finite adelic unitary group of `Y_j` modulo
`levelY ϑ j` over which the `j`-th variable is summed. If `b` lies in the level `D.levelX j` of
`U(X_j)`, then a class `c` lies in `cutPoints ϑ j` if and only if its translate by the image of `b`
in `U(Y_j)` does. 

### `cutMultiplicity_smul`

 For a finite point `b` of `U(X_j)` and a class `c` modulo `levelY ϑ j`, moving `c` by the image
`(D.gradingY j hj).inclXFin b` of `b` in `U(Y_j)` does not change `cutMultiplicity ϑ j hj c`. 

### `card_le_residueMatrixCount`

 Suppose that the modulus `ϑ.Q` of `ϑ` is empty (`hQ`) and that `k < D.m`. Let `T` be a finite
set of classes of `Gf D.E (D.Y k)` modulo `levelY ϑ k`, and suppose (`hT`) that every point over `T`
lies in `localLevel` at the places not dividing `ϑ.normQ = 1`. Then `T` has at most
`D.residueMatrixCount = M ^ (f n²)` elements, where `M = D.M = p₀ p₁` (the primes of `D`), `f = D.f`
is the number of infinite places of `E`, and `n = D.n D.m`. 

 ### Sums over the cuts 

### `cutSumAt`

 The sum of `S` over the tuples obtained from `c` by letting the `j`-th coordinate run over
`cutPoints ϑ j`, each term divided by the multiplicity of that coordinate. 

### `cutSum`

 The sum of `S` over `Ω_0 × ⋯ × Ω_{k-1}`, `Ω_j = cutPoints ϑ j`, each term divided by the
multiplicities of its coordinates; the coordinates from `k` on are the class of `1`. 

### `map_cutSum`

 A ℂ-linear map `L : M → M'` commutes with `cutSum ϑ k`: the sum of `S` over `Ω_0 × ⋯ × Ω_{k-1}`,
`Ω_i = cutPoints ϑ i`, with each term divided by the multiplicities of its coordinates. 

### `cutSumAt_smul`

 Let `S` be a function on tuples of classes modulo the levels `levelY ϑ i` with values in a
complex vector space `M`, and `h` a tuple of group elements whose `k`-th entry is the image of an
element `b` of the level `D.levelX k` of `U(X_k)`. Then `h k` drops out of `cutSumAt ϑ k`, the sum
over the `k`-th coordinate in `cutPoints ϑ k` weighted by the inverses of the multiplicities: this
sum of `S` translated by `h` at `c` is the same sum of `S` at the translate of `c` by `h` with
`k`-th entry replaced by `1`. 

### `cutSum_comp_smul`

 Let `S` be a function on tuples of classes modulo the levels `levelY ϑ i` with values in a
complex vector space `M`. The sum `cutSum` of `S` over `Ω_0 × ⋯ × Ω_{k-1}`, `Ω_i = cutPoints ϑ i`,
weighted by the inverses of the multiplicities of the coordinates, is invariant under translation
of `S` by a tuple `h` of group elements such that `h i` is the image of an element of the level
`D.levelX i` of `U(X_i)` for `i < k` and `h i = 1` for `i ≥ k`. 

### `isAdmissibleCombination_cutSumAt`

 Let `k ≤ 2 ϱ + 1`, let `S` be a function from tuples of classes modulo the levels `levelY ϑ i`
to a complex vector space `M`, and let `y` be a tuple of points integral at the places that do not
divide `q = ϑ.normQ`. Let `cutSumAt` be the sum of `S` over the tuples got from `y` by letting the
`k`-th coordinate run over the finite set `cutPoints ϑ k`, each term divided by the multiplicity of
that coordinate. It is an admissible combination of the values of `S` at all such tuples `y'`: a
finite linear combination with coefficients integral away from `q` (denominator `1`) that, if the
modulus `ϑ.Q` is empty, have absolute sum at most `D.residueMatrixCount` under every automorphism of
`ℂ`. 

### `isAdmissibleCombination_cutSum`

 Let `k ≤ 2 ϱ + 2` and let `S` be a function from tuples of classes modulo the levels
`levelY ϑ i` to a complex vector space `M`. Let `cutSum` be the sum of `S` over `Ω_0 × ⋯ × Ω_{k-1}`,
`Ω_i = cutPoints ϑ i`, each term divided by the multiplicities of its coordinates, the other
coordinates being the class of `1`. It is an admissible combination of the values of `S` at all
tuples of points integral at the places that do not divide `q = ϑ.normQ`: a finite linear
combination with coefficients integral away from `q` (denominator `1`) that, if the modulus `ϑ.Q` is
empty, have absolute sum at most `D.residueMatrixCount ^ k` under every automorphism of `ℂ`. 
