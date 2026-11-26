---
{
  "module": "src/Development/WeilBound/CoreStatements/OrbitDecayEstimates/CurveDerivativeDecay/DerivativeUpperBound.lean",
  "declarations": [
    "CompanionTheory.Lime.T3.decay_estimate",
    "CompanionTheory.Lime.T3.derivative_upper_bound"
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

## Decay of translated lowest-type matrix coefficients

[Theorem REP.1418](https://andrewodesky.com/rh/lean/CompanionTheory.Lime.T3.decay_estimate/)

Let $1\le m\le N$, choose signs $\varepsilon_a\in\{\pm1\}$, and put $G=U(\operatorname{diag}\varepsilon)$. Let $\lambda_1>\cdots>\lambda_m$ satisfy $\lambda_a-(m-1)/2\in\mathbb Z$ and $$|\lambda_a-\lambda_b|\ge200N^3\qquad(\varepsilon_a\ne\varepsilon_b).$$ Let $\pi$ be a discrete series model of parameter $\lambda$ on a complex Hilbert space, with the full discrete series conditions specified below, and let $v$ be a unit vector in the sum of its compact types of highest weight $\lambda+\rho_n-\rho_c$. Here $\rho_n,\rho_c$ are the half sums of noncompact and compact positive roots. Define $Q(g)=\sum_{a,b}|g_{ab}|^2$. For every $g_0\in G$ and $Y\in\mathbb R$ with $Q(g_0)\le Y$, and every $g\in G$, $$\left|\left\langle\pi(g_0)v,\pi(g)\pi(g_0)v\right\rangle\right| \le e^{6N^2\log m+12N^2}Y^{12N^2}Q(g)^{-6N^2}.$$

## A formal degree bound from a small neighborhood

[Theorem REP.1467](https://andrewodesky.com/rh/lean/CompanionTheory.Lime.T3.derivative_upper_bound/)

Let $m\ge2$, $\epsilon\in\{+,-\}^m$, and $\lambda_1>\cdots>\lambda_m$ with $\lambda_i-(m-1)/2\in\mathbb Z$. Let $\pi$ on a complex Hilbert space satisfy the discrete-series conditions of ([A nonzero discrete-series coefficient integral gives an intertwiner](https://andrewodesky.com/rh/lean/PositivityTheory.RgHe.LowestKTypeModel.ofInt/)) for $(\epsilon,\lambda)$ on $U(\epsilon)$, and suppose $$|\lambda_i|\le B,\qquad |\lambda_i-\lambda_j|\ge100m^3\quad(\epsilon_i\ne\epsilon_j).$$ Let $\mu$ be Haar measure and let $d>0$ be a formal degree for $\pi$ relative to $\mu$ in the matrix-coefficient identity specified below. Put $\mathcal B_\epsilon(\delta)=\{g\in U(\epsilon):\sum_{i,j}|g_{ij}-\delta_{ij}|^2\le\delta^2\}$. Then $$d\,\mu\!\left(\mathcal B_\epsilon\left((100m(B+1))^{-2}\right)\right)\le4.$$ The product and inequality are interpreted in the nonnegative extended reals.
