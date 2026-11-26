---
{
  "module": "src/Formalism/WachLatticeTwists/RamifiedBlockRings/RamifiedBlockProofs/KerEqOfFactor.lean",
  "declarations": [
    "Formalism.RepresentationBoundsCohomology.ringDataObjects.kerBc"
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

## Kernel lengths under ramified extension of discrete valuation rings

[Theorem ALG.0818](https://andrewodesky.com/rh/lean/Formalism.RepresentationBoundsCohomology.ringDataObjects.kerBc/)

Let $O\to O'$ be an algebra homomorphism of discrete valuation rings, with fraction fields $K,K'$, and let $e\ge0$. Suppose their normalized additive valuations satisfy $$v_{O'}(a)=e\,v_O(a)\qquad(a\in O),$$ where on the left $a$ denotes its image in $O'$. For finite sets $I,J$ and a matrix $A\in M_{I,J}(O)$, let $$A:(K/O)^J\to(K/O)^I,\qquad A':(K'/O')^J\to(K'/O')^I$$ be the induced linear maps, using the image matrix over $O'$ for $A'$. Then $$\operatorname{length}_{O'}\ker A'=e\,\operatorname{length}_O\ker A.$$
