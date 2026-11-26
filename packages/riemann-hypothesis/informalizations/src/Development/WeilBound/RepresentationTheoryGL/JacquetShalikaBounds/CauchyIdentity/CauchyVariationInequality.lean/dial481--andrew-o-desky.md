---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/JacquetShalikaBounds/CauchyIdentity/CauchyVariationInequality.lean",
  "declarations": [
    "PositivityTheory.RgJS.cauchy_variation_inequality"
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

## Absolute convergence and sum of the Schur Cauchy series

[Theorem ALG.1191](https://andrewodesky.com/rh/lean/PositivityTheory.RgJS.cauchy_variation_inequality/)

Let $0\le m'\le m$, $\alpha\in(\mathbb C^\times)^m$, $\beta\in(\mathbb C^\times)^{m'}$, $X\in\mathbb C$, and $A,B\in\mathbb R$. Assume $$|\alpha_i|\le A,\quad |\beta_j|\le B,\quad |X|AB<1.$$ For a weakly decreasing tuple $\lambda=(\lambda_1,\ldots,\lambda_{m'})$ of nonnegative integers, let $\widetilde\lambda$ be its extension to length $m$ by zeros, let $|\lambda|=\sum_j\lambda_j$, and let $s_\lambda$ denote the Schur polynomial. Then $$\sum_\lambda\left|s_{\widetilde\lambda}(\alpha)s_\lambda(\beta)X^{|\lambda|}\right|<\infty,\qquad \sum_\lambda s_{\widetilde\lambda}(\alpha)s_\lambda(\beta)X^{|\lambda|}=\prod_{i=1}^m\prod_{j=1}^{m'}(1-\alpha_i\beta_jX)^{-1}.$$
