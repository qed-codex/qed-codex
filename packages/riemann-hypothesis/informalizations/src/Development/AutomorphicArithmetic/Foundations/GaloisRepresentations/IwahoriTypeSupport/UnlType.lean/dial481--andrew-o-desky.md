---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IwahoriTypeSupport/UnlType.lean",
  "declarations": [
    "UpperTheory.Gal.TypesAndIwahori.unlinked_of_typeVec"
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

## Distinct residue characters exclude adjacent cuspidal twists

[Theorem REP.0075](https://andrewodesky.com/rh/lean/UpperTheory.Gal.TypesAndIwahori.unlinked_of_typeVec/)

Let $k$ be a nonarchimedean local field of characteristic zero, with residue field $\kappa$, and let $d_1,\ldots,d_c>0$ sum to $N$. Let $\pi$ be a smooth irreducible generic complex representation of $\operatorname{GL}_N(k)$. Let $\theta_1,\ldots,\theta_c:\kappa^\times\to\mathbb C^\times$ be pairwise distinct characters. Let $P\subset\operatorname{GL}_N(\mathcal O_k)$ be the inverse image of the standard block parabolic of sizes $d_i$ in $\operatorname{GL}_N(\kappa)$, and let $\overline g_i$ be the diagonal Levi blocks of the reduction of $g\in P$. Suppose there exists a nonzero vector $v$ with $$\pi(g)v=\left(\prod_{i=1}^c\theta_i(\det\overline g_i)\right)v\qquad(g\in P).$$ For every cuspidal-support multiset $S$ of $\pi$ and all $y,z\in S$, $$y\not\simeq z\otimes|\det|_k.$$
