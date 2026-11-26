---
{
  "module": "src/Formalism/GaussJetBounds/GaussJetProofs/ConstantCoeffAevalLinP.lean",
  "declarations": [
    "Formalism.DworkPowerSeriesWeights.jet_pair_linearity"
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

## Transposition of a linear substitution in the differential pairing

[Theorem ALG.0768](https://andrewodesky.com/rh/lean/Formalism.DworkPowerSeriesWeights.jet_pair_linearity/)

Let $K$ be any field, let $I,J$ be finite sets, and let $A=(a_{ij})\in K^{I\times J}$. For a polynomial $P\in K[X_i:i\in I]$ and a formal power series $F\in K[[Y_j:j\in J]]$, put $$L_j(X)=\sum_{i\in I}a_{ij}X_i,\qquad M_i(Y)=\sum_{j\in J}a_{ij}Y_j.$$ Then $$\langle P(X),F(L(X))\rangle=\langle P(M(Y)),F(Y)\rangle.$$
