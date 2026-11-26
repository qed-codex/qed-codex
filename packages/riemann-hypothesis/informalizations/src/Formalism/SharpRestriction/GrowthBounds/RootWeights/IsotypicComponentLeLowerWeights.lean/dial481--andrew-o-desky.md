---
{
  "module": "src/Formalism/SharpRestriction/GrowthBounds/RootWeights/IsotypicComponentLeLowerWeights.lean",
  "declarations": [
    "Formalism.MainNotions.G.GLWeightTheory.cr_hwv_dom"
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

## Dominance of a highest weight from the matrix-unit relations

[Theorem REP.0292](https://andrewodesky.com/rh/lean/Formalism.MainNotions.G.GLWeightTheory.cr_hwv_dom/)

Let $K$ be a field of characteristic zero, $V$ a finite-dimensional $K$-vector space, and $E_{ab}\in\operatorname{End}_K(V)$ for $1\le a,b\le n$. Suppose $$[E_{ab},E_{cd}]=\delta_{bc}E_{ad}-\delta_{da}E_{cb}.$$ If $v\ne0$ and $\mu_1,\ldots,\mu_n\in\mathbb Z$ satisfy $$E_{aa}v=\mu_av,\qquad E_{ab}v=0\quad(a<b),$$ then $\mu_1\ge\cdots\ge\mu_n$.
