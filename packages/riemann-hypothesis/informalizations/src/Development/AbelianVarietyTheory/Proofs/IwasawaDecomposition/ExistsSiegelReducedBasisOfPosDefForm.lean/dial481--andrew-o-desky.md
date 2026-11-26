---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsSiegelReducedBasisOfPosDefForm.lean",
  "declarations": [
    "GlobalTheory.RedTh.RedBasis.exists_siegel_basis"
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

## A reduced basis for a positive definite form

[Theorem ARAK.0408](https://andrewodesky.com/rh/lean/GlobalTheory.RedTh.RedBasis.exists_siegel_basis/)

Let $Y$ be a free abelian group with a specified basis of rank $n\ge0$, and let $B:Y\times Y\to\mathbb R$ be a symmetric $\mathbb Z$-bilinear form. Assume it is positive definite: for every finite $\mathbb Z$-linearly independent family $(e_i)_{i=1}^t$ in $Y$ and every nonzero $c\in\mathbb R^t$, $$\sum_{i,j}c_ic_j B(e_i,e_j)>0.$$ There is a basis $b$ of $Y$, positive real numbers $d_i$, and a real upper triangular matrix $u$ such that $$u_{ii}=1,\qquad |u_{ij}|\le\frac12\ (i<j),\qquad d_i\le4d_{i+1}\ (0\le i<n-1),$$ $$\bigl(B(b_i,b_j)\bigr)_{i,j}=u^{\mathsf T}\operatorname{diag}(d_i)u.$$
