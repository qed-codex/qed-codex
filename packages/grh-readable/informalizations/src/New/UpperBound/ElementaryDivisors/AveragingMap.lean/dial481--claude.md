---
{
  "module": "src/New/UpperBound/ElementaryDivisors/AveragingMap.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/AveragingMap.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/AveragingMap.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Averaging: removing the terms of large defect in all Levi translates at once

Fix a Frobenius cycle `T` over `W` and `O` (`New.FrobeniusCycle`; `N = 2 ℓ` letters, `P` a power of
the prime `p`, `w ^ 2 = p`) and an edge, with the Levi subgroup `G` of blocks of sizes `r` and
`k - r`. Forms are written in the normalized monomials of the edge with weights `b_β`, and
`⟨h, h'⟩ = ∑_β h'_β b_β h_β` is the pairing with the forms of the dual edge
(`New.FrobeniusCycle.IsEdgePairing`). Fix `c : ℕ` and put `c* = 3 k c` (`New.defectThreshold`) and
`c₀ = T.multinomialExponent k`. Let `O` be a valuation domain of characteristic `0` in which `p` is
not a unit, and let `P ^ ℓ` be large. The main result
`New.FrobeniusCycle.exists_average_mem_defectConditions_and_dvd_sub` gives a matrix `Av` such that
no `G(W)`-translate of `Av h` has a term of defect above `3 c*` modulo `w ^ c`, while
`⟨Av h, h'⟩ ≡ p ^ (N c₀) ⟨h, h'⟩` modulo `w ^ c` for all `h'` in the halfway lattices of all edges
from the origin of the dual edge (`New.FrobeniusCycle.allEdgesForms`).

Substitute generic matrices, one copy for each letter, in `h`
(`New.FrobeniusCycle.substitutionOperator`). For a set `J` of copies, `Av_J h`
(`New.FrobeniusCycle.partialAverage`) is obtained by applying the average (`New.Average.IsAverage`)
in the copies `j ∈ J` and `p ^ c₀` times the evaluation at `1` in the others. Then
`Av_∅ h = p ^ (N c₀) h`, and `Av` is `Av_J` for the set of all copies. A monomial in one copy is bad
if its row weight for `New.rootVector a r`, `r = a + 1`, is above `2 c* P ^ ℓ`. The substitution in
the frame `g ∈ G(W)` is the one formed from the factors
`New.FrobeniusCycle.conjFrobGenericMatrix g`.

* `New.FrobeniusCycle.contractOtherCopies`, `New.FrobeniusCycle.conjSubst_contractOtherCopies_one`:
  the linear forms are applied in all copies but one, in a frame `g`; the change of frame conjugates
  the remaining copy.
* `New.FrobeniusCycle.abs_weight_div_sub_defect_le`: let the forms be invariant under `G(W)`. If the
  coefficient of `α` in the entry `β` of `contractOtherCopies` is not divisible by `w ^ c`, then the
  row weight of `α` over `P ^ ℓ` is within `c*` of the defect of `β` at the letter `j + ℓ`, for the
  remaining copy `j`.
* `New.FrobeniusCycle.lt_weight_and_lt_defect_of_not_dvd_coeff_contractOtherCopies`: hence a defect
  of `β` above `3 c*` makes `α` bad, and a bad `α` makes the defect exceed `c*`.
* `New.FrobeniusCycle.pow_dvd_pairing_partialAverage_insert_sub`: one more copy in `J` does not
  change the pairing modulo `w ^ c`. The main result adds these differences along a chain of
  subsets.

Notions from other files:
* `New.FrobeniusCycle.letterRep`: the matrix of `g ∈ GL_k(W)` on the forms, which have degree `n` in
  each letter and are twisted at the letter `s` by `T.embedding s`.
* `New.FrobeniusCycle.substitutionOperator`: the Kronecker product over the letters `s` of the
  matrices on forms of degree `n` that are built from given factors `ψ s d`; with
  `New.FrobeniusCycle.frobGenericMatrix` the factor is the entrywise power `P ^ d` of the copy
  `s - d` of the generic matrix, and odd letters take the cofactor matrix of the product.
* `New.Average.IsAverage`: a linear form that is invariant under conjugation by the Levi subgroup
  and vanishes on bad monomials. If a polynomial of bounded degree has all bad coefficients of its
  Levi conjugates in an ideal, the form agrees on it with a multiple of the evaluation at `1` modulo
  this ideal.
* `New.FrobeniusCycle.defectConditions`: the vectors whose `G(W)`-translates have their coefficients
  of defect above a bound in a given ideal.

## Relation to the literature

Linear forms on polynomials in a generic matrix that are invariant under the Levi subgroup split
evaluation at the identity by weight, up to a power of `p`. This gives a map into the forms without
terms of large defect that keeps the pairing up to `p ^ (N c₀)` modulo `w ^ c`. The Schur algebra as
dual of polynomials in a generic matrix, its spanning by finite points in low degree, and truncation
by weights are known in the literature. Related work: Benson–Doty, Schur–Weyl duality over finite
fields, 2009; Green, Polynomial representations of GL_n, 1980; Donkin, On Schur algebras and related
algebras I, 1986.


 ### Tensor products of linear forms on polynomials 

### `map_eq_sum_coeff_mul`

 A linear form on polynomials is determined by its values on the monomials. 

### `dvd_map_of_forall_monomial`

 If for each exponent `α` either `z` divides the coefficient of `α` in `ψ` or the linear form `m`
vanishes on the monomial of exponent `α`, then `z` divides `m ψ`. 

### `tensorDual`

 The tensor product of linear forms `l j` on polynomials in disjoint blocks of variables: the
product of the forms on `⨂_ι R[X_σ]`, pulled back along `R[X_{ι × σ}] → ⨂_ι R[X_σ]`. 

### `tensorDual_prod_rename`

 On a product of polynomials `f j`, one in each block, the tensor product of the forms `l j` is
the product of the values `l j (f j)`. 

### `tensorDual_monomial`

 On the monomial of exponent `ν`, the tensor product of the forms `l j` is the product of the
values of `l j` at the monomials of exponent `ν.curry j`, the parts of `ν` in the blocks. 

### `tensorDual_eq_sum`

 The value of the tensor product of the forms `l j` at `f` is the sum over the monomials of `f`
of the coefficient times the product of the values of the `l j` at the parts of the monomial. 

### `tensorDual_evalAtOne`

 If the form in each block is `evalAtOne z`, that is `z` times the evaluation at the identity
matrix, then the tensor product of the forms is `z` to the number of blocks times the evaluation at
the identity matrix in every block. 

### `tensorDualExcept`

 Apply the forms `l i` in all blocks `i ≠ j` of variables; a polynomial in the block `j`
remains. A monomial of exponent `ν` gives the product of the values of the `l i` at its parts
`ν.curry i`, times the monomial of exponent `ν.curry j`. 

### `map_tensorDualExcept`

 Applying a form `m` to `tensorDualExcept l j f`, the polynomial left in the block `j` after the
forms `l i` are applied in the other blocks, gives `tensorDual (update l j m) f`: the tensor product
of the forms with `l j` replaced by `m`. 

### `exists_of_not_dvd_coeff_tensorDualExcept`

 Let `f` be a polynomial in blocks of variables indexed by `ι`, and let `tensorDualExcept l j f`
be the polynomial in the block `j` obtained by applying the linear forms `l i` in all blocks
`i ≠ j`. If `z` does not divide its coefficient of `α`, then `α` is the part in the block `j` of a
monomial `ν` whose coefficient in `f` is not divisible by `z` and whose other parts are not killed
by the forms `l i`. 

### `tensorDualExcept_mem_restrictTotalDegree`

 The polynomial in the block `j` that remains of `f` after the forms `l i` are applied in the
blocks `i ≠ j` has at most the degree of `f` in the block `j`. 

 ### Linear forms applied to the substitution 

### `frobContraction`

 The entries of `T.substitutionOperator r ℓ n T.frobGenericMatrix` are polynomials in `N` generic
`k × k` matrices, the copies, one for each letter `j ∈ ℤ/N`. This is the matrix over `O` obtained by
applying to each entry the tensor product of linear forms `l j`, one for each copy. Its rows and
columns are indexed by the monomials of degree `n` in each of `N` groups of `k` variables. 

### `frobContraction_evalAtOne`

 The matrix `T.frobContraction n r ℓ l`, indexed by the monomials of degree `n` in each of `N`
groups of `k` variables (`Exponents N k n`), arises from the substitution of `N` generic `k × k`
matrices by applying a linear form `l j` in the entries of the `j`-th one. If each form is `z` times
the evaluation at the identity matrix (`evalAtOne z`), it is the scalar matrix `z ^ N`. 

### `letterRep_mul_frobContraction`

 Let `T` be a Frobenius cycle, with ring maps `T.embedding j : W →+* O` for the letters
`j ∈ ℤ/N`, and let `ρ(g) = T.letterRep n g` be the matrix of `g ∈ GL_k(W)` on polynomials of degree
`n` in each of `N` groups of `k` variables. For a family `ψ` of factors,
`S(ψ) = T.substitutionOperator r ℓ n ψ` is a matrix of the same size; here its entries are
polynomials in `N` generic matrices `X_j`. Write `l(S)` for `S.map (tensorDual l)`, the matrix over
`O` obtained by applying the linear form `l j` in the entries of `X_j` for every `j`. Let `g` be
block diagonal with blocks of sizes `r` and `k - r`, and let `m j` be `l j` composed with
`X ↦ g⁻¹ X g` through `T.embedding j` (`conjSubst`). Then `ρ(g) m(S(ψ₁)) = l(S(ψ_g)) ρ(g)`. Here
`ψ₁ = T.frobGenericMatrix` consists of the entrywise powers `P ^ d` of the `X_j`, so that
`m(S(ψ₁)) = T.frobContraction n r ℓ m`, and `ψ_g = T.conjFrobGenericMatrix g` is the same family
with the powers taken in the basis given by `g`. 

 ### One copy at a time 

### `contractOtherCopies`

 The substitution in the frame `g`, that is `T.substitutionOperator` at the factors
`T.conjFrobGenericMatrix g`, is a matrix of polynomials in `N` generic matrices, the copies. It is
applied to the translate `T.letterRep n g *ᵥ h`, and the linear forms `l i` are applied in all
copies `i ≠ j`. The result is a vector, indexed by `β`, of polynomials in the entries of the copy
`j`. 

### `map_contractOtherCopies`

 Let `g` be block diagonal with blocks of sizes `r` and `k - r`, and let each `l i` be invariant
under `X ↦ g⁻¹ X g` through `T.embedding i` (`conjSubst`). Then a form `m` applied to the entries of
`T.contractOtherCopies r ℓ l j g h` gives the translate by `g` of `T.frobContraction n r ℓ l' *ᵥ h`,
where `l'` is `l` with `l j` replaced by `m` composed with the conjugation. 

### `map_contractOtherCopies_one`

 The entries of `T.contractOtherCopies r ℓ l j 1 h` are the polynomials in the `j`-th generic
matrix that are left when the forms `l i` are applied in the others. A form `m` applied to them
gives `T.frobContraction`, with `m` at the place `j` and `l i` at the others, applied to `h`. 

### `conjSubst_contractOtherCopies_one`

 Change of basis. Let `F_g = T.contractOtherCopies r ℓ l j g h` be the vector of polynomials in
one generic matrix `X` that arises by substituting `N` generic matrices, in the basis given by `g`,
in the translate of `h` by `g`, and applying the linear forms `l i` in all of them but the `j`-th.
Let `g` be block diagonal with blocks of sizes `r` and `k - r`, and let each `l i` be invariant
under `X ↦ g⁻¹ X g` through `T.embedding i` (`conjSubst`). Then `F_1(g⁻¹ X g)`, with the conjugation
through `T.embedding j`, is the translate of `F_g(X)` by `g⁻¹`. 

### `contractOtherCopies_one_mem_restrictTotalDegree`

 Each polynomial `T.contractOtherCopies r ℓ l j 1 h β`, which is left in the `j`-th generic
matrix when the forms `l i` are applied in the others, has total degree at most
`N n k (ℓ + 2) P ^ ℓ`. 

### `abs_weight_div_sub_defect_le`

 Weight and defect in one copy. Let `T` be a Frobenius cycle (`P = T.P`, `w = T.sqrtPrime`,
`w ^ 2 = p`) from a local ring `W` to a domain
`O` of characteristic `0` in which `p` is not a unit. Let `r = a + 1`, `N n k (ℓ + 2) ≤ P ^ ℓ` and
`ℓ ≤ N`. Let each linear form `l i` be invariant under conjugation, through `T.embedding i`, by the
Levi subgroup of the blocks of sizes `r` and `k - r`. Let `β` be a monomial of degree `n` in each
letter. The polynomial `T.contractOtherCopies r ℓ l j g h β` in one generic matrix is the entry `β`
of the vector obtained from `T.letterRep n g *ᵥ h` by substituting the `N` generic matrices
conjugated by `g` and applying the `l i` in all of them but the `j`-th. Let its coefficient of `α`
not be divisible by `w ^ c`. Then the row weight of `α` (its degree in the row `r` minus its degree
in the row `a`), divided by `P ^ ℓ`, is within `defectThreshold k c = 3 k c` of the defect of `β` at
the letter `j + ℓ`. The defect is a weighted sum over all letters of the degrees of `β` in the
variables `a` and `r`, with the real weights `T.defectWeight (j + ℓ) a r`; `exponentOf β` is `β` as
one exponent vector. 

### `lt_weight_and_lt_defect_of_not_dvd_coeff_contractOtherCopies`

 Let `T` be a Frobenius cycle from a local ring `W` to a domain `O` of characteristic `0` in
which `p` is not a unit. Let `r = a + 1`, `N n k (ℓ + 2) ≤ P ^ ℓ` and `ℓ ≤ N`. Let each linear form
`l i` be invariant under conjugation, through `T.embedding i`, by the Levi subgroup of the blocks of
sizes `r` and `k - r`. Let `β` be a monomial of degree `n` in each letter. The polynomial
`T.contractOtherCopies r ℓ l j g h β` in one generic matrix is the entry `β` of the vector obtained
from `T.letterRep n g *ᵥ h` by substituting the `N` generic matrices conjugated by `g` and applying
the `l i` in all of them but the `j`-th. Let its coefficient of `α` not be divisible by `w ^ c`, and
put `c* = 3 k c`. The row weight of `α` is its degree in the row `r` minus its degree in the row
`a`, and the defect of `β` at the letter `j + ℓ` is its weighted degree for the weights
`T.defectWeight (j + ℓ) a r`. If the defect is above `3 c*`, then the row weight is above
`2 c* P ^ ℓ`; if the row weight is above `2 c* P ^ ℓ`, then the defect is above `c*`. 

 ### The averaging map 

### `partialAverage`

 The map `Av_J`: the substitution `T.substitutionOperator` at generic matrices, one for each
letter, is applied, then the forms `I j` (averages, in the applications) in the copies `j ∈ J` and
`p ^ c₀` times the evaluation at the identity matrix in the other copies,
`c₀ = T.multinomialExponent k`. 

### `partialAverage_empty`

 With no average, the map `Av_∅` is `p ^ (N c₀)` times the identity, where
`c₀ = T.multinomialExponent k`. 

### `partialAverage_univ_mulVec_mem_defectConditions`

 Let `T` be a Frobenius cycle over a domain `O` of characteristic `0` in which `p` is not a unit.
Let `r = a + 1`, `N n k (ℓ + 2) ≤ P ^ ℓ` and `ℓ ≤ N`, and put `c* = 3 k c`. Let the `I j` be
averages; they are linear forms on polynomials in a generic matrix, invariant under the Levi
subgroup of the blocks of sizes `r` and `k - r`, that vanish on the monomials of row weight above
`2 c* P ^ ℓ`. Let `Av = T.partialAverage n r ℓ I univ` be the matrix obtained from the substitution
of `N` generic matrices by applying `I j` in the `j`-th one for every `j`. Then for every
coefficient vector `h`, `w ^ c` divides the coefficient in each Levi translate of `Av h` of each
monomial with defect above `3 c*` at some letter; the defect is the weighted degree for
`T.defectWeight`. 

### `pow_dvd_pairing_partialAverage_insert_sub`

 Let `T` be a Frobenius cycle over a valuation domain `O` of characteristic `0` in which `p` is
not a unit. Let `r = a + 1`, `N n k (ℓ + 2) ≤ P ^ ℓ` and `ℓ ≤ N`, and put `c* = 3 k c` and
`c₀ = T.multinomialExponent k`. Let the `I j` be averages up to the degree `N n k (ℓ + 2) P ^ ℓ`,
whose bad monomials are those of row weight above `2 c* P ^ ℓ`. The matrix
`Av_J = T.partialAverage n r ℓ I J` arises from the substitution of `N` generic matrices by applying
`I i` in the `i`-th one for `i ∈ J`, and `p ^ c₀` times the evaluation at `1` for `i ∉ J`. Let the
weights `b` define a pairing `⟨h, h'⟩ = ∑_β h'_β b_β h_β` that makes the matrices of `g` and `gᵀ`
adjoint, with `b b' = p ^ (N c₀)`. Let `h' ∈ T.allEdgesForms k n r`: it is `w ^ (-m) Δ f` for a
vector `f` over `O` with `w ^ (-m) Δ g f` integral for all `g ∈ GL_k(W)`, where
`Δ = T.depthScaling k n r` is a diagonal matrix of powers of `w`. Then
`⟨Av_{J ∪ {j}} h, h'⟩ ≡ ⟨Av_J h, h'⟩` modulo `w ^ c` for `j ∉ J`. 

### `exists_average_mem_defectConditions_and_dvd_sub`

 The averaging map. Let `T` be a Frobenius cycle (`P = T.P`, `w = T.sqrtPrime`, `w ^ 2 = p`)
over a valuation domain `O` of characteristic
`0` in which `p` is not a unit. Vectors are coefficient vectors of polynomials of degree `n` in each
of `N` groups of `k` variables, on which `GL_k(W)` acts by `T.letterRep n`. Let `r = a + 1`,
`N = 2 ℓ` and `N k (ℓ + 2) n + n + k < P ^ ℓ`. Put `c* = 3 k c` and
`c₀ = T.multinomialExponent k = k² log_p P^N`. Let the weights `b` define a pairing
`⟨h, h'⟩ = ∑_β h'_β b_β h_β` that makes the matrices of `g` and `gᵀ` adjoint, with
`b b' = p ^ (N c₀)`. For every `c` there is a matrix `Av` with two properties.
* For all `h` and all `g` in the Levi subgroup of the blocks of sizes `r` and `k - r`, `w ^ c`
  divides the coefficient in `g Av h` of each monomial with defect above `3 c*` at some letter `i`;
  the defect is the weighted degree for the weights `T.defectWeight i a r`.
* `⟨Av h, h'⟩ ≡ p ^ (N c₀) ⟨h, h'⟩` modulo `w ^ c` for all `h` and all
  `h' ∈ T.allEdgesForms k n r`. 
