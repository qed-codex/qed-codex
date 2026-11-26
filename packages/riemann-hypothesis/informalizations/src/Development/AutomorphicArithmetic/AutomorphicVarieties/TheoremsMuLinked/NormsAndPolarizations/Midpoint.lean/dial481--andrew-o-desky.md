---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/TheoremsMuLinked/NormsAndPolarizations/Midpoint.lean",
  "declarations": [
    "UpperTheory.V.Th.Nm.midpoint"
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

## An integral unimodular form after a change of basis

[Theorem PHT.0605](https://andrewodesky.com/rh/lean/UpperTheory.V.Th.Nm.midpoint/)

Let $\ell$ be prime, let $n\ge0$, and let $S\subseteq\operatorname{GL}_n(\overline{\mathbb Q}_\ell)$. Let $P\in\operatorname{GL}_n(\overline{\mathbb Q}_\ell)$ satisfy $P^t=P$ or $P^t=-P$. Suppose that for every $g\in S$, every entry of $g$ and of $PgP^{-1}$ has $\ell$-adic norm at most one. There exist $Q,P'\in\operatorname{GL}_n(\overline{\mathbb Q}_\ell)$ such that $$P'=Q^tPQ,$$ every entry of $P'$ and $(P')^{-1}$ has norm at most one, and every entry of $Q^{-1}gQ$ has norm at most one for every $g\in S$.
