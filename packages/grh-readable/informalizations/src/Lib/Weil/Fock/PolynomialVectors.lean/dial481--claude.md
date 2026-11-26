---
{
  "module": "src/Lib/Weil/Fock/PolynomialVectors.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Fock/PolynomialVectors.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Fock/PolynomialVectors.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Polynomial vectors in Fock space: inner product, density and Weil derivative

The polynomial vectors v_P = `New.Fock.polyVector` ε P lie in the Fock space `New.Fock.fockSpace`
with signs ε. On this space U(ε) acts by the Weil representation ω₀ = `New.Fock.realWeil`.

## Main definitions and results

* `New.Fock.fockMatrixCoeff_raiseOp`, `New.Fock.fockMatrixCoeff_lowerOp`: how the operators
  `New.Fock.raiseOp`, `New.Fock.lowerOp` (multiplication by X_a or differentiation, according to
  the sign ε_a) move across ω₀(u) in a matrix coefficient `New.Fock.fockMatrixCoeff`.
* `New.Fock.fockInner_X_mul`, `New.Fock.fockInner_polyVector`: X_i is adjoint to ∂_i, so ⟨v_P, v_Q⟩
  is the Fischer pairing (P̄(∂)Q)(0). For monomials see `New.Fock.fockInner_polyVector_monomial`.
* `New.Fock.denseRange_polyVector`: the vectors v_P are dense.
* `New.Fock.hasDerivAt_realWeil`: along a curve in U(ε) through 1 with velocity Y, ω₀ has derivative
  v_Q on v_P, where Q = `New.Fock.weilDeriv` ε Y P.

The action of block diagonal isometries on the v_P by substitution is
`New.Fock.realWeil_polyVector_of_mem_blockDiagAlg` in `Lib.Weil.DualPair.WeilAction`.

Notions from other files:
* `New.Fock.vacVector`: The Gaussian exp(−|x|²/2) regarded as an element of the Fock space.
* `New.USign`: For a vector of signs ε, the unitary group U(J) of the diagonal matrix J=diag(ε).

## Relation to the literature

Known; see `Lib.Weil.Fock.OscillatorPair` for sources.


### `MvPolynomial.sesqForm_apply_eq_zero_of_mul_X_eq_pderiv`

 A sesquilinear form B on complex polynomials vanishes if B(1, 1) = 0 and multiplication by each
variable X_j on either side moves to the derivative ∂_j on the other side:
B(Q, P X_j) = B(∂_j Q, P) and B(Q X_j, P) = B(Q, ∂_j P). 

 ## The inner product of polynomial vectors and their density 

### `realWeil_vacVector_apply_zero`

 For u in U(ε), the value at 0 of ω₀(u) applied to the vacuum `New.Fock.vacVector` is the inverse
of the principal minor of u on the coordinates of sign −1. 

### `fockMatrixCoeff`

 The matrix coefficient ⟨v_P, ω₀(u)v_Q⟩ of the Weil representation, for u in U(ε) and complex
polynomials P, Q with Fock vectors v_P, v_Q (`New.Fock.polyVector`, applied through the coercion
of polynomials to `New.Fock.fockSpace`). It is conjugate-linear in P. 

### `fockMatrixCoeff_heisenbergDeriv_single`

 For u in U(ε), polynomials P, Q, an index j and c in ℂ, the Heisenberg derivative
D_c = `New.Fock.heisenbergDeriv` ε (c e_j) (v_{D_c P} is the derivative at t = 0 of
`New.Fock.realHeisenbergOp` (t c e_j) v_P) on the right of the matrix coefficient ⟨v_Q, ω₀(u) ·⟩
becomes the derivative in the direction −c times column j of u on the left: ⟨v_Q, ω₀(u) v_{D_c
P}⟩ = conj ⟨ω₀(u) v_P, v_{D' Q}⟩, where D' = `New.Fock.heisenbergDeriv` ε (−c u e_j). 

### `fockMatrixCoeff_raiseOp`

 For u in U(ε) with entries u_ij, an index j and polynomials P, Q, the operator
A_j = `New.Fock.raiseOp` ε j (X_j if ε_j = 1, else −∂_j) on the right of the matrix coefficient
⟨v_Q, ω₀(u) ·⟩ becomes Σ_i u_ij ε_i B_i on the left, where B_i = `New.Fock.lowerOp` ε i
(∂_i if ε_i = 1, else X_i): ⟨v_Q, ω₀(u) v_{A_j P}⟩ = Σ_i u_ij ε_i ⟨v_{B_i Q}, ω₀(u) v_P⟩. 

### `fockMatrixCoeff_lowerOp`

 For u in U(ε) with entries u_ij, an index j and polynomials P, Q, the operator
B_j = `New.Fock.lowerOp` ε j (∂_j if ε_j = 1, else X_j), times ε_j, on the right of the matrix
coefficient ⟨v_Q, ω₀(u) ·⟩ becomes Σ_i conj(u_ij) A_i on the left, where
A_i = `New.Fock.raiseOp` ε i (X_i if ε_i = 1, else −∂_i):
ε_j ⟨v_Q, ω₀(u) v_{B_j P}⟩ = Σ_i conj(u_ij) ⟨v_{A_i Q}, ω₀(u) v_P⟩. 

### `fockMatrixCoeff_raiseOp_lowerOp`

 Both relations of `New.Fock.fockMatrixCoeff_raiseOp` and `New.Fock.fockMatrixCoeff_lowerOp`:
for u in U(ε), polynomials P, Q and an index j, with A_a = `New.Fock.raiseOp` ε a and
B_a = `New.Fock.lowerOp` ε a, ⟨v_Q, ω₀(u) v_{A_j P}⟩ = Σ_i u_ij ε_i ⟨v_{B_i Q}, ω₀(u) v_P⟩ and ε_j
⟨v_Q, ω₀(u) v_{B_j P}⟩ = Σ_i conj(u_ij) ⟨v_{A_i Q}, ω₀(u) v_P⟩. 

### `fockInner_X_mul`

 Multiplication by X_i is adjoint to the derivative ∂_i for the inner product
`New.Fock.fockInner` of polynomial vectors: ⟨v_{X_i P}, v_Q⟩ = ⟨v_P, v_{∂_i Q}⟩. 

### `fockInner_polyVector`

 For polynomials P, Q, the inner product ⟨v_P, v_Q⟩ is the Fischer pairing (P̄(∂)Q)(0), where P̄
has the complex conjugate coefficients of P. 

### `fockInner_polyVector_monomial`

 The Fock vectors of monomials are orthogonal, and the vector of the monomial `X ^ μ` has
squared norm `μ! = ∏ i, (μ i)!`. 

### `denseRange_polyVector`

 The Fock vectors v_P of the polynomials P are dense in the Fock space with signs ε. 


## The derivative of the real Weil representation on polynomial vectors

`New.Fock.hasDerivAt_realWeil`: along a curve in U(ε) through 1 with velocity Y, ω₀ acts on v_P with
derivative v_Q, where Q = ∑ Y_ab A_a B_b P (`New.Fock.weilDeriv`). The two sides are compared
through their inner products with the dense family of the v_R, using
`New.Fock.fockMatrixCoeff_raiseOp` and `New.Fock.fockMatrixCoeff_lowerOp`.


### `hasDerivAt_det_posProj_add_mul`

 For a curve γ in U(ε) with γ(0) = 1 whose matrix has derivative Y at 0, the determinant
det(P₊ + P₋γ(t)) has derivative tr(P₋Y) at 0. Here P₊ = `New.Fock.posProj` ε is the projection
on the coordinates of sign 1 and P₋ = 1 − P₊; the determinant is the minor of γ(t) on the
coordinates of sign −1 (`New.Fock.principalMinor_sign_eq_det`). 

### `star_mul_sign_eq_neg_sign_mul_of_hasDerivAt`

 For a curve γ in U(ε) with γ(0) = 1 whose matrix has derivative Y at 0, the matrix Y is
skew-adjoint for the signs: conj(Y_ji) ε_j = −ε_i Y_ij for all indices i, j. 

### `differentiableAt_realWeil_polyVector`

 For a curve γ in U(ε) with γ(0) = 1 whose matrix has derivative Y at 0, and a polynomial P,
the curve t ↦ `New.Fock.realWeil`(γ(t))v_P in the Fock space is differentiable at 0. 

### `valueAt_zero_polyVector_glOp_one`

 The polynomial vector of A_a B_b 1 = `New.Fock.glOp` ε a b 1 (A_a = X_a or −∂_a, B_b = ∂_b or
X_b by the signs) takes at 0 the value −1 if a = b has sign −1, and 0 otherwise: minus the (b, a)
entry of 1 − `New.Fock.posProj` ε. 

### `fockInner_raiseOp_eq_of_hasDerivAt`

 The relation `New.Fock.fockMatrixCoeff_raiseOp`, differentiated along a
curve γ in U(ε) with γ(0) = 1 whose matrix has derivative Y at 0. Here `hD` says that ⟨v_Q, D P⟩
is the derivative at 0 of the matrix coefficient ⟨v_Q, ω₀(γ(t))v_P⟩ for all polynomials Q, P. Then
⟨v_Q, D(A_j P)⟩ = Σ_i Y_ij ε_i ⟨v_{B_i Q}, v_P⟩ + ε_j ⟨v_{B_j Q}, D P⟩, with
A_a = `New.Fock.raiseOp` ε a and B_a = `New.Fock.lowerOp` ε a. 

### `fockInner_lowerOp_eq_of_hasDerivAt`

 The relation `New.Fock.fockMatrixCoeff_lowerOp`, differentiated along a
curve γ in U(ε) with γ(0) = 1 whose matrix has derivative Y at 0, with `hD` as in
`fockInner_raiseOp_eq_of_hasDerivAt`: ε_j ⟨v_Q, D(B_j P)⟩ = Σ_i conj(Y_ij) ⟨v_{A_i Q}, v_P⟩ +
⟨v_{A_j Q}, D P⟩. 

### `hasDerivAt_realWeil`

 If γ is a curve in U(ε) with γ(0) = 1 whose matrix has derivative Y at 0, then
t ↦ `New.Fock.realWeil`(γ(t)) v_P has derivative v_Q at 0 in the Fock space `New.Fock.fockSpace` ε.
Here Q = `New.Fock.weilDeriv` ε Y P = Σ_{a,b} Y_ab A_a B_b P is a polynomial, viewed in the Fock
space as v_Q, and A_a B_b is the ε-dependent quadratic operator in the X_i and ∂_i given by
`New.Fock.glOp` ε a b.

A special case of the standard infinitesimal action of the oscillator representation in the
Bargmann–Fock model by quadratic operators in X_i and ∂_i. 
