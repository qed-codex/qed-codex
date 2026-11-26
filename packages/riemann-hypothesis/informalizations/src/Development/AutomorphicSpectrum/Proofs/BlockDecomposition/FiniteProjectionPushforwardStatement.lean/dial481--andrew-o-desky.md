---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/FiniteProjectionPushforwardStatement.lean",
  "declarations": [
    "GlobalTheory.T.finite_projection_pushforward"
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

## A proper disc cover inside an irreducible analytic germ

[Theorem AG.1718](https://andrewodesky.com/rh/lean/GlobalTheory.T.finite_projection_pushforward/)

Assume the following four general analytic projection results: openness of finite germ projections, existence of a primitive linear form for an irreducible germ, holomorphic sheets off its discriminant, and constancy of the number of sheets of a proper unbranched projection.

Let $Y\subseteq\mathbb C^n$ be cut out by finitely many holomorphic functions near $w$, and suppose its germ at $w$ is irreducible. Let $A:\mathbb C^n\to\mathbb C$ be complex linear. Assume there is a neighborhood $U$ of $w$ with $\{x\in Y\cap U:A(x)=A(w)\}=\{w\}$. Also assume that every function $h$ holomorphic near $A(w)$ which vanishes on $A(Y)$ near $w$ vanishes as a germ at $A(w)$.

There are $Y'\subseteq Y$, a complex-linear $p:\mathbb C^n\to\mathbb C$, $\rho>0$ and an integer $N>0$ such that $w\in Y'$, $p(Y')\subseteq B(p(w),\rho)$, the fiber over $p(w)$ is $\{w\}$, and every other fiber over this disc has exactly $N$ points. Preimages in $Y'$ of compact subsets of the disc are compact. At every $x\in Y'$ with $p(x)\ne p(w)$ there are ambient open sets $V\ni x$, $O\subseteq\mathbb C$ and a holomorphic map $g:O\to\mathbb C^n$ with $p\circ g=\mathrm{id}_O$ and $Y'\cap V=g(O)$.
