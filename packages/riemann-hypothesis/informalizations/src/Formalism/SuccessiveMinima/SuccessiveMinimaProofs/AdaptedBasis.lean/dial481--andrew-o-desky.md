---
{
  "module": "src/Formalism/SuccessiveMinima/SuccessiveMinimaProofs/AdaptedBasis.lean",
  "declarations": [
    "Formalism.FN.existsAdaptedBasis"
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

## A lattice basis adapted to an integral flag

[Theorem ALG.1090](https://andrewodesky.com/rh/lean/Formalism.FN.existsAdaptedBasis/)

Let $E$ be a finite-dimensional real normed vector space of dimension $d$, and $L\subseteq E$ a discrete full $\mathbb Z$-lattice. For any real-linearly independent $v_1,\ldots,v_d\in L$, there is a $\mathbb Z$-basis $b_1,\ldots,b_d$ of $L$ such that $$\operatorname{span}_{\mathbb R}(b_1,\ldots,b_j)=\operatorname{span}_{\mathbb R}(v_1,\ldots,v_j)\qquad(1\le j\le d).$$
