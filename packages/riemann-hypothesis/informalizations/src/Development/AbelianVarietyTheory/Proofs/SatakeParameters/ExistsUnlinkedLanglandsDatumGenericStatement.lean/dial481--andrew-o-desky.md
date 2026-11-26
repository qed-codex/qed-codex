---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/ExistsUnlinkedLanglandsDatumGenericStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_unlinked_langlandsDatum_generic"
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

## Unlinked segment data for a generic representation

[Theorem REP.1255](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_unlinked_langlandsDatum_generic/)

Let $k$ be a nonarchimedean local field of characteristic zero and $\pi$ a smooth irreducible generic complex representation of a general linear group over $k$. There is a finite family of segments $\Delta_1,\ldots,\Delta_c$ with no linked pair at distinct indices, whose Langlands representation is $\pi$.

A segment consists of a supercuspidal representation and its consecutive twists by powers of $\nu=|\det|_k$. Two segments are linked when their union is a segment and neither contains the other. For each segment take the irreducible cosocle of its ordered induced product; order the segments so that no earlier segment precedes a later one, where precedence means linkage and a positive integral $\nu$-shift of the initial term. The assertion that their Langlands representation is $\pi$ means that $\pi$ is the irreducible cosocle of the induced product of these segment cosocles.
