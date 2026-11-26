---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/AlgebraTools/CaMvpsCot.lean",
  "declarations": [
    "UpperTheory.V.AlgebraTools.mvPowerSeries_cotInd"
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

## Regularity and cotangent independence for power series over a DVR

[Theorem ALG.0484](https://andrewodesky.com/rh/lean/UpperTheory.V.AlgebraTools.mvPowerSeries_cotInd/)

Let $O$ be a discrete valuation domain, let $\varpi\in O$ be irreducible, and let $S$ be a finite set. Put $R=O[[X_s:s\in S]]$ and let $\mathfrak m$ be its maximal ideal. Then $R$ is a regular local ring, $$\dim R=|S|+1,$$ and the classes of $\varpi$ and the $X_s$ are linearly independent over $R/\mathfrak m$ in $\mathfrak m/\mathfrak m^2$.
