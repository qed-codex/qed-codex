---
{
  "module": "src/CompanionTheory/AutomorphicTheory/MirabolicRestriction/MirabolicInduction/CuspidalRestrictsToInduced.lean",
  "declarations": [
    "CompanionTheory.Mirab.Restr.finrank_and_whit"
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

## Dimension and a Whittaker functional for a finite cuspidal representation

[Theorem REP.1496](https://andrewodesky.com/rh/lean/CompanionTheory.Mirab.Restr.finrank_and_whit/)

Let $k$ be a finite field of cardinality $q$, $d\ge0$, and $\psi:(k,+)\to\mathbb C^\times$ a nontrivial additive character. Let $\rho$ be an irreducible cuspidal representation of $\mathrm{GL}_d(k)$ on a finite-dimensional complex vector space $V$. Then $$\dim_{\mathbb C}V=\prod_{i=1}^{d-1}(q^i-1).$$ There is a nonzero linear functional $\lambda:V\to\mathbb C$ such that, for every upper unitriangular matrix $u$ and $v\in V$, $$\lambda(\rho(u)v)=\psi\!\left(\sum_{i=1}^{d-1}u_{i,i+1}\right)\lambda(v).$$ Empty products are one and empty sums are zero.
