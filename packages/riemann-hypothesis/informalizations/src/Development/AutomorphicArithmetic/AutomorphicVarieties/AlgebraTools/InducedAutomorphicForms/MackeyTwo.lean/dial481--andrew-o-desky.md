---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/AlgebraTools/InducedAutomorphicForms/MackeyTwo.lean",
  "declarations": [
    "UpperTheory.V.AlgebraTools.mackeyTwo"
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

## An irreducibility criterion for a subgroup of index two

[Theorem REP.0250](https://andrewodesky.com/rh/lean/UpperTheory.V.AlgebraTools.mackeyTwo/)

Let $k$ be a field, $G$ a group, $\rho:G\to\operatorname{GL}_k(V)$ a representation, and $H\subset G$ a subgroup of index two. Choose $s\in G\setminus H$ and an $H$-stable subspace $V_1\subseteq V$. Suppose the only $H$-stable subspaces of $V_1$ are $0$ and $V_1$, and $$V=V_1\oplus\rho(s)V_1.$$ If there is no $H$-equivariant linear isomorphism $V_1\simeq\rho(s)V_1$, then every $G$-stable subspace of $V$ is either $0$ or $V$.
