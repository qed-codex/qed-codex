---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/ComplexAnalyticSets/PGenericNoetherNormalisation.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.GenericNoetherNormalisation.proof"
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

## Finite generation after inverting one base element

[Theorem ALG.0559](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.GenericNoetherNormalisation.proof/)

Let $A$ be a commutative domain, let $n\ge0$, and let $\mathfrak q\subseteq A[X_0,\ldots,X_n]$ be a nonzero prime ideal with $\mathfrak q\cap A=0$. Put $R=A[X_0,\ldots,X_n]/\mathfrak q$. There are $0\ne a\in A$, elements $z_1,\ldots,z_n\in R$, and a finite set $S\subseteq R$ such that, for every $d\in R$, some integer $k\ge0$ and polynomials $c_s\in A[T_1,\ldots,T_n]$ satisfy $$a^k d=\sum_{s\in S}c_s(z_1,\ldots,z_n)s.$$
