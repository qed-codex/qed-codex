---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/TransportedWeylLatticeHermitianDualityStatement.lean",
  "declarations": [
    "GlobalTheory.T.transported_weylLattice_hermitianDuality"
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

## Hermitian duality of transported Weyl lattices

[Theorem REP.0311](https://andrewodesky.com/rh/lean/GlobalTheory.T.transported_weylLattice_hermitianDuality/)

Let $K$ be a number field with involution $a\mapsto\bar a$, $I$ a finite set, $n\ge0$, and $\lambda_\tau\in\mathbb Z^n$ weakly decreasing for each $\tau\in I$. Let $G_\tau\in M_n(K)$ be invertible Hermitian matrices, and $M_\tau\subseteq K^n$ full $\mathcal O_K$-lattices. With the polynomial spaces, actions and lattices defined below, $$\mathcal N(M)^{\#}=\mathcal D(M^{\#}),\qquad\mathcal D(M)^{\#}=\mathcal N(M^{\#}).$$ Here $M_\tau^{\#}=\{x:\bar y^{\mathsf T}G_\tau x\in\mathcal O_K\text{ for every }y\in M_\tau\}$, and the duals on the left use the pairing $B_G$ below.
