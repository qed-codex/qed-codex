---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CoboundaryIffIsCrys.lean",
  "declarations": [
    "GlobalTheory.CrysExtCrit.coboundary_iff_isCrys"
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

## Crystallinity of a codimension-one extension and a period coboundary

[Theorem PHT.0718](https://andrewodesky.com/rh/lean/GlobalTheory.CrysExtCrit.coboundary_iff_isCrys/)

Let $p$ be prime, let $K,L$ be finite extensions of $\mathbb Q_p$, and use the local period data specified below. Let $V_0,V_1$ be finite-dimensional $L$-representations of $G_K$, with their compatible $\mathbb Q_p$-scalar structures. Let $\iota:V_0\hookrightarrow V_1$ be an equivariant $L$-linear injection with $\dim_LV_1=\dim_LV_0+1$, and suppose $V_0$ is crystalline. Fix $x\notin\iota(V_0)$ and a function $c:G_K\to V_0$ such that $$\iota(c(g))=g x-x\qquad(g\in G_K).$$ Then $V_1$ is crystalline if and only if there exists $y\in V_0\otimes_{\mathbb Q_p}B_{\mathrm{cris}}$ with $$c(g)\otimes1=g y-y\qquad(g\in G_K).$$
