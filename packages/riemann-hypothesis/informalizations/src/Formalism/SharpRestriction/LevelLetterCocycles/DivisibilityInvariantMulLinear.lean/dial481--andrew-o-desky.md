---
{
  "module": "src/Formalism/SharpRestriction/LevelLetterCocycles/DivisibilityInvariantMulLinear.lean",
  "declarations": [
    "Formalism.MainNotions.ArcLiftingSetup.content_divisibility"
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

## A coefficient obstruction to membership in a power-series ideal

[Theorem PHT.0717](https://andrewodesky.com/rh/lean/Formalism.MainNotions.ArcLiftingSetup.content_divisibility/)

Let $O$ be a discrete valuation domain with uniformizer $\varpi$. Let $\ell$ be prime, $e\ge1$, and $u\in O^\times$ satisfy $\ell=u\varpi^e$ in $O$. Let $f\in O[[X]]$ and $a,A,y,B,v,k\ge0$ satisfy $$\varpi^{ev}\mid f(0),\qquad\varpi^{ev+1}\nmid f(0),\qquad y+A+a+v+1\le B.$$ If $$\ell^a f(X)(X-\ell)^A X^y\in(\varpi^k,X^B)\subseteq O[[X]],$$ then $$k/e<a+v+1.$$
