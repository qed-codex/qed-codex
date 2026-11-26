---
{
  "module": "src/Formalism/WachLatticeTwists/RamifiedBlockRings/RamifiedBlockProofs/IdempotentImageSurjective.lean",
  "declarations": [
    "Formalism.RepresentationBoundsCohomology.ringDataObjects.resConst"
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

## Residues of functions in a local subalgebra are constant

[Theorem ALG.0651](https://andrewodesky.com/rh/lean/Formalism.RepresentationBoundsCohomology.ringDataObjects.resConst/)

Let $O$ be a commutative local ring, let $X$ be a set, and let $T\subseteq O^X$ be an $O$-subalgebra. If $T$ is a local ring, then every $f\in T$ has constant image in the residue field of $O$: $$f(x)\bmod\mathfrak m_O=f(y)\bmod\mathfrak m_O\qquad(x,y\in X).$$
