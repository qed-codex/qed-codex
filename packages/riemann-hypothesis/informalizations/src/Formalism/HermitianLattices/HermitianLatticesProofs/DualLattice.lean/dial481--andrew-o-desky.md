---
{
  "module": "src/Formalism/HermitianLattices/HermitianLatticesProofs/DualLattice.lean",
  "declarations": [
    "Formalism.HermitianLatticesTheory.dualLattice"
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

## Duality for Hermitian lattices over a Dedekind domain

[Theorem ALG.0437](https://andrewodesky.com/rh/lean/Formalism.HermitianLatticesTheory.dualLattice/)

Let $R$ be a Dedekind domain with fraction field $K$, equipped with an involution $a\mapsto\bar a$ preserving $R$. Let $V$ be a finite-dimensional $K$-vector space with a nondegenerate Hermitian form $h$, conjugate-linear in its first variable. Let $L\subset V$ be a finitely generated $R$-submodule spanning $V$ over $K$, and put $$L^\vee=\{x\in V:h(y,x)\in R\text{ for every }y\in L\}.$$ Then $L^\vee$ is a finitely generated full $R$-lattice and $$(L^\vee)^\vee=L,\qquad (aL)^\vee=\bar a^{-1}L^\vee\quad(a\in K^\times).$$
