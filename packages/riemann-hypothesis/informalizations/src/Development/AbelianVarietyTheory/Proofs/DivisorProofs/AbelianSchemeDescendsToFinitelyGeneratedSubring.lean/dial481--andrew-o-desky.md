---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/AbelianSchemeDescendsToFinitelyGeneratedSubring.lean",
  "declarations": [
    "GlobalTheory.AbelianLimit.abelianScheme_descends_to_fg_subring"
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

## Finite type descent preserving finitely many base elements

[Theorem AV.1124](https://andrewodesky.com/rh/lean/GlobalTheory.AbelianLimit.abelianScheme_descends_to_fg_subring/)

Let $R$ be any commutative ring, let $A/R$ be an abelian scheme smooth of constant relative dimension $g\ge0$, and let $F\subset R$ be finite. There are a subring $S\subset R$ containing $F$, finitely generated as a $\mathbb Z$-algebra, and an abelian scheme $B/S$ smooth of constant relative dimension $g$, together with a group-scheme base-change isomorphism $$A\simeq B\times_{\operatorname{Spec}S}\operatorname{Spec}R.$$
