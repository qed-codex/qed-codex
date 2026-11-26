---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/TorsionBoundsChains/Subquot.lean",
  "declarations": [
    "UpperTheory.V.KH.subquot"
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

## Cardinality of a torsion quotient of a subgroup of a free abelian group

[Theorem ALG.0748](https://andrewodesky.com/rh/lean/UpperTheory.V.KH.subquot/)

Let $I$ be a finite set and let $Z,H$ be abelian groups. Suppose there are homomorphisms $$i:Z\hookrightarrow\bigoplus_{a\in I}\mathbb Z,\qquad q:Z\twoheadrightarrow H.$$ If $n\ge1$ and $nh=0$ for every $h\in H$, then $H$ is finite and $$|H|\le n^{|I|}.$$
