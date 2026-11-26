---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/SiegelThetaMapDeepLevelFiniteFibres.lean",
  "declarations": [
    "GlobalTheory.SiegThQF.finite_thData"
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

## Finiteness of fibres with prescribed theta coordinates

[Theorem AV.1285](https://andrewodesky.com/rh/lean/GlobalTheory.SiegThQF.finite_thData/)

Let $g\ge0$, $n\ge2$, and let $\mathcal F\to X$ be a Siegel family of principally polarized abelian varieties of dimension $g$ with level $n$ over $R_n=\mathbb Z[\zeta_n,1/n]$, satisfying the Siegel-family package in the conventions. Fix $W\in M_8(\mathbb Z)$ such that $W+W^t$ is positive definite over $\mathbb R$ and $\det(W+W^t)=1$.

Let $\ell$ be an odd prime, let $h\ge0$ and $j\ge4$, and suppose that $$\ell^{4h}h!<\ell^j.$$ Let $K$ be any algebraically closed field with $\ell\ne0$ in $K$, choose $\zeta\in K^\times$, and fix a vector $$v:(\mathbb Z/\ell^{2j}\mathbb Z)^{2h}\longrightarrow K.$$ There are only finitely many $y\in X(K)$ for which there exist a polarized abelian variety $(A,L)$ of dimension $h$, a full level $\ell^{2j}$ structure with pairing parameter $\zeta$, and the following two properties:

1. $(A,L)$ is isomorphic to the eightfold product of the polarized fibre at $y$, with its line bundle formed from the fibre's Poincare bundle using the coefficients $W_{ab}$.
2. Its level structure has theta coordinate vector $v$ at parameter $\ell^j$, in the following convention: symmetric theta-group lifts of the level points act on the pullback of a generating theta section, their values are evaluated at the identity, and one common nonzero scalar is allowed.
