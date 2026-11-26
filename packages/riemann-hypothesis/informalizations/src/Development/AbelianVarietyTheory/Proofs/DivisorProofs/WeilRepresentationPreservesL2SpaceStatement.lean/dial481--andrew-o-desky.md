---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/WeilRepresentationPreservesL2SpaceStatement.lean",
  "declarations": [
    "GlobalTheory.T.weil_representation_preserves_L2_space"
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

## Preservation of the local L2 norm by the Weil action

[Theorem THETA.1731](https://andrewodesky.com/rh/lean/GlobalTheory.T.weil_representation_preserves_L2_space/)

Use the data of ([Local Weil data and action formulas](https://andrewodesky.com/rh/lean/GlobalTheory.KSp.IsKW/)), and let $\kappa\in\mathbb C$ and a complex-linear representation $\omega$ of $G$ on $\mathcal S(V)$ satisfy the local Weil action formulas. For every additive Haar measure $\mu'$ on $V$, every $g\in G$ and every $\phi\in\mathcal S(V)$, $$\int_V|\omega(g)\phi(x)|^2\,d\mu'(x)=\int_V|\phi(x)|^2\,d\mu'(x).$$
