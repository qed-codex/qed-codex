---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/NegativeNormPowerIntegrableOfBallVolumeStatement.lean",
  "declarations": [
    "GlobalTheory.T.negativeNormPowerIntegrable_of_ballVolume"
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

## Integrability of negative norm powers from volume growth

[Theorem REP.1506](https://andrewodesky.com/rh/lean/GlobalTheory.T.negativeNormPowerIntegrable_of_ballVolume/)

For $m\ge0$ and a sign vector $\epsilon\in\{\pm1\}^m$, let $G_\epsilon=\{g\in\mathrm{GL}_m(\mathbb C):g^*J_\epsilon g=J_\epsilon\}$, where $J_\epsilon=\operatorname{diag}(\epsilon)$, and fix a Haar measure $\mu_\epsilon$. Put $h(g)=(\sum_{i,j}|g_{ij}|^2)^{1/2}$ and $U_\delta=\{g\in G_\epsilon:h(g-1)\le\delta\}$.

Assume the following volume bounds for every $m,\epsilon$ and every $\delta,R>0$: $$0<\mu_\epsilon(U_\delta)<\infty,\qquad \mu_\epsilon\{g:h(g)\le R\}\le(1+2R^2/\delta)^{2m^2}\mu_\epsilon(U_\delta).$$ Then for every $m\ge1$, every $\epsilon$, and every real $A\ge4m^2+1$, the function $g\mapsto h(g)^{-A}$ is integrable and $$\int_{G_\epsilon}h(g)^{-A}\,d\mu_\epsilon(g)\le e^{10m^2}\mu_\epsilon(U_{1/4}).$$
