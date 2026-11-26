---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/AeTranscendentalPointNonvanishing.lean",
  "declarations": [
    "GlobalTheory.ae_eval₂_ne_zero_of_countable"
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

## Simultaneous nonvanishing over a countable field

[Theorem ALG.1163](https://andrewodesky.com/rh/lean/GlobalTheory.ae_eval%E2%82%82_ne_zero_of_countable/)

Let $K$ be a countable field, $\sigma:K\hookrightarrow\mathbb C$ a field embedding, and $I$ a finite set. For almost every $t\in\mathbb C^I$, with respect to Lebesgue measure, every nonzero polynomial $Q\in K[X_i:i\in I]$ satisfies $$Q^\sigma(t)\ne0,$$ where $Q^\sigma$ is obtained by applying $\sigma$ to its coefficients.
