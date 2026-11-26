---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExistsIsHilbertSchmidtOrthonormalApply.lean",
  "declarations": [
    "GlobalTheory.exists_isHilbertSchmidt_orthonormal_apply"
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

## A Hilbert-Schmidt operator with prescribed orthonormal images

[Theorem ALG.0659](https://andrewodesky.com/rh/lean/GlobalTheory.exists_isHilbertSchmidt_orthonormal_apply/)

Let $H,K$ be complex Hilbert spaces, let $J$ be any index set, and let $(u_j)_{j\in J}$ be an orthonormal family in $H$. Given $w_j\in K$ satisfying $\sum_{j\in J}\|w_j\|^2<\infty$, there is a bounded complex-linear Hilbert–Schmidt operator $G:H\to K$ such that $$G u_j=w_j\quad(j\in J),\qquad Gv=0\quad\text{if }\langle u_j,v\rangle=0\text{ for all }j\in J.$$
