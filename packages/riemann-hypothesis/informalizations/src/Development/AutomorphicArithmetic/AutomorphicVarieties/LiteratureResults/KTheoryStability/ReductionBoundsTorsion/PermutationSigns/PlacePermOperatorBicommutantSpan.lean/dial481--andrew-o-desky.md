---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/ReductionBoundsTorsion/PermutationSigns/PlacePermOperatorBicommutantSpan.lean",
  "declarations": [
    "PositivityTheory.KB.BlockInvariants.sw1"
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

## The bicommutant of colored permutation matrices

[Theorem ALG.0234](https://andrewodesky.com/rh/lean/PositivityTheory.KB.BlockInvariants.sw1/)

Let $W$ be a finite set and $m,q\ge0$. Put $J=(W\times\{1,\ldots,m\})^{\{1,\ldots,q\}}$. For $\sigma\in S_q$ and $w\in W^{\{1,\ldots,q\}}$, define a matrix $P_{\sigma,w}\in M_J(\mathbb C)$ by $$(P_{\sigma,w})_{I,J'}=\begin{cases}1,&\text{the first coordinate of }I(i)\text{ is }w(i)\text{ for every }i,\ J'=I\circ\sigma,\\0,&\text{otherwise}.\end{cases}$$ If $T\in M_J(\mathbb C)$ commutes with every matrix $Z$ that commutes with every $P_{\sigma,w}$, then $$T\in\operatorname{span}_{\mathbb C}\{P_{\sigma,w}:\sigma\in S_q,\ w\in W^{\{1,\ldots,q\}}\}.$$
