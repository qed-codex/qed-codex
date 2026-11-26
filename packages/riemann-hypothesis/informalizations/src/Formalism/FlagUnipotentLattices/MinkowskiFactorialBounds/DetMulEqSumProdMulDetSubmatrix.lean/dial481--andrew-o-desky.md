---
{
  "module": "src/Formalism/FlagUnipotentLattices/MinkowskiFactorialBounds/DetMulEqSumProdMulDetSubmatrix.lean",
  "declarations": [
    "Formalism.HermitianLatticeCounting.P.norm_det_mul_le"
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

## A determinant bound from entries and maximal minors

[Theorem ALG.0967](https://andrewodesky.com/rh/lean/Formalism.HermitianLatticeCounting.P.norm_det_mul_le/)

Let $t,N\ge0$, $X\in M_{t\times N}(\mathbb C)$, $Y\in M_{N\times t}(\mathbb C)$, and $\rho,Q\in\mathbb R$ satisfy $\rho\ge1$, $Q\ge0$, $$|X_{ik}|\le\rho\quad\text{for all }i,k,\qquad |\det(Y_{f(i),j})_{1\le i,j\le t}|\le Q\quad\text{for every }f:\{1,\ldots,t\}\to\{1,\ldots,N\}.$$ Then $$|\det(XY)|\le N!\,\rho^NQ.$$
