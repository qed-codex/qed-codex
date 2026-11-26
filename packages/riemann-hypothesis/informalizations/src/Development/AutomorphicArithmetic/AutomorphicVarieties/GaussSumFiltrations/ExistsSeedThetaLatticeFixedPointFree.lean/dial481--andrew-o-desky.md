---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/GaussSumFiltrations/ExistsSeedThetaLatticeFixedPointFree.lean",
  "declarations": [
    "GlobalTheory.T.exists_seed_theta_lattice_fixedPointFree"
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

## A Hilbert modular function congruent to one after specified translates

[Theorem ANT.0439](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_seed_theta_lattice_fixedPointFree/)

Let $F$ be totally real, $p\ne2$ a rational prime, and $\iota:\overline{\mathbb Q}_p\simeq\mathbb C$ a field isomorphism. Choose $\delta\in F$ whose additive valuation at each prime $w\mid p$ equals the exponent of $w$ in the different $\mathfrak D_{F/\mathbb Q}$. Put $\mathfrak H_F=\prod_{\tau:F\hookrightarrow\mathbb R}\mathfrak H$. There is a holomorphic $\theta:\mathfrak H_F\to\mathbb C$ with $$|\theta(z)|\le C\left(\prod_\tau\frac{1+|z_\tau|^2}{\operatorname{Im}z_\tau}\right)^A$$ for some $C\in\mathbb R$, $A\in\mathbb N$, and the following properties.

For every $\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\operatorname{GL}_2(F)$ with totally positive determinant, with $a,\delta b,c/\delta,d$ integral at every $w\mid p$, and determinant a unit at those primes, the function $\theta|_{p-1}\gamma-1$ has an expansion $$\sum_{\xi\in F}a_\xi e^{2\pi i\sum_\tau\tau(\xi)z_\tau}$$ converging at every $z\in\mathfrak H_F$. Its nonzero coefficients are supported on zero and totally positive elements, and some integer $D\ge1$ makes every $D\xi$ in its support integral over $\mathbb Z$. Every coefficient satisfies $|\iota^{-1}(a_\xi)|_p\le p^{-1}$.

There is $N\ge1$ such that for every $\gamma\in\operatorname{SL}_2(F)$ with $a,b,c/N,d$ integral over $\mathbb Z$, there is $\zeta\in\mathbb C$ with $\zeta^8=1$ and $\theta|_{p-1}\gamma=\zeta\theta$.
