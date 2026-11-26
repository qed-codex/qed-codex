---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/PropertyDescendsFiniteLengthToIrreducibleSubquot.lean",
  "declarations": [
    "GlobalTheory.ExactIrr.main"
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

## Extracting an irreducible subquotient with a prescribed property

[Theorem REP.0597](https://andrewodesky.com/rh/lean/GlobalTheory.ExactIrr.main/)

Let $H$ be a group, $\rho$ a complex representation of finite length, and $P$ a property of complex representations of $H$. Suppose:

1. If an injective intertwining map $\sigma\to\sigma'$ exists and $P(\sigma)$ holds, then $P(\sigma')$ holds.
2. Every representation satisfying $P$ is nonzero.
3. For all subrepresentations $B\subseteq A\subseteq\rho$, $P(A)$ implies $P(B)$ or $P(A/B)$.

If $P(\rho)$ holds, there is an irreducible subquotient $\sigma$ of $\rho$ satisfying $P(\sigma)$.
