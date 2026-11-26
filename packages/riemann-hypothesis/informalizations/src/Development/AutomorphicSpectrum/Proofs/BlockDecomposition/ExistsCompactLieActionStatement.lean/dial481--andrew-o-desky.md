---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ExistsCompactLieActionStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_compact_lie_action"
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

## Infinitesimal operators of a finite-dimensional unitary representation

[Theorem REP.0707](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_compact_lie_action/)

Let $H$ be a finite-dimensional complex inner product space and $\rho:U(n)\to\operatorname{End}_{\mathbb C}^{\mathrm{cont}}(H)$ a continuous monoid homomorphism with $\|\rho(k)v\|=\|v\|$ for every $k,v$. There exist complex-linear operators $G_{ab}:H\to H$ such that $$[G_{ab},G_{cd}]=\delta_{bc}G_{ad}-\delta_{da}G_{cb},\qquad \langle G_{ab}x,y\rangle=\langle x,G_{ba}y\rangle.$$ For every skew-Hermitian $X\in M_n(\mathbb C)$ and every function $\gamma:\mathbb R\to U(n)$ with $\gamma(t)=\exp(tX)$ as matrices, $$\left.\frac d{dt}\rho(\gamma(t))w\right|_{t=0} =\sum_{a,b}X_{ab}G_{ab}w\qquad(w\in H).$$
