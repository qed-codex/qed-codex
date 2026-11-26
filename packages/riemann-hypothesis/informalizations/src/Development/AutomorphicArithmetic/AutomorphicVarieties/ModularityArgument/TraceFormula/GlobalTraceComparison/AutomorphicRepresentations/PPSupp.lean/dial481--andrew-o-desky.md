---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/TraceFormula/GlobalTraceComparison/AutomorphicRepresentations/PPSupp.lean",
  "declarations": [
    "UpperTheory.V.Z.Tf.GlobalTraceComparison.Pi.pSupp_pf"
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

## Cuspidal projection preserves determinant support

[Theorem REP.0238](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.Tf.GlobalTraceComparison.Pi.pSupp_pf/)

Let $E$ be a CM number field and $n\ge0$. Put $G=\operatorname{GL}_n(\mathbb A_E)\times\operatorname{GL}_0(\mathbb A_E)$ and $\Gamma=\operatorname{GL}_n(E)\times\operatorname{GL}_0(E)$. Choose a left and right invariant, locally finite, positive-on-open-sets Borel measure $\mu$ on $G$, a fundamental domain $\mathcal F$ for $\Gamma$, and $\nu=\mu|_{\mathcal F}$. Write $\ell(g)=\log|\det g_1|_{\mathbb A_E}$.

Let $\pi$ be a cuspidal subspace of automorphic forms in the realization specified in the conventions below. In $L^2(G,\nu)$, let $P_\pi$ be orthogonal projection onto the closure of the span of functions $$g\longmapsto\psi(g_1)u(\ell(g)),\qquad\psi\in\pi,\quad u\in C_c(\mathbb R).$$ For all $a,b\in\mathbb R$ and $v\in L^2(G,\nu)$, $$v=0\text{ almost everywhere on }\{g:\ell(g)\notin[a,b]\} \quad\Longrightarrow\quad P_\pi v=0\text{ almost everywhere on the same set}.$$
