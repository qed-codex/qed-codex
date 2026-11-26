---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/ThetaTranslateSeriesEqConstMulIntegralOneSeriesStatement.lean",
  "declarations": [
    "GlobalTheory.T.thetaTranslateSeries_eq_const_mul_integral_one_series"
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

## A translated theta series is a scalar times an integral unit series

[Theorem PHT.1519](https://andrewodesky.com/rh/lean/GlobalTheory.T.thetaTranslateSeries_eq_const_mul_integral_one_series/)

Fix the source's full arithmetic theta datum, with imaginary quadratic subfield $K$, discriminant parameter $d$, and chosen complex embedding $\sigma:K\hookrightarrow\mathbb C$. Let $p$ be prime, $\mathfrak c\ne0$ an integral ideal of $K$ whose norm is coprime to $2dp$, and choose $\delta\in\mathbb C$ with $\delta^{12}$ equal to the Weierstrass discriminant of $\sigma(\mathfrak c)$. Put $\Lambda=\delta\sigma(\mathfrak c)$ and choose $\lambda:\overline{\mathbb Q}\cap\mathbb C\hookrightarrow\mathbb C_p$. Extend $\lambda$ to a function $\lambda_0:\mathbb C\to\mathbb C_p$ by assigning zero to nonalgebraic numbers.

Start with the Weierstrass model with coefficients $(0,0,0,\lambda_0(-g_2(\Lambda)/4),\lambda_0(-g_3(\Lambda)/4))$. Let a Weierstrass variable change $(u,r,s,t)$, $u\ne0$, take this to a model $W$ with coefficients $a_i$ of norm at most one and $|\Delta(W)|_p=1$. Choose $w\in\mathbb C_p[[T]]$ satisfying $$w=1+a_1Tw+a_2T^2w+a_3T^3w^2+a_4T^4w^2+a_6T^6w^3,$$ and define $L(T)$ by $L(0)=0$ and $$L'(T)=\frac{-2w-Tw'}{w(a_1T+a_3T^3w-2)}.$$ Assume a chosen formal series with zero constant term is a compositional inverse of $L$. Set $\varepsilon=u^{-1}$ and $x_p(v)=u^{-2}(\lambda_0(\wp_\Lambda(v))-r)$.

Let $A_\Lambda$ be the area of $\Lambda$ and $\sigma_\Lambda$ the normalized odd theta function specified by the following conditions: it is entire, $\sigma'_\Lambda(0)=1$, and $$\sigma_\Lambda(z+\omega)e^{-\pi z\bar\omega/A_\Lambda-\pi|\omega|^2/(2A_\Lambda)}=\begin{cases}\sigma_\Lambda(z)&\omega/2\in\Lambda,\\-\sigma_\Lambda(z)&\omega/2\notin\Lambda\end{cases}\quad(\omega\in\Lambda).$$ For $v\in\mathbb C$ define $F_v(z)=\sigma_\Lambda(z+v)e^{-\pi z\bar v/A_\Lambda-\pi|v|^2/(2A_\Lambda)}$ and $S_v(Z)=\sum_{n\ge0}\lambda_0(F_v^{(n)}(0)/n!)Z^n$. Put $$\Phi(T)=\frac{S_0(\varepsilon L(T))}{\varepsilon T},\qquad \tau_v(T)=\Phi(T)^{-1}S_v(\varepsilon L(T)),\qquad c_v=\lambda_0(F_v(0)).$$ Assume $|x_p(v)|_p\le1$ whenever $v\notin\Lambda$ and $mv\in\Lambda$ for some integer $m>0$ coprime to $p$. For every such $v$ there is $w_v\in\mathbb C_p[[T]]$ with $$w_v(0)=1,\qquad |[T^n]w_v|_p\le1\ (n\ge0),\qquad \tau_v=c_vw_v.$$
