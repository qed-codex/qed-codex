---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/GlobalTwisting/SetUnipotentTranslate.lean",
  "declarations": [
    "GlobalTheory.EX.OB.Obj"
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

## Datum of the construction and objects over it

[Definition / hypothesis THETA.D014](https://andrewodesky.com/rh/lean/GlobalTheory.EX.OB.Obj/)

A *datum* consists of the choices satisfying ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)) and its cited hypotheses.

An *object* $O$ over a datum $D$ consists of *size data* and seven further records of auxiliary choices (not expanded). Size data consist of a *scale*, that is real numbers $x>1$, $0<\varepsilon<\frac1{52}$ and $J\ge1$, together with integers $a_\theta, b_\theta$ indexed by a finite set, subject to $$A\le a_\theta\le A+\frac{A}{k\,x^{13}},\qquad b_\theta\ge \frac{A}{\exp(x^{\varepsilon/3})},\qquad A=x\exp(x^{\varepsilon}),$$ and tied to the weights by $u_1=a_\theta+\frac{k-1}{2}$ and $u_k=-b_\theta-\frac{k-1}{2}$ for the corresponding $\tau$; further fields of the size data have not been expanded.
