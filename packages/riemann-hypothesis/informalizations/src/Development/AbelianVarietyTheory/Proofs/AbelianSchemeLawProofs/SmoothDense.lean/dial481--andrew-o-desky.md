---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/AbelianSchemeLawProofs/SmoothDense.lean",
  "declarations": [
    "GlobalTheory.smoothDense"
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

## Density of the smooth locus over an algebraically closed field

[Theorem AG.1465](https://andrewodesky.com/rh/lean/GlobalTheory.smoothDense/)

Let $k$ be an algebraically closed field and let $f:X\to\operatorname{Spec}k$ be locally of finite type, with $X$ reduced. Then $$\overline{\{x\in X:\text{there is an open }U\ni x\text{ with }U\to\operatorname{Spec}k\text{ smooth}\}}=X.$$
