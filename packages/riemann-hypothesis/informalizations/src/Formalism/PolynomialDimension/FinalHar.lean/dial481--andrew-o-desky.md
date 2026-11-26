---
{
  "module": "src/Formalism/PolynomialDimension/FinalHar.lean",
  "declarations": [
    "Formalism.CountingSumsFrames.Top.gaussProj"
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

## A denominator bound for harmonic and level projections

[Theorem ALG.0808](https://andrewodesky.com/rh/lean/Formalism.CountingSumsFrames.Top.gaussProj/)

Let $K$ be a field of characteristic zero, $R\subseteq K$ a subring, $k\ge1$, $A,B\ge0$, and $p$ prime. Assume $n^{-1}\in R$ whenever $n\in\mathbb N$ and $p\nmid n$. Put $h=\sum_{i=1}^kx_iy_i$, $\Delta=\sum_i\partial_{x_i}\partial_{y_i}$, and define operators on $K[x_1,\ldots,x_k,y_1,\ldots,y_k]$ by $$H_{A,B}=\sum_{\ell=0}^{\min(A,B)}\frac{(-1)^\ell}{\binom{A+B+k-2}{\ell}}\frac{h^\ell}{\ell!}\frac{\Delta^\ell}{\ell!},$$ $$L_{A,B,j}=\binom{A+B+k-2j+j-1}{j}^{-1}\frac{h^j}{j!}\,H_{A-j,B-j}\,\frac{\Delta^j}{j!}.$$ Let $g\in\operatorname{GL}_k(K)$ act by $x_i\mapsto\sum_jg_{ij}x_j$ and $y_i\mapsto\sum_j(g^{-1})_{ji}y_j$. Let $\mathcal G_R$ be the polynomials with coefficients in $R$, and let $\mathcal D_R$ consist of polynomials $\sum a_{\alpha\beta}x^\alpha y^\beta$ with $\alpha!\beta!a_{\alpha\beta}\in R$ for all $\alpha,\beta$. Put $$e=(k+1)\lfloor\log_p(A+B+k)\rfloor.$$ For every polynomial $f$ homogeneous of bidegree $(A,B)$ and each $\mathcal M\in\{\mathcal G_R,\mathcal D_R\}$, $$f\in g\mathcal M\quad\Longrightarrow\quad p^eH_{A,B}f\in g\mathcal M\ \text{ and }\ p^eL_{A,B,j}f\in g\mathcal M\quad(0\le j\le\min(A,B)).$$
