---
{
  "module": "src/Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/JordanIsometryHolds.lean",
  "declarations": [
    "Formalism.L2.SG.Pf.Cnt.jordan_isometry_holds"
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

## Equal local diagonal valuations give a rational Hermitian isometry

[Theorem ANT.0935](https://andrewodesky.com/rh/lean/Formalism.L2.SG.Pf.Cnt.jordan_isometry_holds/)

Let $K$ be a totally complex number field with involution $c$ satisfying $\tau(c(a))=\overline{\tau(a)}$ for every complex embedding. Suppose that for every maximal ideal $P\subseteq\mathcal O_K$ there is $\theta\in\mathcal O_K$ with $\theta-c(\theta)\notin P$. Let $F\subseteq K$ be a number field equal to the fixed field of $c$, and let $(V,h)$ be a finite-dimensional Hermitian $K$-space positive definite at every complex embedding.

Let $L,L'$ be full $\mathcal O_K$-lattices and $\mathfrak p$ a maximal ideal of $\mathcal O_F$. Suppose $b_1,\ldots,b_n$ and $b'_1,\ldots,b'_n$ lie in $V$, where $n=\dim_KV$, and generate the same localized lattices as $L,L'$, respectively, after inverting $\mathcal O_F\setminus\mathfrak p$. Suppose both families are orthogonal, with $$h(b_i,b_i)=a_i,\qquad h(b'_i,b'_i)=a'_i,\qquad a_i,a'_i\in\mathcal O_F\setminus\{0\},\qquad v_{\mathfrak p}(a_i)=v_{\mathfrak p}(a'_i).$$ There is a $K$-linear isometry $g$ of $(V,h)$ carrying $L_{\mathfrak p}$ onto $L'_{\mathfrak p}$.
