---
{
  "module": "Paper/Identity.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Identity.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Identity.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, section "Two crossing wires": the identity

The polynomials B(r,n) and C(r,n) are Nc.Cross.mB and mC (with y an element of a ring), the matrix M is Nc.Cross.matM and
Ψ = det M is Nc.Cross.psi. A state enters them as the pair of the increasing enumerations of its two sets (Nc.Cross.word).


### `mem_stateClass`

 "Fix sizes μ, ν and energies e₁, e₂, and let Σ₁, Σ₂ be the sets of states with size and energy (μ, e₁), respectively (ν, e₂)":
the set Nc.Cross.states μ e. 

### `coeff_mk_mul_zero`

 The coefficients of a power series times 1 + at. 

### `meixner_B`

 "Let B(r,n) and C(r,n) be the coefficients of tⁿ in (1+t)^r/(1+yt)^(r+1) and (1+yt)^r/(1+t)^(r+1)." For B: the recursion
that defines Nc.Cross.mB gives the coefficients of the first series. 

### `meixner_C`

 The same sentence for C: the recursion that defines Nc.Cross.mC gives the coefficients of (1+yt)^r/(1+t)^(r+1). 

### `meixner_reciprocal`

 "They are polynomials in y, and yⁿ B(r,n)|_{1/y} = C(r,n)." Here z is an inverse of y. 

### `meixner_reciprocal'`

 The same relation read backwards: yⁿ C(r,n)|_{1/y} = B(r,n). 

### `tele`

 The telescoping sum. 

### `eq_orth`

 **Paper: display eq:orth.** "(1−y) ∑_{r<R} y^r B(r,i) B(r,j) ≡ [i=j] y^i (mod y^R)." Here y is any element of any
commutative ring; the paper's case is the variable y of ℤ[y]. 

### `prop_identity_blocks`

 Proof of Proposition prop:identity, the coefficients: "So the block of rows a, d and columns c, b is congruent modulo X^(2R)
to FDG". Here F = facA, G = facB, K is the paper's R, and the block is Nc.Cross.blU; its part at (d,b) is treated by (eq:orth).
The other half, "and in the same way that of rows c, b and columns a, d to −G′DF′", is this theorem for the states with I and J
exchanged, transposed. 

### `entries`

 Unfolds an entry of the matrices M and of the multipliers. 

### `prop_identity_exchange`

 Proof of Proposition prop:identity, reflection: "Substitute 1/X for X and multiply the rows and the columns of a, c by
X^(2i+1), those of d by (y−1)y^i and those of b by y^(i+1). The relation between B and C shows that one obtains the matrix M in
which the sites b and d are exchanged (the new site d holds s_b), with the rows and columns of the new d multiplied by 1−y."
Entry by entry; z is the inverse of x, the multipliers are Nc.Cross.scal and scal', and exch exchanges the sites. 

### `prop_identity_exchange_det`

 Proof of Proposition prop:identity, reflection: "Rows and columns are permuted alike, so there is no sign." So the product of
all multipliers times Ψ(1/X; s_a, s_b, s_c, s_d) is (1−y)^(2ν) Ψ(X; s_a, s_d, s_c, s_b). 

### `prop_identity_reflection`

 Proof of Proposition prop:identity, reflection: "The multipliers at a, c, d, b contain X to the powers e₁, e₁, e₂−2ν, e₂+2ν, in
all Θ, and the factors (y−1)^(2ν) and (1−y)^(2ν) on the two sides cancel in ℤ[X]. So
X^Θ Ψ(1/X; s_a, s_b, s_c, s_d) = Ψ(X; s_a, s_d, s_c, s_b)", Θ = 2(e₁+e₂).
Here x is an element of a domain with inverse z and x² ≠ 1; the paper's case is x = X in the field of fractions of ℤ[X]. 

### `prop_identity_one`

 Proof of Proposition prop:identity, X = 1: "for states in the given classes, Ψ|_{X=1} is a sign, depending on μ, ν only,
times [J_c = I_a, I_c = J_a, J_b = I_d, I_b = J_d]." 

### `exists_products`

 A sum of products over a finite index set is a sum of r products, if r is at least the size of the index set. 

 ### The coefficients: the expansion

In this section X = M₁, Y = M₂, A = F, A' = F′, B = G, B' = −G′, and l is the diagonal of D. 

### `prop_identity_schur`

 Proof of Proposition prop:identity, the coefficients: "Up to a sign that depends on R only, the determinant of such a matrix
equals that of" the matrix with the block rows (M₁, 0, F, 0), (0, M₂, 0, G′), (0, DG, −1, 0), (DF′, 0, 0, 1) "(a Schur
complement)". Here the last two block rows are (0, −DB, 1, 0) and (−DA', 0, 0, 1), and there is no sign. 

### `prop_identity_expand`

 Proof of Proposition prop:identity, the coefficients: "Each of the last 2R rows is the sum of its part in DG, respectively
DF′, and its entry ±1. Expand by multilinearity, and let T₁, T₂ be the sets of rows of the third and of the fourth block row for
which the first part is taken." The term of T = (T₁, T₂) is the product of the entries of D in T, which is X^E(T) in the paper,
times the determinant of the matrix Nc.Cross.termMat T, in which the rows outside T have only their entry 1. 

### `prop_identity_term_zero`

 Proof of Proposition prop:identity, the coefficients: "This vanishes if |T₁| ≠ |T₂|, as the blocks are then not square". (In
Lean the rows outside T are kept, with their entry 1; the form with two blocks is Nc.Cross.termMat_eq_glue.) 

### `prop_identity_term_product`

 Proof of Proposition prop:identity, the coefficients: "otherwise it is a polynomial in X depending on (s_a, s_d) times one
depending on (s_b, s_c)". For every T the determinant of the term is a function of (X, A, A') times a function of (Y, B, B'). 

### `prop_identity_term_count`

 Proof of Proposition prop:identity, the coefficients: "The T with |T₁| = |T₂| and E(T) ≤ N are at most P(N) states". 

### `prop_identity_near`

 Proof of Proposition prop:identity, the coefficients: "… and the degree N − E(T) can be split between the two factors in at
most N+1 ways." So the coefficient of X^N of the determinant of a matrix with the diagonal blocks X, Y and the other blocks ADB,
B'DA', D = diag(X^(2r+1)), is a sum, over the T with |T₁| = |T₂| and E(T) ≤ N and over N+1 degrees, of products of a function of
(X, A, A') and one of (Y, B, B'). 

### `prop_identity_coefficients`

 Proof of Proposition prop:identity, the coefficients: "This proves (b)": the coefficient of X^N in Ψ is a sum of at most
(N+1)P(N) products of a function of (s_a, s_d) and one of (s_b, s_c). "This is used only for the coefficients of degree at most
N < 2R", with R = N + 1. 

### `prop_identity_reverse`

 The reflection identity for polynomials: the reverse of Ψ(X; s_a, s_b, s_c, s_d) is Ψ(X; s_a, s_d, s_c, s_b), up to powers
of X. 

### `prop_identity_reflection_coeff`

 Proof of Proposition prop:identity, reflection: "Hence deg Ψ ≤ Θ, and the coefficient of X^N at (s_a, s_b, s_c, s_d) is that
of X^(Θ−N) at (s_a, s_d, s_c, s_b)." 

### `prop_identity`

 **Paper: Proposition prop:identity.** "Let Θ = 2(e₁+e₂). There are integral tensors Ψ_0, …, Ψ_Θ such that, all functions
below being integer valued, (a) ∑_N Ψ_N is ⟨|Σ₁|⟩_ac ⟨|Σ₂|⟩_bd; (b) Ψ_N is a sum of at most (N+1)P(N) products of a function of
(s_a, s_d) and one of (s_b, s_c); (c) Ψ_N is a sum of at most (N′+1)P(N′) products of a function of (s_a, s_b) and one of
(s_c, s_d), where N′ = Θ − N." 
