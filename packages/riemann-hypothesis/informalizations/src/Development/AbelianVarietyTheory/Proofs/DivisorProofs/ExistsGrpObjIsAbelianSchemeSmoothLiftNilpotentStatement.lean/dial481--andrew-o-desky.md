---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsGrpObjIsAbelianSchemeSmoothLiftNilpotentStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_grpObj_isAbelianScheme_smoothLift_nilpotent"
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

## An abelian group structure on a smooth nilpotent lift

[Theorem AV.0524](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_grpObj_isAbelianScheme_smoothLift_nilpotent/)

Let $R\twoheadrightarrow R_0$ be a surjective map of commutative rings with nilpotent kernel. Let $A_0/R_0$ be an abelian scheme and $X/R$ a smooth scheme with a specified identification $X\times_R R_0\simeq A_0$. Suppose the identity section of $A_0$ lifts to a section $e:\operatorname{Spec}R\to X$, and its multiplication lifts to an $R$-morphism $$m:X\times_R X\to X.$$ Then $X$ admits a group-scheme structure making it an abelian scheme over $R$ and making the specified identification with $A_0$ an isomorphism of group schemes.
