---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ModuliProofs/SmoothGrpSchemeDescendsToFgSubring.lean",
  "declarations": [
    "GlobalTheory.smooth_grpScheme_descends_to_fg_subring"
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

## Descent of a smooth commutative group scheme

[Theorem AG.0488](https://andrewodesky.com/rh/lean/GlobalTheory.smooth_grpScheme_descends_to_fg_subring/)

Let $V$ be a commutative ring, let $G\to\operatorname{Spec}V$ be a smooth, separated, quasi-compact commutative group scheme, and let $F\subset V$ be finite. There are a subring $R\subseteq V$ containing $F$, finitely generated as a $\mathbb Z$-algebra, a smooth, separated, quasi-compact commutative group scheme $G_0\to\operatorname{Spec}R$, and an isomorphism of group schemes $$G\simeq G_0\times_{\operatorname{Spec}R}\operatorname{Spec}V.$$ The isomorphism identifies the structure maps and group laws.
