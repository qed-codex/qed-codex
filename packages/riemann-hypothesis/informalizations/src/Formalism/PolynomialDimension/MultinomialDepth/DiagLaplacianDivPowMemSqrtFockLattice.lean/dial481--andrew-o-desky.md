---
{
  "module": "src/Formalism/PolynomialDimension/MultinomialDepth/DiagLaplacianDivPowMemSqrtFockLattice.lean",
  "declarations": [
    "Formalism.CountingSumsFrames.fockLatticeProjection_holds"
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

## Denominator bounds for harmonic projections in a transported polynomial lattice

[Theorem ALG.0838](https://andrewodesky.com/rh/lean/Formalism.CountingSumsFrames.fockLatticeProjection_holds/)

Let $K$ be a characteristic-zero field, $k\ge1$, $A,B\ge0$, and $p$ prime. Let $R\subseteq K$ be a subring containing $1/n$ for every positive integer $n$ not divisible by $p$. Work in $K[x_1,\ldots,x_k,y_1,\ldots,y_k]$ and put $$h=\sum_{i=1}^kx_iy_i,\qquad \Delta=\sum_{i=1}^k\partial_{x_i}\partial_{y_i},\qquad h^{[l]}f=\frac{h^lf}{l!},\qquad\Delta^{[l]}f=\frac{\Delta^lf}{l!}.$$ Define $$H_{a,b}=\sum_{l=0}^{\min(a,b)}\frac{(-1)^l}{\binom{a+b+k-2}{l}}\,h^{[l]}\Delta^{[l]},$$ $$P_{A,B,j}=\binom{A+B+k-2j+j-1}{j}^{-1}h^{[j]}H_{A-j,B-j}\Delta^{[j]}.$$ Let $$\mathcal L_R=\left\{\sum_{\alpha,\beta}c_{\alpha,\beta}x^\alpha y^\beta: \alpha!\,c_{\alpha,\beta}\in R\text{ for all }\alpha,\beta\right\}.$$ For $g\in\operatorname{GL}_k(K)$, let $T_g$ substitute $x\mapsto gx$ and $y\mapsto(g^{-1})^ty$, and put $\mathcal L_g=T_g(\mathcal L_R)$. Write $e=\lfloor\log_p(A+B+k)\rfloor$. Every polynomial $f\in\mathcal L_g$ homogeneous of degree $A$ in $x$ and $B$ in $y$ satisfies $$p^eH_{A,B}f\in\mathcal L_g,\qquad p^{2e}P_{A,B,j}f\in\mathcal L_g\quad(0\le j\le\min(A,B)).$$
