---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/AbelianSchemeStructureSheafCohomologyNoetherianStatement.lean",
  "declarations": [
    "GlobalTheory.T.abelianScheme_structureSheafCohomology_noetherian"
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

## Structure-sheaf cohomology of an abelian scheme

[Theorem AV.1155](https://andrewodesky.com/rh/lean/GlobalTheory.T.abelianScheme_structureSheafCohomology_noetherian/)

Let $R$ be a commutative Noetherian ring and $A\to\operatorname{Spec}R$ an abelian scheme, smooth of relative dimension $g\ge0$. Then $H^1(A,\mathcal O_A)$ is a finite projective $R$-module of rank $g$ at every prime of $R$, and cup product induces an isomorphism $$\bigwedge_R^2H^1(A,\mathcal O_A)\simeq H^2(A,\mathcal O_A).$$ For every commutative $R$-algebra $R'$ and $A'=A\times_R R'$, pullback induces isomorphisms $$R'\otimes_R H^i(A,\mathcal O_A)\simeq H^i(A',\mathcal O_{A'})\qquad(i=1,2),$$ carrying $1\otimes c$ to the pullback of $c$.
