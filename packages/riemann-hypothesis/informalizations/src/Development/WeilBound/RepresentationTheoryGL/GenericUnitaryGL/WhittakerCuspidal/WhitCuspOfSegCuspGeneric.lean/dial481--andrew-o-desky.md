---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/GenericUnitaryGL/WhittakerCuspidal/WhitCuspOfSegCuspGeneric.lean",
  "declarations": [
    "PositivityTheory.rg.gu.whit.whitLeOne"
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

## Dimension bound for Whittaker coinvariants

[Theorem REP.1487](https://andrewodesky.com/rh/lean/PositivityTheory.rg.gu.whit.whitLeOne/)

Let $k$ be a nonarchimedean local field, $n\ge0$, $\psi:k\to S^1$ a continuous nontrivial additive character, and $\pi$ a smooth irreducible complex representation of $\operatorname{GL}_n(k)$. Let $N$ be the upper unitriangular subgroup and $\psi_N(u)=\psi(\sum_{i=1}^{n-1}u_{i,i+1})$. Then $$\dim_{\mathbb C}\left(\pi\big/\operatorname{span}_{\mathbb C}\{\pi(u)v-\psi_N(u)v:u\in N,\ v\in\pi\}\right)\le1.$$
