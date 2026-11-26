---
{
  "module": "src/Development/AutomorphicSpectrum/PublishedTheorems/Algebra₂/QuotientByFiniteFlatStatement.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.Ar.GR.QuotientByFiniteFlatStatement"
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

## An affine finite-flat quotient hypothesis for abelian schemes

[Definition / hypothesis AV.D004](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.GR.QuotientByFiniteFlatStatement/)

The following hypothesis concerns the abelian schemes of ([Abelian and semiabelian group schemes](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Semi.IsAbelianScheme/)) and relative ampleness as defined in ([Relative ampleness by affine section charts](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Out.RelAmple/)).

For every commutative ring $R$, every abelian scheme $A\to\operatorname{Spec}R$ with a relatively ample line bundle $L$, every commutative $R$-algebra $B$ that is finitely generated and projective as an $R$-module, and every morphism $$h:\operatorname{Spec}B\longrightarrow A$$ over $R$, suppose the following holds. For every commutative $R$-algebra $S$, the map $$h_S:\operatorname{Hom}_{R\text{-alg}}(B,S)\longrightarrow A(S),\qquad \varphi\longmapsto h\circ\operatorname{Spec}\varphi$$ is injective and its image is a subgroup of $A(S)$.

Then there exist an abelian scheme $A'\to\operatorname{Spec}R$, a relatively ample line bundle $L'$ on $A'$, and a group homomorphism $q:A\to A'$ that is finite, flat and surjective, such that for every commutative $R$-algebra $S$ and every $z\in A(S)$, $$q_S(z)=e_{A'}\quad\Longleftrightarrow\quad z=h_S(\varphi)\text{ for some }\varphi\in\operatorname{Hom}_{R\text{-alg}}(B,S).$$ Here $e_{A'}$ denotes the identity point of $A'(S)$.
