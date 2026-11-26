---
{
  "module": "src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/LandauDichotomy.lean",
  "declarations": [
    "Deduction.landau_dichotomy"
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

## Two disk configurations for a discrete pole set

[Theorem ANT.0143](https://andrewodesky.com/rh/lean/Deduction.landau_dichotomy/)

Let $Z\subseteq\mathbb C$ be a set such that every $z$ with $\Re z>0$ has a punctured neighborhood disjoint from $Z$. Let $\theta,\sigma\in\mathbb R$ satisfy $0<\theta<\sigma$. Suppose $\Re\rho<\sigma$ for every $\rho\in Z$ and there is $\rho_0\in Z$ with $\Re\rho_0>\theta$. Write $B(z,r)$ for the open complex disk. At least one of the following holds.

There are a real $D\le\sigma-\theta$ and $\rho_1\in Z$ such that $$Z\cap B(\sigma,D)=\varnothing,\qquad \sigma-\Re\rho_1<D.$$

There are real numbers $\beta>\theta$ and $r$ such that $$\beta\in Z,\qquad \sigma-\beta<r\le\sigma-\theta,\qquad Z\cap B(\sigma,r)=\{\beta\}.$$
