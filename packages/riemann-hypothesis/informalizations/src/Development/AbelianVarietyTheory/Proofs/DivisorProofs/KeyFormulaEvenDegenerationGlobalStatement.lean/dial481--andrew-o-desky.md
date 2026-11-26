---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/KeyFormulaEvenDegenerationGlobalStatement.lean",
  "declarations": [
    "GlobalTheory.T.keyFormula_evenDegeneration_global"
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

## An eighth-power theta relation in a semiabelian family

[Theorem AV.1307](https://andrewodesky.com/rh/lean/GlobalTheory.T.keyFormula_evenDegeneration_global/)

Let $S$ be an integral normal scheme locally of finite type over $\operatorname{Spec}\mathbb Z$, and assume its ring of global sections has characteristic zero. Let $G/S$ be a smooth semiabelian group scheme of constant relative dimension $g\ge1$, with nonempty open abelian locus $U\subset S$. Let $L$ be a symmetric line bundle on $G$ rigidified at the identity, and let $\delta$ be a line bundle on $S$. Assume $L$ restricts to a relatively ample line bundle with trivial translation kernel on every open subscheme of $U$.

Assume also the source's polarized degeneration-uniformization condition along traits: for every map $\operatorname{Spec}V\to S$ from a complete discrete valuation domain of characteristic zero with finite residue field which meets $U$, the pullback of $G,L$ admits its prescribed polarized uniformization. If $L\otimes\pi^*\delta$ has a global section nonzero somewhere on each fiber of $\pi:G\to S$, then $$\delta^{\otimes8}\simeq\left(\det(e^*\Omega^1_{G/S})\right)^{\otimes4},$$ where $e:S\to G$ is the identity section.
