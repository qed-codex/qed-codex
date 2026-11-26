---
{
  "module": "src/ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/SquareIntegrability/TiledBoundaries/ETSymmApply.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.G.I2.TiledBoundaries.stepD"
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

## A dimension bound for theta sections on a polarized torus

[Theorem THETA.0826](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.I2.TiledBoundaries.stepD/)

Let $E$ be a number field. Choose nonnegative integers $d_\tau$ for its complex embeddings and $r\ge0$ with $d_\tau+d_{\bar\tau}=r$. Put $$V=\bigoplus_{\tau:E\hookrightarrow\mathbb C}\mathbb C^{d_\tau},\qquad g=\dim_{\mathbb C}V,\qquad H(v,w)=\sum_{\tau,j}v_{\tau j}\overline{w_{\tau j}}.$$ Let $\Lambda\subset V$ be the integer span of a real basis, stable under $\alpha\cdot v=(\tau(\alpha)v_{\tau j})_{\tau,j}$ for every $\alpha\in\mathcal O_E$. Assume $\operatorname{Im}H$ is integral and perfect on $\Lambda$. Let $\epsilon:\Lambda\to\{\pm1\}$ satisfy $$\epsilon(x+y)=\epsilon(x)\epsilon(y)\cos\bigl(\pi\operatorname{Im}H(x,y)\bigr),$$ and $\epsilon(x)=1$ whenever $\operatorname{Im}H(\alpha x,x)=0$ for all $\alpha\in\mathcal O_E$. For integers $q\ge1,n\ge0$, let $\mathcal S_{q,n}$ be the vector space of entire $F:V^n\to\mathbb C$ such that for $\gamma\in\Lambda^n$, $$F(v+\gamma)=\left(\prod_{a=1}^n\epsilon(\gamma_a)\right)^q \exp\left(q\pi\sum_{a=1}^nH(v_a,\gamma_a)+\frac{q\pi}{2}\sum_{a=1}^nH(\gamma_a,\gamma_a)\right)F(v).$$ Then $\mathcal S_{q,n}$ is finite-dimensional and $$\dim_{\mathbb C}\mathcal S_{q,n}\le q^{gn}.$$
