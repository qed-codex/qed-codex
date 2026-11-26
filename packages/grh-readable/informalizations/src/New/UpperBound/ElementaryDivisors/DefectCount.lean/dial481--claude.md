---
{
  "module": "src/New/UpperBound/ElementaryDivisors/DefectCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/DefectCount.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/DefectCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The dimension of the forms of bounded defect

Let `T` be a Frobenius cycle (`New.FrobeniusCycle`) over a field `K` of characteristic `p`, with
`P = T.P` and `q = T.q = P ^ N`. Exponents are indexed by `(b, s) ∈ Fin k × ZMod N`, and `s` is
called the letter. The defect of an exponent `β` at the letter `i` along the root `(a, a')` is the
linear form `∑ x, T.defectWeight i a a' x * β x`. Pieri's inequalities say that the defects along
the simple roots `(b, b + 1)` are at most `0`.

The forms whose translates by a Levi subgroup with two blocks have bounded defect along the root
between the blocks are counted by flags and lattice points. One substitutes `x ^ m` for the
variables, `m` a power of `q`, and multiplies by one monomial for each class of exponents modulo
`m`. Give the variable `(b, s)` the height `b` for even `s` and `-b` for odd `s`. Among the terms of
all translates of the resulting polynomial by the Levi subgroup, one of least height has defect at
most `0` along the other simple roots, and it occurs in the translate by a representative of a flag,
that is, of a coset of the lower Iwahori subgroup. A shift by an integral vector moves its exponent,
divided by `m`, into the cone of Pieri's inequalities. As `m` grows, the count of these exponents
becomes the volume of the cone cut by a slab, and the share of the cone in a slab is the inverse of
the number of all flags.

## Main definitions and results

* `New.FrobeniusCycle.defectCone`: the real vectors of bounded defect along the simple roots.
* `New.powerPacking`: a family of forms in the `m`-th powers of the variables, packed into one
  polynomial.
* `New.FrobeniusCycle.exists_finrank_defectConditions_le_volume`: the dimension of the forms of
  bounded defect is at most a number of flags times the volume of the part of a slab in which
  Pieri's inequalities hold.
* `New.FrobeniusCycle.index_mul_finrank_defectConditions_le`: in large degree, the parahoric index
  times the dimension of the forms of bounded defect is at most `1 + θ` times the number of
  exponents.

Notions from other files:
* `New.parahoric`: The parahoric subgroup of a labelling τ: matrices in GL_k(W), W local, whose
  (i,j) entry lies in the maximal ideal whenever τ(i) < τ(j).
* `New.FrobeniusCycle.defectConditions`: The forms F such that, for every g block diagonal with
  blocks of sizes a', k − a' and every β of defect above h along (a, a') at some letter, the
  coefficient of g·F at β lies in a given ideal I. In this file I = ⊥.
* `levi W (twoBlock k r)`: The block diagonal matrices with blocks r and k − r.
* `degreeSlab k D`: The real vectors β ≥ 0 whose degree ∑_b β(b,s) in each letter s lies in [D
  s − 1, D s].

## Notation

In the count, `m = q ^ j` is a power of `q`. As matrices act transposed, the lower Iwahori subgroup
is used.

## Relation to the literature

Volumes of interlacing regions, Frobenius amplification and counting by leading terms along flags
are known in the literature. Related work: Forrester–Zhang, Corank-1 projections and the randomised
Horn problem, 2021 (after Dixon, 1905; Anderson, 1991); Bombieri, Counting points on curves over
finite fields, Sém. Bourbaki 430, 1973; Okounkov, Brunn–Minkowski inequality for multiplicities,
1996.



## Forms of bounded defect: flags times the volume of a cone

The lower Iwahori subgroup is `parahoric W Fin.val`.


### `instance [Finite (IsLocalRing.ResidueField W)] (τ : Fin k → ℕ) : (parahoric (k`

 Over a local ring `W` with finite residue field, the parahoric subgroup of `GL_k(W)` of every
labelling `τ` has finite index. 

### `index_borel_le`

 Bound for the number of full flags over a finite field `K` with `q` elements: the index of the
subgroup of lower triangular matrices in `GL_k(K)` is at most `∏ (q ^ (l + 1) - 1) / (q - 1)` over
`l < k`. 

### `FrobeniusCycle.defectCone`

 The defect of a vector `β` indexed by `(b, s) ∈ Fin k × ZMod N`, at the letter `i` along the
root `(b, b')`, is the linear form with coefficients `T.defectWeight i b b'`, namely
`β v + ∑ s, ± P ^ ((s - i) mod N) * (β (b', s) - β (b, s)) / (q - 1)`, with the sign `+` at even
`s`, and `v = (b', i)` for even `i`, `v = (b, i)` for odd `i`. The set `T.defectCone a h` consists
of the real vectors `β` whose defect, at every letter, is at most `h` along the simple root
`(a, a + 1)` and at most `0` along the other simple roots `(b, b + 1)`. For `h = 0` these are
Pieri's inequalities, see `New.FrobeniusCycle.permStep_mem_defectCone_iff`. The condition `β ≥ 0` is
not part of this set; it comes with the slab. 

### `FrobeniusCycle.convex_defectCone_inter_degreeSlab`

 The vectors `β ≥ 0` with degree `∑ b, β (b, s)` in `[D s - 1, D s]` for each letter `s`, and
with defect at every letter at most `h` along `(a, a + 1)` and at most `0` along the other simple
roots `(b, b + 1)`, form a convex set. 

### `FrobeniusCycle.embedding_pow_q_pow`

 In characteristic `T.p`, the values of the embedding `T.embedding s` of each letter `s` are
fixed by raising to the power `q ^ j`, with `q = T.q = P ^ N`. 

### `FrobeniusCycle.polyAction_commute_expand`

 In characteristic `T.p`, the linear substitution `T.polyAction g` by which a matrix `g` acts on
polynomials over `K` commutes with the substitution `x ↦ x ^ m` of the variables, for every power
`m` of `q = T.q`. 

### `FrobeniusCycle.sum_eq_of_coeff_polyAction_monomial`

 Let `T` be a Frobenius cycle from the local ring `W` to the field `K`: ring maps `ι s : W → K`,
one for each letter `s ∈ ℤ/N`, with `ι (s + 1) ≡ ι s ^ P` modulo the prime `T.p`. A matrix
`g ∈ GL_k(W)` acts on polynomials in the variables `x (b, s)`, `b < k`, by the linear substitution
`T.polyAction g`, given in the letter `s` by `ι s g` for even `s` and by `ι s` of the inverse
transpose of `g` for odd `s`. This action keeps the degree in each letter: if `x ^ ε` occurs in the
translate by `g` of the monomial `x ^ γ`, then `ε` and `γ` have the same degree in the letter
`s`. 

 ### Powers 

### `residueExponent`

 An exponent in the class `u` modulo `m` whose degree in each letter `s` lies in
`[m k, m k + m]`: the number `m (k - ⌊(∑ b, u (b, s)) / m⌋)` is added to the entry of `u` at the
index `(a, s)`. 

### `residueExponent_mod`

 The exponent `New.residueExponent a u` lies in the class `u` modulo `m`. 

### `sum_residueExponent_mem_Icc`

 The exponent `residueExponent a u` has the entries `u (b, s) < m`, with `m (k - ⌊d / m⌋)` added
where `b = a`, for `d = ∑ b, u (b, s)`. Its degree in each letter `s` lies in `[m k, m k + m]`. 

### `powerPacking`

 Packing of a family `F` of forms of degree `n` in each letter, one for each class `u` of
exponents modulo `m`, into the polynomial `∑ u, F u (x ^ m) * x ^ γ u`, with
`γ u = New.residueExponent a u`. 

### `expand_polyOfCoeffs`

 Substituting `x ^ m` for the variables `x` in the form with coefficients `G` multiplies its
exponents by `m`. 

### `coeff_powerPacking`

 Let `F u` be forms of degree `n` in each letter `s ∈ ℤ/N`, one for each class `u` of exponents
modulo `m`. They are packed into `powerPacking a n m F = ∑ u, F u (x ^ m) * x ^ γ u`. Here
`γ u = residueExponent a u` is `u` with multiples of `m` added at the index `(a, s)` in each letter
`s`. The terms do not interfere: the coefficient of the packed polynomial at
`m • exponentOf β + γ u` is the coefficient of `F u` at `β`. 

### `FrobeniusCycle.polyAction_powerPacking`

 Let `T` be a Frobenius cycle from the local ring `W` to the field `K` of characteristic `T.p`:
ring maps `ι s : W → K`, one for each letter `s ∈ ℤ/N`, with `ι (s + 1) ≡ ι s ^ P` modulo the prime
`T.p`. Here `P = T.P` is a power of `T.p`, the residue field of `W` has `q = T.q = P ^ N` elements,
and the letters are alternately even and odd (`T.isEven`). A matrix `g ∈ GL_k(W)` acts on
polynomials in the variables `x (b, s)`, `b < k`, by the linear substitution `T.polyAction g`, given
in the letter `s` by `ι s g` for even `s` and by `ι s` of the inverse transpose of `g` for odd `s`.
Let `m` be a power of `q`. The forms `F u`, of degree `n` in each letter, are packed into
`powerPacking a n m F = ∑ u, F u (x ^ m) * x ^ γ u`, where `γ u = residueExponent a u` is the vector
`u` of residues modulo `m` with `m (k - ⌊(∑ b, u (b, s)) / m⌋)` added at each index `(a, s)`.
Translating by `g` replaces each monomial `x ^ γ u` by its translate and each `F u` by its
translate, which has the coefficients `T.letterRep n g *ᵥ F u`; here `T.letterRep n g` is the matrix
of the action on such forms. 

### `FrobeniusCycle.exists_eq_add_of_coeff_polyAction_powerPacking`

 Let `T` be a Frobenius cycle over a field `K` of characteristic `T.p`, and let `m` be a power of
the number `T.q` of elements of the residue field of `W`. The forms `F u`, of degree `n` in each
letter, are packed into `powerPacking a n m F = ∑ u, F u (x ^ m) * x ^ γ u`, where the exponent
`γ u` is the class `u` modulo `m` with multiples of `m` added at the index `a`. Each exponent `α` of
the translate of this polynomial by `g ∈ GL_k(W)` is `m δ + ε`, where `δ` is an exponent of the
translate `T.letterRep n g *ᵥ F u` of some `F u` and `ε` has degree in `[m k, m k + m]` in each
letter. 

### `FrobeniusCycle.sum_mem_Icc_of_coeff_polyAction_powerPacking`

 Let `T` be a Frobenius cycle over a field `K` of characteristic `T.p`, and let `m` be a power of
the number `T.q` of elements of the residue field of `W`. The forms `F u`, of degree `n` in each
letter, are packed into `powerPacking a n m F = ∑ u, F u (x ^ m) * x ^ γ u`, where the exponent
`γ u` is the class `u` modulo `m` with multiples of `m` added at the index `a`. Each exponent `α` of
the translate of this polynomial by `g ∈ GL_k(W)` has degree in `[m (n + k), m (n + k + 1)]` in each
letter `s`. 

### `FrobeniusCycle.weight_defectWeight_le_of_coeff_polyAction_powerPacking`

 Let `m` be a power of `q`, let `L = levi W (twoBlock k a')` be the group of block diagonal
matrices with blocks `a'` and `k - a'`, and let `g ∈ L`. Let the `F u` lie in
`T.defectConditions n a a' ⊥ h`, the space of forms of degree `n` in each letter whose translates by
`L` have coefficient in the ideal `⊥`, that is `0`, at every exponent of defect above `h` along
`(a, a')` at some letter. Then each exponent `α` of the translate by `g` of the packed polynomial
`∑ u, F u (x ^ m) * x ^ residueExponent a u` has defect at most `m (h + 2 (k + 1))` along `(a, a')`,
at every letter `i`. 

 ### Least height 

### `FrobeniusCycle.polyAction_X_sub_mem_gaussFiltration`

 Let the height of a variable be its row index at even letters and minus its row index at odd
letters. In characteristic `T.p`, a matrix `g` that is lower triangular modulo the maximal ideal
sends the variable `u` to a multiple of itself, by a diagonal entry of `T.letterMatrix u.2 g`, plus
a linear combination of variables of height at least `height u + 1`. The latter is stated as
membership in the Gauss filtration for the heights and the powers of the square root
`T.sqrtPrime = 0` of `T.p`. 

### `FrobeniusCycle.coeff_polyAction_of_mem_parahoric`

 Let the height of a variable be its row index at even letters and minus its row index at odd
letters, and let all terms of `f` have height at least that of `α`. In characteristic `T.p`, a
matrix `g` that is lower triangular modulo the maximal ideal multiplies the coefficient of `f` at
`α` by a product of diagonal entries, because it sends each monomial to a multiple of itself plus
monomials of greater height. 

### `FrobeniusCycle.exists_coeff_ne_zero_weight_defectWeight_nonpos`

 Let `L = levi W τ` be the group of matrices whose entry `(b, c)` vanishes for `τ b ≠ τ c`, and
let `R` represent the right cosets in `L` of its intersection with the lower Iwahori subgroup
`parahoric W Fin.val` of matrices that are lower triangular modulo the maximal ideal. Some translate
of a polynomial `f ≠ 0` by an element `x` of `R` has an exponent `α` of defect at most `0` along all
simple roots `(b, b + 1)` with `τ b = τ (b + 1)`, at all letters. 

 ### The shift 

### `FrobeniusCycle.defectWeight_dotProduct_permStep`

 The defect of a vector `β` indexed by `(b, s) ∈ Fin k × ZMod N`, at the letter `i` along the
root `(a, a')`, is the linear form with coefficients `T.defectWeight i a a'`, namely `β v + ∑ s, ± P
^ ((s - i) mod N) * (β (a', s) - β (a, s)) / (q - 1)`, with the sign `+` at even `s`, where
`v = T.rootVar a a' i` is `(a', i)` for even `i` and `(a, i)` for odd `i`. Let
`β = permStep T.isEven T.P 1 ν`, that is, `β (b, s) = ± (P * ν (b, s + 1) - ν (b, s))` with the same
signs. Then the defect of `β` is `β v - (ν (a, i) - ν (a', i))`. 

### `FrobeniusCycle.exists_mem_defectCone_sum_le`

 There is an integral vector `σ ≥ 0` of degree `∑ b, σ (b, s)` at most `P ^ (2 (a + 1)) - 1` in
each letter `s` that lies in `T.defectCone a (-1)`: its defect, at every letter, is at most `-1`
along `(a, a + 1)` and at most `0` along the other simple roots `(b, b + 1)`. 

### `FrobeniusCycle.smul_add_mem_defectCone_inter_degreeSlab`

 The slab `degreeSlab k D` is the set of vectors `β ≥ 0` with degree `∑ b, β (b, s)` in
`[D s - 1, D s]` for each letter `s`. Let `h ≥ 0`, and let `σ ≥ 0` lie in `T.defectCone a (-1)`.
Adding `h σ` to a vector `β` of `T.defectCone a h` in the slab of degrees in `[d - 1, d]` gives a
vector of `T.defectCone a 0` in the slab whose degrees are raised by those of `h σ`. 

 ### The count 

### `FrobeniusCycle.div_mem_defectCone_inter_degreeSlab`

 Let `T` be a Frobenius cycle from the local ring `W` to the field `K` of characteristic `T.p`:
ring maps `ι s : W → K`, one for each letter `s ∈ ℤ/N`, with `ι (s + 1) ≡ ι s ^ P` modulo the prime
`T.p`. Here `P = T.P` is a power of `T.p`, the residue field of `W` has `q = T.q = P ^ N` elements,
and the letters are alternately even and odd (`T.isEven`). A matrix `g ∈ GL_k(W)` acts on
polynomials in the variables `x (b, s)`, `b < k`, by the linear substitution `T.polyAction g`, given
in the letter `s` by `ι s g` for even `s` and by `ι s` of the inverse transpose of `g` for odd `s`.
The defect of a vector `β` indexed by `(b, s) ∈ Fin k × ZMod N`, at the letter `i` along the root
`(b, b')`, is the linear form with coefficients `T.defectWeight i b b'`, namely
`β v + ∑ s, ± P ^ ((s - i) mod N) * (β (b', s) - β (b, s)) / (q - 1)`, with the sign `+` at even
`s`, and `v = (b', i)` for even `i`, `v = (b, i)` for odd `i`. Let `m` be a power of `q`, let
`a' = a + 1` and `2 (k + 1) ≤ t`, let `L = levi W (twoBlock k a')` be the group of block diagonal
matrices with blocks `a'` and `k - a'`, and let `g ∈ L`. Let the `F u` lie in the space of forms of
degree `n` in each letter whose translates by `L` have coefficient in the ideal `⊥`, that is `0`, at
every exponent of defect above `3 t` along `(a, a')` at some letter. Pack them into
`powerPacking a n m F = ∑ u, F u (x ^ m) * x ^ γ u`, where `γ u = residueExponent a u` is the vector
`u` of residues modulo `m` with `m (k - ⌊(∑ b, u (b, s)) / m⌋)` added at each index `(a, s)`. If an
exponent `α` of the translate of this polynomial by `g` has defect at most `0` along the simple
roots `(b, b + 1)` inside the blocks, then `α / m` has degree in `[n + k, n + k + 1]` in each letter
and lies in `T.defectCone a (4 t)`: its defect is at most `4 t` along `(a, a')` and at most `0`
along the other simple roots. 

### `FrobeniusCycle.finrank_defectConditions_mul_pow_le`

 Let `T` be a Frobenius cycle (`New.FrobeniusCycle`) from the local ring `W` to the field `K` of
characteristic `T.p`. It consists of ring maps `ι s : W → K`, one for each letter `s ∈ ℤ/N`, with
`ι (s + 1) ≡ ι s ^ P` modulo the prime `T.p`. Here `P = T.P` is a power of `T.p`, the residue field
of `W` has `q = T.q = P ^ N` elements, and the letters are alternately even and odd (`T.isEven`). A
matrix `g ∈ GL_k(W)` acts on polynomials in the variables `x (b, s)`, `b < k`, by the linear
substitution `T.polyAction g`. In the letter `s` it is given by `ι s g` for even `s` and by `ι s` of
the inverse transpose of `g` for odd `s`. Let `β` be a vector indexed by `(b, s) ∈ Fin k × ZMod N`.
Its defect at the letter `i` along the root `(b, b')` is the linear form with coefficients
`T.defectWeight i b b'`, namely `β v + ∑ s, ± P ^ ((s - i) mod N) * (β (b', s) - β (b, s)) / (q -
1)`. The sign is `+` at even `s`, and `v = (b', i)` for even `i`, `v = (b, i)` for odd `i`. Let `m`
be a power of `q`, let `a' = a + 1` and `t ≥ 2 (k + 1)`. Let `L = levi W (twoBlock k a')` be the
group of block diagonal matrices with blocks `a'` and `k - a'`. Let
`S = T.defectConditions n a a' ⊥ (3 t)` be the space of forms of degree `n` in each letter whose
translates by `L` have coefficient in the ideal `⊥`, that is `0`, at every exponent whose defect
along `(a, a')` is above `3 t` at some letter. Let `σ ≥ 0` be an integral vector of defect at most
`-1` along `(a, a')` and at most `0` along the other simple roots. Let `D s` be `n + k + 1` plus the
degree of `4 t σ` in the letter `s`. Then `m ^ (k N) * dim S` is at most a product of two factors.
The first is the index in `L` of its intersection with the lower Iwahori subgroup
`parahoric W Fin.val`: the matrices whose `(i, j)` entry lies in the maximal ideal when `i < j`. The
second is the number of points of `m⁻¹ ℤ ^ (k N)` in the cone `T.defectCone a 0` of Pieri's
inequalities, cut by the slab of vectors `β ≥ 0` with degrees in `[D s - 1, D s]`. This cone
consists of the vectors whose defect is at most `0` along all simple roots `(b, b + 1)` at all
letters. 

### `FrobeniusCycle.exists_finrank_defectConditions_le_volume`

 Let `T` be a Frobenius cycle from the local ring `W` to the field `K` of characteristic `T.p`:
ring maps `ι s : W → K`, one for each letter `s ∈ ℤ/N`, with `ι (s + 1) ≡ ι s ^ P` modulo the prime
`T.p`. Here `P = T.P` is a power of `T.p`, the residue field of `W` has `q = T.q = P ^ N` elements,
and the letters are alternately even and odd (`T.isEven`). A matrix `g ∈ GL_k(W)` acts on
polynomials in the variables `x (b, s)`, `b < k`, by the linear substitution `T.polyAction g`, given
in the letter `s` by `ι s g` for even `s` and by `ι s` of the inverse transpose of `g` for odd `s`.
The defect of a vector `β` indexed by `(b, s) ∈ Fin k × ZMod N`, at the letter `i` along the root
`(b, b')`, is the linear form with coefficients `T.defectWeight i b b'`, namely
`β v + ∑ s, ± P ^ ((s - i) mod N) * (β (b', s) - β (b, s)) / (q - 1)`, with the sign `+` at even
`s`, and `v = (b', i)` for even `i`, `v = (b, i)` for odd `i`. Let `a' = a + 1` and `t ≥ 2 (k + 1)`,
and let `L = levi W (twoBlock k a')` be the group of block diagonal matrices with blocks `a'` and
`k - a'`. Let `S = T.defectConditions n a a' ⊥ (3 t)` be the space of forms of degree `n` in each
letter whose translates by `L` have coefficient in the ideal `⊥`, that is `0`, at every exponent of
defect above `3 t` along `(a, a')` at some letter. There are degrees `D s` in
`[1, n + 4 t P ^ (2 a')]` such that `dim S` is at most the index in `L` of its intersection with the
lower Iwahori subgroup `parahoric W Fin.val` of matrices that are lower triangular modulo the
maximal ideal, times the volume of the cone `T.defectCone a 0` of Pieri's inequalities (defect at
most `0` along all simple roots `(b, b + 1)` at all letters) cut by the slab of vectors `β ≥ 0` with
degrees in `[D s - 1, D s]`. 

 ## The volume of a slab and the dimension of the forms of bounded defect 

### `volume_sum_mem_Icc_le`

 The slab of nonnegative vectors in `ℝ ^ (n + 1)` with sum in `[d - 1, d]`, where `d ≤ D`, has
volume at most `|Dⁿ / n!|`. 

### `volume_degreeSlab_le`

 If `D s ≤ B` for all `N` letters `s`, then the slab of nonnegative vectors with `k + 1` entries
in each letter and degree in `[D s - 1, D s]` has volume at most `|B ^ k / k !| ^ N`. 

### `pow_div_factorial_le_card_monomials`

 There are at least `n ^ k / k !` monomials of degree `n` in `k + 1` variables. 

### `FrobeniusCycle.index_mul_relIndex_le`

 Let `q = T.P ^ N` be the number of elements of the residue field of the local ring `W`; the
Frobenius cycle `T` enters only through this number. The index in `GL_k(W)` of the parahoric
subgroup with blocks `r` and `k - r`, times the number of flags of its Levi subgroup `L`, is at most
`∏ (q ^ (l + 1) - 1) / (q - 1)` over `l < k`. 

### `FrobeniusCycle.permStep_mem_defectCone_iff`

 The image of `ν` under `New.permStep` with trivial permutations, that is, the vector
`± (P ν (b, s + 1) - ν (b, s))` with the sign `+` at even letters, has defect at most `0` along all
simple roots if and only if `ν` lies in `New.pieriCone`, the cone of Pieri's inequalities in the
coordinates `ν`. The index `a'` does not matter, as the bound is `0` at every root. 

### `FrobeniusCycle.prod_mul_volume_defectCone_inter_degreeSlab`

 For a Frobenius cycle `T` with `q = T.P ^ N`, the cone `T.defectCone a 0` of Pieri's
inequalities fills the part `∏ (q - 1) / (q ^ (l + 1) - 1)`, over `l < k`, of the volume of every
slab of vectors `β ≥ 0` with degrees in `[D s - 1, D s]`. 

### `FrobeniusCycle.index_mul_finrank_defectConditions_le`

 Few forms have bounded defect. Let `T` be a Frobenius cycle from the local ring `W` to the field
`K` of characteristic `T.p`: ring maps `ι s : W → K`, one for each letter `s ∈ ℤ/N`, with
`ι (s + 1) ≡ ι s ^ P` modulo the prime `T.p`. Here `P = T.P` is a power of `T.p`, the residue field
of `W` has `q = T.q = P ^ N` elements, and the letters are alternately even and odd (`T.isEven`). A
matrix `g ∈ GL_k(W)` acts on polynomials in the variables `x (b, s)`, `b < k`, by the linear
substitution `T.polyAction g`, given in the letter `s` by `ι s g` for even `s` and by `ι s` of the
inverse transpose of `g` for odd `s`. The defect of a vector `β` indexed by
`(b, s) ∈ Fin k × ZMod N`, at the letter `i` along the root `(b, b')`, is the linear form with
coefficients `T.defectWeight i b b'`, namely
`β v + ∑ s, ± P ^ ((s - i) mod N) * (β (b', s) - β (b, s)) / (q - 1)`, with the sign `+` at even
`s`, and `v = (b', i)` for even `i`, `v = (b, i)` for odd `i`. Let `a' = a + 1` and `t ≥ 2 (k + 1)`,
and let `L = levi W (twoBlock k a')` be the group of block diagonal matrices with blocks `a'` and
`k - a'`. Let `S = T.defectConditions n a a' ⊥ (3 t)` be the space of forms of degree `n` in each
letter whose translates by `L` have coefficient in the ideal `⊥`, that is `0`, at every exponent of
defect above `3 t` along `(a, a')` at some letter. Let `θ ≤ 1`, and let `n > 0` satisfy
`8 N k t P ^ (2 a') ≤ θ n`. Then the index in `GL_k(W)` of the parahoric subgroup of these blocks
(upper right block in the maximal ideal) times `dim S` is at most `1 + θ` times the number of
`N`-tuples of monomials of degree `n` in `k` variables. 
