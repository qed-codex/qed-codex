---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/StatementsSupBoundCount.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.HilbertSamuel.SupBoundCount.Statement"
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

## Small sections from comparison of norms

[Theorem ARAK.1121](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.HilbertSamuel.SupBoundCount.full/)

Fix finite coordinate blocks $I_k$ indexed by a finite set $B$, a characteristic-zero field $\Omega$, and a tuple $y=(y_{k,i})$ in $\Omega$. Let $R=\mathbb Z[X_{k,i}]$ and let $P$ be the kernel of $R\to\Omega[T_k:k\in B]$, $X_{k,i}\mapsto y_{k,i}T_k$. Fix $D\ge1$ and a distinguished block $k_0$. Assume the following section data:

1. $P$ is a relevant multihomogeneous horizontal prime defining an integral arithmetic variety of dimension $D+1$; horizontal means $P\cap\mathbb Z=0$, and relevant means no entire block of coordinates lies in $P$.
2. For all integral multihomogeneous polynomials $g,h$ of the same multidegree with $h(y)\ne0$, there are $n'\ge0$ and integral polynomials $g',h'$ homogeneous of degree $n'$ in block $k_0$ and degree zero in every other block, such that $h'(y)\ne0$ and $g(y)h'(y)=g'(y)h(y)$.
3. A smooth Hermitian metric represented on the nonzero coordinate blocks by a positive homogeneous function $h(z)$, with multidegree one in block $k_0$ and zero in the others, invariant under conjugation.
4. An ideal $P_0\subset P$ such that the Levi form of $\log h$ is nonnegative at every complex point of $P$ on every cone-tangent vector to $P_0$.
5. A multihomogeneous exceptional ideal $J\not\subset P$ and a compact Hausdorff complex manifold $M$ of dimension $D$ with a finite holomorphic atlas. There are local holomorphic lifts $z(x)$ to the nonzero coordinate blocks of $P$, agreeing up to block scalars on overlaps. Every point outside $J$ is represented, its preimage is unique, and the inverse image of $J$ has measure zero in every chart.
6. The Borel measurable structure on $M$ and a probability measure $dV$ having positive smooth density in every chart.

For $n\ge0$, let $M_n\subset\Omega$ be the $\mathbb Z$-span of evaluations at $y$ of integral polynomials of multidegree $n$ in block $k_0$ and zero elsewhere, and put $r=\operatorname{rank}_{\mathbb Z}M_n$. For such a polynomial $f$, set $$\|f\|_2^2=\frac12\int_M\left(\frac{|f(z(x))|}{h(z(x))^n}\right)^2dV+\frac12\int_M\left(\frac{|f(\overline{z(x)})|}{h(\overline{z(x)})^n}\right)^2dV.$$ Let $G_n$ be the real Gram matrix obtained from the corresponding symmetrized pairing in the chosen integral section basis, and put $\chi_n=-\tfrac12\log\det G_n$; put $\chi_n=0$ if no such polynomial basis exists. Let $\mathcal B_n$ consist of those $s\in M_n$ such that, for every pair of integral multihomogeneous polynomials $g,v$ with $\deg g-\deg v=n\mathbf e_{k_0}$ and $g(y)=s\,v(y)$, and every complex point $z$ of $P$ with all coordinate blocks nonzero, $$|g(z)|\le |v(z)|h(z)^n.$$

If $c>0$ and $$|f(z)|/h(z)^n\le c\|f\|_2$$ for every integral polynomial $f$ of the indicated degree and every complex point $z$ of $P$, then $$r\le2c^2,\qquad\chi_n-r\log(c\sqrt r)\le\log\operatorname{card}_0\mathcal B_n.$$ Here $\operatorname{card}_0$ is the usual cardinality for finite sets and zero for infinite sets; $\log0=0$, and the product with $r$ is zero at $r=0$.
