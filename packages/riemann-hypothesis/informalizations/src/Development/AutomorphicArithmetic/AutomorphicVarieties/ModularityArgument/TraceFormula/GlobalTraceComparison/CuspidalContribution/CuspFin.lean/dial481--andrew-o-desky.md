---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/TraceFormula/GlobalTraceComparison/CuspidalContribution/CuspFin.lean",
  "declarations": [
    "UpperTheory.V.Z.Tf.GlobalTraceComparison.Cusp.cuspFin"
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

## Finitely many normalized cuspidal subspaces with bounded infinitesimal parameters

[Theorem AGR.0316](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.Tf.GlobalTraceComparison.Cusp.cuspFin/)

Let $E$ be a CM field, $N\ge1$, $K\subseteq\operatorname{GL}_N(\mathbb A_{E,f})$ an open subgroup, $W\subseteq\mathbb C^{K_\infty}$ a finite-dimensional linear subspace, and $R\in\mathbb R$. There are only finitely many cuspidal automorphic subspaces $\pi$ in the smooth realization specified in the conventions of ([Cuspidal projection preserves determinant support](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.Tf.GlobalTraceComparison.Pi.pSupp_pf/)) satisfying all three conditions:

1. $\pi$ is normalized, meaning that its real split central subgroup acts trivially.
2. Some nonzero $\phi\in\pi$ is right $K$-invariant and, for every $g\in\operatorname{GL}_N(\mathbb A_E)$, the function $k\mapsto\phi(gk)$ on $K_\infty$ belongs to $W$.
3. At every complex embedding of $E$, $\pi$ has an infinitesimal-character multiset all of whose elements have complex norm at most $R$.

Here $K_\infty$ is the product of the unitary groups $U(N)$ at the complex places; subspaces in the fixed realization, rather than their isomorphism classes, are counted.
