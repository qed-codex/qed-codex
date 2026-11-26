---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/TensorHomCubes/DedekindSR.lean",
  "declarations": [
    "UpperTheory.V.KL.dedekindSR"
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

## Stable range two for a Dedekind domain

[Theorem ALG.0469](https://andrewodesky.com/rh/lean/UpperTheory.V.KL.dedekindSR/)

Let $R$ be a commutative Dedekind domain. For every $n\ge2$ and every unimodular row $(r_0,\ldots,r_n)\in R^{n+1}$, there are $t_0,\ldots,t_{n-1}\in R$ such that $$(r_0+t_0r_n,\ldots,r_{n-1}+t_{n-1}r_n)$$ is unimodular. A row is unimodular if its entries generate the unit ideal.
