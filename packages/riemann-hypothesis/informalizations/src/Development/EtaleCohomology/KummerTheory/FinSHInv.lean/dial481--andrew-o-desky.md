---
{
  "module": "src/Development/EtaleCohomology/KummerTheory/FinSHInv.lean",
  "declarations": [
    "LateralTheory.Fin.SHInv.etale_sheaf_sections_over_strict_henselization_in_henselization_invari"
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

## A section of a surjective etale map over a strictly henselian ring

[Theorem AG.0900](https://andrewodesky.com/rh/lean/LateralTheory.Fin.SHInv.etale_sheaf_sections_over_strict_henselization_in_henselization_invari/)

Let $A$ be a Henselian local commutative ring with separably closed residue field. Every surjective etale morphism $f:Y\to\operatorname{Spec}A$ has a section: there is $s:\operatorname{Spec}A\to Y$ with $f\circ s=\operatorname{id}$.
