---
{
  "module": "src/CompanionTheory/HarishChandraModules/KFiniteAnalyticVectors/AnalyticIntertwiners/HarishChandraModulesIndefiniteUnitaryGroup.lean",
  "declarations": [
    "CompanionTheory.D.gk.HC.clause1"
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

## Harish–Chandra module of an irreducible unitary representation

[Theorem REP.1715](https://andrewodesky.com/rh/lean/CompanionTheory.D.gk.HC.clause1/)

Let $p,q\ge0$ with $p+q\ge1$. Give the determinant double cover $$\widetilde U(p,q)=\{(g,z):g\in U(p,q),\ z\in\mathbb C^\times,\ z^2=\det g\}$$ the following group data: the subspace topology, Borel structure, a Haar measure, and a continuous exponential lift of the real Lie algebra compatible with one-parameter subgroups. Let $K$ be the preimage of $U(p)\times U(q)$. Let $\pi$ be a strongly continuous unitary representation on a nonzero complex Hilbert space with no nontrivial closed invariant complex subspace.

Every $K$-finite vector is smooth. There is a complex $\mathfrak{gl}_{p+q}$-module $M$ satisfying the compact local-finiteness and rational-weight conditions of ([Globalizing an irreducible graded Lie module inside a unitary representation](https://andrewodesky.com/rh/lean/GlobalTheory.HarmModule.globalize/)) and an injective linear map $j:M\to H_\pi$ with range exactly the $K$-finite vectors, such that $$\left.\frac{d}{dt}\pi(\exp(tX))j(v)\right|_{t=0}=j(Xv)$$ for every real Lie-algebra element $X$ and $v\in M$. Every module with such an embedding is admissible and irreducible.
