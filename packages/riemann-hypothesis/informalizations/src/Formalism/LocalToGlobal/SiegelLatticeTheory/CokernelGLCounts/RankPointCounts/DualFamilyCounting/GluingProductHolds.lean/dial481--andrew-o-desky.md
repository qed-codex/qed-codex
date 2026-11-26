---
{
  "module": "src/Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/GluingProductHolds.lean",
  "declarations": [
    "Formalism.L2.SG.Pf.Cnt.gluing_product_holds"
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

## A product formula for self-dual lattice extensions

[Theorem ARAK.0578](https://andrewodesky.com/rh/lean/Formalism.L2.SG.Pf.Cnt.gluing_product_holds/)

Let $K$ be a totally complex number field with an involution inducing complex conjugation under every complex embedding, and suppose that for every maximal ideal $\mathfrak q\subseteq\mathcal O_K$ some $\theta\in\mathcal O_K$ satisfies $\theta-\bar\theta\notin\mathfrak q$. Let $F$ be its fixed field. Let $(V,h)$ be a finite-dimensional nondegenerate Hermitian $K$-space and let $U\subseteq V$ satisfy $$V=U\oplus U^\perp,$$ with $h$ positive definite on $U^\perp$ at every embedding. Let $M\subseteq U$ and $T\subseteq U^\perp$ be finitely generated $\mathcal O_K$-modules spanning their respective spaces. Fix a full self-dual lattice $\Lambda_0\subseteq V$ with $\Lambda_0\cap U=M$, and put $T_0=\Lambda_0\cap U^\perp$. For a maximal ideal $\mathfrak p\subseteq\mathcal O_F$, let $b_{\mathfrak p}(M,T)$ count the self-dual localized full lattices $L\subseteq V$ with $$L\cap U=M_{\mathfrak p},\qquad L\cap U^\perp=T_{\mathfrak p}.$$ Then $b_{\mathfrak p}(M,T)\ne0$ for every $\mathfrak p$ if and only if, for every $\mathfrak p$, an isometry of $V$ fixing $U$ pointwise carries $(T_0)_{\mathfrak p}$ onto $T_{\mathfrak p}$. Moreover, $$\operatorname{card}_0\{\Lambda\subseteq V:\Lambda\text{ full and self-dual},\ \Lambda\cap U=M,\ \Lambda\cap U^\perp=T\} =\prod_{\mathfrak p}'b_{\mathfrak p}(M,T).$$
