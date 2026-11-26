---
{
  "module": "src/Formalism/LocalToGlobal/Columns/CoefModB.lean",
  "declarations": [
    "Formalism.L2.DIV.fockB"
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

## Bilinear factorial pairing of polynomials

[Definition / hypothesis ALG.D027](https://andrewodesky.com/rh/lean/Formalism.L2.G.Model.TS.fockR/)

Let $R$ be a commutative ring and $S$ a set of variables. For a finitely supported function $\alpha:S\to\mathbb N$, write $$X^\alpha=\prod_{s\in\operatorname{supp}(\alpha)}X_s^{\alpha(s)},\qquad \alpha!=\prod_{s\in\operatorname{supp}(\alpha)}\alpha(s)!.$$ An empty product is $1$.

For polynomials $P,Q\in R[X_s:s\in S]$, let $P_\alpha,Q_\alpha$ be their coefficients at $X^\alpha$. The bilinear factorial pairing is $$[P,Q]_{\rm fac}=\sum_{\alpha\in\operatorname{supp}(P)}P_\alpha Q_\alpha\,\alpha!,$$ where $\operatorname{supp}(P)=\{\alpha:P_\alpha\ne0\}$ and each integer $\alpha!$ is mapped to $R$ by its natural ring homomorphism.
