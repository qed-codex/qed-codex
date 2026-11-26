---
{
  "module": "src/Development/WeilBound/CoreStatements/AutomorphicKernels/LocalLanglandsExistence/LanglandsDataDualGLOfCosocle.lean",
  "declarations": [
    "PositivityTheory.Pf1.LocalLanglands.LDual.lExists_of_cosocle"
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

## Existence of a quotient attached to a multisegment

[Theorem REP.1349](https://andrewodesky.com/rh/lean/PositivityTheory.Pf1.LocalLanglands.LDual.lExists_of_cosocle/)

Assume the following standard-module quotient statement: over every nonarchimedean local field $k$ of characteristic zero, whenever a finite multiset of cuspidal segments has been ordered so that no earlier segment precedes a later one, and irreducible quotient representations for the individual segments have been chosen, their normalized parabolic product has an irreducible cosocle.

Then, for every such $k$ and every finite multiset $\mathfrak m$ of segments, there exist an ordering $\Delta_1,\ldots,\Delta_h$ of $\mathfrak m$, irreducible representations $\sigma_i$ attached as cosocles to the individual segment products, and an irreducible representation $\pi$ which is the cosocle of their normalized parabolic product. The ordering can be chosen with no $\Delta_i$ preceding $\Delta_j$ when $i<j$.

A segment is a finite nonempty sequence $\rho,\rho\nu,\ldots,\rho\nu^{d-1}$ for a positive-rank cuspidal representation $\rho$, where $\nu=|\det|_k$; the ambient rank of each product is the sum of the ranks of its factors. Two segments are linked if their union is a segment and neither contains the other; the first precedes the second if they are linked and the first term of the second is a positive integral $\nu$-twist of the first term of the first.
