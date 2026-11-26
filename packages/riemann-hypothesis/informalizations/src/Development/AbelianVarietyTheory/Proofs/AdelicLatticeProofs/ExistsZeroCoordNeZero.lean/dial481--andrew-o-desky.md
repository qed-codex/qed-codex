---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/AdelicLatticeProofs/ExistsZeroCoordNeZero.lean",
  "declarations": [
    "GlobalTheory.LocalQuad.HermClass.congr_diagonal"
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

## Congruence of diagonal Hermitian forms

[Theorem ALG.1389](https://andrewodesky.com/rh/lean/GlobalTheory.LocalQuad.HermClass.congr_diagonal/)

Assume the following isotropy assertion: over every number field $F$, a diagonal quadratic form with at least five nonzero coefficients represents zero nontrivially if it is indefinite at every real embedding of $F$.

Let $E$ be a CM number field, with complex conjugation $x\mapsto\bar x$, and let $r\ge0$. Let $g_1,\ldots,g_r$ and $g'_1,\ldots,g'_r$ be nonzero elements of $E$ fixed by conjugation. Suppose that for every embedding $\tau:E\hookrightarrow\mathbb C$ the numbers of positive entries among $(\tau(g_i))$ and $(\tau(g'_i))$ agree, and that some $x\in E$ satisfies $$\prod_i g_i=x\bar x\prod_i g'_i.$$ Then there is an invertible matrix $P\in\mathrm{GL}_r(E)$ such that $$\operatorname{diag}(g'_i)=P^{\mathsf T}\operatorname{diag}(g_i)\overline P.$$
