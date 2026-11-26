---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/BesselModels/IrreducibleUnitaryRepIsoHarishChandraType.lean",
  "declarations": [
    "UpperTheory.Lit.Bur.irreducible_unitary_rep_iso_harishChandraType"
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

## Highest weight of an irreducible finite-dimensional unitary representation

[Theorem REP.1128](https://andrewodesky.com/rh/lean/UpperTheory.Lit.Bur.irreducible_unitary_rep_iso_harishChandraType/)

Let $k\ge0$ and let $W$ be a nonzero finite-dimensional complex inner product space. Let $\rho$ be a strongly continuous unitary representation of $U(k)$, and suppose every $\rho$-invariant complex subspace is either $0$ or $W$. There are a nonzero finite-dimensional complex inner product space $W'$, a strongly continuous unitary representation $\rho'$ on $W'$, a complex linear isomorphism $T:W\to W'$, and $u\in\mathbb R^k$ such that $$T\rho(h)=\rho'(h)T\qquad(h\in U(k)),$$ and $W'$ is an irreducible compact type of highest weight $\lambda=u-\rho_c$, where $\rho_c=\tfrac12\sum_{i<j}(e_i-e_j)$. Explicitly, some nonzero vector has diagonal character $\operatorname{diag}(e^{i\theta_j})\mapsto e^{i\sum_j\lambda_j\theta_j}$, and every diagonal weight $\mu$ of a nonzero vector satisfies $$\lambda-\mu=\sum_{i<j}c_{ij}(e_i-e_j),\qquad c_{ij}\in\mathbb N.$$
