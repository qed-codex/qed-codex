---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/ReductionBoundsTorsion/ArithmeticGapBounds/ClosureBound.lean",
  "declarations": [
    "PositivityTheory.KB.SpectralGap.hilb_holds"
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

## An angle bound for intersections of three closed subspaces

[Theorem ALG.0582](https://andrewodesky.com/rh/lean/PositivityTheory.KB.SpectralGap.hilb_holds/)

Let $H$ be a real Hilbert space and let $W_1,W_2,W_3,K_{12},K_{13},K_{23}$ be closed linear subspaces with $K_{ij}\subseteq W_i\cap W_j$. Suppose $$|\langle u,v\rangle|\le\frac15\|u\|\|v\|$$ for each of the following ranges: $u\in W_1\cap K_{12}^{\perp}$ and $v\in W_2$; $u\in W_3\cap K_{13}^{\perp}$ and $v\in W_1$; $u\in W_3\cap K_{23}^{\perp}$ and $v\in W_2$. Then $$|\langle v,w\rangle|\le\frac25\|v\|\|w\|$$ whenever $v\in(W_1\cap W_2)\cap(W_1\cap W_2\cap W_3)^{\perp}$ and $w\in W_1\cap W_3$.
