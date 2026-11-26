---
{
  "module": "src/Formalism/RankGapBounds/RankGapProofs/WeightedMeanData.lean",
  "declarations": [
    "Formalism.RankGapBounds.WeightedMeanData.phi_bound"
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

## An upper bound for the logarithmic slope term

[Theorem ANT.0152](https://andrewodesky.com/rh/lean/Formalism.RankGapBounds.WeightedMeanData.phi_bound/)

Let $r,S,X,b,V$ be real numbers satisfying $$r\ge0,\qquad 0<S\le Xb,\qquad b>0,\qquad X>0,\qquad r\le V.$$ Then $$r\log(1+S/r)\le(V+b)\log(1+X),$$ where the left-hand side is read as $0$ when $r=0$.
