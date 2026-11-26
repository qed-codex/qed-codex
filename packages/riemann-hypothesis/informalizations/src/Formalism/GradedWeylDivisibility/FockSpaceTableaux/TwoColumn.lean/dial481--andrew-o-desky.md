---
{
  "module": "src/Formalism/GradedWeylDivisibility/FockSpaceTableaux/TwoColumn.lean",
  "declarations": [
    "Formalism.GradedWeylDivisibility.lctwo_main"
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

## A column-substitution bound for leading exponents

[Theorem ALG.1751](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.lctwo_main/)

Use the notation and assume all four universal conditions of ([Column slices and substitution bounds for polynomials](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.PeelDecomp/)). Let $B$ be a commutative domain, let $r,n,d,a_0,s\ge0$ be integers, and let $0\le l<j<n$. Work in $B[X_{bc}:0\le b<r,\ 0\le c<n]$.

Let $g\ne0$ be homogeneous of weight $\omega\in\mathbb N^{r\times n}$. Suppose $r-a_0=d$, with subtraction truncated at zero, $\omega_{bl}=0$ for every row $b<a_0$, and $\deg_tD_{lj}g\le s$. Then, for every $0\le a<r$, $$\sum_{b\le a}m(g)_{bj}\le s+\sum_{b<a}m(g)_{bl}.$$
