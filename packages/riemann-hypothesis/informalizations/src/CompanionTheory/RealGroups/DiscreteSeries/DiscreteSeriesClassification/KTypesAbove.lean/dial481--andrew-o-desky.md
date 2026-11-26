---
{
  "module": "src/CompanionTheory/RealGroups/DiscreteSeries/DiscreteSeriesClassification/KTypesAbove.lean",
  "declarations": [
    "CompanionTheory.RgDs.B.classUsed"
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

## Discrete series with a prescribed lowest compact type

[Theorem REP.0099](https://andrewodesky.com/rh/lean/CompanionTheory.RgDs.B.classUsed/)

Let $n\ge0$, let $\varepsilon_1,\ldots,\varepsilon_n\in\{\pm1\}$, and put $G=U(\operatorname{diag}(\varepsilon_i))$, $K=U(p)\times U(q)$. Suppose $$\lambda_1>\cdots>\lambda_n,\qquad \lambda_i-(n-1)/2\in\mathbb Z.$$ Use positive roots $e_i-e_j$ for $i<j$, and let $\rho_c,\rho_n$ be the half-sums of the roots with equal and unequal signs respectively. Put $\kappa=\lambda+\rho_n-\rho_c$. There is an irreducible square-integrable unitary realization $\pi$ on a complex inner-product space, with infinitesimal character $\lambda$, in which the $K$-type $\kappa$ occurs in exactly one subspace. Every $K$-type $\mu$ occurring in $\pi$ has the form $$\mu=\kappa+\sum_{i<j}c_{ij}(e_i-e_j),\qquad c_{ij}\in\mathbb N.$$ Every realization satisfying the discrete-series conditions in the conventions for $(\varepsilon,\lambda)$ is unitarily equivalent to $\pi$.
