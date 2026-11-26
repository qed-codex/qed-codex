---
{
  "module": "src/Lib/DiscreteSeries/Theta/FockDualPair.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Theta/FockDualPair.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Theta/FockDualPair.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fock space oscillator actions, joint harmonics and Fischer decomposition

This file treats polynomials in the variables of `T : New.FockDualPair`, indexed by rows `r : R` and
columns `c : C`. It defines the oscillator action `New.FockDualPair.oscRows` of `gl R` on the rows.
It also defines matched parameters and joint harmonics for the theta correspondence of
`U(ε) × U(ε')`, and proves that these notions are symmetric under `New.FockDualPair.swap`. A
Fischer-type analysis of orthogonal complements in bounded degree gives criteria for the Laplacians
to vanish.

## Main definitions and results

* `New.FockDualPair`, `New.FockDualPair.swap`: the data of the dual pair, and the data with
  `globalSign` negated and rows and columns exchanged.
* `New.FockDualPair.oscRows`: the action of `gl R` on the rows. The action of `gl C` on the columns
  is `oscRows` of `swap`, and its matrix units are given by `New.FockDualPair.swap_oscRows_E`.
* `New.FockDualPair.IsMatchedPair`, `New.IsMatch`: when the parameters `l = 2λ` and `l' = 2λ'`
  correspond.
* `New.FockDualPair.IsTermwiseHarmonic`, `New.IsJointHarmonic`: termwise harmonic polynomials, and
  joint harmonics that are highest for the lowest `K`-types `l.lowestKType` and `l'.lowestKType`.
  The signs `ε` and `ε'` are carried by the types of `l` and `l'`.
* `New.Fischer.fockLaplacian_eq_zero`, `New.Fischer.isLaplaceHarmonic_of_isKHighest`: criteria for
  the Laplacians `New.FockDualPair.fockLaplacian` to vanish.

Notions from other files:
* `New.HCParam.HasGap`: `l.HasGap h` says that the entries of `l = 2λ` are distinct and congruent to
  `n − 1` mod 2, where `n` is their number, and `|λ_i − λ_j| ≥ h` whenever `ε_i ≠ ε_j`.
* `New.HCParam.IsKHighest`: `x` is a `K`-highest vector of weight `ν`: each `E a a` acts on it by
  `ν a`, and it is killed by the compact raising operators, the `E a b` with `ε a = ε b` and
  `l b < l a`. The second condition alone is `New.GlModule.IsCompactPrimitive`.
* `New.HCParam.lowestKType`: for a parameter `l = 2λ`, the integer vector `λ + ρ − 2ρ_c`, which is
  the highest weight of the lowest `K`-type.
* `New.fockPairing`: the bilinear form `⟨P, Q⟩ = P(∂)Q(0)` on polynomials, for which monomials are
  orthogonal and `⟨x^d, x^d⟩ = d!`.

## Relation to the literature

Known; see `Lib.DiscreteSeries.Theta.LocalCorrespondence` for sources.



## Oscillator actions, matched parameters and joint harmonics

`New.Fock.glOp η a b` is `raiseOp η a * lowerOp η b`, and `New.Fock.raiseOp η a` and
`New.Fock.lowerOp η a` are `X a` and `∂ a` if `η a = 1`, and `-∂ a` and `X a` otherwise.


### `Fock.raiseOp_comm`

 The raising operators of the Fock model for the signs `η` commute: `raiseOp η a` is
multiplication by `X a` if `η a = 1` and `-∂ a` otherwise. 

### `Fock.lowerOp_comm`

 The lowering operators of the Fock model for the signs `η` commute: `lowerOp η a` is `∂ a` if
`η a = 1` and multiplication by `X a` otherwise. 

### `Fock.lowerOp_raiseOp`

 The commutator of the lowering operator `lowerOp η a` (`∂ a` or `X a`, by the sign `η a`) with
the raising operator `raiseOp η b` (`X b` or `-∂ b`) is the identity if `a = b`, and zero if not. 

### `Fock.canonical_commutation`

 The canonical commutation relations of the Fock model for the signs `η`: raising operators
commute, lowering operators commute, and the commutator of `lowerOp η a` with `raiseOp η b` is
`δ_ab`. 

 ### Dual pair data and signs of the variables 

### `pairSign`

 The sign `σ * ε r * ε' c` of the variable in row `r` and column `c`, where `i = (r, c)`. 

### `FockDualPair`

 The data of a dual pair in Fock space for the signs `ε`, `ε'`: a sign `σ` (`globalSign`), two
integers `γ` (`rowShift`) and `γ'` (`columnShift`), and a bijection from `R × C` to the index set
`ι` of the variables. 

### `FockDualPair.globalSign`

 The sign `σ`, a factor of the sign `σ * ε r * ε' c` of each variable. 

### `FockDualPair.rowShift`

 The constant `γ` added to the diagonal matrix units of the row action `oscRows`. 

### `FockDualPair.columnShift`

 The constant `γ'` added to the diagonal matrix units of the column action. 

### `FockDualPair.varEquiv`

 The bijection that names the variable of row `r` and column `c`. 

### `FockDualPair.std`

 The dual pair data with sign `σ = 1`, integers `γ` and `γ' + card R`, and variables indexed by
`R × C` itself. Then `E a b` acts on the rows by `∑ c, raiseOp (a, c) * lowerOp (b, c) + γ δ_ab` and
on the columns by `-∑ r, raiseOp (r, b) * lowerOp (r, a) + γ' δ_ab`. 

### `swap`

 The data with rows and columns exchanged: the sign `-σ`, the integers `γ'` and `γ` in this
order, and the variable of `(c, r)` named as that of `(r, c)`. 

### `varSign`

 The sign `σ * ε r * ε' c` of the variable in row `r` and column `c`. 

### `indexSign`

 The signs of the variables as a function on `ι`: the variable `T.varEquiv (r, c)` has the sign
`σ * ε r * ε' c`. 

 ### Vacuum weight, the row action, Laplacians and polarisation 

### `vacuumWeight`

 The weight of the vacuum (the constant polynomial `1`) at a row of sign `s` for the action
`New.FockDualPair.oscRows`: `γ` minus the number of columns `c` with `σ * s * ε' c ≠ 1`. Each such
column contributes `-∂ (X * 1) = -1` to `E r r 1`. 

### `relWeight`

 The entry in row `r` of the lowest `K`-type for `l = 2λ`, minus the weight of the vacuum on a
row of sign `ε r`. 

### `centredParam`

 The integer `l r - 2γ + card C`; for `l = 2λ` it is twice the centred parameter
`λ r - γ + card C / 2`. 

### `_root_.New.Fock.glOp_commutator`

 The operators `glOp η i j = raiseOp η i * lowerOp η j` satisfy the commutation rule
`[E i j, E k m] = δ_jk E i m - δ_im E k j` of the matrix units. Here `raiseOp η i` and `lowerOp η i`
are `X i` and `∂ i` if the sign `η i` is `1`, and `-∂ i` and `X i` otherwise. 

### `_root_.New.Fock.glOp_neg`

 Reversing all signs exchanges raising and lowering operators up to sign, so
`glOp (-η) i j = raiseOp (-η) i * lowerOp (-η) j` is `∓ lowerOp η i * raiseOp η j`, with the minus
sign when `η i = η j`. Here `raiseOp η i` and `lowerOp η i` are `X i` and `∂ i` if `η i = 1`, and
`-∂ i` and `X i` otherwise. 

### `oscRowsUnit`

 The operator by which the matrix unit `E a b` of `gl R` acts on the rows of the variables
`varEquiv (r, c)`: it is `s • ∑ c, glOp η (varEquiv (a, c)) (varEquiv (b, c)) + γ δ_ab`, where
`s = 1` if `ε a = ε b` and `s = σ` otherwise. 

### `sum_glOp_commutator`

 The sums over the columns `x` of the operators `glOp` between the variables `(a, x)` and
`(b, x)` satisfy the commutation rule of the matrix units `E a b` of `gl R`. Here `T.varEquiv` names
the variables, `T.indexSign` gives their signs, and `glOp η i j` raises in `i` after lowering in
`j`. 

### `_root_.New.ite_units_eq_mul_ite_units_eq`

 For a sign `σ`, the factor that is `1` if `s = t` and `σ` if not is multiplicative along three
signs `s`, `t`, `u`. 

### `oscRowsUnit_commutator`

 The operators `oscRowsUnit a b`, by which the matrix units of `gl R` act on the rows, satisfy
the commutation rule `[E a b, E c d] = δ_bc E a d - δ_ad E c b`. 

### `_root_.New.single_mul_single_sub_single_mul_single`

 The commutation rule `[x E a b, y E c d] = x y (δ_bc E a d - δ_ad E c b)` for multiples of two
matrix units in `Matrix R R ℂ`. 

### `oscRows`

 The oscillator action of `gl R` on the rows of the variables `varEquiv (r, c)`: the linear
map that sends the matrix unit `E a b` to `oscRowsUnit a b`. For `σ = -1` its noncompact part
changes sign. 

### `fockLaplacian`

 The operator `∑ c, glOp (a, c) (b, c)` over the columns `c` where `(a, c)` has sign `-1`. For
`ε a ≠ ε b` it is the Laplacian `-∑ c, ∂_{a c} ∂_{b c}`: up to the factor `σ`, the part of the
matrix unit `E a b` of `New.FockDualPair.oscRows` that lowers the degree. 

### `polarisation`

 The polarisation `∑ c, X_{a c} * ∂Φ/∂X_{b c}` of the polynomial `Φ`, summed over the columns `c`
where the variable `(b, c)` has sign `s`. 

 ### Matching parameters and joint harmonics 

### `IsMatchedPair`

 The row `r` is matched with the column `c`: with `n = card R`, `n' = card C` and
`a = l r - 2γ + n'`, one has `a = -(l' c - 2γ' + n)` and `|n - n'| < σ * ε r * ε' c * a`. 

### `IsTermwiseHarmonic`

 `∂_{a c} ∂_{b c} Φ = 0` whenever `ε a ≠ ε b`. This says that no monomial of `Φ` contains two
variables of one column `c` from rows of opposite signs. 

### `IsLaplaceHarmonic`

 `Φ` is killed by the Laplacians of the rows: for `ε a ≠ ε b`, the sum of `∂_{a c} ∂_{b c} Φ`
over the columns `c` where the variable `(a, c)` has sign `-1` is zero. 

### `IsPreJointHarmonic`

 `Φ` is not zero, killed by the compact raising operators of the columns (in the order of `l'`),
`K`-highest of weight `l.lowestKType` for the action on the rows, and killed by the Laplacians of
both sides. The last condition is weaker than `New.FockDualPair.IsTermwiseHarmonic` for both sides;
uniqueness is proved in this wider class, as Howe's argument needs it there. 

### `IsPreJointHarmonic.ne_zero`

 `Φ` is not zero. 

### `IsPreJointHarmonic.isCompactPrimitive_cols`

 The compact raising operators of the column action, in the order of `l'`, kill `Φ`. 

### `IsPreJointHarmonic.isLaplaceHarmonic`

 The Laplacians of the rows kill `Φ`. 

### `IsPreJointHarmonic.isKHighest_rows`

 `Φ` is `K`-highest for the row action, with the lowest `K`-type of `l` as weight. 

### `IsPreJointHarmonic.isLaplaceHarmonic_swap`

 The Laplacians of the columns kill `Φ`. 

### `IsJointHighest`

 `Φ` is not zero, termwise harmonic for both sides, and `K`-highest of weight `ν` for the action
on the rows and of weight `ν'` for the action on the columns. 

### `IsJointHighest.ne_zero`

 `Φ` is not zero. 

### `IsJointHighest.isKHighest_cols`

 `Φ` is `K`-highest of weight `ν'` for the column action, in the order of `l'`. 

### `IsJointHighest.isTermwiseHarmonic`

 No monomial of `Φ` contains two variables of one column from rows of opposite signs. 

### `IsJointHighest.isKHighest_rows`

 `Φ` is `K`-highest of weight `ν` for the row action, in the order of `l`. 

### `IsJointHighest.isTermwiseHarmonic_swap`

 No monomial of `Φ` contains two variables of one row from columns of opposite signs. 

### `swap_oscRows_E`

 For a dual pair `T` in Fock space, with sign `σ`, integers `γ` and `γ'`, and variables
`varEquiv (r, c)` indexed by rows `r : R` and columns `c : C`, the matrix unit `E a b` of `gl C`
acts on the columns by `s • (-∑ r, lowerOp η (varEquiv (r, a)) * raiseOp η (varEquiv (r, b))) + γ'
δ_ab`, where `s = 1` if `ε' a = ε' b` and `s = σ` otherwise. This column action is `T.swap.oscRows`,
the row action of the swapped pair, whose sign is `-σ`. Here `η` gives the signs of the variables,
`raiseOp η i` and `lowerOp η i` are `X i` and `∂ i` if `η i = 1` and `-∂ i` and `X i` otherwise, and
the integer `γ'` of the pair acts as a scalar. 

### `IsMatch`

 The parameters `l = 2λ`, `l' = 2λ'` match. With `n = card R` and `n' = card C`, both have gap
`500 (n + n')³`. Put `ξ r = λ r - γ + n' / 2` and `ξ' c = λ' c - γ' + n / 2`; a pair `(r, c)` is
matched if `ξ r = -ξ' c` and `σ * ε r * ε' c * ξ r > |n - n'| / 2`. Each row is matched or has
`|ξ r| < (n - n') / 2`, and each column is matched or has `|ξ' c| < (n' - n) / 2`. So the matched
entries are the common ones and the others form the block; `New.isBlockRule_iff_isMatch` proves that
this is the block rule. 

### `IsMatch.hasGap_row`

 The row parameter `l` has gap `500 (n + n')³`, where `n = card R` and `n' = card C`. 

### `IsMatch.hasGap_column`

 The column parameter `l'` has the same gap `500 (n' + n)³`. 

### `IsMatch.left`

 Every row `r` is matched with a column, or `|l r - 2γ + n'| < n - n'`. 

### `IsMatch.right`

 Every column `c` is matched with a row, or `|l' c - 2γ' + n| < n' - n`. 

### `IsJointHarmonic`

 `Φ` is a joint harmonic: `l` and `l'` match, and `Φ ≠ 0` is `K`-highest for the row and column
actions, of the weights of the two lowest `K`-types, and satisfies
`New.FockDualPair.IsTermwiseHarmonic` for `T` and for `T.swap`. 

### `IsJointHarmonic.isJointHighest`

 `Φ` is nonzero, termwise harmonic for both sides, and highest of weight `l.lowestKType` for
  the action on the rows and of weight `l'.lowestKType` for the action on the columns. 


## Swap symmetry, Laplacians and Fischer decomposition in Fock space

On polynomials `⟪P, Q⟫` is the Fischer inner product `fockPairing (conj P) Q`, for which `X i` is
adjoint to `∂_i`. For it, `New.Fischer.perpInDegree j G` is the orthogonal complement of `G` in
degree at most `j`.

* `New.Fischer.oscRows_E_eq_polarisation_sub`: the compact matrix units, expressed by polarisations
  and the vacuum weight `New.FockDualPair.vacuumWeight`.


### `FockDualPair.IsMatchedPair.swap`

 If row `r` is matched with column `c` for `T`, then `c` is matched with `r` for `T.swap`, the
data with rows and columns exchanged and the sign `σ` negated. 

### `IsMatch.swap`

 The matching of parameters is symmetric: if `l` and `l'` match for `T`, then `l'` and `l` match
for `T.swap`, the data with rows and columns exchanged and the sign `σ` negated. 

### `FockDualPair.IsJointHighest.swap`

 Let `P ≠ 0` be termwise harmonic for both sides, and `K`-highest of weight `ν` for the rows and
of weight `ν'` for the columns of `T`. Then it is so for `T.swap`, with the parameters `l`, `l'`
and the weights `ν`, `ν'` exchanged. 

### `IsJointHarmonic.swap`

 Let `T` be a dual pair in Fock space with sign `σ`. A joint harmonic `P` of `T` for `l`, `l'` is
a joint harmonic of `T.swap` for `l'`, `l`, where `T.swap` exchanges rows and columns, replaces `σ`
by `-σ` and swaps `γ`, `γ'`. Here a joint harmonic for matching parameters is a nonzero polynomial
that is `K`-highest of the lowest `K`-type weights for the row and column actions, and that has no
monomial with two variables of one column from rows of opposite signs, or of one row from columns of
opposite signs. 

### `oscRows_E_eq_polarisation_sub`

 For rows `a`, `b` of equal sign, the matrix unit `E a b` of the row action sends `P` to the
polarisation `∑ X_ac ∂_bc P` over the columns `c` where `(b, c)` has sign `1`, minus `∑ X_bc ∂_ac P`
over those where it has sign `-1`, plus `T.vacuumWeight (ε a)` (the weight by which `E a a` acts on
the constant `1`) times `P` if `a = b`. 

### `scoped instance : NormedAddCommGroup (MvPolynomial ι ℂ)`

 The inner product `⟪P, Q⟫ = fockPairing (conj P) Q` on polynomials, the Fischer inner product,
makes them a normed group. 

### `inner_X_mul`

 For the Fischer inner product on complex polynomials, multiplication by `X b` is adjoint to the
partial derivative `pderiv b`, on either side of the inner product. 

 ### Degree filtration and vanishing of the Laplacians 

### `polyDegreeLE`

 For an integer `j`, the space of complex polynomials of total degree at most `j` in variables
indexed by `ι`. 

### `X_mul_mem_polyDegreeLE`

 Multiplication by a variable raises the bound on the degree by one. 

### `pderiv_mem_polyDegreeLE`

 A partial derivative lowers the bound on the degree by one. 

### `glOp_mem_polyDegreeLE`

 If `P` has degree at most `j`, then `glOp η a b P` has degree at most every `i` with
`j + η a ≤ i + η b`. 

### `perpInDegree`

 The polynomials of degree at most `j` that are orthogonal, for the Fischer inner product, to
all elements of `G` of degree at most `j`. 

### `eq_zero_of_mem_perpInDegree`

 A polynomial of degree at most `j` that lies in `N` and is orthogonal to the elements of `N` of
degree at most `j` is zero. 

### `fockLaplacian_eq_zero`

 The inductive step in Fischer's argument. Let `G` contain all polynomials of degree
less than `j`, let `P` have degree at most `j` and be orthogonal to the part of `G` of degree at
most `j`, and let `ε a ≠ ε b`. Let `Q = fockLaplacian a b P`, the sum of the `-∂_ac ∂_bc P` over
the columns `c` where `(a, c)` has sign `-1`. If `Q ∈ G` implies `E b a Q ∈ G` for the row action,
then `Q = 0`. 

### `isLaplaceHarmonic_of_isKHighest`

 Let `P` be `K`-highest of weight `ν` for the action `T.oscRows` on rows: each `E r r` acts on it
by `ν r`, and the compact raising operators of `l` kill it. Suppose that no nonzero Laplacian
`T.fockLaplacian a b P` with `ε a ≠ ε b` is `K`-highest of weight
`ν + Pi.single a 1 - Pi.single b 1`. Then `P` is row harmonic: all these Laplacians are zero. The
reason is that they form a tensor operator, so an extremal nonzero one would be highest. 

### `mapsTo_perpInDegree`

 Let `ε a = ε b`. If the compact matrix unit `E b a` of the row action maps `N` into `G`, then
`E a b` maps `perpInDegree j G` (the orthogonal complement of `G` in degree at most `j`) into
`perpInDegree j N`. 
