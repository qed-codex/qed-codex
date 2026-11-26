---
{
  "module": "src/ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/FundamentalDomains/SchwarzLemmaBallHolds.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.G.FD.schwarzLemmaBall_holds"
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

## A quantitative nonvanishing ball for a holomorphic function

[Theorem ALG.0727](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.FD.schwarzLemmaBall_holds/)

Let $V$ be a complex normed vector space, let $\rho>0$ and $S\in\mathbb R$, and let $\gamma:V\to\mathbb C$ be complex differentiable on the closed ball $\overline B(0,\rho)$. If $$|\gamma(Z)|\le e^{9/4}S\quad(\|Z\|\le\rho),\qquad S/2<|\gamma(0)|\le S,$$ then $$\gamma(Z)\ne0\qquad(\|Z\|<\rho/21).$$
