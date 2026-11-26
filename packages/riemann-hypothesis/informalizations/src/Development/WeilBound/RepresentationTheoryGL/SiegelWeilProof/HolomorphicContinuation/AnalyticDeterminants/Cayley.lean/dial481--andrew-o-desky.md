---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/AnalyticDeterminants/Cayley.lean",
  "declarations": [
    "PositivityTheory.Rg.Sw.LVs.cayley"
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

## A determinant differential identity

[Theorem ALG.0421](https://andrewodesky.com/rh/lean/PositivityTheory.Rg.Sw.LVs.cayley/)

Let $n\ge0$, $A\in M_n(\mathbb C)$, and $t\in\mathbb Z$. With matrix coordinates $T_{ij}$, one has $$\left.\det\!\left(\frac{\partial}{\partial T_{ij}}\right)\det(1+AT)^t\right|_{T=0}=\left(\prod_{j=0}^{n-1}(t+j)\right)\det A.$$ The differential operator is $\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)\prod_{i=1}^n\partial/\partial T_{i,\sigma(i)}$, and derivatives are complex derivatives at the zero matrix.
