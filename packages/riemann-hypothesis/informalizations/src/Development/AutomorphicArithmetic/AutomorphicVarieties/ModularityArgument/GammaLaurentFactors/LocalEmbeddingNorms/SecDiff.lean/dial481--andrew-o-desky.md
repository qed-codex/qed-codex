---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/GammaLaurentFactors/LocalEmbeddingNorms/SecDiff.lean",
  "declarations": [
    "UpperTheory.V.Z.Gam.secDiff"
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

## Uniqueness from a multiplicative polynomial second-difference identity

[Theorem ALG.0343](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.Gam.secDiff/)

Let $q>1$ be real, $P,Q\in\mathbb C[X]$ satisfy $P(0)=Q(0)=1$, and let $c\in\mathbb C$. If $$P(q^{-1}X)P(qX)Q(X)^2=c\,Q(q^{-1}X)Q(qX)P(X)^2$$ as polynomials, then $P=Q$.
