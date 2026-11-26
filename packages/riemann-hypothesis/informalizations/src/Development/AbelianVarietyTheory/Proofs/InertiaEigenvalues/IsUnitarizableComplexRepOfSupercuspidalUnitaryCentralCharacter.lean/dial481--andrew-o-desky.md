---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/IsUnitarizableComplexRepOfSupercuspidalUnitaryCentralCharacter.lean",
  "declarations": [
    "GlobalTheory.isUnitarisable_of_isSupercuspidal"
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

## Unitarisability with a unitary central action

[Theorem REP.1639](https://andrewodesky.com/rh/lean/GlobalTheory.isUnitarisable_of_isSupercuspidal/)

Let $G$ be a topological group and $\rho$ an irreducible representation on a complex vector space $V$. Assume $\rho$ is smooth and every coefficient $g\mapsto\lambda(\rho(g)v)$, with $v\in V$ and $\lambda$ a smooth vector in the dual representation, has support contained in $Z(G)C$ for some compact $C\subseteq G$. Suppose a nonzero such smooth dual vector exists and, for each $z\in Z(G)$, there is $c_z\in\mathbb C$ with $|c_z|=1$ and $$\rho(z)v=c_zv\qquad(v\in V).$$ Then $V$ admits a positive-definite Hermitian form $B$ satisfying $$B(\rho(g)v,\rho(g)w)=B(v,w)\qquad(g\in G;\ v,w\in V).$$
