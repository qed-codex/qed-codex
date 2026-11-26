---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsCommonModule.lean",
  "declarations": [
    "GlobalTheory.Poinc.exists_hasSupports"
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

## A uniform multiplier for quadratic supporting sums

[Theorem ALG.0674](https://andrewodesky.com/rh/lean/GlobalTheory.Poinc.exists_hasSupports/)

Let $O$ be a Dedekind domain, finite free over $\mathbb Z$, with finite ideal class group. Fix a map $a\mapsto\bar a$ on $O$, an integer $q\ge0$, and an invariant real-valued function $\phi$ on forms, with the polarization-fan conditions below. For a finite projective $O$-module $X$ of rank at most $q$, call an integral symmetric bilinear form $\beta$ balanced if $$\beta(ax,y)=\beta(x,\bar a y)\qquad(a\in O).$$ For a cone with generators $\gamma_1,\ldots,\gamma_r$ as below, say that $a_1,\ldots,a_m\in X$ support the cone with multiplier $d\ge1$ if they span $X$ over $\mathbb Z$ and $$d\phi(\beta)\le\sum_i\beta(a_i,a_i)$$ for every balanced positive-semidefinite integral form $\beta$, with equality for each $\gamma_j$, and equality only if $$k\beta=\sum_jc_j\gamma_j\quad\text{for some }k>0,\ c_j\in\mathbb N.$$ Suppose every such module and cone has supporting vectors with some positive multiplier, which may depend on both. Then there is a single positive multiplier that works for all these modules and cones.
