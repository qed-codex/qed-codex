---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/AutomorphicForms/SmoothRepresentationsGL/AvgChar.lean",
  "declarations": [
    "UpperTheory.V.Af.Smo.avgChar"
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

## Simultaneous vanishing of finite character sums

[Theorem ALG.0286](https://andrewodesky.com/rh/lean/UpperTheory.V.Af.Smo.avgChar/)

Let $A$ be an abelian group and $L_0\subseteq L\subseteq A$ subgroups with finite index $[L:L_0]$. There is a nonempty finite subset $T\subseteq L$ such that, for every additive character $\chi:A\to\mathbb C$ satisfying $$\chi(x+y)=\chi(x)\chi(y),\qquad\chi(0)=1,$$ if $\chi$ is trivial on $L_0$ and nontrivial on $L$, then $$\sum_{t\in T}\chi(t)=0.$$
