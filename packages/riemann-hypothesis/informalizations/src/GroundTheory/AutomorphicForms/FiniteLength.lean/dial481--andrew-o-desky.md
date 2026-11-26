---
{
  "module": "src/GroundTheory/AutomorphicForms/FiniteLength.lean",
  "declarations": [
    "GroundTheory.Automorphic.Parabolic.hasFiniteLength_parabolicInd"
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

## Finite length of parabolic induction

[Theorem REP.1266](https://andrewodesky.com/rh/lean/GroundTheory.Automorphic.Parabolic.hasFiniteLength_parabolicInd/)

Let $F$ be a nonarchimedean local field, $n\ge0$, and $\beta:\{0,\ldots,n-1\}\to\mathbb N$. Set $G=\operatorname{GL}_n(F)$ and $$P_\beta=\{g\in G:g_{ij}=0\text{ whenever }\beta(j)<\beta(i)\},\qquad M_\beta=\{g\in G:g_{ij}=0\text{ whenever }\beta(i)\ne\beta(j)\}.$$ Thus $\beta$ labels the coordinates, and $M_\beta\simeq\prod_{b\in\operatorname{im}\beta}\operatorname{GL}_{|\beta^{-1}(b)|}(F)$. If $\sigma$ is a smooth complex representation of $M_\beta$ of finite length, its normalized parabolic induction from $P_\beta$ to $G$ has finite length.
