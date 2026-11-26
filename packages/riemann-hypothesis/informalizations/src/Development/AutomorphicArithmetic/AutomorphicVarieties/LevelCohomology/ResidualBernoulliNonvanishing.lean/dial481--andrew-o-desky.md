---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/LevelCohomology/ResidualBernoulliNonvanishing.lean",
  "declarations": [
    "UpperTheory.V.X.residual_bernoulli_nonvanishing"
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

## Residual cocycles are coboundaries under a Bernoulli-unit condition

[Theorem GC.1374](https://andrewodesky.com/rh/lean/UpperTheory.V.X.residual_bernoulli_nonvanishing/)

Let $\Omega/\mathbb Q$ be an algebraic closure, let $\ell\ne2$ be prime, and let $\mathcal O$ be a discrete valuation $\mathbb Z_\ell$-subalgebra of $\overline{\mathbb Q}_\ell$ finite as a $\mathbb Z_\ell$-module. Let $k$ be any field of characteristic $\ell$ and $r:\mathcal O\to k$ a ring homomorphism. Fix $N\ge1$ and a nontrivial Dirichlet character $\chi$ modulo $N$ with values in $\mathcal O$, whose order is prime to $\ell$. Let $\gamma:G_{\mathbb Q}\to k^\times$ be its residual Galois character. Assume $\gamma$ differs from the residual cyclotomic character at some element, and the first generalized Bernoulli number $B_{1,\chi^{-1}}=\sum_{a=1}^N\chi^{-1}(a)(a/N-1/2)$ satisfies $$|B_{1,\chi^{-1}}|_\ell=1.$$ Let $z:G_{\mathbb Q}\to k$ be locally constant with $z(gh)=z(g)+\gamma(g)z(h)$. Suppose that for every valuation subring of $\Omega$, with inertia subgroup $I$, there is a subgroup $H\subset G_{\mathbb Q}$ such that $$\ell\nmid[I\cap\ker\gamma:H\cap I\cap\ker\gamma],\qquad z|_{H\cap I\cap\ker\gamma}=0.$$ Then there is $m\in k$ such that $$z(g)=\gamma(g)m-m\qquad(g\in G_{\mathbb Q}).$$
