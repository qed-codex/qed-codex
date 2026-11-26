---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/ChebotarevFamilies/ChebFam.lean",
  "declarations": [
    "UpperTheory.V.Pa.chebFam"
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

## Simultaneous approximation by Frobenius elements at split primes

[Theorem ANT.0455](https://andrewodesky.com/rh/lean/UpperTheory.V.Pa.chebFam/)

Let $L$ be a CM number field, $L^+$ its maximal real subfield, and $\Omega$ an algebraic closure of $L$. Let $U$ be an open subgroup of $G_L=\operatorname{Gal}(\Omega/L)$, choose $g_1,\ldots,g_q\in G_L$ with $q\ge0$, and let $A$ be a finite set of finite primes of $L^+$. There are pairwise distinct primes $v_1,\ldots,v_q$ of $L^+$ outside $A$, primes $w_j$ of $L$, valuation subrings $B_j$ of $\Omega$, and $\sigma_j\in G_L$ such that $B_j$ lies above both $w_j$ and $v_j$, $$D_{B_j}(\Omega/L^+)\subseteq\operatorname{Gal}(\Omega/L),\qquad\sigma_jg_j^{-1}\in U,$$ and $\sigma_j$ is a Frobenius element at $B_j$ over $L$, inducing the power map $x\mapsto x^{Nw_j}$ on its residue field. Here $D_{B_j}(\Omega/L^+)$ denotes the subgroup preserving $B_j$, viewed in $\operatorname{Gal}(\Omega/L^+)$, and $Nw_j=|\mathcal O_L/w_j|$.
