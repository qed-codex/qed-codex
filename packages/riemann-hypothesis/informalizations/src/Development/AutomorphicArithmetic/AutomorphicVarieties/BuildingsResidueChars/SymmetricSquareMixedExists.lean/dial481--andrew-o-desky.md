---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/BuildingsResidueChars/SymmetricSquareMixedExists.lean",
  "declarations": [
    "UpperTheory.symmetric_square_mixed_exists"
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

## A four-dimensional symplectic extension from an index-two subgroup

[Theorem ALG.0220](https://andrewodesky.com/rh/lean/UpperTheory.symmetric_square_mixed_exists/)

Let $k$ be a field with $2\ne0$, $j:\Gamma_0\hookrightarrow\Gamma$ an injective homomorphism with image of index two, and $t\notin j(\Gamma_0)$. Let $\alpha,\beta\in k^\times$, $\rho:\Gamma_0\to\operatorname{GL}_2(k)$ and $\mu:\Gamma\to k^\times$ satisfy $$\rho(u)=\operatorname{diag}(\alpha^2,\beta^2)\quad\text{if }j(u)=t^2,\qquad \det\rho(h)=\mu(j(h)),\qquad\alpha\beta=\mu(t).$$ There is $R:\Gamma\to\operatorname{GL}_4(k)$ with $$R(t)=\operatorname{diag}(\beta,-\alpha,-\beta,\alpha),\qquad R(j(h))=M_{\beta/\alpha}(\rho(h),\rho(h'))\quad\text{if }j(h')=t^{-1}j(h)t,$$ and $R(g)^t\mathcal JR(g)=\mu(g)\mathcal J$ for every $g\in\Gamma$.
