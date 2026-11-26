---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ChebotarevDegreeOneValuationSubringsStatement.lean",
  "declarations": [
    "GlobalTheory.T.chebotarev_degreeOne_valuationSubrings"
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

## A degree-one prime realizing a Frobenius coset

[Theorem ANT.0870](https://andrewodesky.com/rh/lean/GlobalTheory.T.chebotarev_degreeOne_valuationSubrings/)

Let $E$ be a number field, $\Omega$ an algebraic closure of $E$, and $S$ a finite set of nonzero prime ideals of $\mathcal O_E$. Let $H$ be an open normal subgroup of $G_E=\operatorname{Aut}(\Omega/E)$. Suppose that, for every prime $\mathfrak p\notin S$ and every valuation ring $A\subseteq\Omega$ above $\mathfrak p$, the inertia subgroup at $A$ lies in $H$. For every $\sigma\in G_E$ there are $\mathfrak p\notin S$, a valuation ring $A$ above $\mathfrak p$, and an arithmetic Frobenius element $\phi$ at $(A,\mathfrak p)$ such that $$\#(\mathcal O_E/\mathfrak p)\text{ is prime},\qquad \sigma^{-1}\phi\in H.$$
