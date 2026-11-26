---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/EqDiscreteSeriesOfLowestKTypeCasimir.lean",
  "declarations": [
    "GlobalTheory.PsCo.PcEF.eq_discreteSeries_of_lowestKType_casimir"
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

## Recognition from a compact type and a Casimir eigenvalue

[Theorem REP.0503](https://andrewodesky.com/rh/lean/GlobalTheory.PsCo.PcEF.eq_discreteSeries_of_lowestKType_casimir/)

Let $\varepsilon_1,\ldots,\varepsilon_n\in\{\pm1\}$, let $p,q$ count their positive and negative signs, and put $G=U(\operatorname{diag}(\varepsilon_i))$, $K=U(p)\times U(q)$. Let $\lambda_1>\cdots>\lambda_n$ be real numbers. Suppose there is $h>npq+1$ such that $|\lambda_i-\lambda_j|\ge h$ whenever $\varepsilon_i\ne\varepsilon_j$.

Let $\rho$ be an irreducible unitary representation on a complex Hilbert space $H$, with continuous orbit maps. Suppose its smooth vectors contain a nonzero finite-dimensional irreducible $K$-submodule $V$ of highest weight $\kappa=\lambda+\rho_n-\rho_c$, and its complexified infinitesimal action satisfies $$\left(\sum_{i,j}E_{ij}E_{ji}\right)v=\left(\sum_i\lambda_i^2-\sum_i\left(\frac{n+1}2-i\right)^2\right)v\qquad(v\in V).$$ For every discrete-series realization $D$ of parameter $(\varepsilon,\lambda)$ in the convention below, there is a surjective complex-linear isometry $U:H\to H_D$ intertwining $\rho$ and $D$.
