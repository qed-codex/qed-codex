---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/HeightProofs/EqMatrixCoeffOfLocallyUniformLimitKFinite.lean",
  "declarations": [
    "GlobalTheory.TypeSum.CoefClos.eq_coef_of_closure"
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

## Closedness of a finite sum of distribution-coefficient spaces

[Theorem REP.0814](https://andrewodesky.com/rh/lean/GlobalTheory.TypeSum.CoefClos.eq_coef_of_closure/)

Assume the Harish–Chandra module and Casselman–Wallach packages specified in the conventions. Let $J$ be a diagonal $n\times n$ matrix with diagonal entries in $\{\pm1\}$, put $G=\{g:g^*Jg=J\}$, and let $K$ be its block-diagonal maximal compact subgroup. Let $\sigma$ be an irreducible unitary representation of $G$ on a complex Hilbert space $H$. Assume every $K$-finite vector is smooth, $\sigma$ admits a formal degree, and it has a nonzero $K$-finite vector. Fix $K$-finite vectors $w_1,\ldots,w_d$.

Let $h:G\to\mathbb C$ be continuous with uniformly moderate growth of all right derivatives. Suppose that for every compact $C\subseteq M_n(\mathbb C)$ and every $\delta>0$, there are complex-linear maps $L_a:H\to\mathbb C$, each bounded by a finite Sobolev seminorm on smooth vectors, such that $$\left|h(y)-\sum_{a=1}^dL_a(\sigma(y)w_a)\right|<\delta\qquad(y\in C\cap G).$$ Then there are such maps $L_1,\ldots,L_d$ for which $$h(y)=\sum_{a=1}^dL_a(\sigma(y)w_a)\qquad(y\in G).$$
