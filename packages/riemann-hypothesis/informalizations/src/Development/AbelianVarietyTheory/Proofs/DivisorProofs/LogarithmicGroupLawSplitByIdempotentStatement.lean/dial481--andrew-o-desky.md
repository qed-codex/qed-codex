---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/LogarithmicGroupLawSplitByIdempotentStatement.lean",
  "declarations": [
    "GlobalTheory.T.logarithmic_group_law_split_by_idempotent"
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

## Splitting an integral formal group by a logarithmic projector

[Theorem PHT.0766](https://andrewodesky.com/rh/lean/GlobalTheory.T.logarithmic_group_law_split_by_idempotent/)

Let $C$ be a field of characteristic zero with an additive valuation $v:C\to\mathbb R\cup\{+\infty\}$, and put $O=\{a:v(a)\ge0\}$. Let $G$ be a $d$-dimensional formal group law over $O$ with a logarithm $\ell_G\in C[[X_1,\ldots,X_d]]^d$ having constant term zero and linear term the identity. Let $I\in M_{d,d'}(O)$ and $P\in M_{d',d}(O)$ satisfy $PI=1$.

Suppose there are integral formal endomorphisms of $G$ whose logarithmic matrices are $IP$ and $1-IP$. Then there is a $d'$-dimensional formal group law $G'$ over $O$, with a normalized logarithm over $C$, and integral formal homomorphisms $j:G'\to G$ and $q:G\to G'$ with logarithmic matrices $I$ and $P$.
