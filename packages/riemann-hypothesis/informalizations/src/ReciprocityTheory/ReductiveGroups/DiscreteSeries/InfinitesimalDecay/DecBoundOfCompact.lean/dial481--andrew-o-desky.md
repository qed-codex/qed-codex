---
{
  "module": "src/ReciprocityTheory/ReductiveGroups/DiscreteSeries/InfinitesimalDecay/DecBoundOfCompact.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.DS.DecInf.decSm"
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

## Decay of all smooth discrete-series matrix coefficients

[Theorem REP.1228](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.DS.DecInf.decSm/)

Let $k,r\ge0$, $n=2r+k+1$, and let $H$ be the Hermitian form with $r$ hyperbolic planes and a diagonal block with $k$ positive entries and one negative entry. Choose $n$ signs $\varepsilon$, with $p$ positive and $q$ negative, and a strictly decreasing real tuple $\lambda$ with $\lambda_i-(n-1)/2\in\mathbb Z$. Suppose $|\lambda_i-\lambda_j|\ge h$ for opposite signs. Put $$T=\max\{npq+1,16n\min(p,q)+8\sqrt{2\min(p,q)}\}.$$ Let $m\ge0$ be an integer with $T+m<h$. Let $\sigma$ act on a complex Hilbert space and satisfy the discrete-series conditions in ([A nonzero discrete-series coefficient integral gives an intertwiner](https://andrewodesky.com/rh/lean/PositivityTheory.RgHe.LowestKTypeModel.ofInt/)) after a unitary change of basis carrying $H$ to the diagonal sign form, with parameter $\lambda$.

There exist $C\in\mathbb R$ and a finite list $\mathcal W$ of words in the real Lie algebra of $U(H)$, each of length at most $m(n-1)$, such that for all smooth vectors $u,v$ and $g\in U(H)$, $$\left(\sum_{i,j}|g_{ij}|^2\right)^{m/2}|\langle v,\sigma(g)u\rangle|\le C\left(\sum_{w\in\mathcal W}\|d\sigma(w)u\|\right)\left(\sum_{w\in\mathcal W}\|d\sigma(w)v\|\right).$$
