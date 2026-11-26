---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/SphericalContragredientMonomial.lean",
  "declarations": [
    "GlobalTheory.WeakTheRep.eq_of_mono0_charPol"
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

## Weil characteristic polynomials determine a zero-monodromy parameter

[Theorem REP.0164](https://andrewodesky.com/rh/lean/GlobalTheory.WeakTheRep.eq_of_mono0_charPol/)

Let $E$ be a number field, $v$ a finite place, and fix an algebraic closure of $E$ and a place above $v$. Let $x,y$ be Weil–Deligne parameters in the source's class of parameters for $E_v$. If $N_x=N_y=0$ and $$\det(T-x(g))=\det(T-y(g))\qquad(g\in W_{E_v}),$$ then $x=y$ as equivalence classes of Weil–Deligne representations.
