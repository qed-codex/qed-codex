---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/TransversalZerosLiftOfIsAdicComplete.lean",
  "declarations": [
    "GlobalTheory.KeyKa.etZ_lift_of_isAdicComplete"
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

## Transverse zero sections over a complete discrete valuation ring

[Theorem AV.0357](https://andrewodesky.com/rh/lean/GlobalTheory.KeyKa.etZ_lift_of_isAdicComplete/)

Let $O$ be a complete discrete valuation ring with residue field $k$. Fix theta data over $O$ and $k$ as described below, with the latter obtained from the former by reduction. Let their common dimension be $g\ge1$, let $n,d\ge0$, and let $s_1,\ldots,s_g$ be sections of $L^{\otimes n}$ with reductions $\bar s_1,\ldots,\bar s_g$.

Suppose the common zero set of the $\bar s_i$ consists exactly of $d$ distinct $k$-rational sections $\bar z_a$. For each $a$, choose a line-bundle chart containing $\bar z_a$, on which all $\bar s_i$ vanish at $\bar z_a$ and their derivative matrix in the chosen tangent basis has invertible determinant. Then there exist $d$ sections $z_a\in A(O)$ and line-bundle charts containing their whole images, on which all $s_i$ vanish and their derivative determinants are units. The $z_a$ are distinct in every fibre, and their images cover the common zero set of the $s_i$.
