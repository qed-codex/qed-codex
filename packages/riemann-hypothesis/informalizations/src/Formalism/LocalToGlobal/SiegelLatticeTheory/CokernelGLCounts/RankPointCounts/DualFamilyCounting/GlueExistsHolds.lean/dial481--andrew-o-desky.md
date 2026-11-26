---
{
  "module": "src/Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/GlueExistsHolds.lean",
  "declarations": [
    "Formalism.L2.SG.Pf.Cnt.glueExists_holds"
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

## Extending an integral Hermitian lattice to a unimodular lattice

[Theorem ANT.0308](https://andrewodesky.com/rh/lean/Formalism.L2.SG.Pf.Cnt.glueExists_holds/)

Let $K$ be a totally complex number field with involution $x\mapsto\bar x$, with $\varphi(\bar x)=\overline{\varphi(x)}$ for every complex embedding. Suppose that for every maximal ideal $\mathfrak P\subset\mathcal O_K$ some $\theta\in\mathcal O_K$ satisfies $\theta-\bar\theta\notin\mathfrak P$. Let $F$ be a number field contained in $K$ whose image is exactly the fixed field of the involution. Let $(V,h)$ be a finite-dimensional nondegenerate Hermitian space over $K$, conjugate-linear in the first variable. Let $U\subseteq V$ satisfy $$V=U\oplus U^\perp,$$ and suppose $h$ is positive definite on $U^\perp$ at every complex embedding. Assume $V$ admits a full unimodular $\mathcal O_K$-lattice. Let $M\subset U$ be a finitely generated full $\mathcal O_K$-lattice in $U$ with $h(M,M)\subseteq\mathcal O_K$. If $$c_{\mathfrak p}(M)<\dim_KU^\perp\qquad(\mathfrak p\subset\mathcal O_F\text{ maximal}),$$ then there is a full unimodular lattice $\Lambda\subset V$ such that $\Lambda\cap U=M$.
