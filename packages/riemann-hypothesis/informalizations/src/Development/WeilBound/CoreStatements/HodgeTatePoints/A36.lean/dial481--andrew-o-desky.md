---
{
  "module": "src/Development/WeilBound/CoreStatements/HodgeTatePoints/A36.lean",
  "declarations": [
    "PositivityTheory.HtPt.Ktw.a32",
    "PositivityTheory.HtPt.Ktw.a36",
    "PositivityTheory.HtPt.Ktw.a37",
    "PositivityTheory.HtPt.Ktw.a39"
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

## A bivariate polynomial for sections of a very ample bundle

[Theorem AG.0080](https://andrewodesky.com/rh/lean/PositivityTheory.HtPt.Ktw.a36/)

Let $k\subseteq\Omega$ be fields, let $x=(x_0,\ldots,x_N)\in\Omega^{N+1}$, and let $P$ be its homogeneous ideal of relations. Suppose $P$ is a relevant homogeneous prime and $\dim k[X_0,\ldots,X_N]/P=e+1$ for an integer $e\ge0$. On $X=\operatorname{Proj}(k[X_0,\ldots,X_N]/P)$, let $L$ be a line bundle represented by invertible rank-one modules in $\Omega$ on the coordinate charts, with their compatible restrictions. Assume $L$ is very ample, in the chart sense described below, and write $H=\mathcal O_X(1)$.

Every space $H^0(X,L^{\otimes a}\otimes H^{\otimes c})$ is finite-dimensional for $a\ge0$ and $c\in\mathbb Z$. There exist $Q\in\mathbb Q[A,C]$ of total degree at most $e$ and $c_0\in\mathbb Z$ such that $$h^0(X,L^{\otimes a}\otimes H^{\otimes c})=Q(a,c)\qquad(a\ge0,\ c\ge c_0),$$ and $$h^0(X,L^{\otimes a})=Q(a,0)\qquad\text{for all sufficiently large integers }a.$$

## A lower bound for sections of a very ample line bundle

[Theorem AG.0097](https://andrewodesky.com/rh/lean/PositivityTheory.HtPt.Ktw.a39/)

Let $k\subseteq\Omega$ be fields, $N,d\ge0$, and $x=(x_0,\ldots,x_N)\in\Omega^{N+1}$. Put $P=\ker(k[X_0,\ldots,X_N]\to\Omega[T],\ X_i\mapsto x_iT)$, and assume that $P$ is relevant, meaning that some $X_i\notin P$, and $$\dim(k[X]/P)=d+2.$$ Let $L$ be a line bundle in the coordinate-chart line-bundle system of ([The Hilbert polynomial of a very ample line bundle](https://andrewodesky.com/rh/lean/PositivityTheory.HtPt.Ktw.a37/)), and assume that it is very ample in that system. Put $I=L^{d+1}$ for its $(d+1)$-fold intersection number on $P$, using the intersection normalization of ([The Hilbert polynomial of a very ample line bundle](https://andrewodesky.com/rh/lean/PositivityTheory.HtPt.Ktw.a37/)). There is a real constant $C$ such that for every sufficiently large integer $n$, $$\dim_k H^0(L^{\otimes n})\ge\frac{I}{(d+1)!}\,n^{d+1}-Cn^d.$$ Here $H^0$ is the module of sections satisfying the system's chartwise lattice conditions.

## Polynomiality of Euler characteristics under line-bundle twists

[Theorem AG.0533](https://andrewodesky.com/rh/lean/PositivityTheory.HtPt.Ktw.a32/)

Let $k$ be a field and $X\subseteq\mathbb P_k^N$ an integral projective variety of dimension $e$. Let $\mathcal F$ be a coherent torsion-free sheaf in the chart realization below, and let $L_1,\ldots,L_t$ be line bundles in the same realization. There is a polynomial $Q\in\mathbb Q[T_1,\ldots,T_t,C]$ of total degree at most $e$ such that, for every $n_1,\ldots,n_t\ge0$ and every $c\in\mathbb Z$, $$\chi\!\left(X,\mathcal F\otimes\bigotimes_{i=1}^t L_i^{\otimes n_i}\otimes\mathcal O_X(c)\right)=Q(n_1,\ldots,n_t,c).$$

## The Hilbert polynomial of a very ample line bundle

[Theorem AG.0780](https://andrewodesky.com/rh/lean/PositivityTheory.HtPt.Ktw.a37/)

Let $k\subseteq\Omega$ be fields, let $x=(x_0,\ldots,x_N)\in\Omega^{N+1}$, and let $\mathfrak p$ be the kernel of the map $$k[T_0,\ldots,T_N]\longrightarrow\Omega[T],\qquad T_i\longmapsto x_iT.$$ Suppose $\mathfrak p$ is homogeneous, at least one $T_i$ lies outside $\mathfrak p$, and $$\dim\bigl(k[T_0,\ldots,T_N]/\mathfrak p\bigr)=e+1.$$ Put $X=\operatorname{Proj}(k[T_0,\ldots,T_N]/\mathfrak p)$. Let $L$ be a very ample line bundle on $X$ in the invertible-submodule realization described below. Then $H^0(X,L^{\otimes n})$ is finite-dimensional over $k$ for every $n\ge0$. There is $P\in\mathbb Q[T]$ such that $$\deg P\le e,\qquad e![T^e]P=\int_Xc_1(L)^e,$$ $$\dim_kH^0(X,L^{\otimes n})=P(n)\qquad\text{for all sufficiently large }n.$$
