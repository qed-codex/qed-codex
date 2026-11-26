---
{
  "module": "src/Development/AutomorphicArithmetic/CommutativeAlgebra/FiniteKummerSelmerOfCharts.lean",
  "declarations": [
    "UpperTheory.finite_kummerSelmer_of_charts"
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

## Finiteness of function-field Kummer classes under a chart descent condition

[Theorem AG.0290](https://andrewodesky.com/rh/lean/UpperTheory.finite_kummerSelmer_of_charts/)

Let $k$ be algebraically closed, $K/k$ a function field of one variable, and $q\ge1$. Assume the chart descent condition below. Then $$\{f\in K^\times:q\mid\operatorname{ord}_v(f)\text{ for every place }v\text{ of }K/k\}/K^{\times q}$$ is finite: there is a finite $T\subset K^\times$ such that every such $f$ is $tu^q$ for some $t\in T$, $u\in K^\times$.
