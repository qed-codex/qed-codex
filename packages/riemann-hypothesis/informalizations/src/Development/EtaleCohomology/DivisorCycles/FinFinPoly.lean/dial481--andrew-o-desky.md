---
{
  "module": "src/Development/EtaleCohomology/DivisorCycles/FinFinPoly.lean",
  "declarations": [
    "LateralTheory.Fin.FinPoly.intersectionNumber_baseChange"
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

## Recognizing the characteristic polynomial from an annihilator

[Theorem ALG.1235](https://andrewodesky.com/rh/lean/LateralTheory.Fin.FinPoly.intersectionNumber_baseChange/)

Let $K$ be an algebraically closed field, $n\ge0$, $A\in M_n(K)$, and $P\in K[T]$ monic of degree $n$ with $P(A)=0$. Both assertions hold:

1. If $\det(TI-A)$ is separable, then $\det(TI-A)=P$.
2. Suppose $P$ is separable and its root multiset has this property: every multiset $M$ of $n$ roots of $P$, with repetitions allowed, that differs from the root multiset of $P$ has a different product. If $\det A=(-1)^nP(0)$, then $\det(TI-A)=P$.
