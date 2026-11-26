---
{
  "module": "src/Formalism/SharpRestriction/GrowthBounds/R1sExpLowHolds.lean",
  "declarations": [
    "Formalism.L2.FormalSeriesBounds.r1sExpLow_holds"
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

## Low coefficients of a formal exponential

[Theorem ALG.0644](https://andrewodesky.com/rh/lean/Formalism.L2.FormalSeriesBounds.r1sExpLow_holds/)

Let $k$ be a characteristic-zero field, let $F\in k[[X,Y]]$, and let $m\ge1$. Suppose $$[X^iY^j]F=0\qquad(i\ge0,\ 0\le j<m).$$ Then $$[X^iY^j]\exp(F)=[X^iY^j](1+F)\qquad(i\ge0,\ 0\le j<2m).$$
