---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/HeightsOfSets/HeightsSetAll.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.DenseBoundedHeight.main"
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

## Algebraic points of bounded height with prescribed vanishing ideal

[Theorem ARAK.1650](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.DenseBoundedHeight.main/)

Fix a finite set $J$ and integers $n_j\ge0$. Let $I\subseteq\mathbb Z[X_{ji}:j\in J,\ 0\le i\le n_j]$ be a prime multihomogeneous ideal such that $I\cap\mathbb Z=0$ and, for every $j$, at least one variable $X_{ji}$ is outside $I$. There exist a real number $C$ and a set $S$ of tuples $x=(x_{ji})$ over $\overline{\mathbb Q}$ such that every coordinate block is nonzero, every polynomial in $I$ vanishes at $x$, and $$h(x)\le C\qquad(x\in S).$$ For a number field $L$ containing the coordinates, the height is the normalized logarithmic height with maximum norms at finite places and Euclidean norms at infinity: $$h(x)=\frac{1}{[L:\mathbb Q]} \left(\sum_{v\ \mathrm{finite}}\sum_{j\in J}\log\max_i|x_{ji}|_v+ \sum_{\tau:L\hookrightarrow\mathbb C}\sum_{j\in J} \log\sqrt{\sum_i|\tau(x_{ji})|^2}\right).$$ Moreover, every multihomogeneous polynomial with integral coefficients that vanishes at all $x\in S$ belongs to $I$.
