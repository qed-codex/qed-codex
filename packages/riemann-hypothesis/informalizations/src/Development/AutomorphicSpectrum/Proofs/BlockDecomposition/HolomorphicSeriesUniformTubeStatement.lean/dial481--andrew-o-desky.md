---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/HolomorphicSeriesUniformTubeStatement.lean",
  "declarations": [
    "GlobalTheory.T.holomorphic_series_uniform_tube"
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

## Holomorphy and uniform strip bounds for a sum

[Theorem ALG.1343](https://andrewodesky.com/rh/lean/GlobalTheory.T.holomorphic_series_uniform_tube/)

Let $X$ be a complex Banach space, $T$ a topological space, $I$ an index set, and $\Omega\subseteq\mathbb R^2$. Let $f_r:\mathbb C^2\times T\to X$ for $r\in I$. Suppose each $f_r$ is jointly continuous and, for all $p,v\in\mathbb C^2$ and $g\in T$, the function $\tau\mapsto f_r(p+\tau v,g)$ is entire.

For $V\subseteq\mathbb R^2$ write $\mathcal T(V)=\{z\in\mathbb C^2:\operatorname{Re}z\in V\}$. Assume that for each $x\in\Omega$ and $g\in T$ there are neighborhoods $V$ of $x$ and $U$ of $g$ and a summable real family $(u_r)$ such that $$\|f_r(z,g')\|\le u_r\qquad(z\in\mathcal T(V),\ g'\in U,\ r\in I).$$ Then $F(z,g)=\sum_{r\in I}f_r(z,g)$ is jointly continuous on $\mathcal T(\Omega)\times T$, is holomorphic on every complex line within $\mathcal T(\Omega)$ for fixed $g$, and satisfies $$\sum_r\|f_r(z,g)\|<\infty\qquad(z\in\mathcal T(\Omega),\ g\in T).$$ For every compact $C\subseteq\Omega$ and $g\in T$ there are a neighborhood $U$ of $g$ and $M\in\mathbb R$ with $\|F(z,g')\|\le M$ for all $z\in\mathcal T(C)$, $g'\in U$.
