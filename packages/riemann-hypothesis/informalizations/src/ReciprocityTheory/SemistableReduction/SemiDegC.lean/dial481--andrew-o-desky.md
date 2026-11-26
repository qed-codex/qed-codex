---
{
  "module": "src/ReciprocityTheory/SemistableReduction/SemiDegC.lean",
  "declarations": [
    "ReciprocityTheory.MultiplicativeHeights.integralIndex_holds"
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

## The index of an integral Hermitian lattice is bounded by its Gram determinant

[Theorem ANT.0928](https://andrewodesky.com/rh/lean/ReciprocityTheory.MultiplicativeHeights.integralIndex_holds/)

Let $K$ be a number field with an involution $c$ such that $\tau(c(x))=\overline{\tau(x)}$ for every embedding $\tau:K\hookrightarrow\mathbb C$. Let $h$ be a $c$-Hermitian form on $K^r$, conjugate-linear in its first argument. Let $B\subseteq K^r$ be a finitely generated $\mathcal O_K$-module with $h(B,B)\subseteq\mathcal O_K$. Suppose $b_1,\ldots,b_k\in B$ are $K$-linearly independent and span $B$ over $K$. Set $G=(h(b_i,b_j))_{i,j}$, and assume $\det G\ne0$. Then $$\left[B:\sum_{i=1}^k\mathcal O_K b_i\right]^2\le\left|N_{K/\mathbb Q}(\det G)\right|.$$
