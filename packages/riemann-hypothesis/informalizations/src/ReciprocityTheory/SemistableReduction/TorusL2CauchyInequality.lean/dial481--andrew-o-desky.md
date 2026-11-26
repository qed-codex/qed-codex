---
{
  "module": "src/ReciprocityTheory/SemistableReduction/TorusL2CauchyInequality.lean",
  "declarations": [
    "ReciprocityTheory.MultiplicativeHeights.Closed.sj"
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

## A lower bound for the spherical logarithmic mean of a homogeneous polynomial

[Theorem ARAK.1033](https://andrewodesky.com/rh/lean/ReciprocityTheory.MultiplicativeHeights.Closed.sj/)

Let $n,a\ge0$, let $f\in\mathbb C[Z_1,\ldots,Z_n]$ be homogeneous of degree $a$, and let $u\in\mathbb C^n$ satisfy $\|u\|_2=1$ and $f(u)\ne0$. With $\nu$ the uniform probability measure on the unit sphere, $$\log|f|\in L^1(\nu),\qquad \log|f(u)|-\frac a2H_{n-1}\le\int_{\|z\|_2=1}\log|f(z)|\,d\nu(z),$$ where $H_j=\sum_{k=1}^j1/k$ and $H_0=0$.
