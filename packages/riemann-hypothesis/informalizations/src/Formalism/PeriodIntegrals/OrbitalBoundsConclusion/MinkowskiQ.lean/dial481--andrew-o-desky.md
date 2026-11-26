---
{
  "module": "src/Formalism/PeriodIntegrals/OrbitalBoundsConclusion/MinkowskiQ.lean",
  "declarations": [
    "minkowski_bound_rat"
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

## Minkowski divisibility for finite rational matrix groups

[Theorem ALG.1625](https://andrewodesky.com/rh/lean/minkowski_bound_rat/)

For $N\ge0$ define $$M_N=\prod_{\substack{p<N+2\\p\text{ prime}}}p^{\displaystyle\sum_{i=0}^{N}\left\lfloor\frac{N}{p^i(p-1)}\right\rfloor}.$$ Every finite subgroup $G\subseteq\operatorname{GL}_N(\mathbb Q)$ satisfies $$|G|\mid M_N.$$
