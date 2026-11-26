---
{
  "module": "src/Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/IsCompactOperatorOfIsHilbertSchmidt.lean",
  "declarations": [
    "GlobalTheory.DiscreteSum.EnoughCompact.isDiscreteSum"
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

## Compact operators in the double commutant force a discrete sum

[Theorem REP.1490](https://andrewodesky.com/rh/lean/GlobalTheory.DiscreteSum.EnoughCompact.isDiscreteSum/)

Let $G$ be a topological group and $\rho:G\to\mathcal B(H)$ a unitary representation on a complex Hilbert space. Assume that for every $v\ne0$ there is a compact bounded complex-linear operator $A$ with $Av\ne0$ such that $AS=SA$ for every bounded intertwining operator $S:H\to H$ of $\rho$.

Then $H$ is a Hilbert direct sum of irreducible invariant closed subspaces. Every irreducible unitary representation occurs in $\rho$ with finite multiplicity.
