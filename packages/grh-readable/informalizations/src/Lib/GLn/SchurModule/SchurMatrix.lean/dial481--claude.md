---
{
  "module": "src/Lib/GLn/SchurModule/SchurMatrix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/SchurModule/SchurMatrix.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/SchurModule/SchurMatrix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Schur matrices, the standard basis of ∇, its weights and the highest vector

Polynomials are taken in the entries of an array y with rows (τ, a). Here κ_τ(h) is the number of
columns of height h at the place τ; `New.rankAt n τ` = |n_τ|, and
λ = `New.diagramWeight (rankAt n) κ` has λ(τ, k) = Σ_{k<h<|n_τ|} κ_τ(h). The products
b_i = `New.nablaBasis` of minors of y along standard fillings form a basis of the module
∇ = `New.nablaFamily` of Borel semi-invariants. The Schur matrix S_κ(z) = `New.schur κ z` of a
family of matrices z_τ records the expansion of b'_i(zy); for square z this gives a polynomial
representation of ∏_τ GL(n_τ), which `New.weylRep` twists by integer powers of determinants. For one
place and a one-row shape, S_κ over ℂ is a symmetric power, and, over a topological ring, S_κ(z) is
continuous in z for square z.

## Main definitions and results

* `New.linearIndependent_nablaBasis`, `New.range_nablaCombination`: the b_i form a basis of ∇ over
  every commutative ring.
* `New.sum_schur_smul_nablaBasis`, `New.GL.schur_eq_of_expansion`: row i of S_κ(z) is characterised
  by the expansion of b'_i(zy) in the products b_j(y) ∏_τ det(y_τ)^{d_τ}, with
  d = `New.schurDetExp`.
* `New.schur_map`, `New.schur_mul_left`, `New.schur_mul_right`, `New.schur_apply_eq_prod`: base
  change, multiplicativity, and the product over the places τ.
* `New.schur_diagonal`, `New.weyl_character`: diagonal matrices and Weyl's character formula.
* `New.weylRep κ e` is the matrix representation of `∏ τ, GL (n τ) R` of weight `(κ, e)`: the Schur
  matrix `New.schur κ g` twisted by the powers `det (g τ) ^ e τ`, with integer exponents `e τ`.
* `New.map_nablaBasis_eq_map_weylKernel_mul_weylEval`: fix enumerations e_τ of the rows. Let φ be a
  linear form with φ(b_i) ≠ 0 only if λ(τ, e_τ(a)) ≤ `New.tableauWeight` i τ a for every row (τ, a).
  Then φ(b_i) = φ(k)·b_i(y). Here y is the permutation array of e (`New.permArray`), and k is the
  kernel `New.weylKernel` at y, a substitution (`New.rowSubst`) of the product `New.highestPoly` of
  leading minors, with value k(y) = 1. So on the span of the b_i, φ is determined by its value on k.

Notions from other files:
* `New.schur`: The Schur matrix S_κ(z) of matrices z_τ of size n'_τ×n_τ. Row i holds chosen
  coordinates of b'_i(zy) in the family b_j(y)·∏_τ det(y_τ)^{d_τ}. Here b'_i and b_j are the
  standard basis polynomials in the rows n' and n, and d is given by `New.schurDetExp`.
* `New.rowSubst`: For matrices z_τ of size n'_τ×n_τ, the algebra homomorphism f ↦ f(zy) sending
  variable y_{(τ,b),i} to Σ_a z_τ(b,a) y_{(τ,a),i}.
* `New.WeylIndexFamily`: The type of families choosing, for each place τ, a filling in the chosen
  standard set with rows n_τ, heights below |n_τ| and multiplicities κ_τ.
* `New.schurDetExp`: The natural number κ_τ(|n_τ|) if |n_τ| < |n'_τ|, and 0 otherwise, as a function
  of the place τ.
* `New.FitsRanks`: For row families n and n', the condition, at every place τ, that |n_τ| ≤ |n'_τ|
  and κ_τ(h) = 0 for |n_τ| < h < |n'_τ|.
* `New.detPow`: The product over places τ of the determinant of the variables in all rows of block τ
  (fixed enumeration) and first |n_τ| columns, raised to e_τ.

## Relation to the literature

Known; see `Lib.GLn.SchurModule.MinorBasis` for sources.



## The standard basis of ∇ and Schur matrices

Rectangular z_τ, of size n'_τ × n_τ, are allowed under the condition `New.FitsRanks`.


 ### The standard basis of ∇ 

### `prod_tableauPoly_mem_nabla`

 For each place τ, let `T τ` be a filling with entries in `n' τ` that has `κ τ h` columns of
height `h` for each `h < M τ`. Take the product over τ of the minor products of `T τ`, taken in the
rows (τ, ·). This product lies in `nabla R Sigma.fst (diagramWeight M κ)`. That is, with rows
coloured by τ, it satisfies f(yβ) = ∏ β_{τ,ii}^{l(τ,i)} f(y) for upper triangular β_τ, where l(τ, i)
is the sum of `κ τ h` over i < h < M τ. 

### `exists_isTableauBasis`

 Let ι be a finite alphabet and fix a shape with `k h` columns of height h for each h < M. A
filling (`New.Tableau ι M k`) assigns to each column an h-tuple in ι, with no ordering condition.
Some finite set s of fillings satisfies two conditions: (a) over every commutative ring, the minor
products of the fillings in s form a basis of the span of all minor products; (b) for every
enumeration e of ι and every x : ι → ℂ, (Σ_{T∈s} x^T)·a_0(x) = a_λ(x), where x^T is the product of x
over the entries of T, a is the alternant `New.GL.alternant`, and λ(i) = Σ_{i<h<M} k(h). 

### `isTableauBasis_epsilon`

 Over a finite alphabet `ι`, consider the set of fillings chosen by `Classical.epsilon` (heights
below `M`, `k h` columns of height `h`), which is the set behind `BasisTableau`. This set is a
standard set: (a) over every commutative ring its minor products form a basis of the span of all
minor products; (b) for every enumeration of the rows and every x : ι → ℂ, (Σ_{T∈s} x^T)
a_0(x) = a_λ(x). Here x^T is the product of x over the entries of T, a is the alternant, and λ(i) is
the sum of k(h) over i < h < M.

A weaker form of the standard basis theorem for products of minors. The basis is chosen abstractly,
not described by standard tableaux. 

### `linearIndependent_basisTableau`

 The minor products of the chosen fillings `New.BasisTableau` are linearly independent over
every ring. 

### `exists_sum_basisTableau_smul_eq`

 The minor product of any filling is a linear combination of those of the standard fillings. 

### `sum_basisTableau_mul_alternant`

 The character formula for the standard fillings: the sum of their monomials, times the
alternant of weight zero, is the alternant of the weight whose `i`-th entry counts the columns of
height greater than `i`. 

### `linearIndependent_nablaBasis`

 Over any commutative ring `R`, the polynomials `nablaBasis R n κ` are linearly independent. For
a family `i` of chosen standard fillings, `nablaBasis R n κ i` is the product over places `τ` of the
minor product of `i τ` in the rows of block `τ`.

Part of the standard basis theorem for Schur (dual Weyl) modules over any ring. 

### `isRegular_detPow`

 Over any commutative ring, the polynomial ∏_τ det(y_τ)^{e_τ} is a regular element (not a
zero divisor) of the polynomial ring. 

### `GL.rowSubst_minor`

 For I a tuple of |n_τ| rows of n'_τ, the substitution y ↦ zy sends the minor on rows I
(determinant of the variables in rows (τ, I a) and columns 0, …, |n_τ|−1) to det(z_τ[I, ·]) times
the minor on the rows of n_τ, both taken in the fixed enumeration `New.GL.rowEquivFin n τ` of
n_τ. 

### `rowSubst_detPow`

 Substituting y ↦ g y, for square matrices g_τ of size n_τ, multiplies the product
∏_τ det(y_τ)^{e_τ} of determinants by the scalar ∏_τ det(g_τ)^{e_τ}. 

### `nabla_le_span_nablaBasis_mul_detPow`

 Consider polynomials over `R` in a matrix of variables whose rows, indexed by pairs (τ, row of
`n τ`), are coloured by the place τ. Let f be a Borel semi-invariant (`nabla`) whose weight is
`diagramWeight (rankAt n) κ` plus `e τ` at each column i < |n τ| of each place τ, i.e. the weight of
`κ` with `e τ` further full-height columns at τ. Then f is an `R`-linear combination of the products
`nablaBasis R n κ U * detPow R n e` over `U : WeylIndexFamily n κ`, where `detPow` is the product
over τ of the `e τ`-th powers of the determinants of the block-τ variables in the first |n τ|
columns. 

### `GL.nablaCombination_injective`

 The map `New.GL.nablaCombination` κ, which sends coefficients to the linear combination of the
basis minor products b_i, is injective. 

### `range_nablaCombination`

 The R-linear map `nablaCombination κ`, sending ξ to Σ_i ξ_i b_i with b_i the basis products of
minors `nablaBasis` (indexed by families of chosen standard fillings), has range exactly
`nablaFamily R n κ`. That is the module of Borel semi-invariant polynomials in rows (τ,a), coloured
by τ, whose weight is the partition tuple built from κ using heights below |n_τ|, over any
commutative ring R. 

### `sum_coords_nablaBasis`

 For f in ∇ = `New.nablaFamily`, the coordinates chosen by `invFun` of the linear combination map
`New.GL.nablaCombination` give back f as a combination of the basis products b_i. 

### `GL.linearIndependent_nablaBasis_mul_detPow`

 Over any commutative ring R and for any exponents e_τ, the polynomials b_i · ∏_τ
det(y_τ)^{e_τ}, with b_i the basis minor products for κ, are linearly independent over R. 

### `GL.coord_mem_of_coeff_mem`

 If all coefficients of a combination of the basis products times `detPow R n e` lie in an
additive subgroup `A` of `R`, then so do the coordinates of the combination.

A consequence of the standard basis theorem for products of minors, stated for membership in an
additive subgroup A and with a determinant-power factor. 

 ### Characterisation of Schur matrices and diagonal matrices 

### `FitsRanks.refl`

 A family of row types fits itself: no height lies strictly between |n_τ| and |n_τ|. 

### `schurDetExp_self`

 For equal row families no extra power of the determinants occurs. 

### `GL.schur_eq_of_expansion`

 Let M be a matrix whose row i gives coordinates of b'_i(zy) in the family
b_j(y)·∏_τ det(y_τ)^{d_τ}, with b, b' the basis products `New.nablaBasis` for the rows n and n' and
d = `New.schurDetExp`. Then M is the Schur matrix S_κ(z): the family is linearly independent, so
these coordinates are unique. 

### `schur_diagonal_eq_prod`

 The Schur matrix of diagonal matrices diag(x_τ) is diagonal; its entry at i is the product of
x_τ over all entries of the fillings i_τ. 

### `weyl_character`

 Weyl's character formula over ℂ, for polynomial weights and with the Vandermonde denominator
cleared. Let e_τ enumerate the a_τ rows at each place τ, let x_τ be complex numbers indexed by these
rows, and let λ = `New.diagramWeight`, so λ(τ, k) = Σ_{k<h<|n_τ|} κ_τ(h). The trace of the Schur
matrix `schur κ` of the diagonal matrices diag(x_τ), times the product over τ of the Vandermonde
determinants of x_τ ∘ e_τ, is the product over τ of the determinants of the matrices with (i, j)
entry x_τ(e_τ(i))^{λ(τ, a_τ − 1 − j) + j}. 

### `schur_one`

 The Schur matrix of a family of identity matrices is the identity matrix. 

### `schur_diagonal`

 The Schur matrix of a tuple of diagonal matrices diag(x_τ) is diagonal, with i-th entry ∏_τ
∏_a x_τ(a)^{w}, where w is the number of entries equal to a in the filling i_τ. 

 ### Base change and multiplicativity 

### `GL.diagramWeight_eq_of_fitsRanks`

 If the sizes fit κ, the weight of κ in the larger ranks is its weight in the smaller ranks plus
that of the power `schurDetExp n n' κ` of the determinants. 

### `sum_schur_smul_nablaBasis`

 Assume `FitsRanks n n' κ`: for every τ, |n_τ| ≤ |n'_τ| and κ_τ(h) = 0 for |n_τ| < h < |n'_τ|.
Let b = `nablaBasis` for `n`, b' = `nablaBasis` for `n'`, and let d τ be κ_τ(|n_τ|) if
|n_τ| < |n'_τ| and 0 otherwise. Then for matrices z_τ of size n'_τ × n_τ, row `i` of the Schur
matrix `schur κ z` expresses b'_i(zy) as Σ_j S_{ij} b_j(y) ∏_τ det(y_τ)^{d τ}, where
y_{(τ,b),k} ↦ Σ_a z_τ(b,a) y_{(τ,a),k} defines zy and y_τ is the block of rows (τ, ·) and the first
|n_τ| columns. 

### `schur_map`

 Base change: assume `FitsRanks n n' κ`, that is, for every τ, |n_τ| ≤ |n'_τ| and κ_τ(h) = 0 for
|n_τ| < h < |n'_τ|. Then for a ring homomorphism φ, the Schur matrix of φ(z) (φ applied entrywise)
is φ applied entrywise to the Schur matrix S_κ(z). Here S_κ(z) = `schur κ z` has as row i the
coordinates of b'_i(zy) in the family b_j(y) ∏_τ det(y_τ)^{d τ}, where b and b' are the `nablaBasis`
for `n` and `n'`, and d = `schurDetExp n n' κ`. 

### `map_schur`

 Entrywise form of `New.schur_map`: φ applied to an entry of S_κ(z) is the same entry of the
Schur matrix of the matrices with entries φ(z_τ(a, b)). 

### `schur_mul_left`

 Assume `FitsRanks n n' κ`: at every place τ, |n_τ| ≤ |n'_τ| and κ_τ(h) = 0 for
|n_τ| < h < |n'_τ|. Let S_κ(z) = `schur κ z` be the matrix whose row i holds the coordinates of
b'_i(z y) in the family b_j(y)·∏_τ det(y_τ)^{d_τ}, where b and b' are `nablaBasis` for n and n', and
d is `schurDetExp`. Then S_κ(g z) = S_κ(g) S_κ(z) for square matrices g_τ of size n'_τ and matrices
z_τ of size n'_τ × n_τ over R. 

### `schur_mul_right`

 Assume `FitsRanks n n' κ`: at every place τ, |n_τ| ≤ |n'_τ| and κ_τ(h) = 0 for
|n_τ| < h < |n'_τ|. Let S_κ(z) = `schur κ z` be the matrix whose row i holds the coordinates of
b'_i(z y) in the family b_j(y)·∏_τ det(y_τ)^{d_τ}, where b and b' are `nablaBasis` for n and n', and
d_τ = `schurDetExp n n' κ τ` is κ_τ(|n_τ|) if |n_τ| < |n'_τ| and 0 otherwise. Then S_κ(z g) = ∏_τ
det(g_τ)^{d_τ} · S_κ(z) S_κ(g) for z_τ of size n'_τ × n_τ and square g_τ of size n_τ over R. 

### `schurDetExp_unit_eq`

 The determinant exponent of the one-place families with the data at τ is that at τ. 

### `schur_apply_eq_prod`

 Assume `FitsRanks n n' κ`: at every place τ, |n_τ| ≤ |n'_τ| and κ_τ(h) = 0 for
|n_τ| < h < |n'_τ|. For matrices z_τ of size n'_τ × n_τ, row i of the Schur matrix `schur κ z` holds
the coordinates of b'_i(z y) in the family b_j(y)·∏_τ det(y_τ)^{d_τ}, where b and b' are
`nablaBasis` for n and n', and d is `schurDetExp n n' κ`. Its (i, j) entry equals the product over τ
of the (i τ, j τ) entries of the one-place Schur matrices, namely those of the families over `Unit`
with data κ τ and z τ. 

### `schur_smul`

 If the sizes fit κ, scaling z_τ by t_τ scales S_κ(z) by the product of the t_τ^{|κ_τ|}, where
|κ_τ| = Σ_{h < |n'_τ|} h κ_τ(h) is the number of boxes at τ. 

 ## Schur representations twisted by determinants 

### `New.weylRep`

 The action on the Weyl module of a dominant weight μ, given as (κ, e): κ_τ(h) = μ_h − μ_{h+1} is
the number of columns of height h < |n_τ| at the place τ, and the integer e_τ is the last entry of
μ_τ. The monoid homomorphism sends a family g of invertible matrices g_τ ∈ GL(n_τ, R) to ∏_τ
det(g_τ)^{e_τ} times the Schur matrix S_κ(g). 


## Weights of the basis, evaluation vectors, the highest basis vector, one-row shapes

Weights of the standard basis b_i = `New.nablaBasis` of the module ∇ = `New.nablaFamily`.

* `New.sum_tableauWeight_le`: the weight of each b_i is dominated by the partition
  λ = `New.diagramWeight`.
* `New.schur_mulVec_weylEval`: the Schur matrix of z carries the vector of values b_j(y)
  (`New.weylEval`) to the vector of values at zy, up to a power of determinants of y.
* `New.map_nablaBasis_eq_map_weylKernel_mul_weylEval`: a linear form that sees only basis vectors of
  highest weight is determined by its value on the kernel `New.weylKernel`.


### `tableau_col_injective`

 Let i be a family of chosen standard fillings (`New.WeylIndexFamily`). At a place τ, the column
j of height h of the filling i_τ is an h-tuple of rows; its entries are distinct. 

### `sum_tableauWeight`

 Let i be a family of chosen standard fillings (`New.WeylIndexFamily`) and τ a place. The number
`New.tableauWeight i τ a` of entries of i_τ equal to the row a, summed over all rows a, is the
number of boxes Σ_{h<|n_τ|} h·κ_τ(h). 

### `sum_tableauWeight_le`

 Let i be a family of chosen standard fillings (`New.WeylIndexFamily`) and A a set of rows at the
place τ. Write λ = `New.diagramWeight`, so λ(τ,k) = Σ_{k<h<|n_τ|} κ_τ(h).
(a) The number of entries of i_τ lying in A (counted by `New.tableauWeight`) is at most
Σ_{k<|A|} λ(τ,k).
(b) If equality holds, every entry of a column of height h ≤ |A| lies in A. 

### `GL.eval_rowSubst`

 Let z_τ be matrices of size n'_τ×n_τ, y an array over R with rows (τ, a), and f a polynomial
in an array with rows (τ, b). Then `New.rowSubst z f` evaluated at y is f evaluated at the product
array zy, whose entry at row (τ, b) and column k is Σ_a z_τ(b,a)·y((τ,a),k). 

### `schur_mulVec_weylEval`

 Assume `FitsRanks n n' κ`: for every τ, |n_τ| ≤ |n'_τ| and κ_τ(h) = 0 for |n_τ| < h < |n'_τ|.
Let z_τ be matrices of size n'_τ × n_τ, let y be an array with rows (τ, a), and let zy be the array
with entries (zy)_{(τ,b),k} = Σ_a z_τ(b,a) y_{(τ,a),k}. Write ev_y for the vector of values b_j(y)
of the basis products of minors `nablaBasis` (`weylEval`) and d τ = κ_τ(|n_τ|) if |n_τ| < |n'_τ|,
else 0. Then ∏_τ det(y_τ)^{d τ} · S_κ(z) ev_y = ev_{zy}, where y_τ is the square block of the first
|n_τ| columns of y at τ and S_κ(z) = `schur κ z` is the matrix expressing each b'_i(zy) in the
b_j(y) ∏_τ det(y_τ)^{d τ}. 

### `schur_mulVec_weylEval_of_schurDetExp_eq_zero`

 Suppose the sizes fit κ (`New.FitsRanks`) and the determinant exponents `New.schurDetExp` are
all zero. Then the Schur matrix S_κ(z) carries the evaluation vector `New.weylEval` at y to the
evaluation vector at the product array zy. 

### `weylKernel_mem_nablaFamily`

 For every array y over R with rows (τ, a), the kernel `New.weylKernel` at y lies in the module
∇ = `New.nablaFamily` of Borel semi-invariants: it is a substitution of the product of leading
minors `New.highestPoly`. 

### `GL.eval_weylKernel_permArray`

 Let e_τ enumerate the rows at each place τ, and let y be the permutation array of e
(`New.permArray`): y((τ,a),k) is 1 if e_τ(a) = k and 0 otherwise. The kernel `New.weylKernel` at
y, evaluated at y, equals 1. 

### `nablaBasis_eq_weylEval_smul_weylKernel_of_lt`

 Let e_τ enumerate the rows at each place τ, and let y be the permutation array of e
(`New.permArray`). Let i be a family of chosen standard fillings (`New.WeylIndexFamily`) in which
every entry of a column of height k of i_τ has position below k in the enumeration e_τ. Then the
basis vector b_i = `New.nablaBasis` is its value b_i(y) (`New.weylEval`) times the kernel
`New.weylKernel` at y. 

### `weylEval_permArray_eq_zero_of_le`

 Let e_τ enumerate the rows at each place τ, and let y be the permutation array of e
(`New.permArray`). If, for a family i of chosen standard fillings, some entry of a column of height
k of i_τ has position at least k in the enumeration e_τ, then the value b_i(y) of the basis vector
(`New.weylEval`) is zero. 

### `map_nablaBasis_eq_map_weylKernel_mul_weylEval`

 Let e_τ enumerate the rows at each place τ, let i be a family of chosen standard fillings
(`New.WeylIndexFamily`) with basis vector b_i = `New.nablaBasis`, and let φ be an R-linear form on
polynomials. Suppose that φ(b_i) ≠ 0 only when, at each row (τ, a), the number of entries of i_τ
equal to a (`New.tableauWeight`) is at least λ(τ, e_τ(a)), where λ = `New.diagramWeight`. Then
φ(b_i) = φ(k)·b_i(y), where y is the permutation array of e (`New.permArray`), k is the kernel
`New.weylKernel` at y, and b_i(y) = `New.weylEval`. 

### `exists_equiv_schur_one_row_eq_symPowMatrix`

 One place (Φ = Unit) with a row type m of size |m| > 1, and column multiplicities k with
k(1) = a and k(h) = 0 for 1 < h < |m|: the shape is one row of length a. `New.WeylIndexFamily`
indexes the basis `nablaBasis` b, and S_k(z) (`New.schur`) is the matrix whose row i holds chosen
coordinates of b_i(z y) in the family b_j(y)·det(y)^d. Let q : σ ≃ m be a bijection. Then there is a
bijection φ from these basis indices to the exponents of degree a in σ (`New.Monomials`) such that,
for all complex c and square z, c^a·S_k(z)_{ij} is the (φ j, φ i) entry of the a-th symmetric power
`New.symPowMatrix` of c·zᵀ reindexed along q. 

 ## Continuity of Schur matrices 

### `New.continuous_schur`

 Over a topological ring R, the Schur matrix S_κ(g) = `New.schur κ g` of a family g of square
matrices g_τ of size n_τ is continuous in g: by base change (`New.schur_map`) each of its entries is
a polynomial in the entries of g. 
