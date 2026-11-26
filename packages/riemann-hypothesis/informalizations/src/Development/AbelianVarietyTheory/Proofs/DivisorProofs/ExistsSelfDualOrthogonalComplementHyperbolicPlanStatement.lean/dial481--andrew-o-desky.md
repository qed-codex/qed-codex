---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsSelfDualOrthogonalComplementHyperbolicPlanStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_selfDual_orthogonalComplement_hyperbolicPlane"
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

## A self-dual orthogonal complement to a given hyperbolic plane

[Theorem ALG.0222](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_selfDual_orthogonalComplement_hyperbolicPlane/)

Choose an arithmetic datum satisfying ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)), with CM field $E$. Let $S$ be a Hermitian space with recorded lattice data in the generic definition of ([Hermitian spaces in the theta constructions](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.CMData/)) and $\Lambda\subset S$ a full self-dual $\mathcal O_E$-lattice. Let $x,y\in S$ satisfy $$h(x,x)=h(y,y)=0,\qquad h(x,y)=1,$$ and assume that $h(y,z)x$ and $h(x,z)y$ belong to $\Lambda$ for every $z\in\Lambda$.

There are a Hermitian space $S_1$ with recorded lattice data over the same $E$, a full self-dual lattice $\Lambda_1\subset S_1$ and an isometric $E$-linear embedding $\iota:S_1\to S$ such that $$\dim_E S=\dim_E S_1+2,\qquad h(\iota u,x)=h(\iota u,y)=0,\qquad\iota^{-1}(\Lambda)=\Lambda_1.$$ Every $z\in\Lambda$ has an expression $$z=ax+\iota(u)+by,\qquad ax,by\in\Lambda,\quad u\in\Lambda_1.$$ The auxiliary signature-label function attached to $S_1$ can be any prescribed function $s:\operatorname{Hom}(E,\mathbb C)\to\mathbb N^2$.
