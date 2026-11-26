---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/UniformizationSplitFormalGroupLawEquivariant.lean",
  "declarations": [
    "GlobalTheory.unif_extSer_equivariant"
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

## Equivariant formal extension with an integral matrix action

[Theorem AV.1169](https://andrewodesky.com/rh/lean/GlobalTheory.unif_extSer_equivariant/)

Let $R$ be a commutative domain, complete for an ideal $I$. Assume the source's polarized degeneration and uniformization data: a degeneration $\mathcal D$ with abelian part $B$ and character module $\mathsf X$, a polarized abelian variety $A$ over $\operatorname{Frac}(R)$, a commutative group scheme $G/R$, and a uniformization $\mathcal U$ of $G$ by these data. Let $F,F_B$ be commutative formal group laws of dimensions $d,g$, with nilpotent-point charts for $G,B$, respectively.

There exist $r\ge0$ and formal homomorphisms $$\widehat{\mathbb G}_m^{\,r}\xrightarrow{J}F\xrightarrow{Q}F_B$$ with zero constant terms, whose linear terms form a split exact sequence $$0\longrightarrow R^r\xrightarrow{J_1}R^d\xrightarrow{Q_1}R^g\longrightarrow0.$$ Here a nilpotent-point chart is natural and injective on nilpotent tuples, carries zero to the identity and the formal group law to the group operation, and parametrizes identity kernels over split nilpotent quotient algebras.

Moreover, let $\mathcal O$ be any commutative ring with involution acting on $\mathsf X$, and choose ring actions on $G,\mathcal D,A$ for which $\mathcal U$ is $\mathcal O$-linear. If $\alpha(a),\alpha_B(a)$ are zero-constant-term power series representing these actions in the two charts, there exists a ring homomorphism $N:\mathcal O\to M_r(\mathbb Z)$ such that, for every $a\in\mathcal O$, $$Q_1\alpha_1(a)=\alpha_{B,1}(a)Q_1,\qquad \alpha_1(a)J_1=J_1N(a),$$ where integer matrix entries are mapped to $R$ and the subscript $1$ denotes the linear term.
