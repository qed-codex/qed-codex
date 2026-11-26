---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ModuliProofs/ExistsFinsetIsProjOverDescendsStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_finset_isProjOver_descends_to_subfield"
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

## Projective schemes descend using finitely many field elements

[Theorem AG.1089](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_finset_isProjOver_descends_to_subfield/)

Let $K$ be a field, $K_0\subseteq K$ a subfield, and $X/K$ a projective scheme. There is a finite subset $s\subset K$ such that for every intermediate field $K_0\subseteq K_1\subseteq K$ containing $s$, there is a projective scheme $X_1/K_1$ and a cartesian square identifying $$X\simeq X_1\times_{\operatorname{Spec}K_1}\operatorname{Spec}K.$$
