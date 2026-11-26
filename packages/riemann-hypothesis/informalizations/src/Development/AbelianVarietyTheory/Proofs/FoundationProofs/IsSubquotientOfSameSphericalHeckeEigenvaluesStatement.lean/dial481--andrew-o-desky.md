---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/IsSubquotientOfSameSphericalHeckeEigenvaluesStatement.lean",
  "declarations": [
    "GlobalTheory.T.isSubquotient_of_same_spherical_hecke_eigenvalues"
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

## Common spherical Hecke eigenvalues give a subquotient

[Theorem REP.0490](https://andrewodesky.com/rh/lean/GlobalTheory.T.isSubquotient_of_same_spherical_hecke_eigenvalues/)

Let $G$ be a topological group and let $K\subseteq G$ be a compact commensurated subgroup. Let $\pi$ and $\rho$ be complex representations, with $\pi$ smooth and irreducible and $\rho$ smooth. Suppose there are nonzero vectors $x\in\pi^K$, $y\in\rho^K$ such that for every element $h$ of the Hecke algebra of $K$ there is $c_h\in\mathbb C$ with $$\pi(h)x=c_hx,\qquad\rho(h)y=c_hy.$$ Then $\pi$ is a quotient of a $G$-stable subspace of $\rho$.
