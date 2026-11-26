---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/GaussSumFiltrations/ThetaSeriesHolomorphicQExpansionOfBoundedCoeff.lean",
  "declarations": [
    "GlobalTheory.HilbertThetaSeries.th_expansion"
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

## A Hilbert theta expansion with bounded coefficients

[Theorem ANT.0247](https://andrewodesky.com/rh/lean/GlobalTheory.HilbertThetaSeries.th_expansion/)

Let $F$ be a totally real number field, $I$ a finite set, and $G\in M_I(\mathbb Z)$ a matrix positive definite over $\mathbb R$ with even diagonal. Put $$Q(x)=\tfrac12x^tGx,\qquad e_\xi(z)=\exp\left(2\pi i\sum_\tau\tau(\xi)z_\tau\right),$$ where $\tau$ runs over the real embeddings of $F$ and $z\in\mathfrak H^{\operatorname{Hom}(F,\mathbb R)}$. Let $a\in F$ and $\Phi:F^I\to\mathbb C$ satisfy $\Phi(x)\ne0\Rightarrow x\in a\mathcal O_F^I$ and $|\Phi(x)|\le B$ for some $B\in\mathbb R$.

The series $$\theta(z)=\sum_{x\in F^I}\Phi(x)e_{Q(x)}(z)$$ is summable for every $z$ and defines a holomorphic function. There are $C\in\mathbb R$ and an integer $A\ge0$ such that $$|\theta(z)|\le C\left(\prod_\tau\frac{1+|z_\tau|^2}{\operatorname{Im}z_\tau}\right)^A.$$ It has the expansion $$\theta(z)=\sum_{\xi\in F}c_\xi e_\xi(z),\qquad c_\xi=\sum_{\substack{x\in a\mathcal O_F^I\\Q(x)=\xi}}\Phi(x).$$ The outer sum is an unordered convergent sum. There is an integer $D\ge1$ such that $c_\xi\ne0$ implies $D\xi\in\mathcal O_F$ and either $\xi=0$ or $\xi$ is totally positive.
