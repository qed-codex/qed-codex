---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/ArithmeticBezout/PChowFormAssoc.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.ChowFormAssoc.proof"
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

## Uniqueness of a Chow form up to a scalar

[Theorem AG.0186](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.ChowFormAssoc.proof/)

Let $F$ be a field, $n,k\ge0$, and $I\subseteq F[X_1,\ldots,X_n]$ an ideal. Let $\mathcal I$ be the set of arrays $(u_{ij})\in\overline F^{k\times n}$ for which there is $x\in\overline F^n\setminus\{0\}$ satisfying $$g(x)=0\quad(g\in I),\qquad \sum_j u_{ij}x_j=0\quad(1\le i\le k).$$ Suppose $f,f'\in F[U_{ij}]$ are nonzero and, for every $g\in F[U_{ij}]$, vanishing of $g$ on $\mathcal I$ is equivalent to $f\mid g$, and also equivalent to $f'\mid g$. Then $$f'=cf\qquad\text{for some }c\in F^\times.$$
