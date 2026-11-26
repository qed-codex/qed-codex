---
{
  "module": "src/Formalism/PeriodIntegrals/OrbitalBoundsConclusion/DiagRank.lean",
  "declarations": [
    "diagonal_rank_bound"
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

## A rank bound from a p-adic diagonal factorization

[Theorem PHT.0299](https://andrewodesky.com/rh/lean/diagonal_rank_bound/)

Let $p$ be prime, $n,m\ge0$, $X,Y\in M_{n,m}(\mathbb Z_p)$, $c_1,\ldots,c_m\in\mathbb Q_p$, and $D\in\mathbb Z$. If $$\sum_{a=1}^m X_{ia}c_aY_{ja}=p^D\delta_{ij}\qquad(1\le i,j\le n),$$ then $$n\le\#\{a:c_a\ne0,\ v_p(c_a)\le D\},$$ where $v_p(p)=1$.
