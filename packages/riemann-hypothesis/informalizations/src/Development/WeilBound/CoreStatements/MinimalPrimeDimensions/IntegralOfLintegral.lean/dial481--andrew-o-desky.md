---
{
  "module": "src/Development/WeilBound/CoreStatements/MinimalPrimeDimensions/IntegralOfLintegral.lean",
  "declarations": [
    "ChowFormHeightComparison₂.CF.stArch"
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

## A logarithmic Chern integral in projective coordinates

[Theorem ARAK.1377](https://andrewodesky.com/rh/lean/ChowFormHeightComparison%E2%82%82.CF.stArch/)

Assume the source's point-coordinate comparison and algebraic-chart assertions. Let $K$ be a number field and $p:Z\to\operatorname{Spec}\mathcal O_K$ an integral projective scheme, flat over $\mathbb Z$, of dimension $e+1$. Let $B$ be a line bundle with sections $s_1,\ldots,s_m$ satisfying the following projective-coordinate condition: their nonzero loci cover $Z$, are affine, and their section ratios generate each affine coordinate algebra.

Let $P\subset K[X_1,\ldots,X_m]$ be the homogeneous ideal of the generic section-coordinate point. Assume $P$ is a relevant homogeneous prime and has a Chow form with $e+1$ hyperplane blocks. Fix $\sigma:K\hookrightarrow\mathbb C$, a Hermitian norm $h$ on $\mathbb C^m$, and a smooth Hermitian weight $\phi$ on $B_\sigma$ which is Fubini–Study for these sections and the dual norm $h^*$. Let $u\in K^m$ with $\sum_i u_iX_i\notin P$, and put $$\ell(z)=\sum_i\sigma(u_i)z_i,\qquad f(z)=\log\frac{|\ell(z)|}{h^*(z)}.$$ Then $$\int_{Z_\sigma\setminus\{\ell=0\}}f(s(y))\,c_1(\phi)^e=\int_{[V(P_\sigma)]}f\,c_1(h^*)^e.$$ The right side is the projective fundamental-cycle integral defined in ([A Mahler integral after fixing one Chow-form block](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.Short.mahlerSection/)); both sides use the same Chern normalization. If $e=0$, the finite-support sum $\sum_y f(s(y))$ over all complex points of $Z_\sigma$ equals the same right side.
