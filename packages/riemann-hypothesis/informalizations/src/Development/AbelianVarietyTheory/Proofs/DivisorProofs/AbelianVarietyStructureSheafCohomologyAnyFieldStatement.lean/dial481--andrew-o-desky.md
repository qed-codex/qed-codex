---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/AbelianVarietyStructureSheafCohomologyAnyFieldStatement.lean",
  "declarations": [
    "GlobalTheory.T.abelianVariety_structureSheaf_cohomology_anyField"
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

## Structure-sheaf cohomology and primitive classes over a field

[Theorem AV.0183](https://andrewodesky.com/rh/lean/GlobalTheory.AbCoh.abelian_HO_field_any/)

Let $K$ be any field and $A/K$ an abelian variety of dimension $g\ge0$, with multiplication $\mu:A\times A\to A$, projections $p_1,p_2$, and zero section $0$. Then $$\dim_K H^1(A,\mathcal O_A)=g,\qquad \bigwedge_K^2 H^1(A,\mathcal O_A)\xrightarrow{\ \cup\ }H^2(A,\mathcal O_A)\text{ is an isomorphism}.$$ If $z\in H^2(A,\mathcal O_A)$ satisfies $\mu^*z=p_1^*z+p_2^*z$, then $z=0$. If $y\in H^1(A\times A,\mathcal O_{A\times A})$ restricts to zero along both $a\mapsto(a,0)$ and $a\mapsto(0,a)$, then $y=0$.
