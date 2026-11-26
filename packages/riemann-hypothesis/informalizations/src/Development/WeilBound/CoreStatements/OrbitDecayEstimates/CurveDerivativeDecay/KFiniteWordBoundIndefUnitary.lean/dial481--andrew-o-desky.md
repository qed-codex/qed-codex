---
{
  "module": "src/Development/WeilBound/CoreStatements/OrbitDecayEstimates/CurveDerivativeDecay/KFiniteWordBoundIndefUnitary.lean",
  "declarations": [
    "CompanionTheory.Lime.T3.kFiniteWordBound_indefUnitary"
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

## Arbitrary complex Lie words on the lowest compact type

[Theorem REP.1436](https://andrewodesky.com/rh/lean/CompanionTheory.Lime.T3.kFiniteWordBound_indefUnitary/)

Let $m\ge2$, choose signs $\varepsilon_a\in\{\pm1\}$, and put $G=U(\operatorname{diag}\varepsilon)$. Let $\lambda_1>\cdots>\lambda_m$ satisfy $\lambda_a-(m-1)/2\in\mathbb Z$. Let $B\in\mathbb R$ satisfy $|\lambda_a|\le B$ and $$|\lambda_a-\lambda_b|\ge100m^3\qquad(\varepsilon_a\ne\varepsilon_b).$$ Let $\pi$ be a discrete series model of parameter $\lambda$ with all the conditions in the conventions below. Let $H_\lambda$ be the sum of compact types of highest weight $\lambda+\rho_n-\rho_c$, where $\rho_n,\rho_c$ are the half sums of noncompact and compact positive roots. Every $v\in H_\lambda$ is smooth. For every integer $S\ge0$ and every list of complex matrices $Y_1,\ldots,Y_\ell$ with $\ell\le S$ and $\sum_{a,b}|(Y_j)_{ab}|^2\le1$, $$\|d\pi_{\mathbb C}(Y_1)\cdots d\pi_{\mathbb C}(Y_\ell)v\| \le\bigl(8\sqrt m\,(B+S)\bigr)^\ell\|v\|,$$ where $d\pi_{\mathbb C}$ is the complex-linear extension of the real Lie action.

**Short real Lie words.** Put $J_\varepsilon=\operatorname{diag}\varepsilon$ and $\mathfrak g=\{X:X^*J_\varepsilon+J_\varepsilon X=0\}$. If, in addition, $m\ge3$ and $$|\lambda_a-\lambda_b|\ge1000m^3\qquad(\varepsilon_a\ne\varepsilon_b),$$ then for every unit vector $v\in H_\lambda$ and every list $X_1,\ldots,X_\ell\in\mathfrak g$ with $\ell\le m+2$, $$\|d\pi(X_1)\cdots d\pi(X_\ell)v\|\le\prod_{j=1}^{\ell}(8mB)^2\|X_j\|_{\mathrm{HS}},\qquad \|X\|_{\mathrm{HS}}=\Bigl(\sum_{a,b}|X_{ab}|^2\Bigr)^{1/2}.$$
