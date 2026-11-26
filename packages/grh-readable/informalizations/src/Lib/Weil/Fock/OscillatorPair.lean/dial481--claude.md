---
{
  "module": "src/Lib/Weil/Fock/OscillatorPair.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Fock/OscillatorPair.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Fock/OscillatorPair.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Harmonic matrix coefficients of the Weil representation and oscillator pairs on matrices

Let ω₀ = `New.Fock.realWeil` be the Weil representation of U(ε) on the Fock space. Let u be block
diagonal with respect to labels d, and let P, Q be harmonic: ∂_i∂_j kills them whenever d_i = d_j
and ε_i ≠ ε_j. Then the coefficient ⟨v_Q, ω₀(u) v_P⟩ is an inner product after a linear
substitution, divided by the determinant of the negative block of u. The dual pair U(ε) × U(ε′) acts
on the Fock space of R × C matrices, and the pulled-back, det-twisted Weil representations of the
two factors form an oscillator pair.

## Main definitions and results

* `New.Fock.complexLinearPart`: the matrix formed from the positive block of u and the conjugate of
  its negative block; it is invertible.
* `New.Fock.fockMatrixCoeff_eq_fockInner`: the coefficient is an inner product after a linear
  substitution (`New.linSubst`), divided by the determinant of the negative block of u.
* `New.Fock.detTwist`: the Weil representation `New.Fock.realWeil` pulled back along a homomorphism
  f and twisted by det^γ; `New.Fock.isUnitaryRep_detTwist`, `New.Fock.isDerivedAction_detTwist`,
  `New.Fock.fockInner_detTwist_pos` give unitarity with polynomial growth of the operator norm
  (`New.IsUnitaryRep`), the derivative (`New.IsDerivedAction`) and positivity at positive definite
  elements.
* `New.OscillatorRep`, `New.OscillatorPair`: these three properties as a structure, for U(ε) acting
  on the Fock space of an arbitrary dual-pair datum `T : New.FockDualPair ε ε' ι`, and for commuting
  actions of U(ε) and of U(ε′) (the latter via `T.swap`).
* `New.Fock.oscillatorPair_detTwist`: the twisted left and right actions on matrices form such a
  pair.

Notions from other files:
* `New.USign`: for a vector of signs ε, the unitary group U(ε) of the diagonal matrix diag(ε).
* `New.Fock.fockInner`: the bounded sesquilinear form (c, c′) ↦ ∫ c̄ c′ on the Fock space,
  conjugate-linear in the first variable.
* `New.Fock.polyVector`: the linear map P ↦ v_P from complex polynomials to the Fock space,
  v_P(x) = P(ζ(x))exp(−|x|²/2), where ζ(x)_i is x̄_i at positive and x_i at negative coordinates.
* `New.Fock.fockMatrixCoeff`: the coefficient ⟨v_Q, ω₀(u) v_P⟩, written `fockMatrixCoeff u Q P`.
* `New.Fock.weilDeriv`: the derivative of `New.Fock.realWeil` on polynomials, the linear map u ↦ Σ
  u_ab A_a B_b, where (A_a, B_a) is (X_a, ∂_a) if ε_a = 1 and (−∂_a, X_a) otherwise; A_a is
  `raiseOp ε a` and B_a is `lowerOp ε a`.

## Relation to the literature

Known result: Bargmann–Fock model of the harmonic (oscillator) representation of U(p,q). Here the
space is the L¹ (Feichtinger) space of vacuum coefficients rather than the Hilbert Fock space, and
weighted moments replace Schwartz seminorms. This file treats unitarity, growth, the derivative and
the coefficients between harmonic polynomials. Source: M. G. Davidson, The harmonic representation
of U(p,q) and its connection with the generalized unit disk, Pacific J. Math. 129 (1987), §1 and
Prop. 2.2; G. B. Folland, Harmonic Analysis in Phase Space (1989), ch. 1, 4; H. Reiter, Metaplectic
Groups and Segal Algebras, LNM 1382 (1989).



## Matrix coefficients between harmonic polynomial vectors

The identities `New.Fock.fockMatrixCoeff_raiseOp` and `New.Fock.fockMatrixCoeff_lowerOp`, which
move `raiseOp` and `lowerOp` from one polynomial of a coefficient to the other, are solved for a
factor X_j on the left (`New.Fock.fockMatrixCoeff_X_mul`). Induction by Euler's identity
(`New.Fock.harmonic_induction`) then reduces `New.Fock.fockMatrixCoeff_eq_fockInner` to the overlap
of the vacuum with its image.


### `complexLinearPart`

 For u in U(diag ε), the matrix P₊ u P₊ + P₋ ū P₋, with P₊, P₋ the projections `New.Fock.posProj`
on the positive and negative coordinates and ū the entrywise conjugate of u (written `uᴴᵀ`). 

### `complexLinearPart_apply`

 The entry of `complexLinearPart u` at (i, j) is u_ij if both signs are positive, its conjugate
if both are negative, and zero if the signs differ. 

### `det_complexLinearPart`

 The determinant of `complexLinearPart u` is the conjugate of the determinant of the negative
block of u (`New.Fock.realMultiplier`) times the principal minor of u on the indices whose sign is
not −1, that is, the determinant of the positive block. 

### `realMultiplier_ne_zero`

 For u in U(ε), the conjugate `realMultiplier u` of the determinant of the negative block of u is
not zero. 

### `noncomputable instance : Invertible (complexLinearPart u)`

 The matrix `complexLinearPart u` is invertible, since both diagonal blocks of u are. 

### `harmonic_induction`

 Induction for polynomials P with ∂_i∂_j P = 0 whenever r(i, j). A subspace S contains all of
them if it contains 1 and contains X_j P whenever P ∈ S and ∂_i P = 0 for all i with r(i, j). 

### `fockMatrixCoeff_pderiv`

 Let u in U(ε) be block diagonal for the labels d, and let C = `New.Fock.complexLinearPart` u be
the matrix P₊uP₊ + P₋ūP₋, where P₊, P₋ project on the coordinates with εᵢ = 1 and εᵢ = −1 and ū is
the entrywise conjugate of u. If ∂_k Q = 0 for all k with d_k = d_i and ε_k ≠ ε_i, then ⟨v_Q, ω₀(u)
v_{∂_i P}⟩ = ∑_k conj(C_ki) ⟨v_{X_k Q}, ω₀(u) v_P⟩. Here `fockMatrixCoeff u Q P` is ⟨v_Q, ω₀(u)
v_P⟩, a coefficient of the Weil representation ω₀, and v_P = `polyVector ε P` is the Fock vector of
P. 

### `fockMatrixCoeff_X_mul`

 Let u ∈ U(diag ε) satisfy u_ij = 0 whenever d_i ≠ d_j. Let A = (`New.Fock.complexLinearPart`
u)⁻¹, where `complexLinearPart u` = P₊ u P₊ + P₋ ū P₋, with P₊ and P₋ the projections onto the
positive and negative coordinates and ū the entrywise conjugate of u. If ∂_i Q = 0 for all i with
d_i = d_j and ε_i ≠ ε_j, then ⟨v_{X_j Q}, ω₀(u) v_P⟩ = ∑_i conj(A_ij) ⟨v_Q, ω₀(u) v_{∂_i P}⟩. Here
`fockMatrixCoeff u Q P` is the Weil-representation coefficient ⟨v_Q, ω₀(u) v_P⟩, and conj(A_ij) is
written as the entry (j, i) of the inverse of the conjugate transpose. 

### `fockMatrixCoeff_one_left`

 Let u in U(ε) be block diagonal for the labels d, and let P be killed by ∂_i∂_j whenever
d_i = d_j and ε_i ≠ ε_j. Then ⟨v_1, ω₀(u) v_P⟩ = (det z)⁻¹ ⟨v_1, v_P⟩. Here ω₀ is the Weil
representation, v_P = `polyVector ε P` is the Fock vector of P (v_1 is the vacuum), and z is the
negative block of u (its determinant is the `principalMinor`). 

### `fockMatrixCoeff_eq_fockInner`

 Matrix coefficients of the Weil representation ω₀ between harmonic polynomials. Let u in U(ε) be
block diagonal for the labels d, and let P, Q be killed by ∂_i∂_j whenever d_i = d_j and ε_i ≠ ε_j.
Then ⟨v_Q, ω₀(u) v_P⟩ = (det z)⁻¹ ⟨v_Q′, v_P⟩. Here v_P = `polyVector ε P` is the Fock vector of P,
z is the block of u on the coordinates with εᵢ = −1 (its determinant is the `principalMinor`), and
Q′ = `linSubst A Q` is Q after the substitution X_j ↦ Σ_i A_ij X_i, with A = C⁻¹ for
C = `New.Fock.complexLinearPart` u = P₊uP₊ + P₋ūP₋ (P₊, P₋ the projections on the positive and
negative coordinates, ū the entrywise conjugate). 


## Oscillator pairs on the Fock space of matrices

The dual pair U(ε) × U(ε′) acts on the Fock space `New.Fock.fockSpace` of R × C matrices, with sign
ε_r ε′_c at the entry (r, c).


 ### The twisted Weil representation 

### `pairHom`

 The Kronecker homomorphism (not injective) from the dual pair U(ε′) × U(ε) to the unitary group
for the signs ε_r ε′_c on `R × C`: the pair `(g, h)` goes to `h ⊗ₖ g⁻¹ᵀ`, which is the action x ↦ h
x g⁻¹ on `R × C` matrices. 

### `coe_pairHom`

 The matrix of `pairHom ε ε' (g, h)` is `h ⊗ₖ g⁻¹ᵀ`. 

### `norm_pairHom_le`

 For `g` in U(ε′) and `h` in U(ε), the ℓ² operator norm of the matrix `h ⊗ₖ g⁻¹ᵀ` of
`pairHom ε ε' (g, h)` is at most `‖g‖ * ‖h‖`. 

### `detTwist`

 The Weil representation `realWeil` of U(ε′) on the Fock space, pulled back along a homomorphism
`f` from U(ε) to U(ε′) and twisted by `det ^ γ`: `g` acts by `det g ^ γ • realWeil (f g)`. 

### `norm_realWeil_le`

 For `g` in U(ε′), the operator norm of the Weil operator `realWeil g` on the Fock space is at
most the norm of the vacuum vector times the modulus of `realMultiplier g`, the conjugate of the
determinant of the negative block of `g`. 

### `isUnitaryRep_detTwist`

 Let `f` be a continuous homomorphism from U(ε) to U(ε′) with `‖f g‖ ≤ a * ‖g‖`. Then
`detTwist f γ`, the Weil representation pulled back along `f` and twisted by `det ^ γ`, is strongly
continuous, preserves the positive definite hermitian form `fockInner`, and has operator norm
`O(‖g‖ ^ card C)`. 

### `isDerivedAction_detTwist`

 Let `f` be a homomorphism from U(ε) to U(ε′) with `f (exp Y) = c • F (exp (c • Y))` for `Y` in
the Lie algebra of U(ε), where `F` is a linear map and `c` a sign. Let `ρ` be the `gl R`-module on
polynomials with action `Y ↦ weilDeriv ε' (F Y) + γ * trace Y`. Then `ρ` is the derivative of
`detTwist f γ` on the vectors `polyVector ε' P` of polynomials `P`. 

### `fockInner_detTwist_pos`

 Let π = `detTwist f γ` be the representation of U(ε) on the Fock space in which g acts by
det(g)^γ · `realWeil` (f g), the Weil representation of U(ε′) pulled back along the homomorphism `f`
and twisted by the γ-th power of the determinant. Let `z` in U(ε) and its image `f z` in U(ε′) be
positive definite, with `f z` block diagonal for labels `d` of the variables, and let `P ≠ 0` be a
polynomial killed by ∂_i∂_j whenever `i` and `j` have the same label and opposite signs. Then the
matrix coefficient ⟨v_P, π(z) v_P⟩ at the Fock vector v_P = `polyVector ε' P` is a positive real
number. 

 ### Oscillator pairs 

### `_root_.New.OscillatorRep`

 π is a strongly continuous representation of U(ε) on the Fock space with variables ι, which
preserves the form `New.Fock.fockInner` and has norm O(‖g‖ ^ |ι|). Its derivative on polynomials is
the row action `New.FockDualPair.oscRows` of the dual pair data `T` (a sign, two constants and a
bijection of R × C with ι), and ⟨v_P, π(z) v_P⟩ > 0 for z positive definite and P ≠ 0 satisfying
`New.FockDualPair.IsTermwiseHarmonic`. 

### `_root_.New.OscillatorRep.unitary_rep`

 π is strongly continuous, preserves the positive definite hermitian form `fockInner`, and has
  norm O(‖g‖ ^ |ι|). 

### `_root_.New.OscillatorRep.derives`

 On the vectors v_P of polynomials P, the derivative of π is the action `oscRows` on the
  rows. 

### `_root_.New.OscillatorRep.inner_pos`

 ⟨v_P, π(z) v_P⟩ > 0 for z positive definite and P ≠ 0 satisfying `IsTermwiseHarmonic`: no
  monomial of P has two variables of one column from rows of opposite signs. 

### `_root_.New.OscillatorPair`

 π of U(ε) and π′ of U(ε′) are commuting representations on one Fock space, each a
`New.OscillatorRep`. π acts on the rows, with the data `T`, whose sign is `T.globalSign` and whose
constant on the rows is `T.rowShift`, and π′ acts on the columns, with the data `T.swap`, whose
sign is `-T.globalSign` and whose constant on the rows is `T.columnShift`. 

### `_root_.New.OscillatorPair.column_rep`

 π' has the same properties for `T.swap`, the columns read as rows. 

### `_root_.New.OscillatorPair.commute`

 π and π' commute. 

 ### The left and right actions on matrices 

### `weilDeriv_single_kronecker_one`

 Let η be signs on the R × C matrix entries, and `weilDeriv η` the derivative of the Weil
representation on polynomials. It sends `E_ab ⊗ 1`, with `E_ab = single a b 1` a matrix unit in the
rows, to the sum over the columns `c` of the operators `glOp η (a, c) (b, c)`, that is, of the
images under `weilDeriv η` of the matrix units at ((a, c), (b, c)), so `glOp η i j` is A_i B_j. 

### `weilDeriv_one_kronecker_single`

 Let η be signs on the R × C matrix entries, and `weilDeriv η` the derivative of the Weil
representation on polynomials. It sends `1 ⊗ E_ab`, with `E_ab = single a b 1` a matrix unit in the
columns, to the sum over the rows `r` of the operators `glOp η (r, a) (r, b)`, that is, of the
images under `weilDeriv η` of the matrix units at ((r, a), (r, b)), so `glOp η i j` is A_i B_j. 

### `oscillatorRep_detTwist_inr`

 For finite R, C with signs ε, ε′, let U(ε) act on R × C matrices by x ↦ hx (`pairHom ε ε'` at
(1, h)). On the Fock space with sign ε_r ε′_c at the entry (r, c), the representation π : h ↦ (det
h)^γ ω(x ↦ hx) (`detTwist`), with ω = `New.Fock.realWeil`, is a `New.OscillatorRep`, for the data
`New.FockDualPair.std` (sign 1, constants γ and γ′ + |R|): it is unitary, its derivative is the row
action of these data, and ⟨v_P, π(z) v_P⟩ > 0 for positive definite z and nonzero P satisfying
`IsTermwiseHarmonic`. 

### `oscillatorRep_detTwist_inl`

 For finite R, C with signs ε, ε′, let U(ε′) act on R × C matrices by x ↦ xg⁻¹ (`pairHom ε ε'` at
(g, 1)). On the Fock space with sign ε_r ε′_c at the entry (r, c), the representation
π : g ↦ (det g)^γ′ ω(x ↦ xg⁻¹) (`detTwist`), with ω = `New.Fock.realWeil`, is a `New.OscillatorRep`
for the data `New.FockDualPair.std` with rows and columns exchanged by `swap`: it is unitary, its
derivative is the column action with constant γ′ + |R|, and ⟨v_P, π(z) v_P⟩ > 0 for positive
definite z and nonzero P satisfying `IsTermwiseHarmonic` for the exchanged data. 

### `oscillatorPair_detTwist`

 For finite R, C with signs ε, ε′, consider the Fock space of R × C matrices, with sign ε_r ε′_c
at the entry (r, c). The representations h ↦ (det h)^γ ω(x ↦ hx) of U(ε) and g ↦ (det g)^γ′
ω(x ↦ xg⁻¹) of U(ε′) (`detTwist` along `pairHom ε ε'`), with ω = `New.Fock.realWeil`, form a
`New.OscillatorPair`. That is, they commute, and each is a `New.OscillatorRep`: the first for the
data below, the second for their `swap` (rows and columns exchanged). The data are
`New.FockDualPair.std` (sign 1, constants γ and γ′ + |R|). For this data E_ab acts on the rows by
∑_c raiseOp(a,c) lowerOp(b,c) + γ δ_ab and on the columns by −∑_r raiseOp(r,b) lowerOp(r,a) + γ′
δ_ab. 

### `principalMinor_kronecker_one`

 Let R, C be finite and g a complex R × R matrix. The `principalMinor` (determinant of the
principal submatrix) of `g ⊗ₖ 1` on the indices in R × C satisfying `p` is the product over the
columns `c` of the principal minors of `g` on the rows `r` with `p (r, c)`. 
