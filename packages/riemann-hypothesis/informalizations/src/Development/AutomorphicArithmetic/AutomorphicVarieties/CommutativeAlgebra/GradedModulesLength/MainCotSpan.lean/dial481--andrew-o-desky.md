---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/GradedModulesLength/MainCotSpan.lean",
  "declarations": [
    "UpperTheory.V.Alg.M.main_holds"
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

## Cotangent length bounded by valuations at graded orbits

[Theorem ALG.0060](https://andrewodesky.com/rh/lean/UpperTheory.V.Alg.M.main_holds/)

Let $O$ be a complete discrete valuation domain of characteristic zero, $K$ an algebraically closed field containing $O$, and $v:K^\times\to\mathbb R$ an additive nonarchimedean valuation with $v(c)=\operatorname{ord}_O(c)$ for $c\in O\setminus\{0\}$. Let $A=\bigoplus_{j\in\mathbb Z}A_j$ be a graded commutative $O$-algebra and $x:A\to O$ an $O$-algebra map. Assume $A_0$ is a complete Noetherian local $O$-algebra, its structure map is local and surjective on residue fields, $A$ is generated over $A_0$ by finitely many elements of degrees $-2,-1,1,2$, and $x(A_j)=0$ for $j\ne0$.

Put $\mathfrak m=\ker x$, let $Q$ be the $O$-saturation of $\mathfrak m^2$ in $A$, and let $C_j$ be the image of $A_j\cap\mathfrak m$ in $A/Q$. Choose $r\ge1$, $s,r',s',m\ge0$ and homogeneous lists $$F_0,\ldots,F_r\in A_{-1},\quad G_1,\ldots,G_s\in A_{-2},\quad E_1,\ldots,E_{r'}\in A_1,\quad E'_1,\ldots,E'_{s'}\in A_2,\quad Z_1,\ldots,Z_m\in A_0\cap\mathfrak m.$$ Assume the images of $F,G,Z$ span $C_{-1},C_{-2},C_0$, respectively, after multiplication of each element by some nonzero scalar in $O$. Assume there is a graded map $\phi:A\to\operatorname{Frac}(O)[[T_1,\ldots,T_q]]$ with constant term $x$, whose coordinate weights have multiplicities $r,s,r'+1,s'+1,m$ in degrees $-1,-2,1,2,0$, such that every variable is isolated by the nonzero linear term of some $f\in A$, and any $f\in\mathfrak m$ with zero linear term belongs to $Q$.

Let $I=(F,G,E,E',Z)$. Call a $K$-point $\xi:A\to K$ mixed if it is nonzero on some negative-degree element and on some positive-degree element. Assume:

1. The image of $A_0$ in $A/I$ is finitely generated over $O$.
2. For every $K$-point $\xi_0$ annihilating $I$ and every nonzero degree, with $\xi_0\ne x_K$, at least one of the following two sorts of points is absent among points annihilating $I$ and agreeing with $\xi_0$ on $A_0$: points vanishing on all negative degrees but not all positive degrees; points vanishing on all positive degrees but not all negative degrees.
3. At every mixed $K$-point annihilating $I$, any two $O$-linear derivations at that point that annihilate $I$ are linearly dependent over $K$.
4. There is $a\in A_0$ with $x(a)=0$ and $\xi(a)\ne0$ for every mixed $K$-point annihilating $I$.

Let $K^\times$ act on points by scaling the evaluation of a degree-$j$ element by $t^j$. There is a finite set $T$ of mixed $K$-points annihilating $I$ meeting every such orbit. Moreover, $C_{-1}/\langle F_0,\ldots,F_r\rangle_O$ has finite $O$-length $\ell$, and every such finite set $T$ satisfies $$\ell\le2\sum_{\xi\in T}v(\xi(a)).$$
