---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/Intersections/Assembly.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.Inter.RankFracDegree.full",
    "GroundTheory.Heights₂.Heights.Inter.SemiPosTwist.full",
    "GroundTheory.Heights₂.Heights.Inter.regularityDehomogenization_holds.full"
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

## Module rank equals a field degree

[Theorem ALG.0216](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.Inter.RankFracDegree.full/)

Let $F\subseteq\Omega$ be fields, and let $A\to B$ be a finite homomorphism of commutative rings. Suppose there are injective ring maps $f:A\to\Omega$ and $g:B\to\Omega$ with $g|_A=f$. Let $L_0,L$ be intermediate fields of $\Omega/F$ such that $f(A)\subseteq L_0$, $g(B)\subseteq L$, and $$L_0\subseteq\langle f(A)\rangle_{\mathrm{field}},\qquad L\subseteq\langle g(B)\rangle_{\mathrm{field}},$$ where the brackets mean the smallest subfield of $\Omega$ containing the indicated set. Then $$\operatorname{finrank}_A B=[L:L_0\cap L].$$

## Divisor multiplicity after dehomogenization

[Theorem AG.0241](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.Inter.regularityDehomogenization_holds.full/)

Let $B$ be a finite set and $I_b$ finite sets of coordinates. Set $A=\mathbb Z[X_{b,i}:b\in B,\ i\in I_b]$, with each variable in block $b$ given degree $e_b\in\mathbb N^B$. Let $P\subset A$ be a relevant multihomogeneous prime ideal. Let $s,t\in A$ be multihomogeneous of the same multidegree, with $s\notin P$. Let $W$ be a relevant minimal prime of $P+(s)$, and assume $t\notin W$. If $y\in\operatorname{Frac}(A/P)$ satisfies $y[t]=[s]$, then $y$ belongs to the subring $R_{P,W}$ defined below, and $$\ell^{\mathrm{nat}}_{A_W}\bigl((A/(P+(s)))_W\bigr)=\ell^{\mathrm{nat}}_{R_{P,W}}\bigl(R_{P,W}/(y)\bigr).$$

## Making a smooth multihomogeneous metric semipositive

[Theorem ARAK.1444](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.Inter.SemiPosTwist.full/)

Let $K$ and $I_k$ be finite sets, and put $$U=\{z\in\mathbb C^{\coprod_{k\in K}I_k}:z_k\ne0\text{ for every }k\}.$$ Let $a\in\mathbb Z^K$ and let $h:\mathbb C^{\coprod_k I_k}\to\mathbb R$ be smooth and positive on $U$, with $$h((c_kz_{ki})_{k,i})=\prod_k|c_k|^{a_k}h(z)\qquad(c_k\ne0).$$ There exist $b\in\mathbb Z^K$ and a function $t$ on the same space, smooth and positive on $U$, satisfying the corresponding homogeneity law of degree $b$, such that for every $z\in U$ and every vector $v$, $$\left.\Delta_{s\in\mathbb C}\log t(z+sv)\right|_{s=0}\ge0,\qquad \left.\Delta_{s\in\mathbb C}\log(h(z+sv)t(z+sv))\right|_{s=0}\ge0.$$ The homogeneity laws are required also when $z$ lies outside $U$, with the same homogeneity equations.
