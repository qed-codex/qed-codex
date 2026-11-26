---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/UnitaryExistence/UnivChartOfStandardSmooth.lean",
  "declarations": [
    "GlobalTheory.LieLoc.lie_locally_free"
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

## Local bases for the Lie module of a smooth commutative group scheme

[Theorem AG.0609](https://andrewodesky.com/rh/lean/GlobalTheory.LieLoc.lie_locally_free/)

Let $R$ be a commutative ring and $G$ a commutative group scheme over $R$, smooth of relative dimension $n\ge0$. For every prime ideal $\mathfrak p\subset R$, there is $r\in R\setminus\mathfrak p$ such that the tangent vectors at the identity of $G_{R[1/r]}$ form a free $R[1/r]$-module with a basis of $n$ vectors.
