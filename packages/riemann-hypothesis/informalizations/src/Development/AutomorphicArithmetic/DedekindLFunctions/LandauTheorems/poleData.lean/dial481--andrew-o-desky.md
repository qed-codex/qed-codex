---
{
  "module": "src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/poleData.lean",
  "declarations": [
    "Deduction.poleData"
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

## Laplace transform with character zeros as poles

[Theorem ANT.0141](https://andrewodesky.com/rh/lean/Deduction.poleData/)

Let $r\ge0$ be an integer, let $\chi_1,\ldots,\chi_r$ be Dirichlet characters of positive integer moduli, each of them nonprincipal or of modulus $1$, and let $a_1,\ldots,a_r$ be positive real numbers. Use the functions $g_\chi$ and $L(s,\chi)$ of ([Regularized smoothed character sums](https://andrewodesky.com/rh/lean/Deduction.Gchi/)). Set $g(u)=\sum_i a_i\Re g_{\chi_i}(e^u)$ and $$Z=\{\rho\in\mathbb C:\Re\rho>0,\ L(\rho,\chi_i)=0\text{ or }L(\overline\rho,\chi_i)=0\text{ for some }i\}.$$ Then $g$ is measurable and there is $C_0\in\mathbb R$ such that $|g(u)|\le C_0e^{2u}$ for every $u\ge0$. There exists $\Phi:\mathbb C\to\mathbb C$ with $$\Phi(s)=\int_0^\infty g(u)e^{-su}\,du\qquad(\Re s>2),$$ holomorphic on $\{\Re s>0\}\setminus Z$. Every point of $\{\Re s>0\}$ has a punctured neighborhood disjoint from $Z$. For every $\rho\in Z$ there are $c_\rho\ne0$ and a function $h_\rho$ holomorphic near $\rho$ such that, on a punctured neighborhood of $\rho$, $$\Phi(s)=\frac{c_\rho}{s-\rho}+h_\rho(s).$$ If $\rho$ is real, then $c_\rho$ is positive real.
