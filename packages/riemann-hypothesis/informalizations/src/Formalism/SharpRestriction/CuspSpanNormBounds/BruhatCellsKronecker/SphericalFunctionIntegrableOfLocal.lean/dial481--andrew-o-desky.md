---
{
  "module": "src/Formalism/SharpRestriction/CuspSpanNormBounds/BruhatCellsKronecker/SphericalFunctionIntegrableOfLocal.lean",
  "declarations": [
    "Formalism.MainNotions.BridgeLemma.CData.count_of_steps"
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

## Multiplicity estimate from a cusp projection

[Theorem AGR.0136](https://andrewodesky.com/rh/s/multiplicity.html)

Use the arithmetic unitary-group datum, spaces, operators and functions in ([Cusp projection and multiplicity data](https://andrewodesky.com/rh/lean/Formalism.MainNotions.S.AutInst/)), with all $H_v,H_\infty$ complete. Fix real weights $\lambda_v\in\mathbb R^n$, real constants $c_1,A_1,c'$, and $n_1\in\mathbb N$. Put $$f=[F:\mathbb Q],\qquad \nu=\mu_A|_{\mathcal F},\qquad V_{\mathcal F}=\mu_A(\mathcal F),\qquad D=D_{\mathrm{mult}},\qquad D_*=(\prod_vd_v)V_{\mathcal F}\operatorname{Re}e(1),$$ where the volume in this formula is its finite real value under the assumption below. Define $$\kappa(g)=\phi(g_\infty)e(g_f),\qquad K(x)=\sum_{\gamma\in G(F)}\kappa(x^{-1}\gamma x),\qquad K_{\ne1}(x)=\sum_{\substack{\gamma\in G(F)\\\gamma\ne1}}\kappa(x^{-1}\gamma x).$$ Assume the following numerical implication: for every $N,m\in\mathbb N$ and $M,M_*,r,\eta_1,\eta_2\in\mathbb R$ satisfying $$N\ge n_1,\quad m\ge1,\quad M,M_*\ge0,\quad r\le1,\quad 1-e^{-c_1Nm\log N}\le r,$$ $$|\eta_1|\le A_1e^{-c_1Nm\log N}M_*,\qquad |\eta_2|\le A_1e^{-N^2m}M,\qquad M=M_*r+\eta_1+\eta_2,$$ one has $|M-M_*|\le e^{-c'Nm\log N}M_*$. Assume also:

1. $n\ge n_1$; each $\sigma_v$ satisfies the discrete-series conditions specified below at weight $\lambda_v$, and $\|w_v\|=1$.
2. $e$ is of positive type: for every finite list $x_i\in G_f$ and $a_i\in\mathbb C$, the number $\sum_{i,j}\overline{a_i}a_j e(x_i^{-1}x_j)$ is real and nonnegative.
3. Every bounded operator $T$ realizing convolution by $\kappa$ in the integrable weak sense defined in ([Cusp projection and multiplicity data](https://andrewodesky.com/rh/lean/Formalism.MainNotions.S.AutInst/)) is an orthogonal projection with finite-dimensional image and $\dim_{\mathbb C}\operatorname{im}T=D$. At least one such $T$ exists.
4. For every such convolution operator $T$ which is an orthogonal projection and every finite orthonormal basis $F_1,\ldots,F_s$ of its image, the series defining $K(x)$ is summable and $$K(x)=\sum_{j=1}^s|F_j(x)|^2\qquad\text{for }\nu\text{-almost every }x.$$
5. $\mu_A(\mathcal F)<\infty$. There is a measurable $\mathcal M\subseteq G$ for which $$\nu(\mathcal M)\ge(1-e^{-c_1nf\log n})V_{\mathcal F},$$ $$\left|\int_{\mathcal M}\operatorname{Re}K_{\ne1}(x)\,d\nu(x)\right|\le A_1e^{-c_1nf\log n}D_*,$$ $$\left|\int_{G\setminus\mathcal M}\operatorname{Re}K(x)\,d\nu(x)\right|\le A_1e^{-n^2f}D.$$ Then $$|D-D_*|\le e^{-c'nf\log n}D_*.$$
