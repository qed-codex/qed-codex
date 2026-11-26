---
{
  "module": "src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/landauWindow.lean",
  "declarations": [
    "Deduction.landau_window_key"
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

## One-sided bound for high derivatives

[Theorem ANT.1733](https://andrewodesky.com/rh/lean/Deduction.landau_window_key/)

Let $g$, $\Phi$ and $Z$ satisfy the hypotheses of ([Derivatives of the Laplace transform](https://andrewodesky.com/rh/lean/Deduction.landau_coeff/)), and let $\theta$ and $\delta$ be real numbers with $0<\theta<1$ and $\delta>0$. For a real number $U$ write $I_U=[U,(1+\delta)U]$. Suppose that for every $\eta>0$ and every real number $U_0$ there are a real number $U\ge U_0$ and a function $R:\mathbb R\to\mathbb R$ such that $R(u)\ge0$ and $g(u)\le R(u)$ for every $u\in I_U$, the function $R(u)e^{-\theta u}$ is integrable on $I_U$, and $$\int_{I_U}R(u)e^{-\theta u}\,du\le e^{\eta U}.$$ Then there are real numbers $\sigma>2$ and $B$ such that for every $\eta>0$ and every real number $U_0$ there are a real number $U\ge U_0$ and an integer $k\ge0$ with $k\ge U$ for which $$\left|\frac{(-1)^k\Phi^{(k)}(\sigma+it)}{k!}\right|+\Re\frac{(-1)^k\Phi^{(k)}(\sigma)}{k!}\le\frac{B e^{\eta U}}{(\sigma-\theta)^k}\qquad\text{for every real number }t.$$
