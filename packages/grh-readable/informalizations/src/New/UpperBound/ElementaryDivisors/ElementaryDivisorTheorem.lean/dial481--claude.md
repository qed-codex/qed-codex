---
{
  "module": "src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Elementary divisors of the edge Hecke operator

The main result `New.FrobeniusCycle.elementary_divisors` bounds the mean exponent of the elementary
divisors of an edge Hecke operator `A`, outside a small proportion of them, under the size
conditions `New.FrobeniusCycle.IsLargeDegree`. Colengths in the sense of `New.ColengthDvd` take
the place of lengths, because the ring of coefficients need not be discrete;
`New.FrobeniusCycle.elementary_divisors_length` is the statement in lengths.

Let `w ^ 2 = p`, let `N` be the number of letters of the Frobenius cycle `T` and
`c₀ = T.multinomialExponent k`. Write `M` for the integral functions on lattices, `M_all` for the
functions on edges that depend only on the origin (`New.FrobeniusCycle.originFunctions`) and
`M_edge` for all functions on edges. The operator `A` acts on `M°`, the functions whose value at `L`
is dual to the integral forms on the dual lattice `L*`. Let `𝒩 ⊆ M°` consist of the functions whose
value at `L` is dual to the forms in the halfway lattices of all edges from `L*`. The map
`Add : M_edge → 𝒩` (`New.pairingMap`) adds the values at the edges into `L`. It is written in
coordinates dual to these forms, with one basis for all lattices `L` at once. Then, on vectors
multiplied by the pairing `b`, `A` is the composite `M ⊆ M_all ⊆ M_edge → 𝒩 ⊆ M°`
(`New.FrobeniusCycle.IsEdgePairing.edgeHeckeOperator_regroup`), and the image of `Add` contains
`p ^ (N c₀) 𝒩` (`New.FrobeniusCycle.IsEdgePairing.pairingMap_mul_nearInverse_one`). At each edge
there are conditions modulo `w ^ c`, with the precision `c = T.congruencePrecision k`
(`New.FrobeniusCycle.exists_isEdgeCondition`).

1. The functions that satisfy the conditions have nearly the full image: `Add` has a near inverse
   `Inv` (`New.nearInverse`, `New.FrobeniusCycle.IsEdgeCondition.pow_dvd_mul_sub_smul_one`) whose
   values satisfy them.
2. The conditions hold on `M_all` and leave room for few further generators. By Nakayama's lemma the
   span of `Add M_all` and these generators contains `p ^ (2 N c₀) 𝒩`
   (`New.exists_finset_card_le_smul_top_le_sup_span`).
3. Both ends have small colength (`New.FrobeniusCycle.IsLargeDegree.exists_basis_det_dvd`, used
   twice), and the colengths add along the chain (`New.colengthDvd_mul_mul_of_smul_top_le`).

The three steps are put together in
`New.FrobeniusCycle.exists_colengthDvd_range_pairingMap_mul_edgeRestriction`.

Notions from other files:
* `New.FrobeniusCycle N W O`: a prime `p` with a square root `w` in `O`, a power `P` of `p` such
  that the residue field of `W` has `q = P ^ N` elements, and `N` maps `W → O` (the letters), each
  the `P`-th power of the one before modulo `p`.
* `New.FrobeniusCycle.allEdgesForms`: the forms that lie in the halfway lattices of all edges from a
  lattice; `New.FrobeniusCycle.IsEdgePairing`: the pairing of an edge with its dual.
* `New.FrobeniusCycle.divisorConstant`: the bound `c_div` for the mean depth of the forms that are
  deep for all edges.


 ### Linear algebra of a near inverse 

### `exists_elementary_divisors_mod_summand`

 Let `O` be a valuation domain, let the matrix `Q` have the left inverse `R`, so that its image
is a direct summand of `O ^ K`, and let `A` be a matrix of the same shape as `Q`. There are an
invertible matrix `U` and scalars `t j` such that the images of `Q` and `A` span the same module as
the image of `Q` and the vectors `t j • U.col j`, and `R` kills the columns of `U` with
`t j ≠ 0`. 

### `valuedIn`

 The functions on `X × I` whose values `i ↦ φ (x, i)` lie in `C` for every `x`. 

### `card_add_card_le_mul_finrank`

 Let `Q` have the left inverse `R`, and let `R` kill the columns `j ∈ J` of an invertible matrix
`U`. If the columns of `Q` and these columns of `U` have all their values in `S` modulo the maximal
ideal, then `#E + #J ≤ #X * dim S`, because they are independent modulo the maximal ideal. 

### `smul_top_le_of_le_sup_smul_top`

 If `u` is a multiple of `a * w` with `w` in the maximal ideal and `a • O ^ E` lies in
`G + u • O ^ E`, then `a • O ^ E` lies in `G`, by Nakayama's lemma. 

### `exists_finset_card_le_smul_top_le_sup_span`

 Let `O` be a valuation domain. Let the matrix `Q` have the left inverse `R`, so that its columns
are a basis of a direct summand of `O ^ (X × I)`, and let `B` be a near inverse of `A`: `A * B ≡ a`
modulo `u`, where `u` is a multiple of `a` times a non-unit `w`. Let every vector `φ` in the images
of `Q` and `B` have all its values `φ (x, ·)` in `C`, and let `h` reduce into `S` modulo the maximal
ideal whenever `u • h ∈ C`. Then `a • O ^ E` lies in the span of the image of `A * Q` and of at most
`#X * dim S - #E` further vectors. 

### `colengthDvd_mul_mul_of_smul_top_le`

 The colengths add along a product. If `a • O ^ E` lies in the span of the image of `A` and of a
finite set `s`, then the colength of the image of `d' * A * d` plus `z • O ^ E` in `O ^ E` divides
`det d' * a ^ #E * det d * z ^ #s`. 

 ### Coordinates for edges 

### `regroup`

 A vector indexed by `(H × X) × L`, read as a function `X → I → O` through `I ≃ L × H`. 

### `edgewise`

 The map on functions of edges with values in `O ^ H ⊗ O ^ L` that acts on the value at the edge
`e` by `u e ⊗ A`. 

### `edgewise_mulVec`

 The value of `edgewise u A *ᵥ ψ` at `x = (h', e)` is `A` applied to the combination of the
values `ψ ((h, e), ·)` with the coefficients `u e h' h`. 

### `pairingMap`

 The map `Add` that sends a function on edges to its pairings with the columns of `Q'`, which
are functions on the dual edges. At the edge `e` the pairing is by `u e` on the factor `O ^ H` and
by `(h, h') ↦ h' ⬝ᵥ (b * h)` on the factor `O ^ L`. 

### `nearInverse`

 The map `Inv` in the direction opposite to `New.pairingMap`. It applies `R'ᵀ`, and then at the
edge `e` it applies `(u e)⁻¹` on the factor `O ^ H` and multiplication by `b'` followed by `Av` on
the factor `O ^ L`. 

### `pairingMap_mul_nearInverse_apply`

 Let `Ed` be the set of edges, so that a vector indexed by `(H × Ed) × L` is a function on edges
with values in `O ^ H ⊗ O ^ L`, and let `E` index the columns of `Q'` and the rows of `R'`. The
entry `(i, j)` of `Add * Inv`, for `Add = pairingMap u b Q'` and `Inv = nearInverse u Av b' R'`, is
a sum over `x ∈ H × Ed`: the vector `Av` of `b'` times the part at `x` of row `j` of `R'` is paired,
with the weights `b`, with the part at `x` of column `i` of `Q'`. 

### `EdgeCoordinates`

 The edges of a Hecke operator in coordinates. The situation in mind is this: `p` is a
uniformizer of `W`, and a group `Γ` acts freely, with finitely many orbits, on pairs of a
`W`-lattice of rank `k` and a free `O`-module with a basis indexed by `H`. The points of `X` are
representatives of the orbits, each with a basis of its lattice and of its module, and
`e = (x, b)` is the edge `b` into `x`. The origin of `e` is `δ` times the representative
`origin e` for one `δ ∈ Γ`. In the chosen bases
`δ⁻¹ = originBasisChange e * diag(p⁻¹, …, p⁻¹, 1, …, 1) * terminusBasisChange b`, with `r` entries
`p⁻¹`. Only coordinates are recorded: `p`, `Γ` and `δ` are no part of the structure. 

### `EdgeCoordinates.origin`

 The representative of the origin of an edge. 

### `EdgeCoordinates.originBasisChange`

 The matrix whose columns are a basis of the lattice of `origin e` adapted to `δ⁻¹ e`. 

### `EdgeCoordinates.terminusBasisChange`

 The change of basis at the terminus of an edge. 

### `EdgeCoordinates.transition`

 The matrix of `δ` from the module at `origin e` to the module at `x`. 

### `EdgeCoordinates.mk_terminusBasisChange_inv`

 The inverse of `terminusBasisChange b` represents the coset `b`. 

### `EdgeCoordinates.eq_of_origin_eq`

 An edge is determined by its origin and the coset of its transposed change of basis there;
  this is where the action of `Γ` has to be free. 

 ### The standing assumptions and the sizes that follow 

### `IsLargeDegree`

 The size conditions in the theorem on elementary divisors, for the rank `k`, the degree `n`,
the size `r` of the first block and the proportion `θ` of exceptional elementary divisors. 

### `IsLargeDegree.block_pos`

 The first block is not empty. 

### `IsLargeDegree.two_mul_block_le`

 The first block is at most half of the rank. 

### `IsLargeDegree.proportion_pos`

 The proportion `θ` is positive. 

### `IsLargeDegree.proportion_le_one`

 The proportion `θ` is at most `1`. 

### `IsLargeDegree.degree_pow_le`

 The residue field is large against the degree. 

### `IsLargeDegree.le_degree`

 The degree is large against `N k log q / θ` and `P ^ r`. 

### `card_isEven_add_self`

 Half of the letters are even. 

### `two_le_card_letters`

 The number of letters is positive and even, hence at least `2`. 

### `congruencePrecision`

 The precision `c = 5 N c₀`, with `c₀ = T.multinomialExponent k`, of the congruences modulo
`w ^ c` that are imposed on the value of a function at an edge. 

### `two_le_mul_multinomialExponent`

 For rank `k ≥ 2` one has `N c₀ ≥ 2`, where `N` is the number of letters and
`c₀ = T.multinomialExponent k = k ^ 2 * (frobExp * N)` with `P = p ^ frobExp`. 

### `multinomialExponent_le_mul_log`

 Let `T` be a Frobenius cycle with `N` letters and prime `p = T.p`, and let
`q = T.q = p ^ (T.frobExp * N)` be the size of the residue field of `W`. Then the number
`c₀ = T.multinomialExponent k = k ^ 2 log_p q` is at most `3 / 2 * k ^ 2 * log q`, because
`log p ≥ log 2 ≥ 2 / 3`. 

### `two_le_rank`

 Large degree (`New.FrobeniusCycle.IsLargeDegree`) forces the rank `k ≥ 2 r` to be at least
`2`. 

### `mul_log_le_div`

 Dividing `N k log q` by the proportion `θ ∈ (0, 1]` of exceptional elementary divisors does not
make it smaller; here `q = P ^ N` is the size of the residue field. 

### `mul_pow_le_degree`

 Let `T` be a Frobenius cycle: a prime `p`, a power `P = T.P` of `p` and `N` ring maps `W → O`
(the letters), each the `P`-th power of the one before modulo `p`, where the residue field of `W`
has `q = P ^ N` elements. Let the degree `n` be large: `0 < r ≤ k / 2`, `0 < θ ≤ 1`, `n ^ 4 ≤ q` and
`(N k log q / θ) ^ 5 P ^ (3 r) ≤ n`. Then `(N k) ^ 5 ≤ n`, because `log q ≥ 1`. 

### `twenty_seven_le_log_q`

 Under the size conditions `h_large`, `27 ≤ log T.q`: from `T.q ≥ n ^ 4` and
`n ≥ (N k) ^ 5 ≥ 4 ^ 5` follows `log T.q ≥ 40 log 2 ≥ 27`. 

### `mul_degree_add_lt_P_pow`

 Let `T` be a Frobenius cycle: a prime `p`, a power `P = T.P` of `p` and `N` ring maps `W → O`
(the letters), each the `P`-th power of the one before modulo `p`, where the residue field of `W`
has `q = P ^ N` elements. Let the degree `n` be large: `0 < r ≤ k / 2`, `0 < θ ≤ 1`, `n ^ 4 ≤ q` and
`(N k log q / θ) ^ 5 P ^ (3 r) ≤ n`. For `2 ℓ = N` one has `N k (ℓ + 2) n + n + k < P ^ ℓ`, because
`P ^ ℓ = √q ≥ n ^ 2` and `n ≥ (N k) ^ 2 + 2`. 

### `one_lt_degree`

 A large degree `n` is greater than `1`, because `n ≥ (N k) ^ 5`. 

### `degree_lt_q`

 A large degree `n` is less than the size `q` of the residue field, because `n ^ 4 ≤ q`. 

### `mul_log_pow_mul_le`

 Under the size conditions `h_large`, `(N k log T.q) ^ 5 T.P ^ (3 r) ≤ θ n`: clear the
denominator in the degree condition `(N k log T.q / θ) ^ 5 T.P ^ (3 r) ≤ n` and use `θ ^ 5 ≤ θ`. 

### `multinomialExponent_mul_le_degree`

 Let `T` be a Frobenius cycle with `N` letters and the prime power `P = T.P`, and let
`q = P ^ N`. Let the degree `n` be large: `0 < r ≤ k / 2`, `0 < θ ≤ 1`, `n ^ 4 ≤ q` and
`(N k log q / θ) ^ 5 P ^ (3 r) ≤ n`. Then `c₀ P ^ (2 r) ≤ n`, where
`c₀ = T.multinomialExponent k = k ^ 2 log_p q` for the prime `p = T.p` of which `P` is a power. 

### `mul_multinomialExponent_le_divisorConstant`

 Let `T` be a Frobenius cycle with `N` letters and the prime power `P = T.P`, and let
`q = P ^ N`. Let the degree `n` be large: `0 < r ≤ k / 2`, `0 < θ ≤ 1`, `n ^ 4 ≤ q` and
`(N k log q / θ) ^ 5 P ^ (3 r) ≤ n`. Then `N c₀ ≤ c_div`, where
`c₀ = T.multinomialExponent k = k ^ 2 log_p q` with `p = T.p`, and `c_div = T.divisorConstant k n
r = N n (1 / P ^ (2 r) + r ^ 2 / (k P))`. 

### `mul_defectThreshold_le_mul_degree`

 Let `T` be a Frobenius cycle with `N` letters and the prime power `P = T.P`, and let
`q = P ^ N`. Let the degree `n` be large: `0 < r ≤ k / 2`, `0 < θ ≤ 1`, `n ^ 4 ≤ q` and
`(N k log q / θ) ^ 5 P ^ (3 r) ≤ n`. Then `8 N k c* P ^ (2 r) ≤ θ n`, where
`c* = defectThreshold k c = 3 k c` for the precision
`c = T.congruencePrecision k = 5 N k ^ 2 log_p q`, `p = T.p`. 

 ### Conditions on an edge 

### `IsEdgeCondition`

 Conditions modulo `w ^ c` on the value of a function at an edge. Vectors are coefficients in the
normalized monomials, and `(h, h') ↦ h' ⬝ᵥ (b * h)` is the pairing with the dual edge. The module
`C` consists of the values that satisfy the conditions, `Av` is the averaging map, and `S` contains
the reductions of the vectors `h` with `w ^ (c - 1) • h ∈ C`. 

### `IsEdgeCondition.allEdgesForms_le`

 The conditions hold for the forms in the halfway lattices of all edges from the origin. 

### `IsEdgeCondition.pow_smul_mem`

 The conditions are congruences modulo `w ^ c`: multiples of `w ^ c` satisfy them. 

### `IsEdgeCondition.average_mem`

 The values of `Av` satisfy the conditions. 

### `IsEdgeCondition.pow_dvd_pairing_average`

 Against the forms in the halfway lattices of all edges from the origin of the dual edge, `Av`
  is multiplication by `p ^ (N c₀)` modulo `w ^ c`, with `c₀ = T.multinomialExponent k`. 

### `IsEdgeCondition.residue_mem`

 If `w ^ (c - 1) • h` satisfies the conditions, then `h` reduces into `S`. 

### `IsEdgeCondition.index_mul_finrank_le`

 The number of edges into a lattice times `dim S` is at most `1 + θ` times the number of
  monomials. 

### `mem_translatesIn_of_pow_smul_mem`

 The module `T.translatesIn n τ J B` consists of the vectors whose translates by the Levi
subgroup of `τ` have their coefficients at `B` in the ideal `J`. Let `0 < c`. If
`T.sqrtPrime ^ (c - 1) • h` lies in this module for the ideal `(T.sqrtPrime ^ c)`, then `h` lies in
it for every ideal `J` that contains `T.sqrtPrime`. 

### `sqrtPrime_mem_maximalIdeal`

 If the prime `T.p` is not a unit of the local ring `O`, then its square root `T.sqrtPrime` (with
`T.sqrtPrime ^ 2 = T.p`) lies in the maximal ideal `maximalIdeal O`. 

### `charP_residueField`

 If `p` is not a unit of `O`, then the residue field of `O` has characteristic `p`, the prime of
the reduced Frobenius cycle. 

### `exists_isEdgeCondition`

 Let `W` be a local ring, `O` a valuation domain of characteristic zero and `T` a Frobenius cycle
with `N` letters (ring maps `W → O`). Its prime `p = T.p = w ^ 2`, `w = T.sqrtPrime`, is not a unit
of `O`, and the residue field of `W` has `q = P ^ N` elements for the power `P = T.P` of `p`. Forms
have `k` variables and degree `n` in each letter and are given by their coefficients, and
`g ∈ GL_k(W)` acts on them by the matrix `ρ(g) = T.letterRep n g`. Let `0 < r ≤ k / 2`, `0 < θ ≤ 1`,
`n ^ 4 ≤ q` and `(N k log q / θ) ^ 5 P ^ (3 r) ≤ n` (`h_large`). Let `b` be weights such that `ρ(g)`
and `ρ(gᵀ)` are adjoint for `(h, h') ↦ h' ⬝ᵥ (b * h)`, with `b * b' = p ^ (N c₀)` for
`c₀ = T.multinomialExponent k` (`hb`). Put `c = T.congruencePrecision k = 5 N c₀`, and let
`M = T.allEdgesForms k n r` be the module of forms that lie in the halfway lattices of all edges
from a lattice. Then there are
* a module `C` of forms that contains `M` and the multiples of `w ^ c`,
* a matrix `Av` with values in `C` that, paired against `M`, is multiplication by `p ^ (N c₀)`
  modulo `w ^ c`,
* a space `S` over the residue field of `O` that contains the reductions of the `h` with
  `w ^ (c - 1) • h ∈ C`, such that `dim S` times the index in `GL_k(W)` of the parahoric subgroup
  with blocks `r` and `k - r` is at most `1 + θ` times the number of monomials. 

 ### The operator and its factorization 

### `depthPower`

 The diagonal matrix that multiplies the coefficient of a monomial by `p ^ depth`. 

### `edgeHeckeOperator`

 The edge Hecke operator on functions `F : X → O ^ I`, in coordinates. Here `J` identifies `I`
with (exponents) × `H`, and the values of `F` are coefficients in the basis `(n! ^ N / β!) z ^ β`,
in which the substitution `h ↦ h ∘ g` has the matrix `ρ(g)ᵀ`, `ρ = T.letterRep n`. The value at `x`
is the sum over the edges `e = (x, b)` into `x` of the matrix `(ρ(originBasisChange e) p ^ depth
ρ(terminusBasisChange b))ᵀ ⊗ transition e` applied to `F (origin e)`. In terms of forms this is
`p ^ (N n / 2)` times the sum of the values at the origins of the edges, each carried to `x` by the
element `δ` of its edge. 

### `edgeHeckeOperator_apply`

 The edge Hecke operator entry by entry: at `x`, `i` it is the sum over `b`, `j` of
`𝓔.transition (x, b)` at `(J i).2`, `(J j).2`, times the `((J j).1, (J i).1)` entry of the matrix
product, times `F (𝓔.origin (x, b)) j`. 

### `IsEdgePairing.transpose_mul_diagonal_mul`

 Let `T` be a Frobenius cycle with `N` letters (ring maps `W → O`) and prime `p = w ^ 2`,
`w = T.sqrtPrime`. Let `ρ = T.letterRep n` be the representation of `GL_k(W)` on the forms with `k`
variables and degree `n` in each letter, and let `ρ(g)` and `ρ(gᵀ)` be adjoint for the pairing with
weights `b` (`hb`). Let `D = T.depthScaling k n r` be diagonal with entries `w ^ depth β`, where
`depth β` is the degree of the monomial `β` in the deep variables: those after the first `r` in an
even letter, and the first `r` in an odd letter. So `D ^ 2 = T.depthPower k n r` has entries
`p ^ depth β`. Then `(D ρ(γ))ᵀ diag(b) D ρ(gᵀ) = (ρ(g) D ^ 2 ρ(γ))ᵀ diag(b)`. 

### `IsEdgePairing.edgeHeckeOperator_regroup`

 Let `T` be a Frobenius cycle with `N` letters, and let forms have `k` variables and degree `n`
in each letter. The points of `X` represent lattices of rank `k`, each with a free `O`-module with
basis indexed by `H`. An edge is a pair `e = (x, q)` of its terminus `x ∈ X` and a coset `q` of the
parahoric subgroup of `GL_k(W)` with blocks `r` and `k - r`. The coordinates `𝓔` give the origin of
`e`, bases adapted to `e` at both ends, and the matrix `𝓔.transition e` on `O ^ H`. The bijection
`J` splits the index set `I` into exponents and `H`, and `regroup J` reads a vector indexed by
`(H × X) × exponents` as a function `X → I → O`. The operator sums, over the edges into `x`, the
values at their origins carried to `x`. Let `b` be the weights of a pairing of forms for which `g`
and `gᵀ` act adjointly (`hb`). On vectors multiplied by `b` the operator is the restriction to
edges, which gives an edge the value at its origin in the adapted basis (`T.edgeRestriction`),
followed by the pairing with the functions restricted to the dual edges from their origins, which
are dual to the termini of the edges. 

 ### The proof of the theorem 

### `divisorConstant_nonneg`

 The constant `T.divisorConstant k n r = N n (1 / P ^ (2 r) + r ^ 2 / (k P))` is nonnegative. 

### `IsLargeDegree.exists_basis_det_dvd`

 Let `T` be a Frobenius cycle with `N` letters (ring maps `W → O`) whose prime `p = w ^ 2`,
`w = T.sqrtPrime`, is not a unit of `O`. Forms have `k` variables and degree `n` in each letter, and
their monomials are indexed by `Exponents N k n`. Let `0 < r ≤ k / 2`, `0 < θ ≤ 1`, `n ^ 4 ≤ q` and
`(N k log q / θ) ^ 5 P ^ (3 r) ≤ n` for `P = T.P` and `q = P ^ N` (`h_large`). The edge `e ∈ E` has
the origin `src e ∈ X` and the basis change `g e`, and every edge from every origin occurs: each
pair of a point of `X` and a coset of the parahoric subgroup of `GL_k(W)` with blocks `r` and
`k - r` is `(src e, (g e)⁻¹)` for some `e`. The functions on edges that depend only on the origin
(`T.originFunctions`) are the image of a matrix `Q` with a left inverse, so its columns are a basis,
and the inclusion `T.edgeRestriction` of the integral functions on origins is `Q * d`, where `det d`
divides `w ^ l` and `l` is at most `c_div = T.divisorConstant k n r` times the rank. 

### `IsEdgePairing.pairingMap_mul_nearInverse_one`

 The sums over the edges nearly fill the target of `Add = pairingMap u b Q'`. Let `T` be a
Frobenius cycle with `N` letters and prime `p`, and `c₀ = T.multinomialExponent k`. Forms are given
by their coefficients, indexed by `Exponents N k n`, and the weights `b` pair forms, with
`b * b' = p ^ (N c₀)` (`hb`). Let `Ed` be the set of edges and `u e` an invertible matrix on `O ^ H`
for each edge `e`. The columns of `Q'`, indexed by `ι`, are functions from `H × Ed` to forms, and
`R'` is a left inverse of `Q'`. The map `nearInverse u 1 b' R'` applies `R'ᵀ` and then, at each
edge, `(u e)⁻¹` on `O ^ H` and multiplication by `b'` on forms. It is a right inverse of `Add` up to
the factor `p ^ (N c₀)`. 

### `IsEdgeCondition.pow_dvd_mul_sub_smul_one`

 A near inverse. Let `T` be a Frobenius cycle with `N` letters and prime `p = w ^ 2`, `k` the
rank, `n` the degree and `c₀ = T.multinomialExponent k`. The weights `b` pair forms, with
`b * b' = p ^ (N c₀)` (`hb`). Let `M = T.allEdgesForms k n r` be the module of forms that lie in the
halfway lattices of all edges from a lattice, where `r` is the size of the first block of the
parahoric subgroup. Let `C, S, Av` be conditions on an edge of precision `c` (`hC`). Only one of
their properties is used, which involves neither `C`, `S` nor `θ`: the matrix `Av`, paired against
`M`, is multiplication by `p ^ (N c₀)` modulo `w ^ c`. Let `Ed` be the set of edges and `u e` an
invertible matrix on `O ^ H` for each edge `e`. Let the columns of `Q'`, indexed by `ι`, be
functions from `H × Ed` to forms with all values in `M` (`hQ'`), and let `R'` be a left inverse of
`Q'`.
The map `Add = pairingMap u b Q'` sends a function on edges to its pairings with these columns, by
`u e` on `O ^ H` and by `b` on forms. The map `Inv = nearInverse u Av b' R'` applies `R'ᵀ` and then,
at each edge, `(u e)⁻¹` on `O ^ H` and multiplication by `b'` followed by `Av` on forms. Then
`Add * Inv ≡ p ^ (2 N c₀)` modulo `w ^ c`, entry by entry. 

### `IsEdgeCondition.exists_finset_smul_top_le_range_sup_span`

 Few further generators for the image of a pairing matrix. Let `O` be a valuation domain of
characteristic zero and `T` a Frobenius cycle with `N` letters for `W` and `O`, whose prime
`p = w ^ 2`, `w = T.sqrtPrime`, is not a unit of `O`. Let `k ≥ 2` be the rank, `n` the degree and
`c₀ = T.multinomialExponent k`. A form is given by its coefficients, which are indexed by
`New.Exponents N k n`. The data are the following.
* The weights `b` pair forms by `(h, h') ↦ h' ⬝ᵥ (b * h)`, and `b * b' = p ^ (N c₀)` (`hb`).
* The module `C` of forms describes conditions modulo `w ^ c`, `c = 5 N c₀`, on the value of a
  function at an edge, and the averaging map `Av` has values in `C`. The space `S` over the residue
  field contains the reductions of the `h` with `w ^ (c - 1) • h ∈ C`, and `θ` bounds its dimension
  (`hC`, see `New.FrobeniusCycle.IsEdgeCondition`).
* A vector indexed by `(H × Ed) × exponents` is a function from `H × Ed` to forms, where `Ed` is
  the set of edges and `H` indexes a basis of the coefficient module. The columns of `Q` and `Q'`
  are such functions, indexed by `V × exponents` for a finite set `V` (the origins of the edges).
  Both matrices have left inverses, and their images have values in `T.allEdgesForms k n r`, the
  forms in the halfway lattices of all edges from a lattice.
* The number `|H × Ed|` is `|V|` times the index of the parahoric subgroup with blocks `r` and
  `k - r`.

The matrix `pairingMap u b Q' * Q` pairs the columns of `Q` with those of `Q'`, by `u e` on `O ^ H`
at the edge `e` and by `b` on forms. Then `p ^ (2 N c₀) O ^ (V × exponents)` lies in the span of its
image and of at most `θ |V × exponents|` further vectors. 

### `exists_colengthDvd_range_pairingMap_mul_edgeRestriction`

 The elementary divisors of the operator factored through the functions on edges. Let `T` be a
Frobenius cycle with `N` letters whose prime `p = T.p` is not a unit of `O`. Forms have `k`
variables and degree `n` in each letter, and their monomials are indexed by `Exponents N k n`. Let
the degree be large for the size `r` of the first block and the proportion `θ ∈ (0, 1]` of
exceptional elementary divisors. Let `Ed` be a finite set of edges, let `H` index a basis of the
free module `O ^ H` of coefficients, and let `V` be a finite set of origins. A pair `e ∈ H × Ed` has
the origin `src e ∈ V` with basis change `g e`, and for the dual edge the origin `src' e ∈ V` with
basis change `g' e`. On both sides every pair of a point of `V` and a coset of the parahoric
subgroup of `GL_k(W)` with blocks `r` and `k - r` occurs, and there are no more pairs than that. The
weights `b` pair forms, with `b * b' = p ^ (N c₀)` for `c₀ = T.multinomialExponent k` (`hb`), and
`u` assigns to each edge an invertible matrix on `O ^ H`. Let `A` be the restriction to edges,
followed by the pairing with the functions restricted to the dual edges. Then the image of `A` plus
`p ^ m O ^ (V × exponents)` has colength dividing `p ^ l` (`New.ColengthDvd`) with `l` at most
`3 c_div + θ m` times `|V × exponents|`, where `c_div = T.divisorConstant k n r`. 

 ### The theorem 

### `_root_.New.EdgeCoordinates.surjective_origin_originBasisChange`

 Every pair of a representative `x` and a coset of the parahoric subgroup is the origin and the
coset of the inverse transposed basis change of an edge of `𝓔`: this map is injective on a finite
set, hence onto. 

### `elementary_divisors`

 The theorem on elementary divisors. Let `O` be a valuation domain of characteristic zero and `T`
a Frobenius cycle with `N` letters, prime `p = T.p` and power `P = T.P` of `p`, so that the residue
field of `W` has `q = T.q = P ^ N` elements. Let `k` be the rank and `n` the degree in each letter,
and let `J` split the index set `I` into exponents and `H`. Let `p` be a non-unit of `O`, and let
`Y ∘ f = f ∘ A` for the edge Hecke operator `A` of the edges `𝓔` between the representatives `X`.
Let `0 < r ≤ k / 2`, `0 < θ ≤ 1`, `q ≥ n ^ 4` and `n ≥ (N k log q / θ) ^ 5 P ^ (3 r)`. Then `Y`
keeps the image `L` of `f`, and for every `m` the colength of `Y L + p ^ m L` in `L` divides `p ^ l`
for some `l ≤ (3 c_div + θ m) |X| |I|`, with `c_div = T.divisorConstant k n r`. 

### `elementary_divisors_length`

 The theorem on elementary divisors in terms of lengths. Let `O` be a discrete valuation ring of
characteristic zero and `T` a Frobenius cycle: a prime `p = T.p`, not a unit of `O`, a power
`P = T.P` of `p` and `N` ring maps `W → O` (the letters), where the residue field of `W` has
`q = P ^ N` elements. The points of `X` represent `W`-lattices of rank `k`, each with a free
`O`-module with basis indexed by `H`. The edges into `x ∈ X` are indexed by the cosets of the
parahoric subgroup of `GL_k(W)` with blocks `r` and `k - r`, and `𝓔` records their origins and basis
changes. The bijection `J` splits `I` into `H` and the exponents of the monomials with `k` variables
and degree `n` in each letter. The edge Hecke operator `A` on functions `X → O ^ I` sums, over the
edges into `x`, the values at their origins carried to `x`. Let `Y ∘ f = f ∘ A`, and let
`0 < r ≤ k / 2`, `0 < θ ≤ 1`, `n ^ 4 ≤ q` and `(N k log q / θ) ^ 5 P ^ (3 r) ≤ n` (`h_large`). Then
`Y` keeps the image `L` of `f`, and the length of `L / (Y L + p ^ m L)` (`New.relLength`) is at most
`l` times the length of `O / p`, for a natural number `l ≤ (3 c_div + θ m) |X| |I|` with
`c_div = T.divisorConstant k n r = N n (1 / P ^ (2 r) + r ^ 2 / (k P))`. This is a corollary of
`New.FrobeniusCycle.elementary_divisors`. 
