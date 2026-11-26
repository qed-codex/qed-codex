---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ArtinMapAbelianUnique.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.ArtinUniq.abRestrict_eq"
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

## Uniqueness of Artin maps on finite abelian extensions

[Theorem ANT.1455](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.ArtinUniq.abRestrict_eq/)

Let $K$ be a totally complex number field and let $A,A':C_K\to G_K^{\mathrm{ab}}$ be homomorphisms from the idele class group satisfying the global Artin-map conditions stated in the conventions. For every finite abelian intermediate extension $K\subseteq L\subseteq\overline K$ and every $c\in C_K$, $$A(c)|_L=A'(c)|_L.$$
