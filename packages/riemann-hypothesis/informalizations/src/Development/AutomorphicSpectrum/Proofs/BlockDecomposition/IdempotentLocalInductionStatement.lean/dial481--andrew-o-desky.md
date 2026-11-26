---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/IdempotentLocalInductionStatement.lean",
  "declarations": [
    "GlobalTheory.T.idempotent_local_induction"
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

## A local-to-global principle for properties of idempotents

[Theorem ALG.0208](https://andrewodesky.com/rh/lean/GlobalTheory.T.idempotent_local_induction/)

Let $S$ be a commutative ring and $Q$ a property of its elements. Assume $Q(0)$ and the following conditions:

1. If $e,e'$ are idempotents and $Q(e)$ holds, then $Q(ee')$ holds.
2. If $e,e'$ are idempotents with $ee'=0$ and both $Q(e),Q(e')$ hold, then $Q(e+e')$ holds.
3. For every maximal ideal $\mathfrak m$ there is an idempotent $e\notin\mathfrak m$ satisfying $Q(e)$.

Then $Q(1)$ holds.
