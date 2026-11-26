---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/LatticeDegreeGeHeightPolynomialVectorsDetStatement.lean",
  "declarations": [
    "GlobalTheory.T.lattice_degree_ge_height_polynomialVectors_det"
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

## A lower bound for lattice degree from a polynomial determinant

[Theorem ARAK.0525](https://andrewodesky.com/rh/lean/GlobalTheory.T.lattice_degree_ge_height_polynomialVectors_det/)

Let $F$ be a number field, $V$ a $d$-dimensional $F$-space with positive definite Hermitian forms $h_\sigma$ at every embedding $\sigma:F\hookrightarrow\mathbb C$, and $M\subset V$ a finitely generated full $\mathcal O_F$-lattice. Choose an $F$-basis $b_1,\ldots,b_d$. Let $B,n\ge0$, $N>0$, $w\in M_{N,n}(F)$ have columns spanning $F^N$, and $A_\sigma\in\operatorname{GL}_N(\mathbb C)$. Suppose $\Lambda\ge1$ and $$\|A_\sigma^{-1}\sigma(w_{\cdot j})\|_2\le\Lambda\qquad(\sigma,j).$$ Let $P=(P_{ik})$ be a $d\times d$ matrix of polynomials in $B$ blocks of $N$ variables. Suppose $G=\det P\ne0$ is homogeneous of some specified degree $a_j\ge0$ in each block. Let $C_k>0$. Assume that, after substituting $u_j=wX_j$ in each block, every coefficient of the vector polynomial $\sum_iP_{ik}(u)b_i$ belongs to $M$. Suppose also that $$\left\|\sum_i\sigma(P_{ik})(u)b_i\right\|_{h_\sigma}\le C_k$$ for every $k,\sigma$ and every tuple $u$ with $\|A_\sigma^{-1}u_j\|_2=1$ for every block $j$. Then $$H_{w,A}(G)-\sum_{k=1}^d\log C_k\le\widehat{\deg}(M).$$
