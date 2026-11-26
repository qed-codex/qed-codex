---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/ComplexAnalyticSets/PExtensionQuotientLength.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.ExtensionQuotientLength.proof"
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

## Equality of quotient lengths across a finite-length extension

[Theorem ALG.1211](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.ExtensionQuotientLength.proof/)

Let $R,B$ be commutative rings, let $B$ be an $R$-algebra with injective structure map $\iota:R\to B$, and let $r\in R$. Suppose $\iota(r)$ is a non-zero-divisor in $B$ and the $R$-module $B/\iota(R)$ has finite length. Then $$\operatorname{length}_R(R/rR)=\operatorname{length}_R(B/\iota(r)B).$$ The two displayed lengths are allowed to be infinite.
