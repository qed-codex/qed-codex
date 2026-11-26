---
{
  "module": "src/Formalism/DivisorInequality/DivisorInequalityProofs/EvenDegreeWeightBounds.lean",
  "declarations": [
    "Formalism.DivisorInequality.UniformCovolumeTail.stepDiSharp",
    "Formalism.DivisorInequality.height_bound_at_set"
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

## Numerical height and target comparison

[Theorem ARAK.0176](https://andrewodesky.com/rh/lean/Formalism.L2.DIV.HtNums.le_hu/)

Use the numerical data, size conditions, weight conditions and notation of ([Numerical cancellation of slope and theta heights](https://andrewodesky.com/rh/lean/Formalism.L2.DIV.RecNums.divIneq/)), including $H$, $H_{X,j}$, $M$ and $\mathcal R$.

**Averaged height comparison.** Let $A$ be a nonempty finite set, let $K_{j,s}$ be real numbers for $j\in J$ and $s\in A$, and let $h_P,l\in\mathbb R$. Assume the hypotheses of ([Averaged logarithmic bound for theta kernels](https://andrewodesky.com/rh/lean/Formalism.DivisorInequality.UniformCovolumeTail.stepDiSharp/)), with the same $J,\Sigma,A,r,\nu,\lambda,f,m,N,L,\Lambda,\ell,C_h$ and with its kernel bounds $K_{j,s}$. Assume also the hypotheses of ([Terminal period height with a source-prime saving](https://andrewodesky.com/rh/s/q9-terminal-period-height.html)), with the same $\Sigma,T,a_\rho,a,\Lambda,L,m,f,k,N,S,\eta,b',\ell$, terminal height $h_P$, and bounding constant $C=C_h$. In these two estimates, identify the source-prime constants $C_7=C_T$; distinguish the terminal error constant by writing $C_{\rm ev}$ for its $C_e$.

If $\sum_{j\in J}H_{X,j}\le l$, then $$h_P+\sum_{j\in J}\frac1{|A|}\sum_{s\in A}K_{j,s}-l\le H.$$

**Target comparison.** Let $C_D,C_{\rm abs}\in\mathbb R$ satisfy $$C_D\ge0,\qquad C_D\ge50C_0+10,\qquad C_D\ge60c_e,\qquad C_{\rm abs}\ge1.$$ Then $$\mathcal R\le M+C_D|T|a\Lambda+C_Dm(B_0+N_c)x^{C_{\rm abs}\varepsilon}.$$

## Averaged logarithmic bound for theta kernels

[Theorem THETA.0180](https://andrewodesky.com/rh/lean/Formalism.DivisorInequality.UniformCovolumeTail.stepDiSharp/)

Let $J,\Sigma,A$ be finite sets with $A\ne\varnothing$, and let $r\ge0$ be an integer. Supply real arrays $\nu_{j,\rho,i}$, $g_j$, $K_{j,s}$, $Q_{j,s}$, $\lambda_{\rho,s}$, $\theta_s$, $u_j,u'_j$, for $j\in J$, $\rho\in\Sigma$, $s\in A$ and $1\le i\le r$. Write $\langle\cdot\rangle$ for the mean over $A$, put $n_{j,\rho}=\sum_i\nu_{j,\rho,i}$ and $\phi(y)=y\log y-y$, and let $v,f,m,N,L,\Lambda,\ell,G,\lambda$ be real numbers. Assume $$K_{j,s}\le\sum_\rho\left[\sum_i\phi(\nu_{j,\rho,i})-n_{j,\rho}\lambda_{\rho,s}\right]+|\Sigma|g_j\theta_s+|\Sigma|g_j\log(8+32|\Sigma|g_jv)$$ $$\hspace{12mm}+2Q_{j,s}+\sum_\rho\{1+2g_j\log(2n_{j,\rho}+2)\}+u_j+u'_j.$$ Let $C_2,C_3,C_4,c_5,c_6,C_7,C_8,C_e,C_h$ be real constants with the first eight nonnegative. Assume $$\langle\lambda_{\rho,s}\rangle=\lambda,\quad Q_{j,s}\le C_2fm^2N^2(G+\ell)+C_efN^2G,\quad\langle\theta_s\rangle\le C_3L,$$ $$u_j,u'_j\le C_4fN^2(L+\ell+G),\quad |\Sigma|\le f,\quad 0\le g_j\le N^2,$$ $$1\le m,N,\quad 0\le L\le\Lambda,\quad1\le\Lambda,$$ $$\log(8+32|\Sigma|g_jv)\le c_5\Lambda,\quad\log(2n_{j,\rho}+2)\le c_6\Lambda,\quad\ell\le C_7mL,\quad G\le C_8L,$$ $$C_3+c_5+2c_6+1+2C_4+2C_eC_8\le C_h,\qquad2(C_2+C_4)(C_7+C_8)\le C_h.$$ Then, for every $j\in J$, $$\langle K_{j,s}\rangle\le\sum_\rho\left[\sum_i\phi(\nu_{j,\rho,i})-n_{j,\rho}\lambda\right]+C_hfN^2(\Lambda+m^3L).$$ No relation between $|J|$ and $m$ is assumed in this estimate. The logarithm is the total real logarithm, including $\log0=0$.
