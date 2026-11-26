---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/TransgressionTopChernFormGoodPatchStatement.lean",
  "declarations": [
    "GlobalTheory.T.transgression_topChernForm_goodPatch"
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

## A local transgression integral for a metric with boundary growth

[Theorem AG.1543](https://andrewodesky.com/rh/lean/GlobalTheory.T.transgression_topChernForm_goodPatch/)

Let $F\hookrightarrow\mathbb C$, let $X/F$ be smooth, geometrically integral and projective of dimension $d$, and let $E$ be a rank-$m$ vector bundle. Give $E$ smooth positive Hermitian metrics $H$ on an open $O\subseteq X$ and $H_0$ on all of $X$. Suppose a holomorphic chart $e$, a set of coordinate indices $S$, an algebraic frame and an open $W$ in the chart satisfy $$O(\mathbb C)\cap W=\{z\in W:z_a\ne0\ (a\in S)\},\qquad |z_a|\le\tfrac12\ (z\in W,a\in S).$$ Put $w_a=|z_a||\log|z_a||$ for $a\in S$ and $w_a=1$ otherwise. Assume some $c\in\mathbb R$ bounds the Chern connection and curvature matrices in this frame by $$|(A_H)_a{}_{ij}|w_a\le c,\qquad |(\Omega_H)_{ab}{}_{ij}|w_aw_b\le c$$ on $O(\mathbb C)\cap W$. For every smooth real $\rho$ with $\operatorname{supp}\rho\subseteq W$, the three densities $\rho c_d(E,H)$, $\rho c_d(E,H_0)$ and the following transgression correction are absolutely integrable on their respective domains, and $$\int_{O(\mathbb C)}\rho c_d(E,H)-\int_{X(\mathbb C)}\rho c_d(E,H_0) =\int_{O(\mathbb C)}\mathcal T_\rho(H_0,H).$$ Here $\mathcal T_\rho$ is the following normalized mixed-determinant density: in each algebraic chart it is $\pi^{-d}$ times the real part of the sum, for $0\le j<d$, of the mixed top Chern expression with $j$ curvature factors from $H$, one factor $\bar\partial\rho\,(A_H-A_{H_0})$, and $d-1-j$ curvature factors from $H_0$.
