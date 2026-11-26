---
{
  "module": "src/Development/AutomorphicArithmetic/OrbitLabellings/KvalGeOfNormMfactMulCoeffLe.lean",
  "declarations": [
    "UpperTheory.kvalGe_of_norm_mfact_mul_coeff_le"
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

## A coefficient bound for products of matrix minors acting on a power series

[Theorem PHT.0337](https://andrewodesky.com/rh/lean/UpperTheory.kvalGe_of_norm_mfact_mul_coeff_le/)

Let $\ell$ be prime, $S$ a finite set, $N_0,N_1\ge0$ integers, and $\nu_s$ a Young diagram for every $s\in S$. Write $\mathbb C_\ell$ for the completion of an algebraic closure of $\mathbb Q_\ell$, with absolute value normalized by $|\ell|_\ell=\ell^{-1}$. Let $$\Theta(Z)=\sum_\kappa a_\kappa Z^\kappa\in\mathbb C_\ell[[Z_{sab}:s\in S,\ 0\le a<N_0,\ 0\le b<N_1]],\qquad B\in\mathbb R.$$ Assume $$|\kappa!a_\kappa|_\ell\le\ell^{-B}\quad\text{whenever}\quad\sum_{a,b}\kappa_{sab}=|\nu_s|\quad(s\in S),$$ where $\kappa!=\prod_{s,a,b}\kappa_{sab}!$ and $|\nu_s|$ is the number of cells.

For each column $c$ of $\nu_s$, of height $h_{sc}$, choose a strictly increasing map $I_{sc}:\{0,\ldots,h_{sc}-1\}\to\{0,\ldots,N_1-1\}$. With independent variables $X_{sia}$ for $s\in S$, $i\ge0$ and $0\le a<N_0$, put $$G(X,Z)=\prod_{s,c}\det\left(\sum_{a=0}^{N_0-1}X_{sia}Z_{sa,I_{sc}(k)}\right)_{0\le i,k<h_{sc}}.$$ Every coefficient of the polynomial $$\left.G(X,\partial/\partial Z)\Theta(Z)\right|_{Z=0}$$ has $\ell$-adic norm at most $\ell^{-B}$.
