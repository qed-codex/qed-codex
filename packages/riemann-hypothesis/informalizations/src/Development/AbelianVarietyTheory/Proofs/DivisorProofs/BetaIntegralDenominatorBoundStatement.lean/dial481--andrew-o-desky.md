---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/BetaIntegralDenominatorBoundStatement.lean",
  "declarations": [
    "GlobalTheory.T.beta_integral_denominator_bound"
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

## A uniform denominator for factorial ratios

[Theorem ALG.1200](https://andrewodesky.com/rh/lean/GlobalTheory.T.beta_integral_denominator_bound/)

For every prime $\ell$ and integer $w\ge0$, there is an integer $m\ge0$ with $\ell\nmid m$ such that, for all $j,k\ge0$ satisfying $j+k+1\le w$, $$(j+k+1)!\ \bigm|\ m\ell^{\lfloor\log_\ell w\rfloor}j!k!.$$ Here the exponent is defined to be zero when $w=0$.
