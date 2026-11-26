---
{
  "module": "src/New/UpperBound/ElementaryDivisors/Edges.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/Edges.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/Edges.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Edges, halfway lattices and duality

An edge is a pair of lattices `L' ⊆ L` with `p L ⊆ L'` and `L / L'` of dimension `r` over the
residue field; `L'` is its origin. Let `w ^ 2 = p`, and consider forms of degree `n` in each of `N`
letters, with `k` variables in each letter. In a basis of `L'` adapted to the edge, the forms that
are integral for the lattice `L' + w L`, times `w ^ (-n N / 2)`, have as basis the normalized
monomials `w ^ (-depth β) z ^ β`, where the depth is the degree in the deep variables
(`New.FrobeniusCycle.deepIndicator`). This module of forms is the halfway lattice of the edge. The
file works with coefficient vectors in the normalized monomials, so the halfway lattice is the
module of all vectors.

* `New.monomialLattice`, `New.dividedPowerLattice`: the spans `H ⊇ H°` of the monomials `z ^ β` and
  of the `(n! ^ N / β!) z ^ β`; both are stable under `GL_k(W)`.
* `New.FrobeniusCycle.allEdgesForms`: the forms that lie in the halfway lattices of all edges from
  `L'`.
* `New.FrobeniusCycle.IsEdgePairing`: weights of a pairing for which `ρ(g)` and `ρ(gᵀ)` are adjoint;
  it pairs the halfway lattices of an edge and its dual.
* `New.FrobeniusCycle.edgeRestriction`, `New.FrobeniusCycle.originFunctions`: functions on origins
  as functions on edges, and the functions on edges that depend only on the origin.
* `New.FrobeniusCycle.exists_originFunctions_factorization_det_dvd`,
  `New.FrobeniusCycle.mulVec_mulVec_eq_self_of_mem_originFunctions`: if every edge occurs, these
  functions form a direct summand, in which the integral functions on origins have small colength.
* `New.FrobeniusCycle.pow_dvd_letterRep_mulVec_of_mem_allEdgesForms`,
  `New.FrobeniusCycle.IsEdgePairing.pow_dvd_pairing_letterRep`: vectors in `allEdgesForms` have
  coefficients divisible by a power of `w` at monomials of large defect, and pair with these
  monomials to multiples of a power of `w`.

Notions from other files:
* `New.FrobeniusCycle`: a prime `p`, ring maps from `W` to `O` indexed by the letters `s ∈ ℤ/N`,
  which are alternately even and odd, and an element `w` of `O` with `w ^ 2 = p`.
* `New.FrobeniusCycle.letterRep`: the matrix `ρ(g)` of `g ∈ GL_k(W)` on coefficient vectors. It
  substitutes the image of `g` in even letters and of its inverse transpose in odd letters;
  `ρ(g) h` is the translate of `h` by `g`.
* `New.twoBlock`: the blocks of sizes `r` and `k - r`; `New.parahoric`, `New.levi`: the stabilizer
  of the edge and the block diagonal subgroup.
* `New.FrobeniusCycle.translatesIn`: vectors whose translates by a Levi subgroup have coefficients
  in an ideal at a set of monomials. Two cases are `New.FrobeniusCycle.deepForms` (no translate has
  a monomial of depth below a bound) and `New.FrobeniusCycle.defectConditions`.
* `New.FrobeniusCycle.defectWeight`: real weights on the two variables of a root in each letter; the
  defect of a monomial is its weighted degree, and `defectConditions` is the condition on block
  diagonal translates at the monomials of large defect.

## Relation to the literature

See `New.UpperBound.Divisibility.LocalDivisibility` for related work.


### `ParahoricCosets`

 The left cosets of the parahoric subgroup with blocks of sizes `r` and `k - r`. For `r ≤ k` they
index the edges into the lattice `W ^ k`, that is, the sublattices that contain `𝔪 W ^ k`, for the
maximal ideal `𝔪` of `W`, and have a quotient of dimension `r` over the residue field: the
parahoric subgroup is the stabilizer of one of them. As matrices act transposed, the same cosets
index the edges from a lattice, which is how they are used here. 

 ### Linear algebra and divisibility 

### `exists_mul_inv_eq_mul_diagonal`

 Elementary divisors of a matrix `J` over a valuation domain with at least as many rows as
columns, as witnessed by an embedding `ι` of the column indices in the row indices: there are an
invertible `P` and a matrix `Q` with a left inverse `R` such that column `i` of `J * P⁻¹` is `t i`
times column `i` of `Q`. 

### `card_le_mul_finrank_of_dual_rows`

 Vectors with dual rows are independent modulo the maximal ideal. Let the columns `j ∈ s` of `Q`
have dual rows in `R`, that is, column `j` of `R * Q` is the `j`-th unit vector. Suppose that for
each `x ∈ X` the block `i ↦ Q (x, i) j` of such a column reduces into the subspace `S` over the
residue field. Then `s` has at most `|X| dim S` elements. 

### `prod_dvd_pow_sum_card`

 If every `t i` divides `w ^ x`, then their product divides `w ^ l`, where `l` counts the pairs
`(i, δ)` with `δ < x` such that `t i` does not divide `w ^ δ`. 

### `pow_sub_dvd_of_pow_dvd_pow_mul`

 Cancelling a power of `w ≠ 0` in a divisibility: if `w ^ m` divides `w ^ d * x`, then
`w ^ (m - d)` divides `x`, with truncated subtraction. 

 ### The two lattices of forms 

### `dividedPowerCoeff`

 The number `n! ^ N / β!` for an exponent `β` of degree `n` in each of the `N` letters, where
`β!` is the product of the factorials of all entries of `β`. 

### `dividedPowerCoeff_eq_prod_multinomial`

 The number `n! ^ N / β!` is the product over the letters `s` of the multinomial coefficients of
the exponent vectors `β s`. 

### `monomialLattice`

 The lattice `H` of forms with coefficients in `O`: the `O`-span, in the polynomials over the
`O`-algebra `K`, of the monomials `z ^ β` of degree `n` in each of the `N` letters, with `k`
variables in each letter. 

### `dividedPowerLattice`

 The lattice `H°` of divided powers: the `O`-span, in the polynomials over the `O`-algebra `K`,
of the `(n! ^ N / β!) z ^ β`, for the monomials `z ^ β` of degree `n` in each of the `N` letters,
with `k` variables in each letter. 

### `dividedPowerLattice_le_monomialLattice`

 The span `H°` of the `(n! ^ N / β!) z ^ β` lies in the span `H` of the monomials `z ^ β`. 

### `symPowMatrix_mul_multinomial`

 Over a domain of characteristic `0`, the `n`-th symmetric powers of a matrix `A` and of `Aᵀ` are
transposes of each other up to the multinomial coefficients of the exponents. 

### `mem_translatesIn_iff`

 A coefficient vector `v` lies in `T.translatesIn n τ I B` if and only if its translates by the
Levi subgroup of the labelling `τ` have their coefficients at the exponents in `B` in `I`. 

### `residue_mem_translatesIn`

 Let `v` be a coefficient vector whose translates `T.letterRep n g *ᵥ v`, for `g` in the Levi
subgroup of the labelling `τ`, have their coefficients at the exponents in `B` in the maximal ideal
of `O`. Then the translates of the reduction of `v`, for the Frobenius cycle pushed to the residue
field, have their coefficients at `B` in the zero ideal. 

 ### Stability of the two lattices of forms 

### `polyAction_map_monomial`

 Over an `O`-algebra `K`, the translate by `g ∈ GL_k(W)` of `c z ^ β`, with `c ∈ O`, has the
coefficient `ρ(g)_{αβ} c` at `z ^ α`, where `ρ = T.letterRep n`. 

### `polyAction_mem_monomialLattice`

 The lattice `H`, the `O`-span of the monomials of degree `n` in each letter in the polynomials
over the `O`-algebra `K`, is stable under `GL_k(W)`. An element `g` acts by linear substitution,
through the image of `g` in even letters and of its inverse transpose in odd letters. 

### `polyAction_mem_dividedPowerLattice`

 Let `O` be a domain of characteristic `0`. The lattice `H°`, the `O`-span of the
`(n! ^ N / β!) z ^ β` in the polynomials over the `O`-algebra `K`, is stable under `GL_k(W)`. 

 ### One edge 

### `depthScaling`

 The matrix that takes coefficients in the monomials `z ^ β` to coefficients in the normalized
monomials `w ^ (-depth β) z ^ β`, which form a basis of the halfway lattice of the edge. It is
diagonal with entries `w ^ depth β`, where `depth β` is the degree of `z ^ β` in the deep
variables. The variable `b` of the letter `s`, with `b` counted from `0`, is deep if `s` is even
and `r ≤ b`, or `s` is odd and `b < r`. 

### `depthScaling_mulVec_apply`

 The normalized coefficient at `β`, namely the `β` entry of `T.depthScaling k n r *ᵥ h`, is
`T.sqrtPrime ^ T.depth k n r β` times the coefficient `h β`. 

### `depthScaling_eq_kroneckerPi`

 The matrix `T.depthScaling k n r` scales the deep variables of each letter by `T.sqrtPrime`.
These are the variables where `T.deepIndicator r` is `1`. It is the Kronecker product over the
letters `s` of the `n`-th symmetric powers of the diagonal matrices with entry `T.sqrtPrime` at the
deep variables and `1` at the others. 

### `exists_depthScaling_mul_letterRep_eq`

 The stabilizer of the edge preserves its halfway lattice, spanned by the monomials
`w ^ (-depth β) z ^ β`. The diagonal matrix `Δ = T.depthScaling k n r` has entries `w ^ depth β`. If
`u` lies in the parahoric subgroup for the blocks of sizes `r` and `k - r`, which stabilizes the
edge, then `Δ ρ(u) = A Δ` for a matrix `A` over `O`. 

### `letterMatrix_eq_zero_of_mem_levi`

 If `g` lies in the Levi subgroup of the labelling `τ`, then the matrix of `g` on the letter `s`,
the image of `g` or of its inverse transpose, vanishes at `(i, j)` when `τ i ≠ τ j`. 

### `commute_depthScaling_letterRep`

 The block diagonal subgroup preserves depth. Here `T` is a Frobenius cycle, with letters
`s ∈ ℤ/N`, alternately even and odd, and `w = T.sqrtPrime` a square root of its prime. The matrix
`T.letterRep n g` acts on the coefficient vectors of forms of degree `n` in each letter, in `k`
variables, by the image of `g` in even letters and of its inverse transpose in odd letters. Let
`g ∈ GL_k(W)` be block diagonal with blocks of sizes `r` and `k - r` (`levi W (twoBlock k r)`).
Then this matrix commutes with the diagonal matrix `T.depthScaling k n r`, whose entry at the
exponent `β` is `w ^ depth β`, where `depth β` is the degree in the variables of index `b ≥ r` in
even letters and `b < r` in odd letters. 

### `allEdgesForms`

 The forms that lie in the halfway lattices of all edges from the origin, in the normalized
coefficients `v` of one edge. The form is `w ^ (-m) h` for an integral form `h`; every edge from
the origin has an adapted basis in which it becomes a translate by some `g ∈ GL_k(W)`, and the
normalized coefficients of all these translates are integral. 

### `depthScaling_mulVec_mem_allEdgesForms`

 Integral forms lie in the halfway lattices of all edges from the origin: the normalized
coefficients of a form with coefficients `h` in `O` belong to `allEdgesForms`. 

 ### Duality 

### `multinomialExponent`

 The number `c₀ = k² log_p q`, where `q = p ^ (T.frobExp * N)` is the size of the residue field
of `W`. Here `T.frobExp` is the exponent of the power `P = p ^ T.frobExp` that links consecutive
letters: the ring map of the letter `s + 1` is the `P`-th power of that of `s` modulo `p`. A
multinomial coefficient of degree less than `q` with at most `k²` parts has `p`-adic valuation at
most `c₀`. 

### `IsEdgePairing`

 The weights `b` define a pairing `⟨h, h'⟩ = ∑_β h'_β b_β h_β` on coefficient vectors for which
the matrices `ρ(g) = T.letterRep n g` and `ρ(gᵀ)` are adjoint, and the vector `b'` inverts `b` up to
the factor `p ^ (N c₀)`, where `c₀ = T.multinomialExponent k`. It is used as the pairing, in
normalized coefficients, of the halfway lattices of an edge and of the edge of dual lattices. 

### `IsEdgePairing.adjoint`

 The adjoint of `ρ(g)` is `ρ(gᵀ)`: entry by entry, `diag(b) ρ(gᵀ) = ρ(g)ᵀ diag(b)`. 

### `IsEdgePairing.mul_eq_pow`

 The pairing is perfect up to `p ^ (N c₀)`. 

### `IsEdgePairing.dotProduct_letterRep_mulVec`

 Let `⟨h, h'⟩ = ∑_β h'_β b_β h_β`, where the weights `b` satisfy `diag(b) ρ(gᵀ) = ρ(g)ᵀ diag(b)`
for `ρ = T.letterRep n`. Then translation by `g` is adjoint to translation by the transpose of `g`:
`⟨ρ(g) h, h'⟩ = ⟨h, ρ(gᵀ) h'⟩`. 

### `IsEdgePairing.pairing_mul_eq_pow_mul_dotProduct`

 The pairing `⟨h, h'⟩ = ∑_β h'_β b_β h_β` is perfect up to `p ^ (N c₀)`, where
`c₀ = T.multinomialExponent k` and `b_β b'_β = p ^ (N c₀)` for all `β`: every linear form
`h' ↦ h' ⬝ᵥ η`, times `p ^ (N c₀)`, is the pairing with the vector `h = b' * η`. 

### `exists_isEdgePairing`

 For a Frobenius cycle `T` over a valuation domain `O` of characteristic zero, a pairing of an
edge with the edge of dual lattices exists if `p = T.p` is not a unit in `O` and the degree `n` in
each letter is less than `q = T.q`, the number of elements of the residue field of `W`. 

 ### Functions on edges 

### `edgeRestriction`

 The map from the integral functions on the set `X` of origins to the functions on the set `E`
of edges. The edge `e` has the origin `src e`, and `g e` passes to a basis adapted to `e`. The
value at `e` is the vector of normalized coefficients of the translate by `g e` of the value at
`src e`. 

### `originFunctions`

 The functions `ψ` on edges, with values in the halfway lattices, that depend only on the origin:
some `sqrtPrime ^ m • ψ` is the image under `edgeRestriction` of an integral function `φ` on
origins. 

### `edgeRestriction_mulVec_apply`

 The value at `(e, β)` of `T.edgeRestriction n r src g *ᵥ φ` is the `β` entry of `Δ ρ(g e)`
applied to `α ↦ φ (src e, α)`, where `Δ = T.depthScaling k n r` and `ρ = T.letterRep n`. So it is
the translate by `g e` of the value of `φ` at the origin `src e` of the edge `e`, with coefficients
rescaled by powers of `T.sqrtPrime`. 

### `transpose_edgeRestriction_mulVec`

 The transpose of `edgeRestriction`: its value on `ψ` at the origin `x` is the sum over the edges
`e` from `x` of `(Δ ρ(g e))ᵀ ψ(e)`, where `Δ = T.depthScaling k n r` and `ρ = T.letterRep n`. 

### `dvd_depthScaling_mulVec_of_dvd_edgeRestriction`

 From edges to all bases. Let the edge `e : E` have the origin `src e : X` and a change of basis
`g e ∈ GL_k(W)`. With `ρ = T.letterRep n` and the diagonal matrix `Δ = T.depthScaling k n r`, which
multiplies the coefficient at `β` by `T.sqrtPrime ^ depth β`, the restriction
`T.edgeRestriction n r src g` sends `φ` to the function with value `Δ ρ(g e) φ(src e)` at `e`.
Suppose that every edge from every origin occurs: each pair of a point of `X` and a left coset of
the parahoric subgroup for the blocks of sizes `r` and `k - r` (`ParahoricCosets`) is
`(src e, (g e)⁻¹)` for some `e`. If `z` divides every coefficient of the restriction of `φ`, then it
divides those of `Δ ρ(γ) φ(y)` for all `y ∈ X` and `γ ∈ GL_k(W)`. 

### `apply_mem_allEdgesForms`

 Let `ψ` be in `T.originFunctions n r src g`: for some `m`, the multiple `w ^ m • ψ` is the
restriction to edges (`edgeRestriction`) of a function `φ` on the origins with values in `O`, where
`w = T.sqrtPrime` and the value of the restriction at the edge `e` is `Δ ρ(g e) φ(src e)`, for
`Δ = T.depthScaling k n r` and `ρ = T.letterRep n`. Suppose that every edge from every origin
occurs: each pair of a point of `X` and a left coset of the parahoric subgroup is
`(src e, (g e)⁻¹)` for some `e`. Then each value `v = ψ(e)` lies in the halfway lattices of all
edges (`allEdgesForms`): for some `m` and some `h` with `w ^ m • v = Δ h`, the power `w ^ m`
divides all coefficients of `Δ ρ(γ) h` for every `γ ∈ GL_k(W)`. 

### `dvd_of_forall_dvd_mul_inv_apply`

 If `z` divides `c` times every entry of one column of an invertible matrix, it divides `c`. 

### `exists_originFunctions_factorization_det_dvd`

 The integral functions on origins have small colength in the functions on edges that depend only
on the origin. Here `O` is a valuation domain and `T` is a Frobenius cycle from the local ring `W`
to `O`. `w = T.sqrtPrime` squares to the prime `T.p`. The edge `e : E` has the origin `src e : X`
and a change of basis `g e ∈ GL_k(W)`. The matrix `T.edgeRestriction n r src g` sends a function `φ`
on origins to `e ↦ Δ ρ(g e) φ(src e)`. Here `ρ = T.letterRep n`, and `Δ` multiplies the coefficient
at `β` by `w ^ depth β`. `T.originFunctions n r src g` consists of the `ψ` with some `w ^ m • ψ` in
the image of this matrix.

Suppose that every edge from every origin occurs. That is, each pair of a point of `X` and a left
coset in `ParahoricCosets W k r` is `(src e, (g e)⁻¹)` for some `e`. Suppose also that all depths
are at most `x`. Then there are matrices `Q` and `R` with `R * Q = 1`, such that `Q *ᵥ φ` lies in
`originFunctions` for every `φ`. Moreover `Q * d = edgeRestriction` for a `d` whose determinant
divides `w ^ l`. Here `l` is `|X|` times the sum over `1 ≤ δ ≤ x` of the dimensions of the spaces
`deepForms`. These are the forms over the residue field of `O` all of whose translates have only
monomials of depth at least `δ`. 

### `mulVec_mulVec_eq_self_of_mem_originFunctions`

 Let the edge `e : E` have the origin `src e : X` and a change of basis `g e ∈ GL_k(W)`. Let
`T.edgeRestriction n r src g` be the matrix that sends a function `φ` on origins to
`e ↦ Δ ρ(g e) φ(src e)`, for `ρ = T.letterRep n` and `Δ = T.depthScaling k n r`, and let
`T.originFunctions n r src g` be the module of the `ψ` with `T.sqrtPrime ^ m • ψ` in its image for
some `m`. If `O` is a domain of characteristic zero, `Q` has a left inverse `R` and this matrix
factors as `Q * d`, then `Q R` fixes every such `ψ`. 

 ### Large defect 

### `pow_add_dvd_of_le_defect`

 A large defect forces a divisible coefficient. Let `O` be a domain of characteristic zero, `T` a
Frobenius cycle and `w = T.sqrtPrime`, so `w ^ 2 = p`. Let `a < r` be indices of variables, so `a`
is in the first and `r` in the second of the blocks `b < r`, `b ≥ r`. In a letter `s` let
`(u_s, ū_s)` be `(r, a)` if `s` is even and `(a, r)` if it is odd. The defect of `β` at the letter
`i`, which is its weight for `T.defectWeight i a r`, is `β_i(u_i) + ∑_s P ^ ((s - i) mod N)
(β_s(u_s) - β_s(ū_s)) / (q - 1)`, for `P = p ^ T.frobExp` and `q = P ^ N`.

If `w ^ m` divides `w ^ depth β * (ρ(g) F) β` for all `g` and `β`, where `ρ = T.letterRep n`, then
`w ^ (m + j)` divides it at the exponents `β` of defect at least `3 j`. 

### `pow_dvd_letterRep_mulVec_of_mem_allEdgesForms`

 Let `O` be a domain of characteristic zero, `w = T.sqrtPrime` the square root of the prime of
the Frobenius cycle `T`, and `a < r` indices of variables, one in each of the blocks `b < r`,
`b ≥ r`. Let `v` lie in `T.allEdgesForms k n r`: for some `m` and some `h` with `w ^ m • v = Δ h`,
the power `w ^ m` divides all coefficients of `Δ ρ(γ) h` for every `γ ∈ GL_k(W)`. Here
`ρ = T.letterRep n` and `Δ = T.depthScaling k n r` multiplies the coefficient at `β` by
`w ^ depth β`. Let `g` be block diagonal (`levi`). If `β` has defect at least `3 j` at the letter
`i`, that is, `β_i(u_i) + ∑_s P ^ ((s - i) mod N) (β_s(u_s) - β_s(ū_s)) / (q - 1) ≥ 3 j` with
`(u_s, ū_s)` equal to `(r, a)` for even and `(a, r)` for odd `s` (`T.defectWeight i a r`;
`P = p ^ T.frobExp`, `q = P ^ N`), then `w ^ j` divides the coefficient at `β` of `ρ(g) v`. 

### `allEdgesForms_le_defectConditions`

 Let `O` be a domain of characteristic zero. The forms in the halfway lattices of all edges
(`allEdgesForms`) satisfy the conditions on an edge (`defectConditions`): their block diagonal
translates have, modulo `sqrtPrime ^ c`, no term of defect above `3 c*` along the root `(a, r)`,
where `c* = 3 k c` is `defectThreshold k c` and `a < r` are indices, one in each block. 

### `IsEdgePairing.pow_dvd_pairing_letterRep`

 Let `O` be a domain of characteristic zero, `w = T.sqrtPrime` (so `w ^ 2 = p`) and
`ρ = T.letterRep n`. Let `(b, b')` be an edge pairing: `ρ(g)` and `ρ(gᵀ)` are adjoint for
`∑_β h'_β b_β h_β`, and `b_β b'_β` is a fixed power of `p` (`IsEdgePairing`). Let `v` lie in
`T.allEdgesForms k n r`: for some `m` and some `h` with `w ^ m • v = Δ h`, the power `w ^ m` divides
all coefficients of `Δ ρ(γ) h` for every `γ`, where `Δ = T.depthScaling k n r`. Let `a < r` be
indices of variables, one in each of the blocks `b < r`, `b ≥ r`, let `g` be block diagonal, and let
`β` have defect above `c* = 3 k c` (`defectThreshold k c`) at the letter `i`. This defect, the
weight for `T.defectWeight i a r`, is `β_i(u_i) + ∑_s P ^ ((s - i) mod N) (β_s(u_s) -
β_s(ū_s)) / (q - 1)`, with `(u_s, ū_s) = (r, a)` for even and `(a, r)` for odd `s`,
`P = p ^ T.frobExp`, `q = P ^ N`. Then `w ^ c` divides the pairing, by the weights `b`, of `v` with
the image under `ρ(g)` of the unit vector at `β`. 
