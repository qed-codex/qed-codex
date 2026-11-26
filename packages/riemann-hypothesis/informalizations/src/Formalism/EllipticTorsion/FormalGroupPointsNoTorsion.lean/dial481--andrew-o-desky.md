---
{
  "module": "src/Formalism/EllipticTorsion/FormalGroupPointsNoTorsion.lean",
  "declarations": [
    "Formalism.ELL.formal_group_points_subgroup",
    "Formalism.ELL.torsionIntegral"
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

## Points with nonintegral x-coordinate are closed under the group law

[Theorem PHT.0798](https://andrewodesky.com/rh/lean/Formalism.ELL.formal_group_points_subgroup/)

Let $K$ be an ultrametric normed field and let $W/K$ be a Weierstrass curve whose five coefficients have absolute value at most one and whose discriminant satisfies $|\Delta_W|=1$. On the group of nonsingular affine points together with the point at infinity, put $$U=\{O\}\cup\{(x,y):|x|>1\}.$$ For all $P,Q\in U$, both $P+Q$ and $-P$ belong to $U$.

## Integral coordinates of torsion of unit order

[Theorem AV.0662](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.E.torsionIntegral/)

Let $K$ be an ultrametric normed field and let $$E:\quad y^2+a_1xy+a_3y=x^3+a_2x^2+a_4x+a_6$$ be a Weierstrass curve over $K$ with $|a_i|\le1$ for $i=1,2,3,4,6$ and $|\Delta(E)|=1$. If $N\in\mathbb N$ satisfies $|N|=1$ and a nonidentity point $P=(x,y)$ in the group of nonsingular points of $E$ satisfies $NP=0$, then $$|x|\le1,\qquad |y|\le1.$$
