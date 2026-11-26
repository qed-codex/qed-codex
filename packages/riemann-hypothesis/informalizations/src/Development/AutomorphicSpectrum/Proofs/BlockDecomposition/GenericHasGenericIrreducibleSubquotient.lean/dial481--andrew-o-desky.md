---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/GenericHasGenericIrreducibleSubquotient.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.GenExists.exists_generic_subQuot"
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

## A generic irreducible subquotient of a finite-length representation

[Theorem REP.0515](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.GenExists.exists_generic_subQuot/)

Let $k$ be a nonarchimedean local field, $N\ge0$, and $\psi:k\to S^1$ a continuous additive character. Let $\rho$ be a smooth complex representation of $\operatorname{GL}_N(k)$ of finite length. Let $U$ be the upper unitriangular subgroup and define $$\psi_U(u)=\psi\left(\sum_{i=1}^{N-1}u_{i,i+1}\right).$$ If the twisted coinvariant space $$\rho_{U,\psi_U}=V/\langle\rho(u)v-\psi_U(u)v:u\in U,\ v\in V\rangle$$ is nonzero, then there are invariant subspaces $B\subseteq A\subseteq V$ such that $A/B$ is smooth and irreducible and $(A/B)_{U,\psi_U}\ne0$.
