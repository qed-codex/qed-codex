---
{
  "module": "src/New/UpperBound/ElementaryDivisors/FrobeniusFactors.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/FrobeniusFactors.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/FrobeniusFactors.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The substitution by Frobenius powers of generic matrices; weight and defect

Fix a Frobenius cycle `T` (`New.FrobeniusCycle`; letters `s : ZMod N`, even or odd, `P` a power of
the prime `p`, `q = P ^ N`, `w ^ 2 = p`). The twists `T.embedding s g` are not algebraic in `g`, but
modulo `p` they are entrywise powers of one another. So we take one generic `k × k` matrix for each
letter (a copy) and let the copy `s - d`, `0 ≤ d ≤ ℓ`, act on the letter `s` through its entrywise
power `P ^ d`, or through the cofactor matrix of this power if `s` is odd; the last factor, `d = ℓ`,
acts on the deep variables only. The matrix of this substitution on forms is
`New.FrobeniusCycle.substitutionOperator` at the factors `New.FrobeniusCycle.frobGenericMatrix`.
Matrices act on vectors of coefficients, so they are the transposes of the matrices that are
substituted in the variables: the row index of an entry here is its column index there.

* `New.FrobeniusCycle.substitutionOperator_map_eq_conj`: conjugation of the factors by a block
  diagonal matrix.
* `New.FrobeniusCycle.copyWeight`: the weight of a monomial in the entries of all copies.
* `New.FrobeniusCycle.abs_defect_sub_copyWeight_le`: let `a' = a + 1`, `ℓ ≤ N` and
  `N n k (ℓ + 2) ≤ P ^ ℓ`, and take an entry in row `β` of the operator with `r = a'` at the factors
  `New.FrobeniusCycle.conjFrobGenericMatrix h` (the generic factors after a change of frame by `h`).
  If the coefficient of a monomial in it is not divisible by `w ^ c`, the weight of the monomial at
  the copy `i` is within `c* = 3 k c` of the defect of `β` at the letter `i + ℓ`.

A term of an entry of a product of matrices belongs to a path of indices. The weight of a step is a
difference of two scaled index weights (`New.FrobeniusCycle.scaledIndexWeight`) up to `1 / P ^ ℓ`,
so the weights telescope along a path and leave the scaled index weight of its last index, up to
`(ℓ + 2) / P ^ ℓ`. For an even letter this scaled index weight is `1 - 1 / q` times the defect
weight. For an odd letter the cofactor matrix changes its sign, which again gives this multiple of
the defect weight, and multiplies the loss by at most `k`. What remains, the defect divided by `q`,
has size at most `1`, as `2 n ≤ q`. `New.FrobeniusCycle.substitutionOperator_mem` carries this out
for all terms at once. An element has level `t` in a filtration `G` (`New.IsRealFiltration`) if it
lies in `G t`, and the levels of the entries are bounded from the levels of the factors. The main
filtrations used are `New.gaussFiltration (New.adicFiltration w) ω`: divisibility of coefficients by
powers of `w`, shifted by weights `ω` of the variables. They also absorb the error terms, which are
multiples of `p` (`New.FrobeniusCycle.conjFrobGenericMatrix_mem_gaussFiltration`). With `0` in place
of `w` the level bounds the weights of the monomials that occur.

Notions from other files:
* `New.FrobeniusCycle.deepIndicator`: the indicator of the deep variables `(b, s)`: it is `1` if `s`
  is even and `r ≤ b`, or `s` is odd and `b < r`, and `0` otherwise.
* `New.FrobeniusCycle.defectWeight i a a'`: the weight of `(b, s)` is
  `± P ^ ((s - i) mod N) / (q - 1)` for `b = a, a'` (with the sign `+` at `a'` for even and at `a`
  for odd `s`, and `1` added to the positive weight at `s = i`), and `0` for other `b`. The defect
  of a monomial at the letter `i` is the sum of these weights over its variables.
* `New.exponentOf`: a family `β` of exponent vectors, one for each letter, as one exponent vector on
  the variables `(b, s)`.
* `New.levi W (New.twoBlock k r)`: the block diagonal matrices in `GL_k(W)` with blocks of sizes `r`
  and `k - r`.

## Notation

Here `h` is a matrix in `GL_k(W)`, not a form.


 ### The substitution and the weights 

### `frobGenericMatrix`

 The generic matrix of the copy `s - d`, whose entries are the variables `X (s - d, b, c)`, with
its entries raised to the power `P ^ d`. 

### `parityCofactor`

 The matrix `M` if the letter `s` is even, and the transposed adjugate of `M` if `s` is odd. 

### `substitutionLetterMatrix`

 The matrix of the letter `s` in `substitutionOperator`. Its row `b` is row `b` of
`T.parityCofactor s` of the product `ψ s (m - 1) * ⋯ * ψ s 0`, where `m = ℓ + 1` if the variable
`(b, s)` is deep (`T.deepIndicator r (b, s) = 1`) and `m = ℓ` if not. 

### `substitutionOperator`

 The Kronecker product over the letters `s` of the `n`-th symmetric powers of the matrices
`T.substitutionLetterMatrix r ℓ ψ s`. In use the factors `ψ s d` are the entrywise powers `P ^ d` of
the copies `s - d` (`frobGenericMatrix`), or these after a change of frame
(`conjFrobGenericMatrix`). 

### `letterConj`

 Conjugation `M ↦ ι(h) M ι(h)⁻¹` by the image of `h` under `ι = T.embedding s`. 

### `_root_.New.rootVector`

 The integer vector `ρ = e_{a'} - e_a`: its entry at `a'` is `1`, at `a` it is `-1`, and the
other entries are `0` (for `a ≠ a'`). For `a' = a + 1` it is minus the simple root
`e_a - e_{a + 1}` of `GL_k`. 

### `indexWeight`

 The weight of the index `b`: the entry at `b` of `ρ = New.rootVector a a'`, divided by
`P ^ ℓ`. 

### `copyWeight`

 The weight at the copy `i` of a monomial `ν` in the entries of all the generic matrices. For a
monomial in one matrix let `row` and `col` be the sums of the entries of
`ρ = New.rootVector a a'` over its row indices and over its column indices. The weight is
`P ^ (-ℓ)` times the sum of `row` at the copy `i` and of `P ^ (-u) (row - col)` at the copies
`i - u`, `0 < u < N`. 

### `scaledIndexWeight`

 The scaled index weight of the index `b` at the exponent `m`: its weight
`New.FrobeniusCycle.indexWeight` times `P ^ m / q`. 

### `entryWeight`

 The weight at the copy `i` of the entry `(b, c)` of the generic matrix of the copy `j`: the
weight of the row `b` if `j = i`, and else the difference of the scaled index weights of `b` and `c`
at the exponent `(j - i) mod N`. 

### `_root_.New.mul_adjugate_conj_mul`

 The adjugate commutes with conjugation: if `A B = 1`, then `B adj(A M B) A = adj(M)`. 

### `letterMatrix_mul_parityCofactor_letterConj_mul`

 Let `T` be a Frobenius cycle, with ring maps `ι = T.embedding s : W → O` for the letters
`s : ZMod N`, each even or odd, and let `h` be in `GL_k(W)`. For even `s`, `T.parityCofactor s M`
is `M` and `T.letterMatrix s h` is `ι(h)`; for odd `s` they are the transposed adjugate of `M` and
the inverse transpose of `ι(h)`. Conjugation by `T.letterMatrix s h` undoes the conjugation
`T.letterConj h s M = ι(h) M ι(h)⁻¹` inside `T.parityCofactor s`. 

### `parityCofactor_map`

 The map `T.parityCofactor s` commutes with applying a ring map to all entries. 

### `letterMatrix_inv_apply_eq_zero`

 If `h` is block diagonal with blocks cut at `r`, then `T.letterMatrix s h⁻¹` mixes row `b` only
with the rows `x` for which `(x, s)` has the same depth `T.deepIndicator r` as `(b, s)`. 

### `substitutionLetterMatrix_map`

 Let `T` be a Frobenius cycle, with ring maps `ι = T.embedding s : W → O` for the letters `s`,
and let `h` in `GL_k(W)` be block diagonal with blocks of sizes `r` and `k - r`. Row `b` of
`T.substitutionLetterMatrix r ℓ ψ s` is row `b` of `ψ s (m - 1) * ⋯ * ψ s 0` for even `s`, and of
its transposed adjugate for odd `s`, where `m = ℓ + T.deepIndicator r (b, s)` is `ℓ` on one block
and `ℓ + 1` on the other. Apply a ring map `χ` to all entries. If `S` is this matrix and `S'` the
one formed from the factors `ι(h) (ψ s d) ι(h)⁻¹` (`T.letterConj`), then `S = H⁻¹ S' H`, where
`H = T.letterMatrix s h` is `ι(h)` for even `s` and its inverse transpose for odd `s`. 

### `substitutionOperator_map_eq_conj`

 Apply a ring map `χ` to all entries, and let `h` be block diagonal with blocks cut at `r`.
Conjugating each factor `ψ s d` by `h` through `T.embedding s` conjugates `T.substitutionOperator`
by `T.letterRep n h`, the matrix of `h` on forms of degree `n` in each letter. 

### `substitutionOperator_frobeniusCycle_map`

 Applying a ring map to the Frobenius cycle does not change the operator, which uses only the
parities of the letters. 

### `substitutionOperator_one`

 If all factors `ψ s d` are the identity matrix, then the substitution operator
`T.substitutionOperator r ℓ n ψ` is the identity matrix. 

 ### Levels of the entries in a filtration 

### `_root_.New.adjugate_transpose_mem`

 Let each entry of row `b` of `M` lie in `G (x b - v)` for the filtration `G`, where `v ≥ 0` and
the `x b` add up to `0`. Then each entry of row `b` of the transposed adjugate `M.adjugateᵀ` (the
cofactor matrix) lies in `G (-x b - k * v)`. 

### `_root_.New.symPowMatrix_mem`

 Let the entries of row `b` of `M` have level `y b` in the filtration `G`. Rows and columns of
the `n`-th symmetric power of `M` are indexed by exponent vectors of degree `n`, and row `β` has
level `∑ b, β b * y b`. 

### `_root_.New.reverse_prod_map_range_mem`

 Filtration levels add up along a product. Suppose that for `d < m` each entry `(b, c)` of `A d`
lies in `G (α (d + 1) b - α d c - u)` for the filtration `G`, and that `α 0 b ≤ u` for all `b`. Then
each entry of row `b` of `A (m - 1) * ⋯ * A 0` lies in `G (α m b - (m + 1) * u)`. 

### `parityCofactor_mem`

 Let the entries of row `b` of the `k × k` matrix `M` have level `x b - v` in the filtration `G`
(that is, lie in `G (x b - v)`), where `v ≥ 0` and the `x b` add up to `0`. The matrix
`T.parityCofactor s M` is `M` for an even letter `s` and the transposed adjugate of `M` for an odd
one. Its row `b` has level `± x b - k v`, with the sign `+` for even and `-` for odd `s`. 

### `substitutionOperator_mem`

 Let `T` be a Frobenius cycle, whose letters `s : ZMod N` are even or odd (`T.isEven`). The
variable `(b, s)` is deep (`T.deepIndicator r (b, s) = 1`, else `0`) if `r ≤ b` for even and `b < r`
for odd `s`. The matrix `T.substitutionOperator r ℓ n ψ` is the Kronecker product over `s` of the
`n`-th symmetric powers of the matrices whose row `b` is that of `ψ s (m - 1) * ⋯ * ψ s 0` (of its
transposed adjugate for odd `s`), with `m = ℓ + 1` or `ℓ` as `(b, s)` is deep or not. Its rows are
indexed by families `β` of exponent vectors `β s` of degree `n`, and `exponentOf β` sends `(b, s)`
to `β s b`. Let `G` be a filtration of `R` (an element of `G t` has level `t`), `u ≥ 0`, and
`α s d` real vectors of sum zero (potentials) with `|α s 0 b| ≤ u`. Let entry `(b, c)` of `ψ s d`
have level `α s (d + 1) b - α s d c - u` for `d ≤ ℓ`, and let `x (b, s) = ± α s m b`, with `+` for
even `s`. Then row `β` has level `∑ b s, β s b * x (b, s) - N n k (ℓ + 2) u`. 

 ### Weights of indices and the Gauss filtration 

### `mul_defectWeight_eq_indexWeight_mul`

 Let `T` be a Frobenius cycle: its letters `s : ZMod N` are alternately even and odd
(`T.isEven`), `P = T.P` is its prime power and `q = T.q = P ^ N`. Let `a' = a + 1`. The defect
weight `T.defectWeight j a a' (b, s)` at a letter `j` is `± P ^ ((s - j) mod N) / (q - 1)` for
`b = a, a'` (positive at `a'` for even and at `a` for odd `s`, with `1` added to the positive weight
if `s = j`) and `0` for other `b`. For `j = i + ℓ`, this weight times `1 - 1 / q` is
`± ρ b / P ^ ℓ * P ^ (d + m) / q`, with `+` for even and `-` for odd `s`. Here `ρ b` is `1` at `a'`,
`-1` at `a` and else `0`, `ρ b / P ^ ℓ` is the index weight of `b`, `m = (s - d - i) mod N`, and
`d = ℓ + 1` or `ℓ` as `(b, s)` is deep for the cut at `a'` or not. 

### `_root_.New.mem_gaussFiltration_adicFiltration_iff`

 A polynomial has level `t` in the Gauss filtration over the `w`-adic filtration if and only if
its coefficient at each monomial `μ` is divisible by `w ^ ⌈t - weight ω μ⌉₊`. 

### `_root_.New.le_weight_of_mem_gaussFiltration_zero`

 If `f` lies at level `t` of the Gauss filtration with variable weights `ω` over
`adicFiltration 0`, then every monomial `μ` with `f.coeff μ ≠ 0` has `t ≤ weight ω μ`. 

### `X_mem_gaussFiltration`

 The variable `X v` has level `ω v` in the Gauss filtration with variable weights `ω` over the
`w`-adic filtration. 

 ### Change of frame 

### `p_dvd_letterConj_pow_sub`

 Conjugate `Y` by `h⁻¹` through `T.embedding (s - d)`, raise the entries to the power `P ^ d`,
and conjugate by `h` through `T.embedding s`. Modulo `p` this is the entrywise `P ^ d`-th power of
`Y`, as `T.embedding (s - d)` to the power `P ^ d` is `T.embedding s` modulo `p`. 

### `conjFrobGenericMatrix`

 The matrix `T.frobGenericMatrix s d` with a change of frame by `h`: the generic matrix of the
copy `s - d` is conjugated by `h⁻¹` through `T.embedding (s - d)`, its entries are raised to the
power `P ^ d`, and the result is conjugated by `h` through `T.embedding s`. 

### `letterConj_mem_gaussFiltration`

 A polynomial over `O` has level `t` (lies in `gaussFiltration (adicFiltration w) ω t`) if its
coefficient at each monomial `μ` is divisible by `w ^ ⌈t - weight ω μ⌉₊`. If all entries of `Y` have
level `t`, so have those of `ι(h) Y ι(h)⁻¹`, where `h` is in `GL_k(W)` and `ι = T.embedding s` maps
`W` to `O`, seen as constant polynomials (`T.map C`). 

### `conjFrobGenericMatrix_mem_gaussFiltration`

 Let all variable weights `ω v` have size at most `1 / T.P ^ d`. Then the entry `(b, c)` of
`T.conjFrobGenericMatrix h s d` has the level `t = T.P ^ d • ω (s - d, b, c)` of the same entry
`X (s - d, b, c) ^ T.P ^ d` without the conjugations: its coefficient at a monomial `μ` is divisible
by `T.sqrtPrime ^ ⌈t - weight ω μ⌉₊`. 

### `weight_entryWeight`

 Let `ν` be a monomial in the variables `(j, b, c)`, the entries of `N` generic `k × k` matrices,
let `P = T.P`, `q = P ^ N` and `ρ = rootVector a a' = e_{a'} - e_a`. The weight
`T.entryWeight ℓ a a' i (j, b, c)` is `ρ b / P ^ ℓ` if `j = i` and else
`P ^ ((j - i) mod N) / q * (ρ b - ρ c) / P ^ ℓ`. Its sum over the variables of `ν` equals
`T.copyWeight ℓ a a' i ν`, which is defined copy by copy from the sums of `ρ` over the row indices
and over the column indices. 

### `abs_scaledIndexWeight_le`

 The scaled index weight of an index at an exponent `m ≤ N` has size at most `1 / P ^ ℓ`. 

### `abs_entryWeight_le`

 For every copy `i` and every entry `v` (a copy together with a row and a column index), the
weight `T.entryWeight ℓ a a' i v` has absolute value at most `2 / T.P ^ ℓ`. 

### `abs_scaledIndexWeight_sub_scaledIndexWeight_sub_entryWeight_le`

 Let `P = T.P`. The entry `(b, c)` of
`T.frobGenericMatrix s d` is the variable `(s - d, b, c)` to the power `P ^ d`, so its weight at the
copy `i` is `P ^ d` times `T.entryWeight`. For `d ≤ N` this weight differs by at most `1 / P ^ ℓ`
from the scaled index weight of `b` at the exponent `d + 1 + (s - (d + 1) - i) mod N` less that of
`c` at the exponent `d + (s - d - i) mod N`. 

### `substitutionOperator_conj_mem_gaussFiltration`

 Let `T` be a Frobenius cycle, with letters `s : ZMod N`, prime power `P = T.P`, `q = P ^ N` and
`w = T.sqrtPrime`, `w ^ 2 = p`. Let `a' = a + 1`, `ℓ ≤ N`, `|ε| ≤ 1 / 2` and `ρ = e_{a'} - e_a`.
Take a generic matrix `X_j` for each `j : ZMod N`, and give its entry `(b, c)` the weight `ε` times
`T.entryWeight ℓ a a' i (j, b, c)`, which is `ρ b / P ^ ℓ` if `j = i` and else
`P ^ ((j - i) mod N) / q * (ρ b - ρ c) / P ^ ℓ`. The matrix `T.substitutionOperator` is the
Kronecker product over `s` of `n`-th symmetric powers of products (transposed adjugates of products
for odd `s`) of the entrywise powers `P ^ d`, `d ≤ ℓ` in deep rows and `d < ℓ` in the others, of the
`X_{s - d}`, taken between conjugations by `h⁻¹` and `h`; its rows `β` are monomials of degree `n`
in the variables `(b, s)` of each letter `s`. The defect of `β` at `i + ℓ` is the sum over its
variables of `T.defectWeight`, which is `± P ^ ((s - i - ℓ) mod N) / (q - 1)` for `b = a, a'` (`+`
at `a'` for even and at `a` for odd `s`, plus `1` there if `s = i + ℓ`) and else `0`. Then the
entries of row `β` have level `t = ε (1 - 1 / q) defect - N n k (ℓ + 2) / (2 P ^ ℓ)`: the
coefficient of a monomial `ν` is divisible by `w ^ ⌈t - weight of ν⌉₊`. 

### `abs_defect_sub_mul_le_one`

 If `2 n ≤ T.q`, the defect `Δ` at the letter `i` along the root `(a, a')` of a monomial `β` of
degree `n` in each letter (the sum of `T.defectWeight i a a'` over `exponentOf β`) satisfies
`|Δ - (1 - 1 / T.q) Δ| ≤ 1`. 

### `abs_defect_sub_copyWeight_le`

 Weight and defect. Let `T` be a Frobenius cycle, with letters `s : ZMod N` (even or odd), ring
maps `W → O`, prime `p`, the power `P = T.P` of `p`, `q = P ^ N` and `w = T.sqrtPrime` in `O` with
`w ^ 2 = p`. Let `a' = a + 1`, `N n k (ℓ + 2) ≤ P ^ ℓ`, `ℓ ≤ N` and `h` in `GL_k(W)`. Take a generic
matrix `X_j` for each `j : ZMod N` (a copy). The matrix `T.substitutionOperator a' ℓ n` is the
Kronecker product over `s` of `n`-th symmetric powers of products (transposed adjugates of products
for odd `s`) of the entrywise powers `P ^ d` of the `X_{s - d}`, taken between conjugations by `h⁻¹`
and `h` (`T.conjFrobGenericMatrix h`); here `d ≤ ℓ` in the rows `b ≥ a'` for even and `b < a'` for
odd `s`, and `d < ℓ` in the others. Its rows `β` are monomials of degree `n` in the variables
`(b, s)` of each letter `s`.

* The defect of `β` at `i + ℓ` is the sum over its variables of `T.defectWeight`, which is
  `± P ^ ((s - i - ℓ) mod N) / (q - 1)` for `b = a, a'` (`+` at `a'` for even and at `a` for odd
  `s`, plus `1` there if `s = i + ℓ`) and else `0`.
* The weight `T.copyWeight` at the copy `i` of a monomial `ν` in the entries of the `X_j` is the sum
  over its variables `(j, b, c)` of `ρ b / P ^ ℓ` if `j = i` and else of
  `P ^ ((j - i) mod N) / q * (ρ b - ρ c) / P ^ ℓ`, where `ρ = e_{a'} - e_a`.

If the coefficient of `ν` in the entry `(β, γ)` is not divisible by `w ^ c`, then the weight of `ν`
is within `defectThreshold k c = 3 k c` of the defect of `β`. 

 ### Degrees 

### `degree_le_of_coeff_substitutionOperator`

 Let `T` be a Frobenius cycle with letters `s : ZMod N` and prime power `P = T.P`. Take a generic
matrix with entries `X (j, b, c)` for each `j : ZMod N` (a copy); `T.frobGenericMatrix s d` is the
entrywise power `P ^ d` of the copy `s - d`. The matrix `T.substitutionOperator r ℓ n` is the
Kronecker product over `s` of `n`-th symmetric powers of products (transposed adjugates of products
for odd `s`) of these for `d < ℓ + 1` or `d < ℓ`, as the side of `r` on which the row lies and the
parity of `s` decide. Its rows and columns `β`, `γ` are families of exponent vectors of degree `n`,
one for each letter. A monomial `ν` that occurs in an entry has degree at most
`N n k (ℓ + 2) P ^ ℓ` in the variables of each copy `j`. 
