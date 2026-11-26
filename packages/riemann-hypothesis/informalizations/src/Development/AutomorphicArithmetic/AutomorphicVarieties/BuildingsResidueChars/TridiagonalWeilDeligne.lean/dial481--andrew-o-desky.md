---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/BuildingsResidueChars/TridiagonalWeilDeligne.lean",
  "declarations": [
    "UpperTheory.tridiagonal_weil_deligne"
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

## Diagonalization of a finite triangular group action

[Theorem REP.0288](https://andrewodesky.com/rh/lean/UpperTheory.tridiagonal_weil_deligne/)

Let $I$ be a group, $W$ a complex vector space, $n\ge0$, and $\rho:I\to\operatorname{End}_{\mathbb C}(W)$ a multiplicative representation with finite image. Suppose there is a basis $(b_1,\ldots,b_n)$ in which every $\rho(s)$ is upper triangular, with diagonal entries $d_1(s),\ldots,d_n(s)$. There is a basis $(b'_1,\ldots,b'_n)$ such that $$[\rho(s)]_{b'}=\operatorname{diag}(d_1(s),\ldots,d_n(s))\qquad(s\in I).$$
