---
{
  "module": "src/CompanionTheory/RealGroups/DiscreteSeries/DiscreteSeriesClassification/DiscreteSeriesExhaustion/MatrixCoefficientDecay/LineFormulas/LineFinal.lean",
  "declarations": [
    "CompanionTheory.RgExh.Dec.N.S.line_formula"
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

## Integration along a parabolic one-parameter subgroup

[Theorem REP.1508](https://andrewodesky.com/rh/lean/CompanionTheory.RgExh.Dec.N.S.line_formula/)

Let $n\ge0$, $J=\operatorname{diag}(\epsilon_1,\ldots,\epsilon_n)$ with $\epsilon_i\in\{\pm1\}$, and $G=U(J)$ with reference Haar measure $\mu$. Let $A\in M_n(\mathbb C)$ satisfy $$A^*J+JA=0,\qquad A^*=A,\qquad A^3=A,\qquad A\ne0.$$ Put $V_-=\operatorname{im}((A^2-A)/2)$, $W_-=\ker((A^2+A)/2)$, and let $P\subset G$ be the subgroup preserving both subspaces. Set $$a_t=\exp(tA),\qquad j=\operatorname{Re}\operatorname{tr}((A^2+A)/2),\qquad \rho_A=j(n-j).$$ Let $\nu$ be a Haar measure on $P$ and $\tau:G\to\mathbb R$ continuous. Assume that $\tau(y)=\tau(x)+t$ whenever $x,y\in P$ and $y=xa_t$. Then there is $0<\kappa<\infty$ such that, for every nonnegative extended-real-valued function $F$ on $M_n(\mathbb C)$ whose restriction to $G$ is measurable and right-invariant under $K=G\cap U(n)$, $$\int_G F(g)\,d\mu(g)=\kappa\int_{\{x\in P:0\le\tau(x)<1\}}\int_{\mathbb R}F(xa_t)e^{2\rho_A t}\,dt\,d\nu(x).$$
