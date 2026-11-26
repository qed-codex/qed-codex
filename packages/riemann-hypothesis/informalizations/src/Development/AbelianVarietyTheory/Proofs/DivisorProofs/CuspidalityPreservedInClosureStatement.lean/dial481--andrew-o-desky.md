---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/CuspidalityPreservedInClosureStatement.lean",
  "declarations": [
    "GlobalTheory.T.cuspidality_preserved_in_closure"
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

## Cuspidality in a closed cyclic automorphic subspace

[Theorem REP.0869](https://andrewodesky.com/rh/lean/GlobalTheory.T.cuspidality_preserved_in_closure/)

Fix the full arithmetic unitary datum in ([The convergent doubling integral identity](https://andrewodesky.com/rh/lean/GlobalTheory.T.doubling_basicIdentity_unfolding/)), compatible archimedean coordinates, and a Hermitian space $V$. Put $G=U(V)(\mathbb A_F)$ and $\Gamma=U(V)(F)$. Let $\mu$ be a left and right invariant Haar measure, and $\mathcal F$ a fundamental domain for $\Gamma\backslash G$ of finite measure. Equip $\Gamma\backslash G$ with the pushforward of $\mu|_{\mathcal F}$. Let $\rho$ be a strongly continuous norm-preserving right regular representation on its $L^2$ space, agreeing almost everywhere with right translation.

Let $\phi,\psi:G\to\mathbb C$ be continuous left $\Gamma$-invariant functions, each fixed on the right by an open subgroup at the finite places, and let $F_0,F$ be their $L^2$ representatives, agreeing almost everywhere with the functions after pullback to $G$. Suppose all the isotropic-line integrals of $\phi$ vanish. If $$F\in\overline{\operatorname{span}_{\mathbb C}\{\rho(g)F_0:g\in G\}},$$ then all the isotropic-line integrals of $\psi$ vanish as well.
