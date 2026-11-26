---
{
  "module": "src/Formalism/SharpRestriction/CuspSpanNormBounds/CayleyDegreeNondegeneracy/TraceInnerPosOfOrthonormalPair.lean",
  "declarations": [
    "Formalism.MainNotions.BridgeLemma₂.short_vector_every_place"
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

## A vector bounded at every embedding in a binary Hermitian genus

[Theorem ANT.0753](https://andrewodesky.com/rh/lean/Formalism.MainNotions.BridgeLemma%E2%82%82.short_vector_every_place/)

Let $K$ be a totally complex number field with an involution $a\mapsto\overline a$ such that $\tau(\overline a)=\overline{\tau(a)}$ for every complex embedding $\tau$. Assume that for every maximal ideal $\mathfrak p\subset\mathcal O_K$ there is $\theta\in\mathcal O_K$ with $\theta-\overline\theta\notin\mathfrak p$. Put $$\operatorname{rd}_K=|\operatorname{disc}K|^{1/[K:\mathbb Q]}.$$ Let $V$ be a $K$-vector space with compatible $\mathcal O_K$-module structure and a Hermitian form $h$, conjugate-linear in the first variable. Suppose $V$ has a basis $e_1,e_2$ with $h(e_i,e_j)=\delta_{ij}$, and put $L=\mathcal O_Ke_1+\mathcal O_Ke_2$.

For every full $\mathcal O_K$-lattice $M$ in the genus of $L$, there is $0\ne x\in M$ such that $$|\tau(h(x,x))|\le2[K:\mathbb Q]\operatorname{rd}_K\qquad(\tau:K\hookrightarrow\mathbb C).$$
