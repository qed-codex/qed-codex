---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/QuotientMeasureNormalisedByHaarUniqueStatement.lean",
  "declarations": [
    "GlobalTheory.T.quotientMeasure_normalised_by_haar_unique"
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

## Unique quotient measure with prescribed Haar normalization

[Theorem REP.1315](https://andrewodesky.com/rh/lean/GlobalTheory.T.quotientMeasure_normalised_by_haar_unique/)

Let $G$ be a locally compact, second-countable Hausdorff topological group and $H\subset G$ a closed subgroup. Give $G$, $H$, and $G/H$ their Borel measurable structures, and assume $G$ and $H$ are unimodular. For prescribed left Haar measures $dg$ on $G$ and $dh$ on $H$, there is a unique nonzero $G$-invariant measure $d\mu$ on $G/H$, finite on compact sets, such that for every measurable $f:G\to[0,\infty]$ the function $$gH\longmapsto\int_Hf(gh)\,dh$$ is measurable and $$\int_Gf(g)\,dg=\int_{G/H}\int_Hf(gh)\,dh\,d\mu(gH).$$
