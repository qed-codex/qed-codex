---
{
  "module": "src/Lib/GLn/SchurModule/MinorBasis.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/SchurModule/MinorBasis.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/SchurModule/MinorBasis.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A basis of minor products for Borel semi-invariants over any ring, by induction on rows

Polynomials are in variables `X (a, i)`, where `a` is a row with colour `c a` and `i : ℕ` is a
column (`New.MatrixPoly`). For finitely many rows and `l = New.GL.columnWeight τ h`, the module
`New.nabla R c l` of Borel semi-invariants has a basis of products of minors that does not depend on
the ring `R`. The proof takes leading terms in one row: bordering lifts a family of minor products,
and a leading-term analysis describes the leading term of a semi-invariant.

## Main definitions and results

* `New.GL.HasLeadingTerm F γ G`: `F` is `G` times the monomial of exponent `γ` plus smaller terms;
  `New.GL.rowExpansion x` expands in row `x`.
* `New.GL.columnWeight`, `New.GL.ColouredTableau`, `New.GL.minorProduct`: the weight of a family of
  coloured columns, its fillings by rows, and the product of the minors of a filling.
* `New.GL.interlacing l`: the exponents `γ` with `γ i ≤ l i - l (i + 1)` (truncated subtraction).
  For antitone `l`, these are the `γ ≤ l` such that `l - γ` interlaces `l`.
* `New.GL.exists_bordering`: a filling that avoids `x` is lifted to one whose product of minors has,
  in the variables of row `x`, leading term `X ^ γ` times the old product.
* `New.GL.degree_rowExpansion_mem_interlacing`: the leading exponent of a Borel semi-invariant in
  the variables of one row `x` lies in `New.GL.interlacing` of its weight at the colour of `x`.
* `New.GL.HasLeadingTerm.leadingCoeff_mem_nabla`: the leading coefficient of a semi-invariant in row
  `x` is a semi-invariant in the other rows, of the weight lowered by that exponent.
* `New.GL.exists_isStdMinorFamily`: some finite family of fillings has products of minors that are
  linearly independent and span the semi-invariants of its weight over every ring, recorded as
  `New.GL.IsStdMinorFamily`.

Notions from other files:
* `New.nabla`: For a row colouring c and weight l, the module of Borel semi-invariants: polynomials
  f with f(yβ) = ∏β_{τ,ii}^{l(τ,i)} f(y) for generic upper triangular matrices β_τ, one per colour.
* `New.minor`: For an h-tuple I of rows, the polynomial determinant of the h×h matrix of variables
  in rows I and the first h columns.
* `New.GL.alternant`: For x in ℂ^N and l : ℕ → ℕ, the alternant det(x_i^{l(N−1−j)+j}), 0 ≤ i, j < N,
  if l(N) = 0, and zero otherwise.

## Relation to the literature

Known result: The standard basis theorem for Schur (dual Weyl) modules over any ring, with their
character. Here the module is the space of polynomials on matrices that are semi-invariant under a
triangular group, for several row colours at once. It lies in the span of a set of products of
minors built one row at a time rather than the semistandard tableaux, and this set is linearly
independent over every ring. For a single colour its character is given by Weyl's quotient of
alternants. Source: De Concini, Eisenbud, Procesi, Young diagrams and determinantal varieties,
Invent. Math. 56 (1980); Akin, Buchsbaum, Weyman, Schur functors and Schur complexes, Adv. Math. 44
(1982), II.2.16, II.4.11.

See also `Lib.DiscreteSeries.Character.WeylCharacterFormula`.


 ## Leading terms of products of minors and bordering 

 ### Leading terms 

### `columnOrder`

 The lexicographic monomial order on variables indexed by ℕ that compares exponents at the
highest index first, so that x₀ ≺ x₁ ≺ …. 

### `columnOrder_lt_of_eq_above`

 If the exponents `γ` and `δ` agree in the columns beyond `i` and `γ i < δ i`, then `γ` is
below `δ` in `New.GL.columnOrder`. 

### `HasLeadingTerm`

 No monomial of F exceeds x^γ in the order `New.GL.columnOrder`, and the coefficient of x^γ in F
is G (G = 0 is allowed). 

### `HasLeadingTerm.degree_le`

 If `F` has leading term `a * x ^ γ`, then no monomial of `F` exceeds `x ^ γ`. 

### `HasLeadingTerm.mul`

 Leading terms multiply: if `F` has leading term `a * x ^ γ` and `F'` has leading term
`a' * x ^ γ'`, then `F * F'` has leading term `(a * a') * x ^ (γ + γ')`. 

### `HasLeadingTerm.prod`

 Leading terms of finite products: if each `F i` has leading term `G i * x ^ δ i`, then the
product of the `F i` over `t` has leading term `(∏ G i) * x ^ (∑ δ i)`. 

### `HasLeadingTerm.sum`

 Let each `F i` have leading term `G i * x ^ δ i`. If `δ j` exceeds every other exponent `δ i`
with `i ∈ t`, then the sum of the `F i` over `t` has leading term `G j * x ^ δ j`. The index `j`
may lie outside `t` when `G j = 0`. 

### `HasLeadingTerm.finsuppProd_pow`

 If each `u j` has leading term `b j` times the variable `x j` (exponent `single j 1`),
then the product of the powers `u j ^ n j` has leading term `∏ b j ^ n j` times the monomial of
exponent `n`. 

 ### Columns, fillings and products of minors 

### `rowExpansion`

 For a row x, the R-algebra isomorphism writing a polynomial in the y_{a,i} as a polynomial
in the y_{x,i}, i ∈ ℕ, over the polynomials in the other rows. 

### `interlacing`

 The finite set of the `γ` with `γ i ≤ l i - l (i + 1)` (truncated subtraction) for all `i`. For
antitone `l` these are the `γ ≤ l` such that `μ = l - γ` interlaces `l`: `l (i + 1) ≤ μ i ≤ l i`. 

### `columnWeight`

 For finitely many columns j with colour τ_j and height h_j, the weight whose value at (τ,i)
counts the columns of colour τ with height exceeding i. 

### `ColouredTableau`

 The type of assignments giving each column j an h_j-tuple of rows, all of colour τ_j. 

### `minorProduct`

 For a coloured column filling I, the polynomial over S that is the product over columns j of
the minor with rows I_j on the first h_j columns. 

### `diagramWeight_eq_columnWeight`

 The weight `New.diagramWeight N κ` equals the weight `New.GL.columnWeight` of the family having
`κ τ h` columns of colour `τ` and height `h`, for every `τ` and `h < N τ`: its columns are the
triples `⟨τ, h, j⟩` with `j < κ τ h`, of colour `τ` and height `h`. 

### `minorProduct_mem_nabla`

 For an assignment I of h_j rows of colour τ_j to each column j, the product of minors
`New.GL.minorProduct` of I is a Borel semi-invariant: it lies in `New.nabla` for the weight
`New.GL.columnWeight` of τ, h. 

### `hasLeadingTerm_rowExpansion_minor_border`

 Bordering one minor: take a tuple `I` of `k` rows other than `x` and append the row `x` if
`e = 1`. After `New.GL.rowExpansion x`, the new minor has leading term `X k ^ e` times the old
minor, where `X k` is the variable of row `x` in column `k`. 

### `exists_bordering`

 Bordering. Let `γ` lie in `interlacing` of the weight `l` of the columns at the colour of the
row `x`, that is `γ i ≤ l i - l (i + 1)` for all `i`, so `γ` is the amount by which `l` is lowered
to an interlacing weight. Then (a) there are heights `k` whose column weight is that of `h` minus
`γ` placed in colour `c x`. For every filling `I` of heights `k` by rows other than `x` there is a
filling `K` of heights `h` such that (b) over every commutative ring `R`, the expansion of
`minorProduct R K` in the variables of row `x` has no monomial above the one of exponent `γ` in
`columnOrder`, and the coefficient of that monomial is `minorProduct R I`, and (c) the entries of
`K` are those of `I` together with `degree γ` copies of `x`. 

 ### The recursion for alternants 

### `_root_.Matrix.det_pow_eq_det_sub_mul_geom_sum`

 Column reduction for a matrix of powers. Let `p` be a monotone family of exponents and `i` a
row. Subtracting from each column `j + 1` the power `x i ^ (p (j + 1) - p j)` times column `j`
keeps the determinant of `(x a ^ p j)`, and turns the entry `x a ^ p (j + 1)` into `x a - x i`
times the sum of `x a ^ k * x i ^ (p (j + 1) - 1 - k)` over `p j ≤ k < p (j + 1)`. 

### `alternant_succ`

 The branching rule for alternants. Here `alternant x l` for `x : Fin (N + 1) → ℂ` is
`det (x a ^ (l (N - j) + j))` over `0 ≤ a, j ≤ N`, or zero if `l (N + 1) ≠ 0`, and `interlacing l`
is the set of `γ` with `γ k ≤ l k - l (k + 1)` for all `k`, so that `l - γ` interlaces `l`. For
antitone `l` and an index `i`, the alternant of `l` is `(-1) ^ i * ∏ a ≠ i, (x a - x i)` times the
sum, over `γ ∈ interlacing l`, of `x i ^ |γ|` times the alternant of `l - γ` in the other `N`
variables. 


## The leading term of a semi-invariant in one row

Throughout, `f` is a Borel semi-invariant and `G * X_x ^ γ` is its leading term in the variables
`X (x, i)` of one row `x`, where `X_x ^ γ` is the monomial of exponent `γ` in these variables.


### `MvPolynomial.aevalTower_apply`

 The map `aevalTower g y` is `eval₂` with the coefficient map `g`. 

### `columnOrder_lt_of_forall_add_ite_eq`

 Let the exponents `n` and `γ` agree outside the columns `i` and `i + 1` and have the same sum
`n i + n (i + 1) = γ i + γ (i + 1)`, in the pointwise form that a comparison of coefficients
gives. If `n i ≤ γ i` and `n ≠ γ`, then `γ` is below `n` for `columnOrder`. 

### `degree_rowExpansion_mem_interlacing`

 Let `f` be a Borel semi-invariant of weight `l` for the row colouring `c` (`f ∈ nabla R c l`),
and let `γ` be the leading exponent of `f` in the variables `X (x, i)` of the row `x`, for the order
`columnOrder` (which compares the highest column first). Then `γ i ≤ l (c x, i) - l (c x, i + 1)`
for every column `i`, with truncated subtraction: `γ` lies in `interlacing` of the weight at the
colour of `x`. 

### `HasLeadingTerm.leadingCoeff_mem_nabla`

 Let `γ` be the leading exponent of `f` in the variables of the row `x` (for `columnOrder`, the
lexicographic order that compares exponents at the highest column first), and let `f` be a Borel
semi-invariant of weight `γ + l`, where `γ` is placed at the colour `c x` (`γ.mapDomain (c x, ·)`).
Then the leading coefficient `G` of `f` in the row `x`, a polynomial in the other rows, is a Borel
semi-invariant of weight `l` for the colouring `c` restricted to the rows other than `x`. 


## The basis theorem and the character identity

The proof of `New.GL.exists_isStdMinorFamily` is an induction on the number of rows by leading
terms in one row.


### `IsStdMinorFamily`

 A standard family of fillings `I` for rows coloured by `c` and columns `j` of colour `τ j` and
height `h j`: each `I i` (a `ColouredTableau`) gives column `j` an `h j`-tuple of rows of colour
`τ j`; `minorProduct R (I i)` is the product of the minors on these rows and the first `h j`
columns. 

### `IsStdMinorFamily.linearIndependent`

 Over every commutative ring the products of minors are linearly independent. 

### `IsStdMinorFamily.nabla_le_span`

 Over every commutative ring the span of the products of minors contains the
  semi-invariants of weight `columnWeight τ h`. 

### `IsStdMinorFamily.character`

 If `t` is the only colour and `e` enumerates the rows, then the sum over the fillings of the
  products of the `x a` over their entries `a`, times the alternant of the zero weight, is the
  alternant of the weight `columnWeight τ h (t, ·)`. 

### `HasLeadingTerm.rowExpansion_combination`

 If `p i` has leading term `q i` times the monomial of exponent `γ` in the row `y` for every `i`,
then a combination of the `p i` has as leading term the same combination of the `q i`, times that
monomial. Here `HasLeadingTerm F γ G` says that no exponent of `F` exceeds `γ` for `columnOrder`
(lexicographic, comparing exponents at the highest column first) and that the coefficient of the
monomial of exponent `γ` is `G`; `rowExpansion y` writes a polynomial as one in the variables of the
row `y` over the polynomials in the other rows. 

### `linearIndependent_of_hasLeadingTerm`

 Polynomials `p γ i` with leading terms `q γ i` times the monomial of exponent `γ` in the row
`y` (`HasLeadingTerm`), for distinct exponents `γ` from a finite set `Γ`, are linearly independent
if for each exponent `γ` the coefficients `q γ i` are. 

### `nabla_le_span_of_hasLeadingTerm`

 Let `γ` run over the exponents interlacing the weight `l` at the colour of the row `y`, and let
`l' γ` be `l` lowered by `γ`. Borel semi-invariants (`nabla`) `p γ i` of weight `l` with leading
terms `q γ i` times the monomial of exponent `γ` in the row `y` span all semi-invariants of weight
`l`, if for each `γ` the span of the `q γ i` contains the semi-invariants of weight `l' γ` in the
other rows. 

### `antitone_columnWeight_curry`

 At each colour `t` the number of columns of height above `k` does not increase with `k`. 

### `exists_isStdMinorFamily_of_isEmpty`

 Rows `m` are coloured by `c`; column `j : J` has colour `τ j` and height `h j`, and a
`ColouredTableau c τ h` gives it an `h j`-tuple of rows of colour `τ j`. With no rows there is a
standard family (`IsStdMinorFamily`) of these: the one empty filling if all heights are zero, and
the empty family otherwise. 

### `exists_isStdMinorFamily`

 Take finitely many rows coloured by `c`, and finitely many columns `j` of colour `τ j` and
height `h j`. Then there is a finite type `ι` and a family `I` of fillings indexed by it that is
standard in the sense of `IsStdMinorFamily`. Each `I i` gives column `j` an `h j`-tuple of rows of
colour `τ j`, and has minor product `minorProduct R (I i)`: the product of the minors on these rows
and the first `h j` columns.

This is an existence form of the standard basis theorem for Schur modules (Akin–Buchsbaum–Weyman),
stated for products of minors with coloured rows; the index type is not identified with the
semistandard tableaux. 
