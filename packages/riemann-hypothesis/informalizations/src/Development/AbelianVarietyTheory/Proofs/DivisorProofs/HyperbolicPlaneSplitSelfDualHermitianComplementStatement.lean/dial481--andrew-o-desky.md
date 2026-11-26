---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/HyperbolicPlaneSplitSelfDualHermitianComplementStatement.lean",
  "declarations": [
    "GlobalTheory.T.hyperbolicPlane_split_selfDual_hermitian_complement"
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

## Splitting a hyperbolic plane from a self-dual Hermitian lattice

[Theorem ALG.0820](https://andrewodesky.com/rh/lean/GlobalTheory.T.hyperbolicPlane_split_selfDual_hermitian_complement/)

Choose an arithmetic datum satisfying ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)), with CM field $E$. Let $S$ be a Hermitian space of dimension $m$ with recorded lattice data in the generic definition of ([Hermitian spaces in the theta constructions](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.CMData/)), and let $\Lambda\subset S$ be a full self-dual $\mathcal O_E$-lattice. Let $q\in\mathbb N$. Suppose $q+2\le m$, $3\le m$, and the Gram matrix of $S$ has signature $(m-q-1,q+1)$ at every embedding in the selected CM type of $E$.

There exist a Hermitian space $S_1$ with recorded lattice data over the same $E$, a full self-dual lattice $\Lambda_1\subset S_1$, an isometric $E$-linear embedding $\iota:S_1\to S$, and $x,y\in S$ such that $$\dim S_1=m-2,\quad h(x,x)=h(y,y)=0,\quad h(x,y)=1,\quad h(\iota u,x)=h(\iota u,y)=0,$$ $$\iota^{-1}(\Lambda)=\Lambda_1.$$ Every $z\in\Lambda$ has an expression $$z=ax+\iota(u)+by,\qquad ax,by\in\Lambda,\quad u\in\Lambda_1.$$ The Gram matrix of $S_1$ has signature $(m-2-q,q)$ at every embedding in the selected CM type of $E$, and its signature labels agree with its actual signatures at every complex embedding of $E$.
