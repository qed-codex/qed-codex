---
{
  "module": "src/ReciprocityTheory/ReductiveGroups/DiscreteSeries/ExceptionalGroupG2/HarishChandraMultiplicityBound.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.DS.G2.discrete_series_exists_large_gap"
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

## Discrete series with a prescribed minimal compact type

[Theorem REP.1220](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.DS.G2.discrete_series_exists_large_gap/)

Let $n\ge0$, let $\varepsilon_1,\ldots,\varepsilon_n\in\{+,-\}$, and put $p=\#\{i:\varepsilon_i=+\}$ and $q=n-p$. Let $\lambda_1>\cdots>\lambda_n$ satisfy $\lambda_i-(n-1)/2\in\mathbb Z$. Suppose $h\in\mathbb R$ satisfies $|\lambda_i-\lambda_j|\ge h$ whenever $\varepsilon_i\ne\varepsilon_j$. Assume either $p=0$ or $q=0$, or $$h>\max\{2n,8n\min(p,q)\}.$$ There is a nonzero irreducible unitary representation of $U(p,q)$ on a complex Hilbert space, with square-integrable matrix coefficients, containing the compact type of highest weight $\lambda+\rho_n-\rho_c$. Here $\rho_n,\rho_c$ are the half sums of the positive noncompact and compact roots for the given order and sign pattern. Among all occurring compact types of highest weight $\mu$, this type minimizes $\|\mu+2\rho_c\|^2$.
