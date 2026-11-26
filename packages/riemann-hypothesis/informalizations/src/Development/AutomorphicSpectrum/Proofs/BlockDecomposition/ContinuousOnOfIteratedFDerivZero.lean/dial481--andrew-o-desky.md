---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ContinuousOnOfIteratedFDerivZero.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.ParamInt.intSmooth"
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

## Smoothness of a parameter integral with local compact support

[Theorem REP.0225](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.ParamInt.intSmooth/)

Let $X$ be a second-countable topological space with a measurable structure in which open sets are measurable, and let $\nu$ be a measure finite on compact sets. Let $V$ be a finite-dimensional complex normed vector space, $n\ge0$, and $F:X\times M_n(\mathbb C)\to V$. Suppose:

1. For every $t\in X$, the function $g\mapsto F(t,g)$ is smooth over $\mathbb R$ on $\operatorname{GL}_n(\mathbb C)$.
2. For every $m\ge0$, its $m$-th real Fréchet derivative is jointly continuous on $X\times\operatorname{GL}_n(\mathbb C)$.
3. For every $g_0\in\operatorname{GL}_n(\mathbb C)$ there are a neighborhood $U$ of $g_0$ and a compact $C\subseteq X$ such that $F(t,g)=0$ for $t\notin C$ and $g\in U$.

Then $g\mapsto\int_X F(t,g)\,d\nu(t)$ is smooth over $\mathbb R$ on $\operatorname{GL}_n(\mathbb C)$.
