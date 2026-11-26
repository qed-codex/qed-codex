---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/GrothendieckMessingLiftHomomorphismOfSquareZeroStatement.lean",
  "declarations": [
    "GlobalTheory.T.grothendieckMessingLiftHomomorphism_of_squareZero"
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

## Lifting homomorphisms through a square-zero quotient

[Theorem AV.1481](https://andrewodesky.com/rh/lean/GlobalTheory.T.grothendieckMessingLiftHomomorphism_of_squareZero/)

Assume the source's abelian de Rham comparison package. Let $R\twoheadrightarrow R_0$ be a surjective map of commutative rings with kernel $I$ and $I^2=0$, and assume the source's classification of smooth lifts at this quotient by admissible Hodge submodules. Equip $I$ with the divided powers equal to the identity in degree one and zero in degrees at least two.

Let $A,B$ be abelian schemes over $R$, smooth of constant relative dimensions $g,g'\ge0$, with specified special fibres $A_0,B_0$ and their pullback identifications. For a group homomorphism $f_0:A_0\to B_0$, suppose the induced map on the source's crystalline realization carries the lifted Hodge filtration for $A$ into that for $B$. There is a unique group homomorphism $f:A\to B$ whose reduction is $f_0$.
