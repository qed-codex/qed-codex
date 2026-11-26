---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/InertiaQuadraticRamification/MainUnr.lean",
  "declarations": [
    "UpperTheory.Gal.UnramifiedFromSplittingCriterion.unrSplit_holds"
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

## An abelian CM extension with prescribed residue degree

[Theorem ANT.1338](https://andrewodesky.com/rh/lean/UpperTheory.Gal.UnramifiedFromSplittingCriterion.unrSplit_holds/)

Let $E$ be a CM field, $\Omega$ an algebraic closure of $E$, $w$ a finite place of $E$ split over $E^+$, $f\ge1$, and $S$ a finite set of finite places of $E$. There is a CM number field $K\subseteq\Omega$, abelian over $E$, obtainable by a finite tower of prime-degree Galois extensions with the auxiliary ramification outside $S$ specified in the conventions, with these properties:

For every valuation ring of $\Omega$ over $w$, its inertia subgroup over $E$ fixes $K$, and every place $w'$ of $K$ beneath that valuation ring satisfies $$Nw'=(Nw)^f.$$ At every finite place $u$ of $E$ that is not split over $E^+$, every inertia subgroup over $u$ also fixes $K$.
