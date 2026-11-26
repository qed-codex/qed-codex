---
{
  "module": "src/ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/InterBridgeA.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.G.Geo.logAbsLocInt"
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

## Local integrability of logarithms of analytic functions

[Theorem AG.1525](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.logAbsLocInt/)

Let $D\ge0$, let $U\subseteq\mathbb C^D$ be open, and let $f:\mathbb C^D\to\mathbb C$ be analytic in a neighborhood of each point of $U$. Then $$z\longmapsto\log|f(z)|$$ is locally integrable on $U$ with respect to Lebesgue measure. Here the logarithm is assigned the value $0$ at $f(z)=0$.
