---
{
  "module": "src/Formalism/LatticeSlopes/ExistsSaturatedSlopeEqMuMax.lean",
  "declarations": [
    "Formalism.F.finiteSaturated"
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

## Finiteness of saturated sublattices of bounded covolume

[Theorem ARAK.0463](https://andrewodesky.com/rh/lean/Formalism.F.finiteSaturated/)

Let $E$ be a finite-dimensional real inner-product space and let $L\subset E$ be a discrete $\mathbb Z$-submodule. For every $X\in\mathbb R$, there are only finitely many submodules $N$ satisfying $$N=L\cap\operatorname{span}_{\mathbb R}N,\qquad\operatorname{covol}(N)\le X.$$ Here covolume is computed in the real span of $N$, using its induced Euclidean metric; the zero submodule has covolume one.
