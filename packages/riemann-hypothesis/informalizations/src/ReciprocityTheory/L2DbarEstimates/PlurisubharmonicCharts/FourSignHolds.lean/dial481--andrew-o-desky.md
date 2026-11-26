---
{
  "module": "src/ReciprocityTheory/L2DbarEstimates/PlurisubharmonicCharts/FourSignHolds.lean",
  "declarations": [
    "ReciprocityTheory.L2DbarEstimates.Y.four_sign_holds"
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

## Polynomial growth forces a sign condition on Fourier support

[Theorem ANT.0202](https://andrewodesky.com/rh/lean/ReciprocityTheory.L2DbarEstimates.Y.four_sign_holds/)

Let $f\ge0$ and $\Omega\subseteq\mathbb R^f$ be open and preconnected. Let $h$ be holomorphic on $\{z\in\mathbb C^f:\operatorname{Im}z\in\Omega\}$ and satisfy $h(z+m)=h(z)$ for $m\in\mathbb Z^f$. Let $b_0,\kappa\in\mathbb R^f$ and $C,E\in\mathbb R$ satisfy, for every $t\ge0$, $$b_0+t\kappa\in\Omega,\qquad |h(x+i(b_0+t\kappa))|\le C(1+t)^E\quad(x\in\mathbb R^f).$$ For $\nu\in\mathbb Z^f$ define $$a_\nu=\int_{(0,1]^f}h(x+ib_0)\exp\bigl(-2\pi i\,\nu\cdot(x+ib_0)\bigr)\,dx.$$ Then $a_\nu\ne0$ implies $\nu\cdot\kappa\ge0$.
