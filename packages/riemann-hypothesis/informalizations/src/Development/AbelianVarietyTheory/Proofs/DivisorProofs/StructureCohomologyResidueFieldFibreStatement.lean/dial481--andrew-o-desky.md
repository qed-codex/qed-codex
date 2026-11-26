---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/StructureCohomologyResidueFieldFibreStatement.lean",
  "declarations": [
    "GlobalTheory.T.structure_cohomology_residue_field_fibre"
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

## Finite projective structure cohomology from residue-fibre surjectivity

[Theorem AG.0411](https://andrewodesky.com/rh/lean/GlobalTheory.T.structure_cohomology_residue_field_fibre/)

Let $R$ be noetherian and $s:X\to\operatorname{Spec}R$ proper and flat. Assume that after every commutative $R$-algebra base change $R'$, the map $R'\to H^0(X_{R'},\mathcal O)$ is an isomorphism. Suppose that for every artinian local $R$-algebra $A$, every field $k$ with an $R$-algebra structure, and every surjective $R$-algebra map $A\to k$, both maps $$H^i(X_A,\mathcal O)\longrightarrow H^i(X_k,\mathcal O),\qquad i=1,2,$$ are surjective. Then $H^1(X,\mathcal O)$ and $H^2(X,\mathcal O)$ are finite projective $R$-modules, and for every commutative $R$-algebra $R'$ there are $R'$-linear isomorphisms $$R'\otimes_R H^i(X,\mathcal O)\simeq H^i(X_{R'},\mathcal O),\qquad i=1,2,$$ sending $1\otimes c$ to the pullback of $c$.
