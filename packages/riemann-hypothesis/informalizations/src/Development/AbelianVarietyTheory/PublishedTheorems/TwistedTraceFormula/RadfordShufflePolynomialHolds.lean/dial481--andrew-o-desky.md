---
{
  "module": "src/Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/RadfordShufflePolynomialHolds.lean",
  "declarations": [
    "GlobalTheory.Lyndon.aeval_injective",
    "GlobalTheory.Lyndon.aeval_surjective"
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

## Lyndon words generate the shuffle algebra

[Theorem ALG.1656](https://andrewodesky.com/rh/lean/GlobalTheory.Lyndon.aeval_surjective/)

Let $K$ be a field of characteristic zero and let $A$ be a linearly ordered alphabet. The shuffle algebra $\operatorname{Sh}_K(A)$ is the free $K$-vector space on finite words in $A$, with multiplication given by the sum of all order-preserving interleavings, counted with multiplicity. A Lyndon word is a nonempty word lexicographically smaller than each of its nonempty proper suffixes. The algebra homomorphism $$K[X_\ell:\ell\text{ a Lyndon word in }A]\longrightarrow\operatorname{Sh}_K(A), \qquad X_\ell\longmapsto\ell,$$ is surjective.

## Algebraic independence of Lyndon words

[Theorem ALG.1720](https://andrewodesky.com/rh/lean/GlobalTheory.Lyndon.aeval_injective/)

Let $K$ be a field of characteristic zero and $A$ a linearly ordered alphabet. A Lyndon word is a nonempty finite word strictly smaller in lexicographic order than every nonempty proper suffix. Let $\mathcal L$ be the set of Lyndon words, and let $\operatorname{Sh}_K(A)$ be the $K$-vector space with basis all finite words, with product given by the sum of all order-preserving shuffles, counted with multiplicity.

The algebra homomorphism $$K[T_l\mid l\in\mathcal L]\longrightarrow\operatorname{Sh}_K(A),\qquad T_l\longmapsto l,$$ is injective.
