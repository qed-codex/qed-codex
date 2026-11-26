---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/FinrankOrth.lean",
  "declarations": [
    "GlobalTheory.WittLow.exists_lower"
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

## A smaller Hermitian space orthogonal to an isotropic subspace

[Theorem ALG.0438](https://andrewodesky.com/rh/lean/GlobalTheory.WittLow.exists_lower/)

Let $E$ be a number field with an involution $x\mapsto\bar x$ preserving its algebraic integers. Let $(V,h)$ be a finite-dimensional nondegenerate Hermitian $E$-space supplied with a basis and a full self-dual $\mathcal O_E$-lattice. Suppose $e_1,\ldots,e_i$ are linearly independent and $h(e_a,e_b)=0$ for all $a,b$. There are another finite-dimensional nondegenerate Hermitian space $(V',h')$, supplied with a basis and a full self-dual $\mathcal O_E$-lattice, and an $E$-linear map $j:V'\to V$ such that $$\dim_EV'+2i=\dim_EV,\qquad h(jx,jy)=h'(x,y),\qquad h(jx,e_a)=0.$$ The last two identities hold for all $x,y\in V'$ and $1\le a\le i$.
