---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/ComplexAnalyticSets/PCurveProperClosedFinite.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.CurveProperClosedFinite.proof"
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

## A proper closed subset of an affine curve is finite

[Theorem AG.0318](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.CurveProperClosedFinite.proof/)

Let $n\ge0$, let $W,K$ be ideals in $\mathbb C[X_1,\ldots,X_n]$, and write $Z(I)\subseteq\mathbb C^n$ for the common zero set of an ideal $I$. If $W$ is prime, $$\dim\bigl(\mathbb C[X_1,\ldots,X_n]/W\bigr)=1,\qquad K\nsubseteq W,$$ then $Z(W)\cap Z(K)$ is finite.
