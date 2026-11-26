---
{
  "module": "src/Formalism/GaussJetBounds/GaussJetProofs/LogarithmWeightComparison.lean",
  "declarations": [
    "Formalism.DworkPowerSeriesWeights.generalized_log_inverse"
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

## A compositional inverse for a family of formal logarithms

[Theorem PHT.0569](https://andrewodesky.com/rh/lean/Formalism.DworkPowerSeriesWeights.generalized_log_inverse/)

Let $K$ be a characteristic-zero field, let $\ell$ be prime, let $I$ be a finite set, and let $p:I\to I$ be any map. Define the formal power-series map $L=(L_i)_{i\in I}$ by $$L_i(X)=\sum_{e\ge0}\frac{X_{p^e(i)}^{\ell^{2e}}}{\ell^e}.$$ There is $G=(G_i)_{i\in I}\in K[[X_j:j\in I]]^I$, with $G_i(0)=0$ for every $i$, such that $$L(G(X))=X,\qquad G(L(X))=X.$$
