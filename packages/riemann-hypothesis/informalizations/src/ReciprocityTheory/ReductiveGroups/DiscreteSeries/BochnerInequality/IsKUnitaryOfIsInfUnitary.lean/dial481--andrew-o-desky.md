---
{
  "module": "src/ReciprocityTheory/ReductiveGroups/DiscreteSeries/BochnerInequality/IsKUnitaryOfIsInfUnitary.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.DS.exists_khw"
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

## A highest-weight vector in a finite compact-stable subspace

[Theorem REP.1382](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.DS.exists_khw/)

Let $X$ be a complex inner-product space, $n\ge0$, and $\varepsilon:\{1,\ldots,n\}\to\{0,1\}$. Let $A_{ab}\in\operatorname{End}_{\mathbb C}(X)$ satisfy $$[A_{ab},A_{cd}]=\delta_{bc}A_{ad}-\delta_{da}A_{cb}.$$ Assume $\langle A_{ab}x,y\rangle=\langle x,A_{ba}y\rangle$ whenever $\varepsilon(a)=\varepsilon(b)$. Let $S\subset X$ be a nonzero finite-dimensional subspace stable under all such $A_{ab}$.

There are $0\ne w\in S$ and real numbers $\mu_1,\ldots,\mu_n$ such that $$A_{aa}w=\mu_aw,\qquad A_{ab}w=0\quad(a<b,\ \varepsilon(a)=\varepsilon(b)).$$
