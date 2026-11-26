---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/MemSupercuspidalSupportOfTorusJacquetEigenform.lean",
  "declarations": [
    "GlobalTheory.EigenSupport.inSupport_of_torus_eigenform"
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

## Rank-one Levi factors from a Jacquet eigenfunctional

[Theorem REP.0477](https://andrewodesky.com/rh/lean/GlobalTheory.EigenSupport.inSupport_of_torus_eigenform/)

Let $k$ be a nonarchimedean local field, let $n\ge0$, let $\pi$ be a complex representation of $\operatorname{GL}_n(k)$, and let $\psi_1,\ldots,\psi_n:k^\times\to\mathbb C^\times$ be group homomorphisms. Let $J_B(\pi)$ be its normalized Jacquet module for the upper triangular Borel. Suppose there is a nonzero complex-linear functional $\ell:J_B(\pi)\to\mathbb C$ such that $$\ell(t\cdot y)=\left(\prod_{i=1}^n\psi_i(t_i)\right)\ell(y)\qquad(t\in(k^\times)^n,\ y\in J_B(\pi)).$$ For each $i$ there are an ordered block decomposition $n=d_1+\cdots+d_s$, a block $a$ with $d_a=1$, and an irreducible subquotient $\sigma$ of the normalized Jacquet module of $\pi$ for that block parabolic, such that the $a$th Levi factor acts on $\sigma$ by $\psi_i\circ\det$.
