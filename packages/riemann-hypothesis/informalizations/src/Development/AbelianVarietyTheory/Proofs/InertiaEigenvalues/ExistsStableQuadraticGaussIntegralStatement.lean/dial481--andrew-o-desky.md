---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsStableQuadraticGaussIntegralStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_stable_quadraticGaussIntegral"
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

## Stabilization of a local quadratic Gauss integral

[Theorem ANT.0353](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_stable_quadraticGaussIntegral/)

Let $F,E$ be nontrivially normed, locally compact nonarchimedean fields, with $F$ of characteristic zero and $E/F$ a norm-compatible extension of degree two. Let $y\mapsto\bar y$ be a nontrivial isometric involution on $E$ fixing $F$, and assume every norm attained in $E$ is attained in $F$. Let $K/F$ be a finite field extension, locally compact in its finite-dimensional $F$-module topology, with its Borel structure. Suppose $L=E\otimes_FK$ is a field, with the induced $F$-module topology and Borel structure, and involution fixing $K$ and extending that of $E$.

Let $\psi:F\to\mathbb C$ be an additive character trivial on $\{|t|\le1\}$. Assume there is $t$ with $\psi(t)\ne1$ and $|ty|\le1$ for every $|y|<1$. Fix $x\in K^\times$, and a measure $\mu$ self-dual for $$B(y',y)=\psi\!\left(\operatorname{Tr}_{K/F}\bigl(x\operatorname{Tr}_{L/K}(\bar y' y)\bigr)\right).$$ Fix also $\omega:K\to\mathbb C$ whose value on $K^\times$ is $1$ on norms from $L$ and $-1$ on the other elements. For every $u\in K^\times$ there are $G\in\mathbb C$ and a compact open additive subgroup $\Lambda_0\le L$ such that $$\int_\Lambda\psi\!\left(\operatorname{Tr}_{K/F}(uxN_{L/K}(y))\right)\,d\mu(y)=G$$ for every compact open additive subgroup $\Lambda\supseteq\Lambda_0$.
