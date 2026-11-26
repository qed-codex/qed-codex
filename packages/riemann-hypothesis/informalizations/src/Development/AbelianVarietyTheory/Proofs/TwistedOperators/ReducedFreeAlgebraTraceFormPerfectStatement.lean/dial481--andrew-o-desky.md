---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/ReducedFreeAlgebraTraceFormPerfectStatement.lean",
  "declarations": [
    "GlobalTheory.T.reduced_free_algebra_traceForm_perfect"
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

## A perfect trace pairing for a reduced finite free algebra

[Theorem ALG.0341](https://andrewodesky.com/rh/lean/GlobalTheory.T.reduced_free_algebra_traceForm_perfect/)

Let $F$ be a field of characteristic zero, $E$ a finite-dimensional commutative $F$-algebra, and $L$ a reduced commutative $E$-algebra finite and free as an $E$-module. Assume the $F$-algebra structure on $L$ is the composite through $E$. Then $$L\longrightarrow\operatorname{Hom}_E(L,E),\qquad x\longmapsto\bigl(y\longmapsto\operatorname{Tr}_{L/E}(xy)\bigr)$$ is bijective.
