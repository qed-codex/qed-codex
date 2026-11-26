---
{
  "module": "src/ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/FundamentalDomains/CountingExponentialSumHolds.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.G.FD.counting_exponential_sum_holds"
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

## A small exponential sum from polynomial counting

[Theorem ANT.1082](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.FD.counting_exponential_sum_holds/)

Let $K,N,w\in\mathbb R$ satisfy $K,N\ge1$ and $w\ge0$. Let $I$ be a set and $t:I\to\mathbb R$ satisfy $$t_j>w+N\log(2KN)+N+2\qquad(j\in I).$$ Suppose that for every real $T\ge1$, the set $\{j:t_j\le T\}$ is finite and has cardinality at most $(KT)^N$. Then $\sum_{j\in I}e^{-\pi t_j}$ is summable and $$2^{w/2}\sum_{j\in I}e^{-\pi t_j}<\frac12.$$
