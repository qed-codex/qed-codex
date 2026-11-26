---
{
  "module": "src/Formalism/PeriodIntegrals/OrbitalBoundsConclusion/FiltLenF.lean",
  "declarations": [
    "filtration_length_bound"
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

## A quotient-length bound from a finite filtration

[Theorem ALG.0802](https://andrewodesky.com/rh/lean/filtration_length_bound/)

Let $R$ be a commutative ring, $W$ an $R$-module, and $F_0\supseteq F_1\supseteq\cdots$ a decreasing filtration with $F_0=W$ and $F_a=0$ for some $a\ge0$. For each $k\ge0$, let $V_k$ be an $R$-module and $\phi_k:F_k\to V_k$ linear, with $\ker\phi_k\subseteq F_{k+1}$. Let $N\subseteq M\subseteq W$ and let $P_k,Q_k\subseteq V_k$ satisfy, for $k<a$, $$\phi_k(M\cap F_k)\subseteq P_k,\qquad Q_k\subseteq\phi_k(N\cap F_k).$$ Then $$\operatorname{length}_R(M/N)\le\sum_{k=0}^{a-1}\operatorname{length}_R(P_k/Q_k).$$
