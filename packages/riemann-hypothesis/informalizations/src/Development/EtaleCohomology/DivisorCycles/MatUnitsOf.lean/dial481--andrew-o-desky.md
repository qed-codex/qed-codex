---
{
  "module": "src/Development/EtaleCohomology/DivisorCycles/MatUnitsOf.lean",
  "declarations": [
    "LateralTheory.DivDb.MatrixUnitConstruction.partner"
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

## An inverse between nonzero matrix corners

[Theorem ALG.0335](https://andrewodesky.com/rh/lean/LateralTheory.DivDb.MatrixUnitConstruction.partner/)

Let $C$ be a field, $A\subseteq M_N(C)$ a unital $C$-subalgebra, and $p_1,\ldots,p_n\in A$ nonzero pairwise orthogonal idempotents with $\sum_i p_i=1$. Assume $$p_iAp_i=Cp_i\quad(1\le i\le n),$$ and assume that $Y\in A$ is zero whenever $aY$ is nilpotent for every $a\in A$. For any nonzero $Y\in A$ with $p_iY=Y=Yp_j$, there is $w\in A$ such that $$p_jwp_i=w,\qquad Yw=p_i,\qquad wY=p_j.$$
