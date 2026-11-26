---
{
  "module": "src/Formalism/WachLatticeTwists/RamifiedBlockRings/RamifiedBlockProofs/Normal.lean",
  "declarations": [
    "Formalism.RepresentationBoundsCohomology.ringDataObjects.idem_normal_form"
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

## Diagonalizing an idempotent matrix over a local ring

[Theorem ALG.0847](https://andrewodesky.com/rh/lean/Formalism.RepresentationBoundsCohomology.ringDataObjects.idem_normal_form/)

Let $\mathcal O$ be a commutative local ring, let $I$ be a finite set, and let $e\in M_I(\mathcal O)$ satisfy $e^2=e$. There are matrices $P,Q\in M_I(\mathcal O)$ and elements $d_i\in\{0,1\}\subseteq\mathcal O$ such that $$PQ=QP=I,\qquad e=P\operatorname{diag}(d_i)Q.$$
