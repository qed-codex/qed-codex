---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/IsProjOverOfIsProjOverBase.lean",
  "declarations": [
    "GlobalTheory.ProperFinite.relAmple_of_geometricFibres"
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

## Relative ampleness from geometric fibres

[Theorem AG.0640](https://andrewodesky.com/rh/lean/GlobalTheory.ProperFinite.relAmple_of_geometricFibres/)

Let $S$ be a locally noetherian scheme, let $f:X\to S$ be proper and flat, and let $L$ be a line bundle on $X$. Suppose that, for every algebraically closed field $K$ and every $y:\operatorname{Spec}K\to S$, the restriction of $L$ to $X\times_S\operatorname{Spec}K$ is ample. Then $L$ is relatively ample over $S$.
