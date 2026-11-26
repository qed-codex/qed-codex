---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/LocalFiniteness/InjectiveHolomorphicJacobianNeZeroHolds.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.AutoClose.NormalCurveJacobian"
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

## Independent local equations for a normal affine curve

[Theorem AG.0393](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.AutoClose.NormalCurveJacobian/)

Let $I\subseteq\mathbb C[x_1,\ldots,x_N]$ be prime, with integrally closed quotient of Krull dimension one. Let $w\in\mathbb C^N$ vanish on $I$. There are $k\ge0$, polynomials $f_1,\ldots,f_k\in I$, and $D\in\mathbb C[x_1,\ldots,x_N]$ such that $$k+1=N,\qquad D(w)\ne0,$$ the vectors $\bigl(\partial f_j/\partial x_i(w)\bigr)_{i=1}^N$, $1\le j\le k$, are linearly independent over $\mathbb C$, and $$Dp\in(f_1,\ldots,f_k)\qquad(p\in I).$$
