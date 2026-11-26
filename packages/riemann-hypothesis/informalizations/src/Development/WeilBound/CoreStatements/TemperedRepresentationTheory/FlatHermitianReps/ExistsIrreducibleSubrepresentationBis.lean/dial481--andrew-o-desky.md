---
{
  "module": "src/Development/WeilBound/CoreStatements/TemperedRepresentationTheory/FlatHermitianReps/ExistsIrreducibleSubrepresentationBis.lean",
  "declarations": [
    "MainStatements.Flath2.exists_irred_of_compact",
    "MainStatements.Flath2.exists_irreducible_subrepresentation_bis"
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

## An irreducible subrepresentation from a compact operator product

[Theorem REP.0235](https://andrewodesky.com/rh/lean/MainStatements.Flath2.exists_irreducible_subrepresentation_bis/)

Let $G$ be a group equipped with a topology, let $\mathcal H$ be a complex Hilbert space, and let $\rho:G\to\operatorname{GL}(\mathcal H)$ be a unitary representation such that $g\mapsto\rho(g)v$ is continuous for every $v\in\mathcal H$. Let $a,Q$ be bounded complex-linear operators on $\mathcal H$. Suppose $Q$ commutes with every $\rho(g)$ and $a$ commutes with every bounded operator that commutes with every $\rho(g)$. If $aQ$ is compact and nonzero, there is a nonzero closed $\rho(G)$-invariant subspace having no proper nonzero closed invariant subspace.

## An irreducible subrepresentation detected by a compact operator

[Theorem REP.0236](https://andrewodesky.com/rh/lean/MainStatements.Flath2.exists_irred_of_compact/)

Let $G$ be a group equipped with a topology, $\mathcal H$ a complex Hilbert space, and $\rho:G\to\operatorname{GL}(\mathcal H)$ a unitary representation whose orbit maps $g\mapsto\rho(g)v$ are continuous. Let $W\subseteq\mathcal H$ be a closed invariant subspace, and let $A$ be a nonzero compact complex-linear operator. Suppose $$AP_W=A,$$ and, for every closed invariant subspace $Y\subseteq W$, $$AP_Y=P_YA,$$ where $P_Y$ denotes orthogonal projection. Then $W$ contains a nonzero closed invariant subspace with no proper nonzero closed invariant subspace.
