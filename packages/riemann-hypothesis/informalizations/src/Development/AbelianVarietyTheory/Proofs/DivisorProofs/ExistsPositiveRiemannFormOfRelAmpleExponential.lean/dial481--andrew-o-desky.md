---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsPositiveRiemannFormOfRelAmpleExponential.lean",
  "declarations": [
    "GlobalTheory.exists_riemannForm_of_relAmple"
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

## A positive Riemann form compatible with the Weil pairing

[Theorem AV.1025](https://andrewodesky.com/rh/lean/GlobalTheory.exists_riemannForm_of_relAmple/)

Let $A\to X$ be a commutative abelian scheme smooth of constant relative dimension $g$, and let $L$ be a relatively ample line bundle on $A$. Let $y:\operatorname{Spec}\mathbb C\to X$, and let $e:\mathbb C^g\to A_y(\mathbb C)$ be a surjective holomorphic group homomorphism whose differential identifies $\mathbb C^g$ with the tangent space at the identity. Let $\Lambda$ be an abelian group and $P:\Lambda\hookrightarrow\mathbb C^g$ an injective additive map with image $\ker e$.

There are a positive definite Hermitian matrix $H$ and an integral bilinear form $E:\Lambda\times\Lambda\to\mathbb Z$ such that $$\operatorname{Im}\bigl((Pa)^tH\overline{Pb}\bigr)=E(a,b),$$ and for every $k\ge1$, $$e_{L^{\otimes k}}\bigl(e(Pa/k),e(Pb/k)\bigr)=\exp\!\left(-\frac{2\pi iE(a,b)}k\right).$$
