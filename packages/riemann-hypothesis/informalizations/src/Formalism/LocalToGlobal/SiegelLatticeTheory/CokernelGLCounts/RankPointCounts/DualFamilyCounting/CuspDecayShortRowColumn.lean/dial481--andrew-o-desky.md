---
{
  "module": "src/Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/CuspDecayShortRowColumn.lean",
  "declarations": [
    "Formalism.L2.SG.Pf.G1.jordan_exists"
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

## Orthogonal local generators of an integral Hermitian lattice

[Theorem ALG.0652](https://andrewodesky.com/rh/lean/Formalism.L2.SG.Pf.G1.jordan_exists/)

Let $K,F$ be number fields with $F\subseteq K$, and let $c$ be an involution of $K$ with fixed field $F$. Assume $K$ is totally complex, every complex embedding carries $c$ to complex conjugation, and for every maximal ideal $P\subseteq\mathcal O_K$ some $\theta\in\mathcal O_K$ satisfies $\theta-c(\theta)\notin P$.

Let $V$ be a finite-dimensional $K$-vector space with its compatible $\mathcal O_K$-module structure, let $h$ be Hermitian, let $X\subseteq V$ be a subspace on which $h$ is nondegenerate, and let $L\subseteq V$ be a finitely generated $\mathcal O_K$-module spanning $X$. Assume $h(L,L)\subseteq\mathcal O_K$. For every maximal ideal $\mathfrak p\subseteq\mathcal O_F$, there are $b_1,\ldots,b_d\in X$ and nonzero $a_1,\ldots,a_d\in\mathcal O_F$, with $d=\dim_K X$, such that $$L_{\mathfrak p}=\sum_{i=1}^{d}(\mathcal O_K)_{\mathfrak p}b_i,\qquad h(b_i,b_j)=0\ (i\ne j),\qquad h(b_i,b_i)=a_i.$$
