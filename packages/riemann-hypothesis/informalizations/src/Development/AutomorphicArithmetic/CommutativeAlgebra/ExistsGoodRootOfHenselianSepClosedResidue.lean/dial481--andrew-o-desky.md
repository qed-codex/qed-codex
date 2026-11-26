---
{
  "module": "src/Development/AutomorphicArithmetic/CommutativeAlgebra/ExistsGoodRootOfHenselianSepClosedResidue.lean",
  "declarations": [
    "UpperTheory.exists_goodRoot_of_henselian_sepClosed_residue"
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

## Separated roots of unity over a strictly Henselian local ring

[Theorem ALG.0924](https://andrewodesky.com/rh/lean/UpperTheory.exists_goodRoot_of_henselian_sepClosed_residue/)

Let $A$ be a Henselian commutative local ring with separably closed residue field. If $q\ge0$ is an integer whose image in $A$ is a unit, there is $\zeta\in A$ such that $$\zeta^q=1,\qquad\zeta^a-\zeta^b\in A^\times\quad(0\le a,b<q,\ a\ne b).$$ For every homomorphism $\phi:A\to B$ to a commutative ring and every $x\in B$, $$x^q-1=\prod_{a=0}^{q-1}\bigl(x-\phi(\zeta)^a\bigr).$$
