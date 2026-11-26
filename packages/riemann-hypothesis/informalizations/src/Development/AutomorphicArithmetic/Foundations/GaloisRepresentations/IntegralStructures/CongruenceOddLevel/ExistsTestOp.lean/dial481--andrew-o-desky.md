---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/CongruenceOddLevel/ExistsTestOp.lean",
  "declarations": [
    "UpperTheory.Gal.Int.Cong.exists_testOp"
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

## A local Hecke operator detecting nonvanishing of a polynomial

[Theorem AGR.1393](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.Cong.exists_testOp/)

Let $E$ be a CM number field, $a\ge0$, and $U$ the adelic unitary group of the identity Hermitian form of rank $a$. Let $w$ be a finite place split over the maximal real subfield, so that its local subgroup $U_w$ is identified by $c_w$ with $\mathrm{GL}_a(E_w)$. Let $K\subset U$ be any subgroup such that $$K\cap U_w=c_w^{-1}\bigl(\mathrm{GL}_a(\mathcal O_{E_w})\bigr).$$ Fix a polynomial $\Phi\in\mathbb C[X_1,\ldots,X_a]$. There are a finitely supported function $f:U\to\mathbb C$ supported in $U_w$, and scalars $\eta(\Pi)$ assigned to the automorphic representation subspaces $\Pi$ defined below, such that $$\sum_gf(g)R(g)\varphi=\eta(\Pi)\varphi\qquad(\varphi\in\Pi^K).$$ Whenever $\Pi^K\ne0$, one has $\eta(\Pi)\ne0$ if and only if $\Phi(z_1,\ldots,z_a)\ne0$ for every ordered Satake tuple $(z_i)$ of a local component of $\Pi$ at $w$. Here $R$ denotes right translation. An automorphic representation subspace is a nonzero irreducible right-translation-invariant complex subspace of continuous functions on $U$ which are left rational-invariant, have an open finite-level stabilizer, and span a finite-dimensional space under archimedean compact translation.
