---
{
  "module": "src/New/Derivatives/Divisibility/Count.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/Count.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/Count.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Divisibility of the jets of a series with the normal form along products of minors

* `New.norm_jet_le_of_isHomogeneous`: Legendre's bound for the jet of an integral series along a
  homogeneous integral polynomial.
* `New.minorProd`, `New.predictedDivisibility`: products of minors, and the divisibility predicted
  by their shape.
* `New.Parameters.norm_jet_minorProd_le_of_hasNormalForm`: the count. The jet of a series with the
  normal form along a product of minors has the predicted divisibility, up to an error term.
* `New.Parameters.norm_jet_minorProd_le_of_charges`: the count with charges. The columns of height
  one at a set of marked places are removed from the prediction, and powers `p ^ w` of `p` on the
  rows, the charges, pay for them. The exponents `w` satisfy the condition of `New.IsChargeExponent`
  for pairs of columns that occur in `κ`, and `New.fillingCharge` is their sum over the boxes.
* `New.exists_norm_schurJet_le_norm_jet_minorProd`: an entry of the Schur matrix may be replaced by
  a product of minors of `z y` with `y` integral.

A linear substitution makes the couplings that matter in the degree of the jet divisible by `π_p`,
so that the series becomes integral in that degree. Legendre's bound applies, and the chain rule
gives the factor whose valuation is deducted. Each box gains about `γ_p`, and the deduction is
`v(π_p)` times a sum of numbers `New.deductionTerm`. The argument is carried out once, with charges
(`New.Parameters.norm_jet_minorProd_le_of_isChargeExponent`); the count itself is the case without
marked places and with all charges equal to one.

Notions from other files:
* `valRingCp p`: the valuation ring of `ℂ_[p]`; its elements are called integral, and a lower bound
  for a valuation is written as an upper bound for the norm.
* `New.jet R Q F`: the number `(Q(∂) F)(0)`, for a polynomial `Q` and a power series `F`.
* `New.WeylIndex n κ`, `New.schur`, `New.schurJet`: `κ τ h` is the number of columns of height `h`
  of a diagram at the place `τ`. The standard fillings of these diagrams index the Schur matrix of a
  family of matrices `z_τ`, and `schurJet κ F` is the matrix of jets of `F` along its entries.
* `New.coupling pr e`: the series `Γ_e = ∑ z_(τ, c) ^ p ^ e * z_(pr e τ, c)`, where `pr e τ` is the
  partner of the place `τ`. `New.deductionTerm p κ N marked τ τ' e` is the real number
  `min (t / p ^ e) (r' + t') + r / p ^ e + min (B / p ^ e) B'`. Only heights below `N` count: `t`
  is the number of columns of height one at `τ` (zero if `τ ∈ marked`), `r` that of the low columns
  (the other ones) and `B` that of their boxes. The primed letters refer to `τ'`.
* For `K = ℚ(√-d)`: `χ_K = New.chiK d`, `π_p = New.piPrimeInt d` has valuation
  `v(π_p) = New.piPrimeValuation d p`, `ρ_p = New.varpiValuation d p`, and
  `γ_p = New.gammaPrime d p = 1 / (p - 1) - ρ_p`. The set `I_p° = New.partnerExponents d p` consists
  of the odd numbers if `p` is inert and of all numbers if `p = d`, and
  `I_p = New.positivePartnerExponents d p` of its positive elements. `New.Parameters.partner` is the
  partner `-p ^ e τ` of `τ`.
* `New.HasNormalForm`: `F(ϖ z)` is an integral series times the exponential of `ϖ ^ (p + 1) / p`
  times an integral combination of the powers `Γ_e ^ p ^ j`.

## Relation to the literature

One- and two-variable divisibility at inert `p` over an imaginary quadratic field is known in the
literature.

Related work: Katz, Divisibilities, congruences, and Cartier duality, 1981; Chellali, Congruences
entre nombres de Bernoulli–Hurwitz dans le cas supersingulier, 1990; Fujiwara, On divisibilities of
special values of real analytic Eisenstein series, 1988; Bannai–Kobayashi–Yasuda, Radius of
convergence of the p-adic sigma function, 2017.


### `norm_prod_factorial_le`

 Legendre's bound for a multi-index `d`, of degree `l = d.degree`: the valuation of `∏ (d x)!`
is at least `l / (p - 1) - card σ * (1 + ⌊log_p l⌋)`. 

### `norm_jet_le_of_isHomogeneous`

 If the coefficients of degree `l` of the series `G` are integral and `Q` is a homogeneous
polynomial of degree `l` with integral coefficients, then the jet `(Q(∂) G)(0)` has valuation at
least `l / (p - 1) - card σ * (1 + ⌊log_p l⌋)`.

A consequence of the lower bound `v(m!) ≥ m / (p - 1) - (1 + ⌊log_p m⌋)` given by Legendre's
formula, applied to each exponent of each monomial of `Q`. 

### `minorProd`

 The polynomial `P_y(z)` in the entries `X (τ, b, a)` of matrices `z_τ` of size `n' × n`. It is
the product, over the places `τ` and the columns `j` of height `h < card n'` of the diagram `κ τ`,
of the minor of `z_τ y_τ` on the rows `(i' τ).1 h j b` that the filling `i'` puts into the column
and on the first `h` columns. 

### `DirectionVar`

 The index type of the new variables `s_(τ h k b)`: an index `(⟨h, k⟩, τ, b)` consists of a
height `h < N`, a direction `k < h` of that height, a place `τ` and a row `b`. 

### `directionSubst`

 The matrix of the linear substitution `z(s)` with row factors `c` and directions `β`: row `b`
of `z_τ(s)` is `∑_(h, k) c_(τ h b) s_(τ h k b) β_(τ h k)`. So the entry at `x = (τ, b, a)` and
`o = (⟨h, k⟩, τ', b')` is `c τ h b * β τ h k a` if `(τ', b') = (τ, b)`, and zero otherwise. 

### `linSubst_directionSubst_X`

 The map `linSubst M` sends each variable `X o` to `∑_x M x o • X x`. For the matrix `M` of the
substitution `z(s)` it sends `s_(τ h k b)` to `c_(τ h b)` times the linear form
`∑_a β_(τ h k a) z_(τ b a)`. 

### `columnDetProd`

 The polynomial `P_*` in the new variables: the product, over the places `τ` and the columns `j`
of height `h < card n'` of the diagram `κ τ`, of the determinants `det (s_(τ h k b))`, with `k < h`
and `b` among the rows that the filling `i'` puts into the column. 

### `map_columnDetProd`

 The polynomial `columnDetProd R i'` is compatible with change of the coefficient ring. 

### `isHomogeneous_det_directionVar`

 The determinant of the `h × h` matrix of the variables `s_(τ h k b) = X (⟨h, k⟩, τ, I b)` of
`MvPolynomial (DirectionVar Φ n' N) R`, with rows `I b` and directions `k < h`, is homogeneous of
degree `h`. 

### `isHomogeneous_columnDetProd`

 The product `columnDetProd R i'` of the determinants of the columns of `κ` is homogeneous. Its
degree `boxes κ (card n')` is the number of boxes in the columns of height below `card n'`. 

### `jet_columnDetProd_subst`

 The chain rule for the substitution `z(s)` along the polynomial `P_* = columnDetProd R i'`. The
filling `i'` puts the row `(i' τ).1 h j b` into box `b` of column `j` of height `h` at the place
`τ`. With new variables `s_(τ h k r)`, `P_*` is the product over all `τ`, `h`, `j` of the
determinants `det (s_(τ h k r))`, with `k < h` and `r` among the rows of the column. The matrix
`directionSubst c (newDirection g y)` defines the substitution `z_(τ r a) = ∑_(h, k) c_(τ h r) *
β_(τ h k a) * s_(τ h k r)`, where `β_(τ h k a)` is the new direction
`∑_k' (g τ h)_(k k') y_(τ a k')`. The jet of `F(z(s))` along `P_*` is the jet of `F` along the
product of minors `minorProd i' y`, times `det (g τ h)` for each column and `c_(τ h r)` for each
box, `r` being its row. 

### `dvd_subst_coupling`

 Let `π` divide `p`, let `α` be the index type of the entries at one place, and substitute linear
forms `∑_o z x o * s_o` for the variables `X_x`, `x = (τ, a) ∈ Φ × α`, of the coupling
`Γ_e = ∑ X_(τ, a) ^ p ^ e * X_(pr e τ, a)`. Modulo `p` the result is a combination of the
`s_o ^ p ^ e * s_q`. If `π` divides all coefficients of this combination, it divides the result. 

### `dvd_subst_coupling_directionSubst`

 Let `π` divide `p`. The source variables `s_(τ h k b)` are indexed by a height `h < N`, a
direction `k < h`, a place `τ` and a row `b`. The matrix `directionSubst c β` defines the
substitution `z_(τ b a) = ∑_(h, k) c_(τ h b) * β_(τ h k a) * s_(τ h k b)`, with row factors `c` and
directions `β`. If `π` divides `c ^ p ^ e * c'` times the pairing `[β, β']_e = ∑ β_a ^ p ^ e * β'_a`
for each place `τ` and its partner `pr e τ`, each row and all directions `β` at `τ` and `β'` at the
partner, then `π` divides `Γ_e(z(s))`. 

### `IsChargeExponent`

 The charges `p ^ w τ h b` (place, height, row) cover the exempt pairs for the set `ev` of marked
places and the map `partner` on places. A pair consists of the height one at `τ` and a height `h` at
`partner τ`. It is exempt if `τ ∈ ev`, or if `h = 1` and `partner τ ∈ ev`. In each exempt pair and
each row `b`, one of the two exponents is not zero, so that `p` divides the product of the
charges. 

### `fillingCharge`

 The sum of the exponents `w τ h r` over the boxes in the columns of height `h < card n'` of the
diagrams `κ τ`, where `r` is the row that the filling `i'` puts into the box. 

### `fillingCharge_congr`

 The sum `fillingCharge w i'` of the exponents `w` over the filling `i'` depends only on the
values `w τ h b` at the heights `h` that occur in `κ τ` (those with `κ τ h ≠ 0`). 

### `dvd_subst_coupling_directionSubst_of_charges`

 Let `π` divide `p` and let `marked` be a set of places. A pair of heights `h` at `τ` and `h'` at
the partner `τ' = pr e τ` is exempt (`IsExemptPair`) if `h = 1`, and `τ ∈ marked` or both `h' = 1`
and `τ' ∈ marked`. Suppose that `π` divides the pairings `∑ β_a ^ p ^ e * β'_a` of directions `β` at
`τ` and `β'` at `τ'`, except for the exempt pairs. If one of the two exponents `w` is positive in
each exempt pair (`IsChargeExponent`), then `π` divides the coupling
`Γ_e = ∑ z_(τ b a) ^ p ^ e * z_(pr e τ, b a)` after the substitution `directionSubst`. 

### `norm_jet_columnDetProd_subst`

 The chain rule in norms for `F(ϖ z)`. Here `z` is the linear substitution `directionSubst`, that
is `z_(τ r a) = ∑_(h, k) p ^ (w τ h r) * β_(τ h k a) * s_(τ h k r)` with the new directions
`β_(τ h k a) = ∑_k' (g τ h)_(k k') y_(τ a k')`, and `seriesToCp` reads an integral series as one
over `ℂ_[p]`. The filling `i'` puts a row `r` into each box of the `κ τ h` columns of height `h` at
the place `τ`. The polynomial `columnDetProd` is the product over the columns with `h < card n'` of
the determinants `det (s_(τ h k r))`, with `k < h` and `r` among the rows of the column, and
`minorProd` is the product of the corresponding minors of `z_τ y_τ`. The norm of the jet along the
former is that of the jet of `F` along the latter up to factors: each box gives `ϖ` and its row
factor, and each column gives `det (g τ h)`. 

### `heightOneColumns`

 The number `a_τ` of columns of height one at `τ`, among the heights below `N`. Here `κ τ h` is
the number of columns of height `h` at the place `τ`. 

### `lowColumnCount`

 The number `a'_τ` of low columns at `τ`, those whose height is below `N` and is not one. (A
diagram has no column of height zero; if `κ τ 0 ≠ 0`, these columns count here.) 

### `lowBoxCount`

 The number `l_τ` of boxes in the low columns at `τ`, those whose height is below `N` and is not
one. 

### `eraseHeightOne`

 The diagrams `κ` without their columns of height one at the places of the set `ev`, the marked
places. 

### `predictedDivisibility`

 The predicted divisibility at a prime `p`. Let `a_τ` be the number of columns of
height one, `a'_τ` the number of the other columns and `l_τ` the number of boxes in these, all
among the heights below `N`. With `τ' = pr e τ` the predicted divisibility is
`v(π_p) ∑_e ∑_τ ((a_τ / p ^ e - a_τ' - a'_τ')₊ + (l_τ / p ^ e - l_τ')₊ - a'_τ / p ^ e)`. Here
`v(π_p) = piPrimeValuation d p`, and `e` runs over `I_p = positivePartnerExponents d p` (the odd
numbers if `p` is inert, all `e ≥ 1` if `p = d`, none if `p` splits). If `p = d`, half the sum of
`min (a_τ, a_τ' + a'_τ') + a'_τ + min (l_τ, l_τ')` with `τ' = pr 0 τ` is subtracted. 

### `deductionAt`

 The sum of the deduction terms for the couplings of the places `τ` with their partners `pr e τ`,
without marked places; it is zero unless `e` lies in `I_p° = partnerExponents d p`. 

### `deductionTerm_empty`

 The deduction term without marked places, in terms of the numbers of columns of height one, of
low columns (those of other height) and of boxes in the low columns. 

### `deductionTerm_eraseHeightOne`

 Marking the places of `marked` has the same effect on the deduction terms as removing their
columns of height one. 

### `boxes_eq_sum`

 The number `boxes κ N` of boxes in the columns of height below `N` is the sum over the places
`τ` of `heightOneColumns κ N τ`, the columns of height one, and `lowBoxCount κ N τ`, the boxes in
the columns of other height below `N`. 

### `summable_deductionAt`

 The sums of deduction terms are summable over `e`: they are bounded by a constant times `p⁻ᵉ`.
The term `deductionAt d p pr κ N e` is the sum over `τ` of `deductionTerm p κ N ∅ τ (pr e τ) e` if
`e ∈ partnerExponents d p` (odd if `p` is inert in `ℚ(√-d)`, arbitrary if `p = d`, none if `p`
splits), and zero otherwise. 

### `mul_tsum_deductionAt`

 The deduction is `γ_p B` less the predicted divisibility. Here `d` is the prime of `ℚ(√-d)`, `p`
the prime at which one counts, `pr e τ` the partner of the place `τ`, `κ τ h` the number of columns
of height `h` at `τ`, `B` the number of boxes in the columns of height below `N`, and as usual
`v(π_p) = piPrimeValuation d p`, `γ_p = gammaPrime d p`. 

### `mul_sum_deductionTerm_le`

 Let `d` and `p` be primes, `pr e τ` the partner of the place `τ` and `κ τ h` the number of
columns of height `h` at `τ`; only heights below `N` count. The deduction for the set `marked` of
places is `v(π_p) = piPrimeValuation d p` times the sum of `deductionTerm p κ N marked τ (pr e τ) e`
over all `τ` and the `e ≤ e₀` in `I_p° = partnerExponents d p`. It is at most `γ_p B°` less the
predicted divisibility of `κ° = eraseHeightOne κ marked`, which is `κ` without its columns of height
one at the marked places. Here `B°` is the number of boxes of `κ°` and `γ_p = gammaPrime d p`. 

### `norm_jet_minorProd_le_of_isChargeExponent`

 The count with charges, with the deduction cut at `⌊log_p B⌋`. Here `P` fixes the prime `d` of
`K = ℚ(√-d)`, `P.Φ s` is the set of infinite places of the field of level `s`, the instance
`PadicPlace p` is an embedding of `ℂ` into `ℂ_[p]`, and `κ τ h` is the number of columns of height
`h` at the place `τ`. Let `p` be non-split (`chiK P.d p ≠ 1`), let `v(ϖ) = ρ_p`, where
`ρ_p = varpiValuation P.d p = v(π_p) / (q_p - 1)` for the norm `q_p` of a prime above `p`, and let
`F` have the normal form for the exponents `e ∈ I_p°` (odd; all `e` if `p = d`): `F(ϖ z)` is an
integral series times the exponential of the product of `ϖ ^ (p + 1) / p` with a combination of
powers `Γ_e ^ p ^ j` of couplings, whose integral coefficients are given by `l`. Mark a set `marked`
of places, and give row `b` of the columns of height `h` at `τ` a charge `p ^ w τ h b`. For a
partner `τ'` of `τ`, one of `w τ 1 b` and `w τ' h b` is positive if `τ ∈ marked`, or if `h = 1` and
`τ' ∈ marked` (`IsChargeExponent`). The filling `i'` puts a row into each box of `κ`, and with the
integral matrices `y_τ` it defines the product of minors `P_y = minorProd i' y`: over the columns,
the minor of `z_τ y_τ` on the rows of the column and the first `h` columns. Let `B` be the number of
boxes. Then the valuation of `jet` of `F` along `P_y`, plus the sum `fillingCharge w i'` of the
exponents over the boxes, is at least `gammaPrime P.d p * B`, less `v(π_p) = piPrimeValuation P.d p`
times the sum of `deductionTerm` over all places and the exponents `e ∈ I_p°` with `e ≤ ⌊log_p B⌋`,
and less `f N ^ 3 (1 + ⌊log_p B⌋)`. Here `f` is the number of infinite places, `N` the number of
rows, and only columns of height below `N` are counted. 

### `norm_jet_minorProd_le_of_charges`

 **The count with charges.** Here `P` fixes the prime `d` of `K = ℚ(√-d)`, `P.Φ s` is the set of
infinite places of the field of level `s`, the instance `PadicPlace p` is an embedding of `ℂ` into
`ℂ_[p]`, and `κ τ h` is the number of columns of height `h` at the place `τ`. Let `p` be non-split,
let `v(ϖ) = ρ_p`, where `ρ_p = varpiValuation P.d p = v(π_p) / (q_p - 1)` for the norm `q_p` of a
prime above `p`, let `F` have the normal form for the exponents `e ∈ I_p°` (odd; all `e` if
`p = d`): `F(ϖ z)` is an integral series times the exponential of `ϖ ^ (p + 1) / p` times a
combination of powers `Γ_e ^ p ^ j` of couplings, with integral coefficients `l`. The filling `i'`
puts a row into each box of `κ` and, with the integral matrices `y_τ`, defines
`P_y = minorProd i' y`: the product over the columns of the minor of `z_τ y_τ` on the rows of the
column and the first `h` columns, `h` being its height. Let `κ°` arise from `κ` by removing the
columns of height one at the places of `marked`. Let charges `p ^ w` be given such that one of
`w τ 1 b` and `w τ' h b` is positive whenever `τ'` is a partner of `τ`, the heights `1` at `τ` and
`h` at `τ'` occur, and either `τ ∈ marked`, or `h = 1` and `τ' ∈ marked`. Then the valuation of the
jet of `F` along `P_y`, plus the sum `fillingCharge w i'` of the exponents over the boxes, is at
least the predicted divisibility of `κ°`, plus `γ_p = gammaPrime P.d p` for each removed box, less
`f N ^ 3 (1 + log_p max (B, 1))`. Here `f` is the number of infinite places, `N` the number of rows
and `B` the number of boxes of `κ` in columns of height below `N`. 

### `norm_jet_minorProd_le_of_hasNormalForm`

 **The count.** Here `P` fixes the prime `d` of `K = ℚ(√-d)`, `P.Φ s` is the set of infinite
places of the field of level `s`, and the instance `PadicPlace p` is an embedding of `ℂ` into
`ℂ_[p]`. Let `p` be non-split (`chiK P.d p ≠ 1`), and let `v(ϖ) = ρ_p`, where
`ρ_p = varpiValuation P.d p = v(π_p) / (q_p - 1)` for the norm `q_p` of a prime above `p`. Let `F`
have the normal form (`HasNormalForm`) for the exponents `e ∈ I_p°` (odd; all `e` if `p = d`):
`F(ϖ z)` is an integral series times the exponential of `ϖ ^ (p + 1) / p` times a combination of
powers `Γ_e ^ p ^ j` of couplings, with integral coefficients `l`. The filling `i'` puts a row into
each box of `κ` and, with the integral matrices `y_τ`, defines `P_y = minorProd i' y`, the product
over the columns of the minor of `z_τ y_τ` on the rows of the column and the first `h` columns, `h`
being its height. Then the valuation of the jet `P_y(∂)F(0)` of `F` along `P_y` is at least the
predicted divisibility of `κ`, less `f N ^ 3 (1 + log_p max (B, 1))`. Here `f` is the number of
infinite places, `N` the number of rows and `B` the number of boxes of `κ` in columns of height
below `N`. The predicted divisibility is
`v(π_p) ∑_e ∑_τ ((a_τ / p ^ e - a_τ' - a'_τ')₊ + (l_τ / p ^ e - l_τ')₊ - a'_τ / p ^ e)` over
positive `e ∈ I_p°`, where `τ' = P.partner s p e τ = -p ^ e τ` is the partner
of `τ` and `a`, `a'`, `l` count the columns of height one, the other columns and the boxes in these;
for `p = d` half a term for `e = 0` is subtracted (`predictedDivisibility`). 

 ## From entries of the Schur matrix to products of minors 

### `exists_norm_le_norm_sum_mul_eval`

 If polynomials `b t` over the valuation ring of `ℂ_[p]` stay linearly independent over the
residue field, then for all numbers `α t` there is an integral point `y` at which
`∑ α t * b t (y)` has norm at least that of a given `α t₁`. 

### `minorProd_eq_sum`

 Expansion of the product of minors `P_y(z) = minorProd i' y`: the entries of row `i'` of the
Schur matrix of the variables `z_τ` are its coefficients in the family `nablaBasis i * detPow`
evaluated at `y`. Here `nablaBasis i` is the product of minors for the filling `i`, and `detPow` is
the product, over the places `τ`, of the determinant of the first `card n` columns of `y_τ`, each to
the power `schurDetExp`: the number `κ τ (card n)` if `card n < card n'`, and zero otherwise. The
hypothesis `FitsRanks` says `card n ≤ card n'` and that `κ` has no column of height strictly between
the two. 

### `exists_norm_schurJet_le_norm_jet_minorProd`

 An entry of the Schur matrix `schur κ z` may be replaced by a product of minors. Suppose
`card n ≤ card n'` and that `κ` has no column of height strictly between the two (`FitsRanks`). Take
a power series `F` and standard fillings `i'`, `i`. Let `P` be the polynomial entry of `schur κ z`
at `(i', i)`. Then there are matrices `y_τ` with entries in `valRingCp p` such that
`schurJet κ F i' i = (P(∂) F)(0)` has norm at most that of `(P_y(∂) F)(0)`, where
`P_y = minorProd i' y`. 
