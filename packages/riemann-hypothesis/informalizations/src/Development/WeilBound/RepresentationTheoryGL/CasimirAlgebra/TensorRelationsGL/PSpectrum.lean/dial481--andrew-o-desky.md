---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/CasimirAlgebra/TensorRelationsGL/PSpectrum.lean",
  "declarations": [
    "PositivityTheory.Rg.Cz.SpecA.Kl_sum"
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

## Annihilating polynomials for sums of commuting operators

[Theorem ALG.1381](https://andrewodesky.com/rh/lean/PositivityTheory.Rg.Cz.SpecA.Kl_sum/)

Let $V$ be a complex vector space, $A,B\in\operatorname{End}_{\mathbb C}(V)$ commute, and let $\alpha,\beta\in\mathbb C$. Assume there are finite lists of nonnegative integers $(r_i)$ and $(s_j)$ such that $$\prod_i(A-(\alpha+r_i)\operatorname{id})=0,\qquad\prod_j(B-(\beta+s_j)\operatorname{id})=0.$$ Then there is a finite list of nonnegative integers $(t_k)$ with $$\prod_k(A+B-(\alpha+\beta+t_k)\operatorname{id})=0.$$ The lists may be empty and factors may repeat.
