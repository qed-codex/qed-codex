---
{
  "module": "src/Development/WeilBound/CoreStatements/PublishedTheorems/NefNumerics/NefRiemannRoch/NefIntersectionNonnegAllDims.lean",
  "declarations": [
    "GlobalTheory.kleiman_interNum_nonneg"
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

## Nonnegative mixed intersections of nef line bundles

[Theorem AG.1437](https://andrewodesky.com/rh/lean/GlobalTheory.kleiman_interNum_nonneg/)

Let $k$ be an infinite field and $X$ a projective $k$-scheme. Let $d\ge0$, let $\mathcal E$ be a finite quasicoherent $\mathcal O_X$-module with $\dim\operatorname{Supp}\mathcal E\le d$, and let $L_1,\ldots,L_d$ be nef line bundles, meaning that their degrees on every reduced irreducible proper curve in $X$ are nonnegative. Define $$I(\mathcal E;L_1,\ldots,L_d)=\sum_{S\subset\{1,\ldots,d\}}(-1)^{|S|}\chi\left(X,\mathcal E\otimes\bigotimes_{i\in S}L_i^{-1}\right),$$ where $\chi$ is the coherent Euler characteristic over $k$. Then $$I(\mathcal E;L_1,\ldots,L_d)\ge0.$$
