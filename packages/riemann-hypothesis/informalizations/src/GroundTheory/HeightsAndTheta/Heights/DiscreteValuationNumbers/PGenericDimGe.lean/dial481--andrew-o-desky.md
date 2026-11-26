---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/DiscreteValuationNumbers/PGenericDimGe.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.NumbersDVR.GenericDimGe.proof"
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

## Dimension over a DVR is at most generic dimension plus one

[Theorem ALG.0199](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.NumbersDVR.GenericDimGe.proof/)

Let $O$ be a discrete valuation domain with fraction field $K$, let $I$ be a finite set, and let $J_i$ be finite sets for $i\in I$. Put $$R=O[X_{ij}:i\in I,j\in J_i].$$ Let $P\subset R$ be a prime ideal with $P\cap O=0$, and let $P_K$ be its extension to $K[X_{ij}]$. Then $$\dim(R/P)\le\dim(K[X_{ij}]/P_K)+1.$$
