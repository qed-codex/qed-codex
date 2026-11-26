---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/AssemblyBase.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.HilbertSamuel.GramChiDerivative.full",
    "GroundTheory.Heights₂.Heights.HilbertSamuel.RankOfSections.full",
    "GroundTheory.Heights₂.Heights.HilbertSamuel.SupBoundCount.full",
    "GroundTheory.Heights₂.Heights.HilbertSamuel.SupNormAgainstL2.full",
    "GroundTheory.Heights₂.Heights.HilbertSamuel.UniformBergmanBound.full"
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

## Derivative of a Gram determinant under metric variation

[Theorem ARAK.1468](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.HilbertSamuel.GramChiDerivative.full/)

Let $X$ be compact Hausdorff with its Borel measurable structure and a finite holomorphic atlas of complex dimension $D$. Let $L$ be a holomorphic line bundle given on this atlas, let $\phi_0,\phi_1$ be smooth real metric weights, and let $dV$ be a probability measure with smooth strictly positive densities in the charts. Put $\phi_t=\phi_0+t(\phi_1-\phi_0)$. Let $n\ge0$, let $V\subseteq H^0(X,L^{\otimes n})$ be finite-dimensional, and choose a basis $(e_a)$. In chart coordinates use $|s(x)|_t^2=|s_j(x)|^2e^{-n\phi_{t,j}(x)}$, and put $$G_{ab}(t)=\int_X e_{a,j}(x)\overline{e_{b,j}(x)}e^{-n\phi_{t,j}(x)}\,dV(x),$$ $$\chi(t)=-\tfrac12\log\operatorname{Re}\det G(t),\qquad B_t(x)=\sup_{s\in V}\frac{|s(x)|_t^2}{\int_X|s|_t^2\,dV},$$ with $0/0=0$. For every $t\in\mathbb R$, $$\chi'(t)=\frac n2\int_X(\phi_1-\phi_0)(x)B_t(x)\,dV(x).$$

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

## A uniform Bergman bound along an interval of metrics

[Theorem ARAK.1367](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.HilbertSamuel.UniformBergmanBound.full/)

Let $X$ be a compact Hausdorff space with its Borel measurable structure, equipped with a finite holomorphic atlas of complex dimension $D\ge0$. Let $L$ be a holomorphic line bundle on this atlas, $W_0,W_1$ two semipositive weights on $L$, and $dV$ a smooth positive probability volume measure. Put $W_t=(1-t)W_0+tW_1$ for $0\le t\le1$.

For a finite-dimensional complex subspace $V\subseteq H^0(X,L^{\otimes n})$, define its Bergman function by $$B_{n,t,V}(x)=\sup_{s\in V}\frac{|s(x)|_{nW_t}^2}{\displaystyle\int_X|s|_{nW_t}^2\,dV},$$ where division by zero is assigned zero. There is $C\in\mathbb R$ such that $$B_{n,t,V}(x)\le C n^D$$ for every integer $n\ge1$, every $t\in[0,1]$, every such $V$, and every $x\in X$.

## Comparison of supremum and L2 section norms

[Theorem AG.1410](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.HilbertSamuel.SupNormAgainstL2.full/)

Let $X$ be a compact Hausdorff space with its Borel measurable structure, a finite holomorphic atlas of complex dimension $D$, a holomorphic line bundle $L$, and a smooth semipositive Hermitian metric on $L$. Fix a probability measure $dV$ whose density in every holomorphic chart is smooth and strictly positive. For a holomorphic section $s$ of $L^{\otimes n}$ put $$\|s\|_2=\left(\int_X\|s(x)\|^2\,dV(x)\right)^{1/2}.$$ There is a real constant $C$ such that for every integer $n\ge1$, every such section, and every $x\in X$, $$\|s(x)\|\le Cn^{D/2}\|s\|_2.$$ Moreover, for every $n\ge0$ and every real $M$, a pointwise bound $\|s(x)\|\le M$ for all $x$ implies $\|s\|_2\le M$.

## A uniform remainder for the Hilbert function

[Theorem AG.1425](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.HilbertSamuel.RankOfSections.full/)

Let $I$ be a finite set, let $q\subset\mathbb Q[X_i:i\in I]$ be a homogeneous prime ideal not containing the irrelevant ideal, and let $D\ge0$. Assume $$\dim\bigl(\mathbb Q[X_i:i\in I]/q\bigr)=D+1.$$ Let $h_q(n)$ be the dimension over $\mathbb Q$ of its homogeneous degree-$n$ piece, and let $\delta$ be the intersection number of $D$ hyperplanes on its associated projective variety. There is $C\in\mathbb R$ such that for every integer $n\ge0$, $$\left|h_q(n)-\frac{\delta}{D!}n^D\right|\le C(n+1)^{D-1}.$$
