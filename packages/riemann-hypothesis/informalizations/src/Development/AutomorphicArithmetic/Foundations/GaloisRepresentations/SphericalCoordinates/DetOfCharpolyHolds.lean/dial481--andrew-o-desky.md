---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/SphericalCoordinates/DetOfCharpolyHolds.lean",
  "declarations": [
    "UpperTheory.Gal.W2.LocSum_holds",
    "UpperTheory.Gal.W2.NewtonPoly_holds",
    "UpperTheory.Gal.W2.TanChart_holds",
    "UpperTheory.Gal.W2.TorusCount_holds",
    "UpperTheory.Gal.W2.TraceDual_holds",
    "UpperTheory.Gal.W2.TraceLat_holds"
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

## The trace of an endomorphism preserving a complex lattice

[Theorem ALG.0387](https://andrewodesky.com/rh/lean/UpperTheory.Gal.W2.TraceLat_holds/)

Let $L$ be a finite free abelian group and let $P:L\to\mathbb C^g$ be an injective additive map whose image is discrete and spans $\mathbb C^g$ over $\mathbb R$. Let $f:L\to L$ be $\mathbb Z$-linear and $H\in\operatorname{Mat}_g(\mathbb C)$. If $P(fx)=HP(x)$ for every $x\in L$, then $$\operatorname{tr}_{\mathbb Z}(f)=\operatorname{tr}(H)+\overline{\operatorname{tr}(H)}$$ as an equality in $\mathbb C$.

## A tangent characteristic polynomial from a holomorphic parametrization

[Theorem AG.0414](https://andrewodesky.com/rh/lean/UpperTheory.Gal.W2.TanChart_holds/)

Let $V$ be a $d$-dimensional complex normed vector space, $B\subset V$ open, and $v_0\in B$. Let $Y,Z$ be schemes over $\mathbb C$, $c_1,c_2:Y\to Z$ morphisms over $\mathbb C$, and $s:B\to Y(\mathbb C)$ holomorphic. Suppose the only $w\in V$ such that $$D(f\circ s)(v_0)w=0$$ for every regular function $f$ defined near $s(v_0)$ is $w=0$. Let $G:V\to V$ be differentiable at $v_0$, with derivative $G'$, and assume $$G(v_0)=v_0,\qquad c_2(s(v))=c_1(s(G(v)))$$ for all $v$ sufficiently close to $v_0$. Put $y=s(v_0)$. If $A\in\operatorname{Mat}_d(\mathbb C)$ describes the cotangent comparison of $c_2$ with $c_1$ at $y$ in the sense below, then $$\det(T-A)=\det(T-G').$$

## Descent of complex coordinates with integral trace pairings

[Theorem ANT.0443](https://andrewodesky.com/rh/lean/UpperTheory.Gal.W2.TraceDual_holds/)

Let $F$ be a number field and choose $s_\tau\in\mathbb C$ for each embedding $\tau:F\hookrightarrow\mathbb C$. Suppose $$\sum_{\tau:F\hookrightarrow\mathbb C}\tau(c)s_\tau\in\mathbb Z\qquad(c\in\mathcal O_F).$$ There is $b\in F$ such that $s_\tau=\tau(b)$ for every $\tau$.

## A polynomial over a number field from its complex power sums

[Theorem ALG.0448](https://andrewodesky.com/rh/lean/UpperTheory.Gal.W2.NewtonPoly_holds/)

Let $F$ be a number field, $n\ge0$, and for every embedding $\tau:F\hookrightarrow\mathbb C$ let $M_\tau$ be a multiset of $n$ complex numbers. Suppose that for every integer $j\ge0$ there is $b_j\in F$ with $$\sum_{z\in M_\tau}z^j=\tau(b_j)\qquad\text{for every }\tau.$$ There is a monic polynomial $P\in F[X]$ of degree $n$ such that $$\tau(P)=\prod_{z\in M_\tau}(X-z)\qquad\text{for every }\tau.$$ All sums and products count multiplicities.

## Fixed points of a linear endomorphism of a complex torus

[Theorem AV.1130](https://andrewodesky.com/rh/lean/UpperTheory.Gal.W2.TorusCount_holds/)

Let $W$ be a finite-dimensional complex normed vector space and let $\Lambda\subset W$ be a discrete additive subgroup spanning $W$ over $\mathbb R$. Let $\Theta:W\to W$ be complex linear, preserve $\Lambda$, and satisfy $\det_{\mathbb C}(1-\Theta)\ne0$. There is a finite set $F\subset W$ with $\Theta z-z\in\Lambda$ for $z\in F$, such that every $z$ with $\Theta z-z\in\Lambda$ is congruent modulo $\Lambda$ to a unique member of $F$. Its cardinality satisfies $$|F|=\det_{\mathbb C}(1-\Theta)\,\overline{\det_{\mathbb C}(1-\Theta)}.$$

## A determinant formula for a finite fixed-point sum

[Theorem AG.1263](https://andrewodesky.com/rh/lean/UpperTheory.Gal.W2.LocSum_holds/)

Let $O$ be a ring with a map $a\mapsto\overline a$, let $g,d,k\ge0$, and let $\rho:O\to M_g(\mathbb C)$ be a ring homomorphism. Fix a polarized $O$-lattice $D$: a finite free $\mathbb Z$-module with $O$-action and a nondegenerate alternating integral form satisfying $E(ax,y)=E(x,\overline a y)$. Let $X$ be smooth of relative dimension $d$ over $\mathbb C$, $A$ a group scheme over $X$, and choose the source's full period-sheet package $S$ for $A,D,\rho$. For a period map $P$, write $u(P)\in X(\mathbb C)$ for its base point and $s_P(z)\in A^k(\mathbb C)$ for the point given by the exponential maps on a $k$-tuple $z\in(\mathbb C^g)^k$.

Choose morphisms $c_1,c_2:A^k\to Z$ over $\mathbb C$, a period map $P_0:D\to\mathbb C^g$, and a positive-definite Hermitian matrix $M_0$ with $\operatorname{Im}h_{M_0}(P_0x,P_0y)=E(x,y)$. Choose a complex-linear isomorphism from $\mathbb C^d$ onto $$\{C\in M_g(\mathbb C):C^tM_0\text{ is symmetric and }(C^tM_0)\overline{\rho(\overline a)}=\rho(a)^*(C^tM_0)\text{ for every }a\in O\},$$ and denote it by $c$. Let $\gamma:D\to D$ be $O$-linear with $E(\gamma x,\gamma y)=mE(x,y)$ for some integer $m>0$, and let $H\in M_g(\mathbb C)$ satisfy $P_0\gamma=HP_0$. Let $T\in\operatorname{End}_{\mathbb C}(\mathbb C^d)$ satisfy $c(Tb)=Hc(b)\overline H^{-1}$. Choose a complex-linear map $L$ on $(\mathbb C^g)^k$ such that $$c_2(s_P(z))=c_1(s_{P'}(Lz))\quad\text{whenever }P'\gamma=P.$$ Put $Bz=(H(Lz)_j)_{j=1}^k$. Assume $B(P_0(D)^k)\subseteq P_0(D)^k$, $c_1$ is injective on the fibre parametrized by $s_{P_0}$, and $\det(1-T)\det(1-B)\ne0$.

Then the set $F$ of points $y\in A^k(\mathbb C)$ over $u(P_0)$ with $c_1(y)=c_2(y)$ is finite. For every choice of normalized cotangent comparison matrices $A_y\in M_{d+kg}(\mathbb C)$ for $c_1,c_2$ at the points of $F$, one has $\det(1-A_y)\ne0$ and, for every $t\in\mathbb C$, $$\sum_{y\in F}\frac{\det(1-tA_y)}{\det(1-A_y)}=\frac{\det(1-tT)}{\det(1-T)}\det(1-tB)\,\overline{\det(1-B)}.$$
