---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/LowestKtypeCoefficientExplicitPowerDecayStatement.lean",
  "declarations": [
    "GlobalTheory.T.lowest_Ktype_coefficient_explicit_power_decay"
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

## Power decay of a minimal compact-type coefficient

[Theorem REP.1475](https://andrewodesky.com/rh/lean/GlobalTheory.T.lowest_Ktype_coefficient_explicit_power_decay/)

Let $m\ge3$, $\epsilon\in\{+,-\}^m$, and $\lambda_1>\cdots>\lambda_m$ with $\lambda_i-(m-1)/2\in\mathbb Z$. Suppose $$|\lambda_i-\lambda_j|\ge1000m^3\quad(\epsilon_i\ne\epsilon_j),\qquad |\lambda_i|\le B$$ for some $B\in\mathbb R$. Let $\pi$ on a complex inner product space satisfy the discrete-series conditions stated in the conventions for $(\epsilon,\lambda)$ on $U(\epsilon)$. For every unit vector $v_0$ in the sum of compact subrepresentations of the prescribed minimal type, and every $g\in U(\epsilon)$, $$|\langle v_0,\pi(g)v_0\rangle|\le e^{100m^3}\|g\|_{\mathrm{HS}}^{-40m^2},\qquad \|g\|_{\mathrm{HS}}=\left(\sum_{i,j}|g_{ij}|^2\right)^{1/2}.$$
