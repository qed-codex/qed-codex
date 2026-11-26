---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/FrobeniusSmoothVectors/AuxwEx.lean",
  "declarations": [
    "UpperTheory.V.Fr.auxw_ex"
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

## A prime splitting three residual characters in a prescribed progression

[Theorem ANT.0535](https://andrewodesky.com/rh/lean/UpperTheory.V.Fr.auxw_ex/)

Let $\Omega/\mathbb Q$ be an algebraic closure and $G=\operatorname{Gal}(\Omega/\mathbb Q)$. Let $\ell$ be an odd prime, $O$ a commutative local ring with finite residue field $k$ of characteristic $\ell$, and let $\eta:G\to\{\pm1\}$ and $\Psi:G\to O^\times$ be homomorphisms. Write $\bar\Psi:G\to k^\times$ for reduction and $\omega:G\to\mathbb F_\ell^\times\subseteq k^\times$ for the mod-$\ell$ cyclotomic character. Let $\sigma\in G$ be complex conjugation, $B$ a valuation ring of $\Omega$ over $\ell$, $M>0$ a multiple of $2\ell$, and $H\le G$. Assume all the conditions below. For every integer $Q>0$, there is a rational prime $w$ such that $$w\nmid M,\qquad w\equiv1\pmod\ell,\qquad w\equiv1\pmod Q,$$ and, for every valuation ring $A$ of $\Omega$ over $w$, $$D_A\subseteq\ker\eta\cap\ker\bar\Psi\cap\ker\omega.$$
