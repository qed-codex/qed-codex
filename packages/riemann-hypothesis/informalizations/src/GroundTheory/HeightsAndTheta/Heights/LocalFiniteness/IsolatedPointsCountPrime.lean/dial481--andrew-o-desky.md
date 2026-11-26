---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/LocalFiniteness/IsolatedPointsCountPrime.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.AutoClose.SameOrdersLiftCentre"
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

## Equal branch orders determine a centre in the normalization

[Theorem AG.0270](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.AutoClose.SameOrdersLiftCentre/)

Let $J\subseteq\mathbb C[x_1,\ldots,x_n]$ be prime with $\dim\mathbb C[x]/J=1$, and let $q\in V(J)$. Let $Y\subseteq\mathbb C^{n+m}$ be an irreducible normal affine variety such that projection to the first $n$ coordinates is finite and birational onto $V(J)$, and the induced inclusion of coordinate rings has kernel $J$.

Let $\gamma:D_r\to V(J)$ and $\gamma':D_{r'}\to V(J)$ be injective holomorphic maps from discs of positive radii about $0$, with $\gamma(0)=\gamma'(0)=q$. Suppose they have holomorphic lifts $\Gamma:D_r\to Y$ and $\Gamma':D_{r'}\to Y$. If $$\operatorname{ord}_0(f\circ\gamma)=\operatorname{ord}_0(f\circ\gamma')\qquad(f\in\mathbb C[x_1,\ldots,x_n]),$$ then $\Gamma(0)=\Gamma'(0)$. The order of an identically zero germ is $\infty$.
