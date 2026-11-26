---
{
  "module": "src/Formalism/LocalToGlobal/Divisibility/DivisionHeightBoundStatement.lean",
  "declarations": [
    "Formalism.L2.DIV.HtNums.le_hu",
    "Formalism.L2.DIV.RecNums.divIneq"
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

## Numerical cancellation of slope and theta heights

[Theorem ARAK.0181](https://andrewodesky.com/rh/lean/Formalism.L2.DIV.RecNums.divIneq/)

Let the numerical data consist of finite sets $J,\Sigma$, a subset $T\subset\Sigma$, an integer $r\ge0$, real arrays $\nu_{j,\rho,i},A_{j,\rho},w_{j,\rho},e_{j,\rho},\delta_{j,\rho},p_j,a_\rho$, and real parameters $x,\varepsilon,L,b,a,d,\Lambda,B_0,N_c,m,f,k,N,S,t_0,\eta,W,b',\lambda_0,C_0,c_e,C_h,n_V,L',\lambda,\ell$. The indices are $j\in J$, $\rho\in\Sigma$ and $1\le i\le r$. For $y<0$ put $\log y=\log|y|$, and put $\log0=0$; division by zero has value zero. Define $\phi(y)=y\log y-y$. Impose the following conditions: $$1<x,\quad\varepsilon>0,\quad L=x^\varepsilon,\quad b=e^L,\quad a=xb,\quad d\ge1,\quad\log d\le L,\quad\log x\le L,\quad\Lambda=\log(ad),$$ $$B_0=fmbx^\varepsilon,\quad N_c\ge0,\quad|J|=m\ge1,\quad |\Sigma|\le f,\quad f\ge1,\quad k\ge1,\quad k+m\le N,$$ $$S,t_0,\eta,b',\lambda_0,n_V,L'\ge0,\quad n_V\le N,\quad0\le w_{j,\rho}\le2b,\quad|p_j-k|\le m,\quad|\lambda|\le\Lambda,$$ $$m\lambda_0\le b,\quad N^2\le b,\quad m^3N^2L\le b,\quad m\eta NL\le b,\quad kN\le b,$$ $$kS\le W,\quad m(t_0+1)\eta\le W,\quad NW\le b,\quad b'N\le a,\quad mkb'\le a,$$ $$1\le C_0\le c_e,\quad0\le C_h\le C_0,\quad C_hL'\le C_0\Lambda.$$ For every $j,\rho$ require the two weight comparisons $$\sum_i\phi(\nu_{j,\rho,i})-A_{j,\rho}\le\mathbf1_{\rho\in T}\phi(a_\rho)+e_{j,\rho},\qquad\sum_i\nu_{j,\rho,i}=\mathbf1_{\rho\in T}a_\rho+kw_{j,\rho}+\delta_{j,\rho},$$ and the error bounds $$e_{j,\rho}\le C_0\{w_{j,\rho}+S+N^2+m(t_0+1)\eta\}\Lambda,$$ $$|\delta_{j,\rho}|\le C_0\{w_{j,\rho}+k(N+S)+m(t_0+1)\eta+\mathbf1_{\rho\in T}kb'\}.$$ Finally, define the height expressions appearing in the conclusion by $$H_A=-\sum_{t\in T}a_t\ell+C_h\{|T|b'N+f(m\eta+S)N+fN^2\}\Lambda,$$ $$H_{B,j}=\sum_\rho\left[\sum_i\phi(\nu_{j,\rho,i})-\left(\sum_i\nu_{j,\rho,i}\right)\lambda\right]+C_hfN^2(\Lambda+m^3L),$$ $$H_{X,j}=\sum_\rho A_{j,\rho}-C_hfn_V^2L',\qquad H=H_A+\sum_j(H_{B,j}-H_{X,j}).$$

Define the main term $M$ and the upper bound $\mathcal R$ by $$M=\sum_{t\in T}\left[m\{\phi(a_t)-a_t\lambda\}-a_t\ell\right],\qquad \mathcal R=M+(50C_0+10)|T|a\Lambda+60c_emx^\varepsilon(B_0+N_c).$$

Let $z,z_0,F,P,E$ be real numbers such that $$z\le z_0+P,\qquad z_0\le\sum_{j,\rho}p_jw_{j,\rho}\lambda+2F+E,$$ $$P\le1+C_0m\lambda_0,\qquad E\le c_emx^\varepsilon(B_0+N_c).$$ Then $$z+H-2F\le\mathcal R.$$
