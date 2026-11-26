---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/KleimanAmpleness/CohMkEqZero.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.Kleiman.SectionsOverLocalization.EulerSES.full"
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

## Additivity of a truncated Euler characteristic

[Theorem ALG.0305](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.Kleiman.SectionsOverLocalization.EulerSES.full/)

Let $F$ be a field and $$0\longrightarrow A^\bullet\xrightarrow{f}B^\bullet\xrightarrow{g}C^\bullet\longrightarrow0$$ a degreewise short exact sequence of cochain complexes of $F$-vector spaces in nonnegative degrees. Assume every cohomology space of each complex is finite-dimensional. If $N\ge0$ and $H^{N+1}(A^\bullet)=0$, then $$\sum_{n=0}^{N}(-1)^n\dim_FH^n(B^\bullet)=\sum_{n=0}^{N}(-1)^n\dim_FH^n(A^\bullet)+\sum_{n=0}^{N}(-1)^n\dim_FH^n(C^\bullet).$$
