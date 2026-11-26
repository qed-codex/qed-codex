---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/StructureSheafCohomologyAbelianVarietyAlgClosed.lean",
  "declarations": [
    "GlobalTheory.AbCoh.structureSheafCoh_abelianVariety_algClosed"
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

## Structure-sheaf cohomology and primitive classes of an abelian variety

[Theorem AV.0544](https://andrewodesky.com/rh/lean/GlobalTheory.AbCoh.structureSheafCoh_abelianVariety_algClosed/)

Let $K$ be algebraically closed and let $A/K$ be an abelian variety of dimension $g\ge0$. Then $H^1(A,\mathcal O_A)$ is finite-dimensional of dimension $g$, and cup product induces an isomorphism $$\bigwedge_K^2H^1(A,\mathcal O_A)\simeq H^2(A,\mathcal O_A).$$ Let $m:A\times A\to A$ be the group law and $p_1,p_2$ the projections. If $z\in H^2(A,\mathcal O_A)$ satisfies $$m^*z=p_1^*z+p_2^*z,$$ then $z=0$. If $y\in H^1(A\times A,\mathcal O_{A\times A})$ restricts to zero on both $A\times\{0\}$ and $\{0\}\times A$, then $y=0$.
