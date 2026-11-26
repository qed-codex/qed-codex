---
{
  "module": "src/ReciprocityTheory/ReductiveGroups/DiscreteSeries/TailIntegrals/PolynomialGrowthIntegrals.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.DS.Xi.quadraticSublevelDecay'"
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

## Decay of an integral involving a quadratic polynomial

[Theorem ALG.0618](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.DS.Xi.quadraticSublevelDecay'/)

For every real $0<\delta\le1/2$, there is $C\in\mathbb R$ such that, for all $c_0,c_1,c_2\in\mathbb C$, $$\int_1^2\bigl(1+|c_0+c_1t+c_2t^2|\bigr)^{-\delta}\,dt\le C\bigl(1+\max\{|c_0|,|c_1|,|c_2|\}\bigr)^{-\delta/2}.$$
