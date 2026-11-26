---
{
  "module": "src/ReciprocityTheory/ReductiveGroups/DiscreteSeries/MultiplicityOne/JDicho.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.DS.Mult1.schurDichotomy"
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

## A transpose dichotomy for square-integrable coefficients

[Theorem REP.0538](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.DS.Mult1.schurDichotomy/)

Let $G$ be a topological group with its Borel measurable structure, and let $\mu$ be a left-invariant, inversion-invariant measure positive on every nonempty open set. Let $H\ne0$ be a complex Hilbert space and $\rho$ an irreducible unitary representation with continuous orbit maps and all matrix coefficients in $L^2(G,\mu)$. Let $\theta:G\to G$ be a continuous, measure-preserving involution satisfying $\theta(ab)=\theta(b)\theta(a)$. Then either $$\int_G\langle y,\rho(\theta(g))x\rangle\,\overline{\langle y',\rho(g)x'\rangle}\,d\mu(g)=0\qquad(x,y,x',y'\in H),$$ or there is a conjugate-linear surjective isometry $C:H\to H$ such that $$\langle y,\rho(\theta(g))x\rangle=\langle Cx,\rho(g)Cy\rangle,\qquad C\rho(h)=\rho(\theta(h))^{-1}C.$$
