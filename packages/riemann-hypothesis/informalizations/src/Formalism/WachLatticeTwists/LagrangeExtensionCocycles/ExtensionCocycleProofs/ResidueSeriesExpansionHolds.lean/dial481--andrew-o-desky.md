---
{
  "module": "src/Formalism/WachLatticeTwists/LagrangeExtensionCocycles/ExtensionCocycleProofs/ResidueSeriesExpansionHolds.lean",
  "declarations": [
    "Formalism.RepresentationBoundsCohomology.N2.residue_series_expansion_holds"
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

## An infinite-series bound for a cyclic recurrence

[Theorem ALG.0756](https://andrewodesky.com/rh/lean/Formalism.RepresentationBoundsCohomology.N2.residue_series_expansion_holds/)

Let $n\ge1$, let $\ell,c\in\mathbb R$ satisfy $\ell\ge3$ and $c\ge0$, and let $s,H:\mathbb Z/n\mathbb Z\to\mathbb R$. Suppose $H(k)\ge0$ and $$s(k-1)\le H(k)+c+3+\frac{s(k)}{\ell-1}\qquad(k\in\mathbb Z/n\mathbb Z).$$ Then for every $i\in\mathbb Z/n\mathbb Z$, $$s(i)\le\sum_{a=0}^\infty\frac{H(i+a+1)+c+3}{(\ell-1)^a}.$$ All arguments of $H$ are taken modulo $n$.
