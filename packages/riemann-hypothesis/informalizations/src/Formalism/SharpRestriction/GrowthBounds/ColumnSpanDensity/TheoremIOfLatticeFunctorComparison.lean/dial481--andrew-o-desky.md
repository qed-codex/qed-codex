---
{
  "module": "src/Formalism/SharpRestriction/GrowthBounds/ColumnSpanDensity/TheoremIOfLatticeFunctorComparison.lean",
  "declarations": [
    "Formalism.MainNotions.flipOneThree.Pf.blockSplit'"
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

## Large scalar blocks in a sum of matrices over a DVR

[Theorem ALG.0968](https://andrewodesky.com/rh/lean/Formalism.MainNotions.flipOneThree.Pf.blockSplit'/)

Let $O$ be a discrete valuation ring, $J$ a finite set, $n\ge0$, and $z\in O\setminus\{0\}$. Suppose matrices $A_j\in M_n(O)$ satisfy $$\sum_{j\in J}A_j=zI_n.$$ There are integers $\nu_j\ge0$ with $n\le\sum_j\nu_j$ and, for each $j$, matrices $$P_j\in M_{\nu_j\times n}(O),\qquad Q_j\in M_{n\times\nu_j}(O),\qquad P_jA_jQ_j=zI_{\nu_j}.$$
