---
{
  "module": "src/Development/AutomorphicArithmetic/OrbitLabellings/ExistsMaxFlowAttainedAndIsOptDual.lean",
  "declarations": [
    "UpperTheory.exists_maxFlow_attained_and_isOptDual"
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

## Attainment and duality for a cyclic linear program

[Theorem ALG.0875](https://andrewodesky.com/rh/lean/UpperTheory.exists_maxFlow_attained_and_isOptDual/)

Let $\ell\ge3$ and $d\ge1$ be integers, let $D:\mathbb Z/d\mathbb Z\to\mathbb R_{\ge0}$, and put $J=\{i\in\mathbb Z:0\le i<d,\ i\text{ odd}\}$. Consider nonnegative families $x_{s,i}$, indexed by $s\in\mathbb Z/d\mathbb Z$ and integers $i\ge0$, satisfying $$\sum_{i\in J}\ell^i x_{s,i}+\sum_{i\in J}x_{s-i,i}\le D(s)\qquad(s\in\mathbb Z/d\mathbb Z).$$ The supremum $M$ of $\sum_s\sum_{i\in J}x_{s,i}$ is attained. There is also $\sigma:\mathbb Z/d\mathbb Z\to[0,1]$ with $$\ell^i\sigma(s)+\sigma(s+i)\ge1\quad(s\in\mathbb Z/d\mathbb Z,\ i\in J),\qquad M=\sum_s D(s)\sigma(s).$$
