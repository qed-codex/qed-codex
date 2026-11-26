---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/HasSumCuspidalMultiplicityTrace.lean",
  "declarations": [
    "GlobalTheory.CuspTraceSum.hasSum_trace_restrict"
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

## Trace decomposition over a Hilbert direct sum

[Theorem REP.0975](https://andrewodesky.com/rh/lean/GlobalTheory.CuspTraceSum.hasSum_trace_restrict/)

Let $\mathscr H$ be a complex Hilbert space and $(W_i)_{i\in I}$ a family of complete linear subspaces whose inclusions give a Hilbert direct-sum decomposition of $\mathscr H$. Let $T:\mathscr H\to\mathscr H$ be a bounded trace-class operator preserving every $W_i$. Then every restriction $T_i=T|_{W_i}$ is trace class, $$\sum_{i\in I}|\operatorname{tr}T_i|<\infty,\qquad \operatorname{tr}T=\sum_{i\in I}\operatorname{tr}T_i.$$
