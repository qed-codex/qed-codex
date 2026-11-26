---
{
  "module": "src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/LandauNearest.lean",
  "declarations": [
    "Deduction.landau_nearest"
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

## A shifted disk containing exactly one pole

[Theorem ANT.0145](https://andrewodesky.com/rh/lean/Deduction.landau_nearest/)

Let $Z\subseteq\mathbb C$ be a set such that every $z$ with $\Re z>0$ has a punctured neighborhood disjoint from $Z$. Let $\sigma,D\in\mathbb R$ with $D<\sigma$, and suppose $\Re\rho<\sigma$ for every $\rho\in Z$. If some $\rho_1\in Z$ satisfies $\sigma-\Re\rho_1<D$, there exist $t\in\mathbb R$, $\rho\in Z$ and $r\in\mathbb R$ such that $$|\sigma+it-\rho|<r\le D,\qquad Z\cap B(\sigma+it,r)=\{\rho\},$$ where $B(z,r)$ is the open complex disk.
