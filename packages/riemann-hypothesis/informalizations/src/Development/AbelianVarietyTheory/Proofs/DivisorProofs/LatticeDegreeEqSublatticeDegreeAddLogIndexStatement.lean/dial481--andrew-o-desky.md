---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/LatticeDegreeEqSublatticeDegreeAddLogIndexStatement.lean",
  "declarations": [
    "GlobalTheory.T.lattice_degree_eq_sublattice_degree_add_log_index"
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

## Arithmetic degree and sublattice index

[Theorem ARAK.0129](https://andrewodesky.com/rh/lean/GlobalTheory.T.lattice_degree_eq_sublattice_degree_add_log_index/)

Let $K$ be a number field, $V$ a finite-dimensional $K$-space with a Hermitian norm at each embedding, and $N\subseteq L\subset V$ be $\mathcal O_K$-submodules. Suppose $L$ is finitely generated and $\operatorname{rk}N=\operatorname{rk}L=m$. Their lattice-index ideal $\mathfrak i(L,N)$ is nonzero and $$\widehat{\deg}L=\widehat{\deg}N+\frac{\log N_{K/\mathbb Q}\mathfrak i(L,N)}{[K:\mathbb Q]}.$$ Here a subscript denotes localization, and the index ideal is the ideal whose localization at every nonzero prime $\mathfrak p$ is $\mathfrak p^{\operatorname{length}_{\mathcal O_{K,\mathfrak p}}(L_\mathfrak p/N_\mathfrak p)}$, and $N_{K/\mathbb Q}$ denotes its absolute norm. Arithmetic degree uses the induced determinant metric and division by $[K:\mathbb Q]$.
