---
{
  "module": "src/Formalism/SharpRestriction/GrowthBounds/SegmentDegree/DminusLeBeS.lean",
  "declarations": [
    "Formalism.MainNotions.SelectionLemmas.Pf.residue_class_count"
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

## Counting tuples with a prescribed sum modulo an integer

[Theorem ALG.0402](https://andrewodesky.com/rh/lean/Formalism.MainNotions.SelectionLemmas.Pf.residue_class_count/)

Let $r,Q,b,c,\rho\ge0$ be integers with $r\ge2$ and $2b<Q$. Then $$\#\left\{(w_1,\ldots,w_r)\in\{0,\ldots,Q-2b-1\}^r:c+\sum_iw_i\equiv\rho\pmod Q\right\} \ge Q^{r-1}\left(1-\frac{2rb}{Q}\right).$$
