---
{
  "module": "src/Development/WeilBound/ThetaLifts/FrameEstimates/LinDer.lean",
  "declarations": [
    "PositivityTheory.ThKEst.linDer_of"
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

## Directional derivatives from finitely many one-parameter subgroups

[Theorem REP.1249](https://andrewodesky.com/rh/lean/PositivityTheory.ThKEst.linDer_of/)

Assume the following two global inputs for every CM extension $E/F$, every choice of a complex embedding of $E$ above each infinite place of $F$, and every nondegenerate Hermitian or skew-Hermitian space $W=E^d$: every continuous one-parameter subgroup of $U(W)(\mathbb A_F)$ supported at infinity has an infinitesimal generator, and every archimedean Lie algebra element generates exactly one such subgroup. Generation means that its matrix at each infinite place is $\exp(tY_w)$. Here the Lie algebra condition at an embedding is $Y_w^tJ_w+J_w\overline{Y_w}=0$, where $J_w$ is the matrix of the chosen form at that embedding, with this matrix convention.

For each such $E/F,W$ and embedding choice, there are finitely many such subgroups $\beta_1,\ldots,\beta_m$ and real-linear functionals $c_i$ on $\prod_{w\mid\infty}M_d(\mathbb C)$ with this property. Let $f:U(W)(\mathbb A_F)\to\mathbb C$ be any function, and suppose continuous functions $f_i'$ satisfy $$\left.\frac{d}{dt}f(h\beta_i(t))\right|_{t=0}=f_i'(h)\qquad\text{for every }i,h.$$ Then for every continuous one-parameter subgroup $\gamma$ supported at infinity, every matrix family $Y$ generating $\gamma$, and every $h$, $$\left.\frac{d}{dt}f(h\gamma(t))\right|_{t=0}=\sum_{i=1}^m c_i(Y)f_i'(h).$$
