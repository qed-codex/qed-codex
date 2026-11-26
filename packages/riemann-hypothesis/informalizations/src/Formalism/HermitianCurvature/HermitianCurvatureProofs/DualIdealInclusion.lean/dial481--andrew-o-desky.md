---
{
  "module": "src/Formalism/HermitianCurvature/HermitianCurvatureProofs/DualIdealInclusion.lean",
  "declarations": [
    "Formalism.FourierDecayAlt.P.dual_third_group_holds"
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

## An inclusion for a trace-dual lattice

[Theorem ANT.0989](https://andrewodesky.com/rh/lean/Formalism.FourierDecayAlt.P.dual_third_group_holds/)

Let $E$ be a number field and $\mathfrak d$ a fractional ideal such that $$\mathcal O_E^{\vee}=\mathfrak d^{-1},\qquad M^{\vee}=\{x\in E:\operatorname{Tr}_{E/\mathbb Q}(xM)\subseteq\mathbb Z\}.$$ Let $\nu\in\mathbb Z$, let $g\in\mathbb Z\setminus\{0\}$, and let $\Lambda\subseteq E$ be a $\mathbb Z$-submodule containing $g^2\mathfrak d^\nu$. Then $$\{x\in E:\operatorname{Tr}_{E/\mathbb Q}(xy/g)\in\mathbb Z\text{ for every }y\in\Lambda\}\subseteq g^{-1}\mathfrak d^{-(\nu+1)}.$$
