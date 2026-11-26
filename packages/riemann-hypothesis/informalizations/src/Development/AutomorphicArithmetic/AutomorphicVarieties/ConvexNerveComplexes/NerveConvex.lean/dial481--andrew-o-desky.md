---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ConvexNerveComplexes/NerveConvex.lean",
  "declarations": [
    "UpperTheory.V.ConeExtensionAcyclic.nerve_convex"
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

## Acyclicity of a locally finite convex-cover nerve

[Theorem AG.0547](https://andrewodesky.com/rh/lean/UpperTheory.V.ConeExtensionAcyclic.nerve_convex/)

Let $F$ be a real normed vector space, let $X\subseteq F$ be nonempty and convex, and let $(A_i)_{i\in I}$ be closed convex subsets of $F$ covering $X$. Suppose that for every finite $S\subseteq X$, only finitely many $i$ satisfy $$\operatorname{conv}(S)\cap A_i\ne\varnothing.$$ The augmented integral chain complex of the nerve is exact.
