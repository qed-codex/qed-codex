---
{
  "module": "src/Formalism/HermitianLattices/FinalNeighbourConstruct.lean",
  "declarations": [
    "Formalism.HermitianLatticesTheory.final_genusCovol"
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

## Equal Euclidean covolumes within a Hermitian genus

[Theorem ARAK.1012](https://andrewodesky.com/rh/lean/Formalism.HermitianLatticesTheory.final_genusCovol/)

Let $K$ be a number field with an involution, $V$ a finite-dimensional $K$-space with its compatible $\mathcal O_K$-module structure, and $h$ a Hermitian form on $V$. Assume $\operatorname{Tr}_{K/\mathbb Q}h(x,x)>0$ for $x\ne0$. Let $\iota:V\to\mathbb R^N$ be additive and satisfy $$\langle\iota(x),\iota(y)\rangle=\operatorname{Tr}_{K/\mathbb Q}h(x,y).$$ Let $L$ be a full $\mathcal O_K$-lattice and let $M$ belong to its Hermitian genus. Assume both $\iota(L)$ and $\iota(M)$ are discrete full $\mathbb Z$-lattices in $\mathbb R^N$. Then $$\operatorname{covol}(\iota(M))=\operatorname{covol}(\iota(L)).$$
