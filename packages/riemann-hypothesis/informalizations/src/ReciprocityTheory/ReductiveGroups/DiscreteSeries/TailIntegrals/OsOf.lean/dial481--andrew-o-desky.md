---
{
  "module": "src/ReciprocityTheory/ReductiveGroups/DiscreteSeries/TailIntegrals/OsOf.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.DS.Xi.ker"
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

## A uniform bound for a singular planar integral

[Theorem ALG.0570](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.DS.Xi.ker/)

Let $0<e<\gamma<2$. There is a real $C$ such that for every $c\in\mathbb C$ and $D>0$, $$\int_{\mathbb C}(|z-c|^2+D^2)^{-1+e/2}|z|^{-\gamma}\,dA(z) \le C(|c|^2+D^2)^{-(\gamma-e)/2}.$$
