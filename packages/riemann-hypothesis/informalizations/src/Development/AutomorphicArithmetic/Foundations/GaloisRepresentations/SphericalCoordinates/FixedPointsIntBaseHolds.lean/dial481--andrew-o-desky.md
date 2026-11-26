---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/SphericalCoordinates/FixedPointsIntBaseHolds.lean",
  "declarations": [
    "UpperTheory.Gal.W2.FixFinite_holds",
    "UpperTheory.Gal.W2.Rigid_holds"
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

## Rigidity of a marked polarized period lattice

[Theorem AV.1288](https://andrewodesky.com/rh/lean/UpperTheory.Gal.W2.Rigid_holds/)

Let $O$ be a ring with a map $a\mapsto\bar a$. Let $\Lambda$ be an $O$-module that is finite free over $\mathbb Z$, with a nondegenerate alternating integral bilinear form $E$ satisfying $E(ax,y)=E(x,\bar a y)$. Fix $g\ge0$, a ring homomorphism $\rho:O\to M_g(\mathbb C)$, and an additive injective map $P:\Lambda\to\mathbb C^g$ whose image is discrete and spans $\mathbb C^g$ over $\mathbb R$. Suppose that $$P(ax)=\rho(a)P(x),\qquad E(x,y)=\Im H(Px,Py)$$ for a positive-definite Hermitian form $H$. Let $N\ge3$, let $T$ be any set, and let $t:T\to\Lambda$ meet every class modulo $N\Lambda$. If an $O$-linear automorphism $w$ preserves $E$, satisfies $$w(t(a))-t(a)\in N\Lambda\qquad(a\in T),$$ and admits a complex-linear automorphism $h$ of $\mathbb C^g$ with $P(wx)=h(Px)$ for every $x$, then $w=1$.

## Finitely many transverse coincidence points

[Theorem AG.1420](https://andrewodesky.com/rh/lean/UpperTheory.Gal.W2.FixFinite_holds/)

Let $Y,Z$ be schemes over $\mathbb C$, with $Z\to\operatorname{Spec}\mathbb C$ separated and $Y\to\operatorname{Spec}\mathbb C$ quasi-compact and locally of finite type. Let $c_1,c_2:Y\to Z$ be morphisms over $\mathbb C$, and fix $d\ge0$. Suppose every complex point $y$ with $c_1(y)=c_2(y)=z$ has affine neighborhoods $V$ of $y$ and $U$ of $z$, with $c_1(V),c_2(V)\subset U$, and regular functions $t_1,\ldots,t_d$ on $U$ such that $$d(c_1^*t_1),\ldots,d(c_1^*t_d)$$ form a basis of the cotangent space $\Omega_{Y/\mathbb C}\otimes\mathbb C(y)$. Write $$d(c_2^*t_j)=\sum_{\ell=1}^dA_{j\ell}\,d(c_1^*t_\ell)$$ in this cotangent space, and assume $\det(I_d-A)\ne0$. Then $$\{y\in Y(\mathbb C):c_1(y)=c_2(y)\}$$ is finite.
