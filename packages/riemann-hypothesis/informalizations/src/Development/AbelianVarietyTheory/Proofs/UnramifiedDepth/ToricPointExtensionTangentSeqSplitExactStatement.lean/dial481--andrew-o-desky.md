---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/ToricPointExtensionTangentSeqSplitExactStatement.lean",
  "declarations": [
    "GlobalTheory.T.toricPointExtension_tangentSeq_splitExact"
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

## Split exactness of the tangent sequence of a torus extension

[Theorem AV.0228](https://andrewodesky.com/rh/lean/GlobalTheory.T.toricPointExtension_tangentSeq_splitExact/)

Let $R$ be a commutative ring complete and separated for an ideal $I$, and let $G,B$ be commutative group schemes over $R$. Let $X$ be a free abelian group with basis $\beta_1,\ldots,\beta_r$. Assume a torus-extension package on the $R$-algebras killed by a power of $I$, as specified below.

Choose formal group laws of dimensions $d,g$ and nilpotent coordinate charts for $G,B$. Let $J\in R[[T_1,\ldots,T_r]]^d$ and $Q\in R[[Z_1,\ldots,Z_d]]^g$ have zero constant terms. Suppose $Q$ represents the map $G\to B$ on nilpotent coordinates over every such algebra, and $J$ represents the torus inclusion when its character $\beta_j$ takes the value $1+T_j$. Then, writing $A=dJ(0)$ and $D=dQ(0)$, there are matrices $A',D'$ with $$DA=0,\qquad A'A=1,\qquad DD'=1,\qquad AA'+D'D=1.$$
