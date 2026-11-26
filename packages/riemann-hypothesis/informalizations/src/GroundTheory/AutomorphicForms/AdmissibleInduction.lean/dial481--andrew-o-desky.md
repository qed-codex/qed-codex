---
{
  "module": "src/GroundTheory/AutomorphicForms/AdmissibleInduction.lean",
  "declarations": [
    "GroundTheory.Automorphic.Parabolic.isAdmissible_parabolicInd"
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

## Parabolic induction preserves admissibility

[Theorem REP.1335](https://andrewodesky.com/rh/lean/GroundTheory.Automorphic.Parabolic.isAdmissible_parabolicInd/)

Let $F$ be a nonarchimedean local field, let $n\ge0$ and $\beta:\{0,\ldots,n-1\}\to\mathbb N$, and put $N=\sum_i\beta_i$. Let $P\subseteq\operatorname{GL}_N(F)$ be the standard block parabolic with Levi subgroup $M=\prod_i\operatorname{GL}_{\beta_i}(F)$. If $\sigma$ is an admissible complex representation of $M$, its parabolically induced representation on $\operatorname{GL}_N(F)$ is admissible.
