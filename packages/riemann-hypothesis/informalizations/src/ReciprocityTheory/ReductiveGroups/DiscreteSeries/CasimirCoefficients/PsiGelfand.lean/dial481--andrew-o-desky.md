---
{
  "module": "src/ReciprocityTheory/ReductiveGroups/DiscreteSeries/CasimirCoefficients/PsiGelfand.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.DS.S7.psiExists"
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

## An equivariant Casimir eigenfunction with exponential decay

[Theorem REP.0545](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.DS.S7.psiExists/)

Let $n\ge0$, choose signs $\varepsilon_1,\ldots,\varepsilon_n$, and put $J=\operatorname{diag}(\varepsilon_i)$, $G=\{g:g^*Jg=J\}$ and $K=G\cap U(n)$. Write $q_0=\min(\#\{i:\varepsilon_i=1\},\#\{i:\varepsilon_i=-1\})$, and assume $q_0\ge1$. Let $\lambda_1>\cdots>\lambda_n$ with $\lambda_i-(n-1)/2\in\mathbb Z$, and let $h\in\mathbb R$ satisfy $|\lambda_i-\lambda_j|\ge h$ when $\varepsilon_i\ne\varepsilon_j$. Let $\tau:K\to U(V)$ be a continuous irreducible representation on a finite-dimensional complex Hilbert space, with a complex-linear derived action and a unit highest-weight vector of weight $\lambda+\rho_n-\rho_c$. There is a smooth $\Psi:G\to\operatorname{End}_{\mathbb C}V$ such that $$\Psi(k_1gk_2)=\tau(k_1)\Psi(g)\tau(k_2),\qquad\Psi(1)=1,$$ $$\mathcal C\Psi=(\|\lambda\|_2^2-\|\rho\|_2^2)\Psi,$$ and, for $k\in K$ and $X\in\mathfrak p$, $$\|\Psi(k\exp X)\|\le\exp\left[-\frac h8\min\left\{\|X\|_{\mathrm{HS}}^2,\frac{\|X\|_{\mathrm{HS}}}{\sqrt{2q_0}}\right\}\right].$$ For every Haar measure on $G$, $\Psi$ is integrable if $h>16nq_0$ and square integrable if $h>8nq_0$. For every $s\ge0$ with $h>8nq_0+4s\sqrt{2q_0}$, $$\int_G\|\Psi(g)\|^2\|g\|_{\mathrm{HS}}^s\,dg<\infty.$$
