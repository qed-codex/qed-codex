---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/AlgebraProofs/MahlerSectionStatementHolds.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.Ar.Short.mahlerSection"
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

## A Mahler integral after fixing one Chow-form block

[Theorem ARAK.0068](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.Short.mahlerSection/)

Let $n,e,\delta\ge0$, let $h\in\operatorname{GL}_n(\mathbb C)$, and put $\|x\|_h=\|hx\|_2$, $\|y\|_{h,*}=\|(h^t)^{-1}y\|_2$. Let $Z=\sum_W m_W[W]$ be a finite integral projective cycle in $\mathbb P^{n-1}_{\mathbb C}$, represented by homogeneous prime ideals. Let $f$ be its Chow form in $e+1$ blocks of $n$ variables, homogeneous of degree $\delta$ in each block. Choose $u\in\mathbb C^n$ such that the linear form $u\cdot y$ lies in none of the primes in the support of $Z$.

For a polynomial $F$ in $k$ blocks, define $M_{h,k}(F)$ as the average of $\log|F(x_1/\|x_1\|_h,\ldots,x_k/\|x_k\|_h)|$ over the product of the open $h$-unit balls, using normalized Lebesgue measure. Let $f_u$ denote $f$ with its first block fixed at $u$. For a scale-invariant real function $g$, define $$I_h(Z,g)=\sum_W m_W\frac{\displaystyle\int_{\substack{\|y\|_2<1\\h^ty\in C(W)}}g(h^ty)\,d\mathcal H^{2(e+1)}(y)}{\displaystyle\mathcal H^{2(e+1)}\{y:\|y\|_2<1,\ y_j=0\ (j>e+1)\}},$$ where $C(W)$ is the affine cone, $\mathcal H^d$ is $d$-dimensional Hausdorff measure, and division by zero is assigned zero. Then $$M_{h,e}(f_u)=M_{h,e+1}(f)+\frac{\delta}{2}\sum_{j=1}^{n-1}\frac1j+ I_h\!\left(Z,y\mapsto\log\frac{|u\cdot y|}{\|y\|_{h,*}}\right).$$
