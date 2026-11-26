---
{
  "module": "src/ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/InterGoodE.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.G.Geo.exists_linear_normalization"
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

## Integral normalization by finitely many linear combinations

[Theorem ALG.1624](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.exists_linear_normalization/)

Let $k$ be an infinite field, $R$ a commutative $k$-algebra, $T$ a finite set, and $v_t\in R$ for $t\in T$. Fix $m\ge0$. Assume that for every $r>m$ and every matrix $(a_{jt})\in k^{\{1,\ldots,r\}\times T}$ the $r$ elements $$\sum_{t\in T}a_{jt}v_t\qquad(1\le j\le r)$$ are algebraically dependent over $k$. There are $r\le m$ and coefficients $b_{jt}\in k$ such that every $v_t$ is integral over $$k\!\left[\sum_t b_{1t}v_t,\ldots,\sum_t b_{rt}v_t\right]\subseteq R.$$
