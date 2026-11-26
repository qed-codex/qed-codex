---
{
  "module": "src/Formalism/HermitianCurvature/HermitianCurvatureProofs/LduDecompositionExists.lean",
  "declarations": [
    "Formalism.FourierDecayAlt.P.ldu_decomposition_exists"
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

## Triangular factorization from invertible leading minors

[Theorem ALG.0736](https://andrewodesky.com/rh/lean/Formalism.FourierDecayAlt.P.ldu_decomposition_exists/)

Let $R$ be a commutative ring, $r\ge0$, and $M\in M_r(R)$. Write $\Delta_l$ for the determinant of the leading $l\times l$ submatrix, with $\Delta_0=1$. If every $\Delta_l$ with $0\le l<r$ is a unit, then there are lower and upper unitriangular matrices $L,U$ and $d_0,\ldots,d_{r-1}\in R$ such that $$M=L\operatorname{diag}(d_0,\ldots,d_{r-1})U,\qquad\Delta_{l+1}=d_l\Delta_l\quad(0\le l<r).$$
