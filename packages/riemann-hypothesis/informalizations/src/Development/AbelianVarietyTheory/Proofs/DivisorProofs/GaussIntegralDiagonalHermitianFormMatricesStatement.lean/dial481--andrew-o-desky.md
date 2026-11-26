---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/GaussIntegralDiagonalHermitianFormMatricesStatement.lean",
  "declarations": [
    "GlobalTheory.T.gaussIntegral_diagonal_hermitianForm_matrices"
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

## Gauss integrals for diagonal norm forms on matrices

[Theorem ANT.1084](https://andrewodesky.com/rh/lean/GlobalTheory.T.gaussIntegral_diagonal_hermitianForm_matrices/)

Let $F$ be a nonarchimedean local field of characteristic zero with its valuation topology. Let $E/F$ be a field extension, with the topology of an $F$-module, and let $c:E\to E$ be an $F$-algebra endomorphism. Assume there is $\delta\in E^\times$ with $c(\delta)=-\delta$ and $(1,\delta)$ an $F$-basis of $E$. Let $A,B$ be finite sets, $\psi:F\to\mathbb C^\times$ a continuous nontrivial additive character with $|\psi|=1$, and $\mu$ an additive Haar measure on $E^{A\times B}$, with its Borel sigma-algebra.

There is $g\in\mathbb C$ such that, for every $(t_{ij})\in(F^\times)^{A\times B}$, the function $$x\longmapsto\psi\!\left(\sum_{i,j}t_{ij}N_{E/F}(x_{ij})\right)$$ has stabilized Gauss integral $$g\prod_{i,j}\eta_{E/F}(t_{ij})|t_{ij}|_F^{-1}.$$
