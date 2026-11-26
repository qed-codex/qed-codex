---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/VacuumFockOfThetaSquareIntegrable.lean",
  "declarations": [
    "GlobalTheory.VacuumFockLaws.fock_of_ccr"
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

## A factorial coefficient identity from creation and annihilation operators

[Theorem REP.0266](https://andrewodesky.com/rh/lean/GlobalTheory.VacuumFockLaws.fock_of_ccr/)

Let $I,X$ be sets and $M\subseteq\mathbb C^X$ a complex vector subspace. For each $i\in I$, let $A_i:\mathbb C^X\to\mathbb C^X$ be a map whose restriction to $M$ is a linear endomorphism $a_i$ of $M$. Let $b_i$ be linear endomorphisms of $M$ satisfying $$a_i a_j=a_j a_i,\qquad b_i a_j-a_j b_i=\delta_{ij}\operatorname{id}_M.$$ Choose $f\in M$ with $b_i f=0$ for every $i$. For every polynomial $P\in\mathbb C[T_i:i\in I]$, the function $P(A)f$ belongs to $M$.

Let $B:\mathbb C^X\times\mathbb C^X\to\mathbb C$ be any map whose restriction to $M\times M$ is additive and complex-linear in the first argument, and suppose $$B(x,0)=0\quad(x\in\mathbb C^X),\qquad B(a_i x,y)=B(x,b_i y),\qquad B(x,a_i y)=B(b_i x,y)\quad(x,y\in M).$$ For every finitely supported $\beta:I\to\mathbb N$ and every $P$, $$B(P(A)f,A^\beta f)=[T^\beta]P\left(\prod_i\beta_i!\right)B(f,f).$$
