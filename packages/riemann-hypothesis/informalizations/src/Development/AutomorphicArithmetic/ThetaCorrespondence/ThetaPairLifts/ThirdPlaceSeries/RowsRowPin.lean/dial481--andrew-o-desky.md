---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowsRowPin.lean",
  "declarations": [
    "Formalism.L2.Rows.LowerMapTieTwAlt"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## Coordinate contractions of lower period maps

[Definition / hypothesis ARAK.D210](https://andrewodesky.com/rh/lean/Formalism.L2.Rows.RowPinMinAlt/)

Use ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)), ([Symmetric finite levels and column identifications](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.FormsTiedSym/)), ([Twisted terminal lattices and period values](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.SymmetricTwistedTiltedData/)) and ([Hermitian duality of transported Weyl lattices](https://andrewodesky.com/rh/lean/GlobalTheory.T.transported_weylLattice_hermitianDuality/)). Write $N=N_m$, $n=N-1$, and $\lambda^0_{u,\tau},\gamma^0_{u,\tau}$ for the specified terminal and period dominant integer weights. Put $c_0=\lfloor m(t+1)/2\rfloor$ and $\lambda=\lambda^0-c_0$, $\gamma=\gamma^0-c_0$, subtracting the same integer from every entry. In the formulas below $\lambda_i,\gamma_i$ are the entries of these shifted integer weights, indexed from zero. Their determinant shifts are $s_{\lambda,\tau}=\lambda_{\tau,N-1}$ and $s_{\gamma,\tau}=\gamma_{\tau,n-1}$; for a zero-length weight its shift is zero. The polynomial weight spaces use the nonnegative differences from the last entry.

Here is the coefficient contraction used in the hypothesis. In one embedding put $a_i=\gamma_i-\lambda_{i+1}$, $b_i=\lambda_i-\gamma_i$, $d=\sum_i a_i$ and $$R_i=[\lambda_{i+1},\min(\lambda_i,\lambda_{i+1}+d)]\cap\mathbb Z,\qquad c=\prod_{i=0}^{n-1}\prod_{v\in R_i\setminus\{\gamma_i\}}\prod_{j=0}^{n-1}(v-i-\gamma_j+j).$$ For a polynomial matrix $X$, let $\Delta_{i+1}$ be its leading minor of size $i+1$ and let $Z_i$ be the minor with rows $0,\ldots,i-1,n$ and columns $0,\ldots,i$. Put $$\Xi=\prod_{i=0}^{n-1}\Delta_{i+1}^{\max(a_i,0)}Z_i^{\max(b_i,0)},\qquad \kappa=\frac{B_{\rm Fock}(\Xi,\Xi)}{B_{\rm Fock}(v_\lambda,v_\lambda)}.$$ Use $B_{\rm Fock}(P,Q)=[P,Q]_{\rm fac}$ from ([Bilinear factorial pairing of polynomials](https://andrewodesky.com/rh/lean/Formalism.L2.G.Model.TS.fockR/)); $v_\lambda$ is the extremal polynomial in ([Hermitian duality of transported Weyl lattices](https://andrewodesky.com/rh/lean/GlobalTheory.T.transported_weylLattice_hermitianDuality/)). First retain precisely the monomials whose last-row exponents in columns $i<n$ are $\max(b_i,0)$ and whose whole last column has exponent zero, and delete that row and column. Project the result to the polynomial weight space for $\gamma$ using its Fock Gram matrix: for a basis $(v_i)$ and Gram matrix $G$, the projection is $P\mapsto\sum_{i,j}(G^{-1})_{ij}B_{\rm Fock}(v_j,P)v_i$. Multiply by $c\kappa$. Apply these maps independently to the variable blocks at all embeddings; call the resulting polynomial map $\mathcal B_u$.

For a block polynomial $P$, integer shifts $s_\tau$, matrices $M_\tau$ and invertible frames $y_\tau$, define $$F_{s,M}(P)(y)=\left(\prod_\tau\det(M_\tau y_\tau)^{s_\tau}\right)P((M_\tau y_\tau)_\tau).$$ The terminal polynomial span is the span of products of one-embedding weight polynomials, with disjoint variable blocks. Let $I:E^n\to E^N$ be the prescribed inclusion of the period space. For the selected terminal vector $z_0$, let $B_z$ have first $n$ columns $I$ and last column $z_0/T_u$. Put $M_\tau=\tau(B_z^{-1})$.

Hypothesis (lower period contractions). For every source $u$, if $B_z$ is invertible over $E$, every terminal input $\psi$, period class $c$ and polynomial $P$ in the terminal polynomial span satisfy the following implication: if the terminal coordinate function of $\psi$ at $c$ is $F_{s_\lambda,M}(P)$ on every terminal frame, then the coordinate function of its lower period image at $c$ is $$F_{s_\gamma,1}(\mathcal B_uP).$$ The same implication holds for each nonbase twist $\mu$ realized by an actual coefficient place, provided $m\ge1$, using its selected terminal vector, terminal input, period class, coordinate functions and lower period map. The twisted frame is obtained by the inverse twisted-to-base frame identification followed by the base frame coordinates; at the terminal stage these are the endpoint coordinates of ([Symmetric finite levels and column identifications](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.FormsTiedSym/)).

Require also the base-twist source-pairing normalization of ([Period, measure and twist comparisons](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Ties/)).
