---
{
  "module": "src/Formalism/PeriodIntegrals/OrbitalBoundsConclusion/PolyCoef.lean",
  "declarations": [
    "polynomial_coefficients"
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

## Polynomial matrix coefficients after a determinant twist

[Theorem REP.0359](https://andrewodesky.com/rh/lean/polynomial_coefficients/)

Let $N\ge0$ and let $H$ be a complex inner product space. Let $\sigma$ assign a bounded complex-linear operator on $H$ to each matrix in $M_N(\mathbb C)$, with restriction to $U(N)$ a unitary representation whose orbit maps are continuous. Let $S\subseteq H$ be a finite-dimensional $U(N)$-stable subspace. For every $v\in S$ and $w\in H$, there are $k\ge0$ and a polynomial $P\in\mathbb C[X_{ij}:1\le i,j\le N]$ such that $$\langle w,\sigma(g)v\rangle\det(g)^k=P((g_{ij}))\qquad(g\in U(N)).$$ The inner product is conjugate-linear in its first argument.
