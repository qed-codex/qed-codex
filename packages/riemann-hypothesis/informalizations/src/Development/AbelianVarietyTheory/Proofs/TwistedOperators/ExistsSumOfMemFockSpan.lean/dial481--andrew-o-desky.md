---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExistsSumOfMemFockSpan.lean",
  "declarations": [
    "GlobalTheory.FockApprox.theta_approx_fock"
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

## Approximation of theta functions by polynomial Fock vectors

[Theorem THETA.0881](https://andrewodesky.com/rh/lean/GlobalTheory.FockApprox.theta_approx_fock/)

Fix the source's full arithmetic oscillator datum, compatible archimedean coordinates, and a standard adelic additive character $\psi$ of sign $-1$. Choose two of its framed Hermitian lattice objects $S,T$, and a sign $\varepsilon\in\{0,1\}$ on $S$. Let $W$ be their adelic oscillator space, and let $U\subseteq W$ be an open additive subgroup. Let $\Theta_U$ be the space of permitted theta functions fixed by every Heisenberg translation in $U$ whose infinite component is zero. Choose an additive Haar measure $\mu$ and a fundamental domain $\mathcal F$ of measure one for the rational lattice in $W$.

For every $\Phi\in\Theta_U$, integer $d\ge0$, and $\delta>0$, there are $n\ge0$, theta functions $f_1,\ldots,f_n$ that are Fock vacua at every archimedean place, and polynomials $P_1,\ldots,P_n$ in the associated Fock variables, such that $$R=\Phi-\sum_{j=1}^n P_j\cdot f_j\in\Theta_U,\qquad \sum_{k=0}^d\ \sum_{a_1,\ldots,a_k}\|D_{a_1}\cdots D_{a_k}R\|_{L^2(\mathcal F,\mu)}<\delta.$$
