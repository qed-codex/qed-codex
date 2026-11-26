---
{
  "module": "src/Lib/DiscreteSeries/FlenstedJensen/PsiKTypes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/FlenstedJensen/PsiKTypes.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/FlenstedJensen/PsiKTypes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# First properties of c_λ and its K-types

We study the function c_λ = `New.HCParam.dsCoeff` on U(diag ε). Here l = 2λ is a parameter, usually
assumed to satisfy `New.HCParam.HasGap`; K = `New.maxCompactU` has its Haar measure `New.haarK` of
mass one. We write m_w = `New.weightMinors` w for the product of principal minors that is the
coefficient of a highest vector for dominant w, and Λ = `New.HCParam.lowestKType` for the lowest
K-type; λ + ρ = `New.paramAddRho` l, with ρ half the sum of the roots positive for l. The first
properties of c_λ are read off from Flensted-Jensen's integral `New.HCParam.flenstedJensen` over K.
Then we compute ∫_K conj(m_ν(k)) c_λ(xkb) dk for a weight ν that is K-dominant for the order −l: it
is a constant times c_λ(x) c_λ(b) for ν = Λ, and 0 if ν − Λ is outside the cone
`New.HCParam.rootCone` of positive roots.

## Main definitions and results

* `New.dsCoeff_one`, `New.dsCoeff_of_mem_blockDiagAlg`, `New.dsCoeff_of_mem_maxCompactU`:
  c_λ(1) = 1, and c_λ = m_Λ on invertible block diagonal matrices, in particular on K.
* `New.dsCoeff_polar`: the formula for c_λ(p z q⁻¹) with p, q in K and z positive definite.
* `New.dsCoeff_inv`, `New.dsCoeff_neg`: inversion of g and λ ↦ −λ both conjugate c_λ(g).
* `New.integral_conj_weightMinors_lowestKType_mul_dsCoeff`,
  `New.integral_conj_weightMinors_mul_dsCoeff_eq_zero`: the projections of c_λ to its K-types.

Notions from other files:
* `New.USign`: for a vector of signs ε, the unitary group U(J) of the diagonal matrix J = diag(ε);
  `New.maxCompactU ε` is its compact subgroup K = U(diag ε) ∩ U(n).
* `New.HCParam.HasGap`: the entries of `l = 2λ` are distinct and congruent to #n − 1 mod 2, and
  `|λ_i − λ_j| ≥ h` whenever `ε_i ≠ ε_j`.
* `New.IsKDominant`: the weight w is K-dominant for the order o if w_j ≤ w_i whenever ε_i = ε_j and
  o_i < o_j.
* `New.HCParam.rootCone`: the integer vectors β with o · β ≤ 0 for every vector o that strictly
  reverses the order of l: the polar cone of these vectors o.

## Relation to the literature

Known result: Flensted-Jensen's function c_λ on U(p,q), classically the coefficient of the lowest
K-type of a discrete series, its first properties and its projections to K-types.

It is treated for U(p,q) and parameters with a gap, with the integrand written by principal minors;
existence of the discrete series is not assumed. Source: M. Flensted-Jensen, Discrete series for
semisimple symmetric spaces, Ann. of Math. 111 (1980) 253-311; B. Sun, Matrix coefficients of
cohomologically induced representations, Compositio Math. 143 (2007), Thm 1.1 (arXiv math/0403440);
A. Knapp, Representation Theory of Semisimple Groups (1986), ch. IX.


 ## Value at one, polar formula and symmetries of c_λ 

### `weightMinors_unitary_inv`

 For g in U(diag ε) and a weight w, the product of principal minors m_w = `New.weightMinors` w
takes conjugate values at g and at g⁻¹. 

### `weightMinors_unitary_neg`

 For g in U(diag ε) and a weight w, negating w conjugates the product of minors m_w(g). 

### `instance {J : Matrix n n ℂ} : SigmaCompactSpace (U J)`

 The group U(J) of a matrix J is σ-compact. 

### `dsCoeff_one`

 The function c_λ = `l.dsCoeff` takes the value 1 at the identity. 

### `dsCoeff_polar`

 For a parameter l = 2λ of gap h (`l.HasGap h`), p, q in K = U(diag ε)∩U(n) and z in U(diag ε)
positive definite, c_λ(pzq⁻¹) equals ∫_K m_Λ(pu) conj(m_Λ(qu)) / m_{−λ−ρ}(uᴴzu) du divided by ∫_K
|m_Λ|², where du is the Haar measure of mass one. Here c_λ = `l.dsCoeff` is the function g ↦ Ξ(a,
a⁻¹g), with a the block diagonal part of g and Ξ the normalised integral
`New.HCParam.flenstedJensen`. The function m_w(g) = `New.weightMinors w` is the product over all
integers t of the principal minor of g on {i | t ≤ w i}, each factor with t ≤ 0 divided by det g,
and Λ = `l.lowestKType` and λ + ρ = `paramAddRho l`. 

### `dsCoeff_inv`

 For a parameter λ of gap h and g in U(diag ε), c_λ(g⁻¹) is the complex conjugate of c_λ(g). 

### `dsCoeff_neg`

 Let `l = 2λ` be a parameter of gap `h`: its entries are distinct and congruent to `card n - 1`
mod 2, and `|λ i - λ j| ≥ h` whenever `ε i ≠ ε j`. Let c_λ = `l.dsCoeff` be the function
c_λ(g) = Ξ(a, a⁻¹g), where a is the block diagonal part of g and Ξ is the normalised integral
`New.HCParam.flenstedJensen`. Then for every g in U(diag ε), c_{−λ}(g) is the complex conjugate of
c_λ(g). 

### `dsCoeff_of_mem_blockDiagAlg`

 Let `l = 2λ` be a parameter of gap `h` (distinct entries congruent to `card n - 1` mod 2, with
`|λ i - λ j| ≥ h` whenever `ε i ≠ ε j`), and let c_λ = `l.dsCoeff`, c_λ(g) = Ξ(a, a⁻¹g) with a the
block diagonal part of g. For an invertible a in `blockDiagAlg ε` (matrices commuting with diag ε),
c_λ(a) = `weightMinors Λ a`, where Λ = `l.lowestKType` = λ + ρ − 2ρ_c, with 2ρ_c the sum of the
compact roots positive for `l`. Here `weightMinors Λ a` is the product over integers t of the
principal minor of a on {i | t ≤ Λ i}, with each factor for t ≤ 0 divided by det a. 

### `dsCoeff_of_mem_maxCompactU`

 For a parameter λ of gap h and k in K = U(diag ε) ∩ U(n), c_λ(k) = m_Λ(k), the product of
principal minors of weight Λ = λ + ρ − 2ρ_c. 


## The lowest K-type of c_λ and vanishing outside Λ + cone

The projection formula for c_λ(x k b) is proved for b near 1, by writing c_λ as Flensted-Jensen's
integral and averaging over a circle in K, and is continued analytically to every b in U(diag ε).


### `New.exists_order_dotProduct_eq_natCast`

 If `β` is `0` or lies outside `l.rootCone`, there is an order `o` opposite to `l` for which
`o ⬝ᵥ β` is a natural number that vanishes only for `β = 0`. 

### `New.injective_and_lt_of_reverses_order`

 An integer vector `o` that strictly reverses the order of a parameter `l` with a gap is
injective, and `o i < o j` holds only if `l j < l i`. 

### `New.analyticAt_integral_conj_weightMinors_mul_dsCoeff`

 The integral ∫_K conj(m_ν(k)) c_λ(x k z) dk, with m_ν = `weightMinors ν` and
c_λ = `l.dsCoeff`, is analytic in the matrix `z` at every point of U(diag ε). 

### `New.integral_circle_weightMinors_div`

 For θ in ℝ/ℤ let s = `θ.toCircle` and t = diag(s ^ o) in K. Let ν be K-dominant for injective
`o`, μ dominant for `-o`, let `y` factor as t⁻¹ y = A(s) t⁻¹ C with `A` entire, `A 0 = 1`, `C`
triangular (`IsCircleFactorization`), with `w * A s` accretive (Hermitian part positive definite) on
the unit disc (w is a matrix), let N = o · (ν − Λ) be a natural number that vanishes only for ν = Λ.
Then the mean over θ of m_ν(k t j⁻¹) · u · conj(m_Λ(k t)) / m_μ(w t* y t) is u conj(m_Λ(j)) / m_μ(w)
times
|m_Λ(k)|² / m_μ(y) if ν = Λ, and 0 otherwise. Here m_ν = `weightMinors ν` for each weight, and
dominance for the signs `1` compares all pairs of indices. 

### `New.eventually_forall_accretive_circleFactorization`

 For `-o` injective, μ dominant for `-o` and `x` in U(diag ε), every `b` near 1 has, for all `k`
in K, the following properties, where a_x = `blockDiagPart ε x` (the entries of x with ε_i = ε_j,
the others replaced by 0) and y = k* b k. The matrix y and its products with each j* a_x⁻¹ x j, j in
K, are accretive (Hermitian part positive definite), and y has a circle factorisation
(`New.IsCircleFactorization`) t⁻¹ y = A(s) t⁻¹ C for |s| = 1, t = diag(s ^ o), A entire, A 0 = 1, C
triangular, such that every product j* a_x⁻¹ x j * A(s),
|s| ≤ 1, is accretive. 

### `New.exists_order_isKDominant_dotProduct_eq_natCast`

 If ν is `K`-dominant for `-l` and is Λ or has ν − Λ outside `l.rootCone`, there is an injective
`o`, with ν `K`-dominant for `o` and −λ − ρ = `-paramAddRho l` dominant for `-o`, such that
N = o · (ν − Λ) is a natural number that vanishes only for ν = Λ. 

### `New.eventually_integral_conj_weightMinors_mul_dsCoeff`

 The projection formula for `b` near `1`. Let `l = 2λ` have a gap and ν be a weight, `K`-dominant
for the order `-l`, that is the lowest `K`-type Λ or has ν − Λ outside `l.rootCone`. Then
∫_K conj(m_ν(k)) c_λ(x k b) dk is ∫_K |m_Λ|² · c_λ(x) c_λ(b) if ν = Λ, and `0` otherwise, where
c_λ = `l.dsCoeff` and m_w = `weightMinors w`. 

### `New.integral_conj_weightMinors_mul_dsCoeff_eq_mul_ite`

 The two cases of the projection formula in one identity, for every `b` in U(diag ε): for
`l = 2λ` with a gap and a weight ν that is `K`-dominant for `-l` and is Λ or has ν − Λ outside
`l.rootCone`, with c_λ = `l.dsCoeff` and m_w = `weightMinors w`, ∫_K conj(m_ν(k)) c_λ(x k b) dk is
∫_K |m_Λ|² · c_λ(x) c_λ(b) if ν = Λ, and `0` otherwise. 

### `New.integral_conj_weightMinors_lowestKType_mul_dsCoeff`

 Projection of c_λ to its lowest `K`-type Λ. For a parameter `l = 2λ` of gap h and `x`, `b` in
U(diag ε), ∫_K conj(m_Λ(k)) c_λ(x k b) dk = ∫_K |m_Λ|² · c_λ(x) c_λ(b), with K = U(diag ε)∩U(n)
carrying its Haar measure of mass one. Here c_λ = `l.dsCoeff`, Λ = `l.lowestKType`, and
m_Λ = `weightMinors Λ` is the function sending g to the product over all integers t of the principal
minor of g on {i | t ≤ Λ i}, each factor with t ≤ 0 divided by det g.

For the matrix coefficient of a unit highest weight vector this identity expresses, by Schur's
orthogonality relations for `K`, that the lowest `K`-type of the discrete series occurs once. 

### `New.integral_conj_weightMinors_mul_dsCoeff_eq_zero`

 c_λ has no `K`-type outside Λ + `l.rootCone`: for a parameter `l = 2λ` with a gap, `x`, `b` in
U(diag ε) and a weight ν that is `K`-dominant for the order `-l`, with ν − Λ outside the cone, ∫_K
conj(m_ν(k)) c_λ(x k b) dk = 0.

This is the form, for the one coefficient c_λ, of the fact that the `K`-types of the discrete series
lie in the cone above the lowest one (a consequence of Blattner's formula). 
