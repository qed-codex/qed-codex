---
{
  "module": "src/Formalism/SharpRestriction/LevelLetterCocycles/StageStep.lean",
  "declarations": [
    "Formalism.MainNotions.UnusedSlot80.CrA.stage_all"
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

## A basis adapted to a finite interval of a decreasing filtration

[Theorem ALG.0917](https://andrewodesky.com/rh/lean/Formalism.MainNotions.UnusedSlot80.CrA.stage_all/)

Let $K$ be a field, $d\ge0$, and $(F^u)_{u\in\mathbb Z}$ a decreasing filtration by $K$-linear subspaces of $K^d$. For every pair of integers $u\le h$, there are a linearly independent set $S\subseteq F^u$ and integers $\ell(s)\in[u,h]$ for $s\in S$ such that $$s\in F^{\ell(s)},\qquad F^v=\operatorname{span}_K\{s\in S:v\le\ell(s)\}\quad(u\le v\le h).$$
