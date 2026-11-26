---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/AutomorphicForms/TemperedLocalComponents/PCuspFin.lean",
  "declarations": [
    "UpperTheory.V.Af.cuspFormsFiniteReal"
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

## Finite-dimensional cusp spaces over a totally real field

[Theorem AGR.0584](https://andrewodesky.com/rh/lean/UpperTheory.V.Af.cuspFormsFiniteReal/)

Let $F$ be a totally real number field, let $a\ge0$, and let $L\subseteq\operatorname{GL}_a(\mathbb A_{F,f})$ be an open subgroup. Put $K_\infty=\prod_{v\mid\infty}O(a)$. Let $\rho$ be a finite-dimensional complex representation of $K_\infty$ whose matrix coefficients are continuous, and prescribe a function $c_v:\mathbb C\to\mathbb C$ for every infinite place $v$. The complex span of smooth cuspidal automorphic forms $\varphi$ on $\operatorname{GL}_a(\mathbb A_F)$ satisfying $$\varphi(gk)=\varphi(g)\quad(k\in L),\qquad(k\mapsto\varphi(gk))\in\operatorname{span}\{k\mapsto\lambda(\rho(k)w)\},$$ for every $g$, and $$C_v(u)\varphi=c_v(u)\varphi\qquad(v\mid\infty,\ u\in\mathbb C),$$ is finite-dimensional. The matrix-coefficient span ranges over all $w$ in the representation space and all complex-linear functionals $\lambda$.
