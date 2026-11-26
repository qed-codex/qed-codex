---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/HomologicalStability/KStability.lean",
  "declarations": [
    "PositivityTheory.v8.KStability.kStability"
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

## Homological stability for general linear groups

[Theorem GC.0118](https://andrewodesky.com/rh/lean/PositivityTheory.v8.KStability.kStability/)

Let $R$ be a commutative ring of stable range at most $s$. For integers $i,n\ge0$ with $n\ge2i+s+2$, the standard block inclusion induces an isomorphism $$H_i(\mathrm{GL}_n(R),\mathbb Z)\xrightarrow{\ \sim\ }H_i(\mathrm{GL}_{n+1}(R),\mathbb Z).$$ Stable range at most $s$ means that every unimodular row of length $n+1$ with $n\ge s$ can be shortened to length $n$ by adding multiples of its last entry to the preceding entries.
