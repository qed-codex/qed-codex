---
{
  "module": "src/ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/Rationality/DescPf.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.G.FreeQuotientRank.galoisDescent_holds"
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

## Descent of a Galois-stable subspace

[Theorem ALG.0761](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.FreeQuotientRank.galoisDescent_holds/)

Let $L/K$ be a finite Galois extension, let $V$ be a $K$-vector space, and let $W\subseteq L\otimes_K V$ be an $L$-linear subspace. Suppose $$(\sigma\otimes1)(W)\subseteq W\qquad(\sigma\in\operatorname{Gal}(L/K)).$$ Put $W_0=\{v\in V:1\otimes v\in W\}$. Then $$W=\operatorname{span}_L\{1\otimes v:v\in W_0\}.$$ No finite-dimensionality assumption on $V$ is required.
